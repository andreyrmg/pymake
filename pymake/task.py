class Task(object):
    def __init__(self, func, name, default):
        self._func = func
        self._name = name if name else func.__name__
        self._default = default

    def run(self):
        self._func()

    @property
    def default(self):
        return self._default

    @property
    def name(self):
        return self._name


def task(*args, **kwargs):
    def task_func(func):
        from pymake import r
        task = Task(func, kwargs.get('name', None), kwargs.get('default', False))
        r.add_task(task)
        return func
    return task_func(*args) if args else task_func
