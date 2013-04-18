from pymake import *


@task
def first():
    print("First task")


@task
def second():
    print("Second task")


make()