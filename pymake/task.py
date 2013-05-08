from .dispatch import catch


class Task(object):
    def __init__(self, func, name, default):
        self._func = func
        self._name = name if name else func.__name__
        self._default = default
        self._executed = False

    def run(self):
        self._func()
        self._executed = True

    def __lt__(self, y):
        return self.name < y.name

    @property
    def default(self):
        return self._default

    @property
    def name(self):
        return self._name

    @property
    def executed(self):
        return self._executed


def task(*args, **kwargs):
    def taskfunc(func):
        from pymake import r
        task = Task(func, kwargs.get('name', None), kwargs.get('default', False))
        try:
            r.addtask(task, kwargs.get('depends', []))
        except Exception as e:
            catch(e)
        return func
    return taskfunc(*args) if args else taskfunc
