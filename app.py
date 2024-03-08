from flask import Flask, request, render_template, redirect, url_for, send_from_directory, jsonify
from dotenv import load_dotenv
import os
import json

from prettytable import PrettyTable
from minio import Minio

from python_files.execution_logs import total_execution
from python_files.model_execution import total_order
from python_files.odoo_connect import connect

new_minio = Minio(
    "137.226.188.114:32763",
    secure=False,
    access_key="databatt",
    secret_key="databatt",
)

load_dotenv()

from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=['http://localhost:9200'], http_auth=("utkarsh123", "dubey1906"))

app = Flask(__name__)

index_settings = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0,
        "refresh_interval": "5s"
    },
    "mappings": {
        "properties": {
            "GrahamNotation": {
                "properties": {
                    "https://www.iop.rwth-aachen.de/PPC/1/1/machineEnvironment": {"type": "keyword"},
                    "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints": {"type": "keyword"},
                    "https://wwwmodels_search.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction": {
                        "type": "keyword"}
                }
            }
        }
    }
}

index_name = 'new_search'

if not es.indices.exists(index=index_name):
    # es.indices.create(index=index_name, body={"settings": index_settings["settings"]})
    es.indices.create(index=index_name, body={"settings": index_settings["settings"]},
                      mappings=index_settings["mappings"])


def load_models(es):
    model_folder = 'jsonModels'
    models = []
    for filename in os.listdir(model_folder):
        if filename.endswith('.json'):
            model_path = os.path.join(model_folder, filename)
            try:
                with open(model_path, 'r', encoding='utf-8') as f:
                    model_data = json.load(f)
                    model_id = model_data.get('_id')
                    if model_id:
                        print(f"Original Model ID: {model_id}")
                        es.index(index=index_name, id=model_id, document=model_data["GrahamNotation"])
                        print(f"Model data: {model_data}")
                        print(f"Indexed model with ID: {model_id}")
                        models.append(model_data)
                    else:
                        print(f"Model ID not found in JSON: {model_path}")
            except FileNotFoundError:
                print(f"Failed to load model: {model_path}")

    return models


# Call the load_models function to start loading the JSON files
loaded_models = load_models(es)


def find_matching_model(es, url1, url2, url3):
    print("Received URLs:", url1, url2, url3)
    len_2 = len(url2)
    len_3 = len(url3)

    query = {
        "query": {
            "bool": {
                "must":
                    [{"match_phrase": {"https://www.iop.rwth-aachen.de/PPC/1/1/machineEnvironment": url1}},
                     {"terms": {
                         "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints.keyword": url2}},
                     {
                         "script":
                             {
                                 "script":
                                     {
                                         "source": "doc['https://www.iop.rwth-aachen.de/PPC/1/1/schedulingConstraints.keyword'].length == params.fixed_array_length",
                                         "params": {
                                             "fixed_array_length": len_2
                                         }
                                     }
                             }
                     },
                     {
                         "terms": {
                             "https://www.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction.keyword": url3}},

                     {
                         "script":
                             {
                                 "script":
                                     {
                                         "source": "doc['https://www.iop.rwth-aachen.de/PPC/1/1/schedulingObjectiveFunction.keyword'].length == params.fixed_array_length",
                                         "params": {
                                             "fixed_array_length": len_3
                                             
                                         }
                                     }
                             }
                     }

                     ]

            }
        }

    }

    print("Elasticsearch Query:", query)

    result = es.search(index='new_search', size=16, body=query)
    hits = result.get('hits', {}).get('hits', [])

    print("Number of hits:", len(hits))

    if hits:
        for hit in hits:
            source = hit.get('_source')
            print("Retrieved Document:", source)

    return hits


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        machine_environment = request.form.get('machine')
        scheduling_constraints = request.form.getlist('checked[]')
        scheduling_objective_function = request.form.getlist('checking[]')
        print("Received values:")
        print("Machine Environment:", machine_environment)
        print("Scheduling Constraints:", scheduling_constraints)
        print("Scheduling Objective Function:", scheduling_objective_function)

        matching_model = find_matching_model(es, machine_environment, scheduling_constraints,
                                             scheduling_objective_function)
        print("Matching models:", matching_model)

        # Extract the relevant information from the hits
        selected_models = []
        for hit in matching_model:
            source = hit.get('_source', {})
            selected_models.append(source)

        print("Matching Models:", selected_models)

        if selected_models:
            return render_template('selection.html', selected_models=selected_models)
        else:
            return "No matching model found."
    return render_template('index.html')


@app.route('/model-execution/', methods=['GET', 'POST'])
def selection():
    x = 0
    models_list = request.form.getlist('selected_model')
    print(models_list)
    return render_template('execution.html', models_list=models_list)


@app.route('/model/<model_name>')
def display_model(model_name):
    # Load all models from the 'jsonModels' folder
    models = load_models(es)

    # Find the matching model based on the model name from the URL
    matching_model = None
    for model in models:
        if model["GrahamNotation"]["name"] == model_name:
            matching_model = model
            break

    if matching_model:
        show = jsonify(matching_model)
        print(show)
        return jsonify(matching_model)
    else:
        return "Model not found."


@app.route('/underlying-asset/<model_name>')
def get_asset(model_name):
    model = model_name.replace(" ID ", "-")
    new_model = model.lower()
    print(new_model)
    asset = connect(new_model)
    # asset = asset.decode("utf-8")
    asset_json = json.dumps(asset, indent=4)
    return asset


@app.route('/execution/<model_name>')
def get_execution(model_name):
    model = model_name.replace(" ID ", "-")
    new_model = model.lower()
    print(new_model)
    job_order = total_order(new_model)
    return job_order

@app.route('/execution_logs/<model_name>')
def get_execution_logs(model_name):
    model = model_name.replace(" ID ", "-")
    new_model = model.lower()
    print(new_model)
    logs = total_execution(new_model)
    return logs

@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory('images', filename)


if __name__ == '__main__':
    app.run()
