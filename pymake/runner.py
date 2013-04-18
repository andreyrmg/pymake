from .error import NoTaskSpecifiedError


class Runner(object):
    def __init__(self):
        self._tasks = []
        self._default_task = None

    def run(self, task_name=None):
        if not task_name:
            if not self._default_task:
                raise NoTaskSpecifiedError(self._tasks)
            self._default_task.run()
            return
        for task in self._tasks:
            if task.name == task_name:
                task.run()

    def add_task(self, task):
        self._tasks.append(task)
        if task.default:
            self._default_task = task



