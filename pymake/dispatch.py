import sys
from .error import NoTaskSpecifiedError, DefaultTaskAlreadyExists


def print_exception(e):
    print('error:', e, file=sys.stderr)


def catch(e):
    print_exception(e)
    t = type(e)
    if NoTaskSpecifiedError == t:
        if e.tasks:
            print('existing task are:', file=sys.stderr)
            for task in e.tasks:
                print('', task.name, file=sys.stderr)
    elif DefaultTaskAlreadyExists == t:
        print('cannot add default task "{}": task "{}" already registered as '
              'default'.format(e.second.name, e.first.name), file=sys.stderr)
    else:
        raise e
    sys.exit(1)


def try_catch(task_name):
    try:
        from pymake import r
        r.run(task_name)
    except Exception as e:
        catch(e)


def run(task_name=None):
    try:
        try_catch(task_name)
    except Exception as e:
        print('uncaught exception:', e)
