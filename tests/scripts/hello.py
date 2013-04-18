from pymake import *


@task
def hello():
    print("Hello from pymake")


make('hello')