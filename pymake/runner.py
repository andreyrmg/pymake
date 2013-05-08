from .error import NoTaskSpecifiedError, DefaultTaskAlreadyExists


class Runner(object):
    def __init__(self):
        self._tasks = {}
        self._graph = {}
        self._default_task = None

    def run(self, task_name=None):
        if task_name:
            task = self._by_name(task_name)
        else:
            if not self._default_task:
                raise NoTaskSpecifiedError(self._tasks.values())
            task = self._default_task
        for t in self._task_deps(task):
            t.run()

    def add_task(self, task, depends):
        self._tasks[task.name] = task
        if task.default:
            if self._default_task:
                raise DefaultTaskAlreadyExists(self._default_task, task)
            self._default_task = task
        deps = []
        for task_name in depends:
            deps.append(self._by_name(task_name))
        self._graph[task] = deps

    def _by_name(self, task_name):
        return self._tasks[task_name]

    def _task_deps(self, task):
        deps = self._graph[task]
        if deps:
            for d in deps:
                yield from self._task_deps(d)
        yield task
