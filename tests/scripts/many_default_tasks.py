from pymake import *


@task(default=True)
def first():
    print("First task")


@task(default=True)
def second():
    print("Second task")


make()