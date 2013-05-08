from .dispatch import run
from .task import task
from .runner import Runner


__ALL__ = ['task', 'make']


r = Runner()


def make(taskname=None):
    run(taskname)