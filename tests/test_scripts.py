import importlib
import io
import unittest
import sys


class ScriptTestCase(unittest.TestCase):

    def runScript(self, name):
        loader = importlib.find_loader(name, ['scripts'])
        out, err = io.StringIO(), io.StringIO()
        stdout, sys.stdout = sys.stdout, out
        stderr, sys.stderr = sys.stderr, err
        try:
            loader.load_module(name)
        finally:
            sys.stdout, sys.stderr = stdout, stderr
        return out.getvalue(), err.getvalue()

    def test_hello(self):
        output, _ = self.runScript('hello')
        self.assertEqual('Hello from pymake\n', output)

    def test_hello_with_custom_name(self):
        output, _ = self.runScript('hello_with_custom_name')
        self.assertEqual('Hello from pymake\n', output)


if __name__ == '__main__':
    unittest.main()
