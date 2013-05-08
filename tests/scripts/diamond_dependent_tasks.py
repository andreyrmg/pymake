from pymake import *


@task
def first():
    print("first task")


@task(depends=['first'])
def second():
    print("second task")


@task(depends=['first'])
def third():
    print('third task')


@task(default=True, depends=['second', 'third'])
def fourth():
    print('fourth task')


make()