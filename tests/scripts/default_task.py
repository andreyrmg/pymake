from pymake import *


@task
def first():
    print("First task")


@task(default=True)
def second():
    print("Second task")


make()