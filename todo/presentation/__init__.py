import flask.views

from todo.presentation.task import TasksView


def register_views(blueprint: flask.Blueprint):
    blueprint.add_url_rule(
        rule="/tasks",
        view_func=TasksView.as_view("tasks"),
        methods=["GET", "POST"]
    )
