from .error import NoTaskSpecifiedError, DefaultTaskAlreadyExists


class Runner(object):
    def __init__(self):
        self._tasks = {}
        self._graph = {}
        self._deftask = None

    def run(self, taskname=None):
        if taskname:
            task = self._byname(taskname)
        else:
            if not self._deftask:
                raise NoTaskSpecifiedError(self._tasks.values())
            task = self._deftask
        for task in self._taskdeps(task):
            task.run()

    def addtask(self, task, depends):
        self._tasks[task.name] = task
        if task.default:
            if self._deftask:
                raise DefaultTaskAlreadyExists(self._deftask, task)
            self._deftask = task
        deps = []
        for taskname in depends:
            deps.append(self._byname(taskname))
        self._graph[task] = deps

    def _byname(self, taskname):
        return self._tasks[taskname]

    def _taskdeps(self, task):
        deps = self._graph[task]
        if deps:
            for dep in deps:
                yield from self._taskdeps(dep)
        if not task.executed:
            yield task
