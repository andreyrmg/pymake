class Runner(object):
    def __init__(self):
        self._tasks = []
        self._default_task = None

    def run(self, task_name):
        for task in self._tasks:
            if task.name == task_name:
                task.run()

    def add_task(self, task):
        self._tasks.append(task)
        if task.default:
            self._default_task = task



