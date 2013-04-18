import sys
from .error import NoTaskSpecifiedError


def try_catch(task_name):
    try:
        from pymake import r
        r.run(task_name)
    except NoTaskSpecifiedError as e:
        print('error:', e, file=sys.stderr)
        if e.tasks:
            print('existing task are:', file=sys.stderr)
            for task in e.tasks:
                print('', task.name, file=sys.stderr)




def run(task_name=None):
    try:
        try_catch(task_name)
    except Exception as e:
        print('uncaught exception:', e)
