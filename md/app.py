from flask import Flask, request, render_template, redirect, url_for, send_from_directory, jsonify
from dotenv import load_dotenv
import os
import json

load_dotenv()

from elasticsearch import Elasticsearch


es = Elasticsearch(hosts=['http://localhost:9200'])


app = Flask(__name__)

def load_models():
    model_folder = 'jsonM'
    models = []
    for filename in os.listdir(model_folder):
        if filename.endswith('.json'):
            model_path = os.path.join(model_folder, filename)
            try:
                with open(model_path, 'r') as f:
                    model = json.load(f)
                    models.append(model)
                    print(f"Loaded model: {model}")
            except FileNotFoundError:
                print(f"Failed to load model: {model_path}")
    return models

def find_matching_model(models, alpha, beta, gamma):
    print("Finding matching model...")
    print(f"Form Alpha: {alpha}, Beta: {beta}, Gamma: {gamma}")
    for model in models:
        model_alpha = model["GrahamNotation"]["alpha"]
        model_beta = model["GrahamNotation"]["beta"]
        model_gamma = model["GrahamNotation"]["gamma"]
        print(f"Model Alpha: {model_alpha}, Beta: {model_beta}, Gamma: {model_gamma}")
        if (
            model_alpha == alpha and
            model_beta == beta and
            model_gamma == gamma
        ):
            return model
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve the form data
        alpha = request.form.get('machine')
        beta = request.form.getlist('checked')
        gamma = request.form.getlist('checking')
        print(f"Alpha: {alpha}, Beta: {beta}, Gamma: {gamma}")

        # Load all models from the 'jsonM' folder
        models = load_models()

        # Find the matching model based on user input
        matching_model = find_matching_model(models, alpha, beta, gamma)
        print(f"Matching model: {matching_model}")

        if matching_model:
            return render_template('selection.html', selected_model=matching_model)
        else:
            return "No matching model found."

    return render_template('index.html')

@app.route('/get_python_file', methods=['POST'])
def get_python_file():
    model_name = request.form.get('model_name')
    return model_name

@app.route('/model/<model_name>')
def display_model(model_name):
    # Load all models from the 'jsonM' folder
    models = load_models()

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
