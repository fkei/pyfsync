# -*- coding: utf-8 -*-

import os
import logging

from distutils.core import setup
from setuptools.command.test import test as TestCommand

DEBUG=True # exec mode

class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        # @see http://pytest.org/latest/usage.html#pytest-main-usage
        self.test_args = []
        if DEBUG is True:
            logging.basicConfig(
                level=logging.DEBUG,
                format="[%(asctime)s] [%(levelname)s] [%(process)d] [%(name)s] %(message)s (%(filename)s:%(lineno)d)")

            self.test_args.append("--capture=no")

        self.test_suite = True

    def run_tests(self):
        import pytest
        pytest.main(self.test_args)

setup(
    name='pyfsync',
    version='0.1.1',
    #tests_require=['pytest'],
    cmdclass = {'test': PyTest},
)
