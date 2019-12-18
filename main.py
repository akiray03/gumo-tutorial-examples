import flask
import os

from gumo.core.injector import injector
from todo.bind import bind_todo


injector.binder.install(bind_todo)

app = flask.Flask(__name__)


@app.route("/")
def root():
    dummy_todos = [
        {"name": "Buy a shampoo"},
        {"name": "Buy a tooth brush"},
    ]

    return flask.render_template("index.html", todos=dummy_todos)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=os.environ.get("SERVER_PORT", 8080), debug=True)
