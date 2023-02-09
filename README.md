#Install Flask
```pip install flask```

#Place dependencies in a text file
```pip freeze > requirements.txt```

#Set the FLASK_APP environment variable for Linux
```export FLASK_APP=app.py```

#Set the FLASK_APP environment variable for Microsoft Windows
```set FLASK_APP=app.py```

#Register environment variables in order to be automatically imported by running the flask command
```pip install python-dotenv```

#Write the environment variable, name and value in a file named .flaskenv
```FLASK_APP=app.py```
