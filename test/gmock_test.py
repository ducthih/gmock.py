#!/usr/bin/env python

import os
import sys
import unittest
import shutil
sys.path.append('..')
import gmock

def read_file(path):
    with open(path, 'r') as content_file:
        content = content_file.read()
    return content

class TestGMock(unittest.TestCase):
    generated_dir = 'generated'

    def setUp(self):
        shutil.rmtree(path = self.generated_dir, ignore_errors = True)

    def tearDown(self):
        shutil.rmtree(path = self.generated_dir, ignore_errors = True)

    def test_gmock_args_fail(self):
        self.assertEqual(-1, gmock.main(['']))

    def test_gmock_args_fail(self):
        self.assertEqual(0, gmock.main(['', '../gmock.conf', self.generated_dir, '', 'not_found.hpp' ]))

    def test_gmock_success(self):
        self.assertEqual(0, gmock.main(['', '../gmock.conf', self.generated_dir, 'n1', 'given/I1.hpp', 'given/I2.hpp', 'given/I3I4.hpp', 'given/C1.hpp']))
        self.assertEqual(3, len([name for name in os.listdir(self.generated_dir)]))
        self.assertTrue('I2Mock.hpp' in os.listdir(self.generated_dir))
        self.assertTrue('I3Mock.hpp' in os.listdir(self.generated_dir))
        self.assertTrue('I4Mock.hpp' in os.listdir(self.generated_dir))
        for file in os.listdir(self.generated_dir):
            self.assertEqual(read_file(self.generated_dir + '/' + file), read_file('then/' + file))

if __name__ == '__main__':
    unittest.main()

