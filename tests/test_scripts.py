import os.path as osp
import subprocess
import unittest
import sys


class ScriptTestCase(unittest.TestCase):
    def run_script(self, name):
        return subprocess.check_output(
            [sys.executable, osp.join('scripts', name)],
            stderr=subprocess.STDOUT, universal_newlines=True)

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
        output = self.run_script('without_default_task.py')
        self.assertEqual('error: no task specified\n'
                         'existing task are:\n'
                         ' first\n'
                         ' second\n',
            output)


if __name__ == '__main__':
    unittest.main()
