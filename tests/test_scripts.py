import os.path as osp
import subprocess
import unittest
import sys


class ScriptTestCase(unittest.TestCase):

    def run_script(self, name):
        return subprocess.check_output(
            [sys.executable, osp.join('scripts', name)],
            stderr=subprocess.STDOUT, universal_newlines=True)

    def run_script_with_error(self, name):
        try:
            self.run_script(name)
            self.fail('script returned zero exit status')
        except subprocess.CalledProcessError as e:
            return e.output

    def test_hello(self):
        output = self.run_script('hello.py')
        self.assertEqual('Hello from pymake\n', output)

    def test_hello_with_custom_name(self):
        output = self.run_script('hello_with_custom_name.py')
        self.assertEqual('Hello from pymake\n', output)

    def test_default_task(self):
        output = self.run_script('default_task.py')
        self.assertEqual('Second task\n', output)

    def test_without_default_task(self):
        output = self.run_script_with_error('without_default_task.py')
        self.assertEqual('error: no task specified\n'
                         'existing task are:\n'
                         ' first\n'
                         ' second\n',
            output)

    def test_empty_script(self):
        self.assertEqual('error: no task specified\n',
            self.run_script_with_error('empty.py'))

    def test_many_default_tasks(self):
        self.assertEqual('error: default task already exists\n'
                         'cannot add default task "second": task "first" '
                         'already registered as default\n',
            self.run_script_with_error('many_default_tasks.py'))

    def test_tasks_dependence(self):
        self.assertEqual('first task\n'
                         'second task\n',
            self.run_script('two_dependent_tasks.py'))


if __name__ == '__main__':
    unittest.main()
