from flask import Flask

app = Flask(__name__)

@app.get("/new")
def get_grettings():
    greet_message = "Hi DevOps team , This is coming from container"
    print(f"get_grettings() :: message is {greet_message}")
    return greet_message, 200