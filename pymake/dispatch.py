import sys
from .error import NoTaskSpecifiedError, DefaultTaskAlreadyExists


def printexc(e):
    print('error:', e, file=sys.stderr)


def catch(e):
    printexc(e)
    t = type(e)
    if NoTaskSpecifiedError == t:
        if e.tasks:
            print('existing task are:', file=sys.stderr)
            for task in sorted(e.tasks):
                print('', task.name, file=sys.stderr)
    elif DefaultTaskAlreadyExists == t:
        print('cannot add default task "{}": task "{}" already registered as '
              'default'.format(e.second.name, e.first.name), file=sys.stderr)
    else:
        raise e
    sys.exit(1)


def trycatch(taskname):
    try:
        from pymake import r
        r.run(taskname)
    except Exception as e:
        catch(e)


def run(taskname=None):
    try:
        trycatch(taskname)
    except Exception as e:
        print('uncaught exception:', e)
        sys.exit(1)
