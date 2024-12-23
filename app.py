import os
from flask import Flask

app = Flask(__name__)

# take value of env variable
change = os.environ.get("change_env_var")

@app.get("/")
def get_greetings():
    greet_message = f"Hi {change} , This is container"
    return greet_message, 200