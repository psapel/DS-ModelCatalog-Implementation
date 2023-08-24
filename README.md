1. Install Flask
```pip install flask```

2. Place dependencies in a text file
```pip freeze > requirements.txt```

3.1 Set the FLASK_APP environment variable for Linux
```export FLASK_APP=app.py```

3.2 Set the FLASK_APP environment variable for Microsoft Windows
```set FLASK_APP=app.py```

4. Register environment variables in order to be automatically imported by running the flask command
```pip install python-dotenv```

5. Write the environment variable, name and value in a file named .flaskenv
```FLASK_APP=app.py```

6. Install Meilisearch
curl -L https://install.meilisearch.com | sh

7. Launch Meilisearch
./meilisearch --master-key=masterKey
