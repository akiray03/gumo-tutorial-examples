import flask.views

from todo.presentation.task import TasksView, TaskDeleteView, TaskUpdateView


def register_views(blueprint: flask.Blueprint):
    blueprint.add_url_rule(
        rule="/tasks",
        view_func=TasksView.as_view("tasks"),
        methods=["GET", "POST"]
    )
    blueprint.add_url_rule(
        rule="/tasks/<task_id>/delete",
        view_func=TaskDeleteView.as_view("tasks/delete"),
        methods=[ "POST"]
    )
    blueprint.add_url_rule(
        rule="/tasks/<task_id>/update",
        view_func=TaskUpdateView.as_view("tasks/update"),
        methods=[ "POST"]
    )
