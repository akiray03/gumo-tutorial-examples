import flask.views

from gumo.core.injector import injector

from todo.application.task import TaskCreateService
from todo.application.task.repository import TaskRepository
from todo.domain import TaskKey


class TasksView(flask.views.MethodView):
    def get(self):
        repository: TaskRepository = injector.get(TaskRepository)
        tasks = repository.fetch_list()

        return flask.render_template("todo/tasks.html", tasks=tasks)

    def post(self):
        task_name: str = flask.request.form.get("task_name", "")
        service: TaskCreateService = injector.get(TaskCreateService)
        service.execute(task_name=task_name)

        return flask.redirect("/tasks")


class TaskDeleteView(flask.views.MethodView):
    def post(self, task_id):
        task_key = TaskKey.build_by_id(task_id=task_id)
        repository: TaskRepository = injector.get(TaskRepository)
        repository.delete(key=task_key)

        return flask.redirect("/tasks")
