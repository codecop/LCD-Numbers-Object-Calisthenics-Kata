#! python
import unittest

import fnmatch
import os
import os.path


# Find all unit tests `test/*Test.py` and execute them.
# see http://stackoverflow.com/questions/1732438/run-all-unit-test-in-python-directory

def all_test_modules(root_dir, pattern):
    test_file_names = all_files_in(root_dir, pattern)
    return [path_to_module(string) for string in test_file_names]


def all_files_in(root_dir, pattern):
    matches = []

    for root, _, fileNames in os.walk(root_dir):
        for filename in fnmatch.filter(fileNames, pattern):
            matches.append(os.path.join(root, filename))

    return matches


def path_to_module(py_file):
    return strip_leading_dots(
        replace_slash_by_dot(
            strip_extension(py_file)))


def strip_extension(py_file):
    return py_file[0:len(py_file) - len('.py')]


def replace_slash_by_dot(string):
    return string.replace('\\', '.').replace('/', '.')


def strip_leading_dots(string):
    while string.startswith('.'):
        string = string[1:len(string)]
    return string


module_names = all_test_modules('test', '*Test.py')
suites = [unittest.defaultTestLoader.loadTestsFromName(module_name)
          for module_name in module_names]

testSuite = unittest.TestSuite(suites)
runner = unittest.TextTestRunner(verbosity=1)
runner.run(testSuite)
