from flask import Flask, request, render_template, redirect, url_for, send_from_directory, jsonify
from dotenv import load_dotenv
import os
import json

load_dotenv()

from elasticsearch import Elasticsearch


es = Elasticsearch(hosts=['http://localhost:9200'])


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
                    "alpha": {"type": "keyword"},
                    "beta": {"type": "keyword"},
                    "gamma": {"type": "keyword"}
                }
            }
        }
    }
}

index_name = 'models_index'


if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name, body={"settings": index_settings["settings"]})

def load_models(es):
    model_folder = 'jsonM'
    models = []  
    for filename in os.listdir(model_folder):
        if filename.endswith('.json'):
            model_path = os.path.join(model_folder, filename)
            try:
                with open(model_path, 'r') as f:
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


def find_matching_model(es, alpha, beta, gamma):
    print(f"Searching with alpha: {alpha}, beta: {beta}, gamma: {gamma}")
    
    query = {
    "query": {
        "bool": {
            "must": [
                {"match_phrase": {"alpha": alpha}},
                {"terms": {"beta.keyword": beta}},
                {"terms": {"gamma.keyword": gamma}}  
            ]
        }
    }
}

    print("Elasticsearch Query:", query)
    
    result = es.search(index='models_index', body=query)
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
        alpha = request.form.get('machine')
        beta = request.form.getlist('checked[]')
        gamma = request.form.getlist('checking[]')
        print("Received values:")
        print("Alpha:", alpha)
        print("Beta:", beta)
        print("Gamma:", gamma)
        

        matching_model = find_matching_model(es, alpha, beta, gamma)
        print("matching models:", matching_model)
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


@app.route('/get_python_file', methods=['POST'])
def get_python_file():
    model_name = request.form.get('model_name')
    return model_name

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
        return render_template('model.html', selected_model=matching_model)
    else:
        return "Model not found."

@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory('images', filename)

if __name__ == '__main__':
    app.run() 