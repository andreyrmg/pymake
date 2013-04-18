from pymake import *


@task(name='hello_task')
def hello():
    print("Hello from pymake")


make('hello_task')