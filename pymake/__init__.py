from .task import task
from .runner import Runner


__ALL__ = ['task', 'make']


r = Runner()


def make(task_name):
    r.run(task_name)