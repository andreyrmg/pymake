from pymake import *


@task
def first():
    print("first task")


@task(default=True, depends=['first'])
def second():
    print("second task")


make()