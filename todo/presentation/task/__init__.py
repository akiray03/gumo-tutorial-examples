import flask.views
import datetime

from gumo.core.injector import injector
from todo.application.task.repository import TaskRepository
from todo.domain import Task
from todo.domain import TaskName
from todo.domain import TaskKey


class TasksView(flask.views.MethodView):
    def get(self):
        repository: TaskRepository = injector.get(TaskRepository)
        tasks = repository.fetch_list()

        return flask.render_template("todo/tasks.html", tasks=tasks)

    def post(self):
        task_name: str = flask.request.form.get("task_name", "")
        repository: TaskRepository = injector.get(TaskRepository)

        task = Task(
            key=TaskKey.build_for_new(),
            name=TaskName(task_name),
            created_at=datetime.datetime.utcnow().astimezone(tz=datetime.timezone.utc),
        )
        repository.save(task=task)

        return flask.redirect("/tasks")
