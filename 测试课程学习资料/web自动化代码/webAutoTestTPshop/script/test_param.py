# 加法操作
def add(x, y):
    return x + y

import unittest
from parameterized import parameterized
# import parameterized.parameterized


def build_data():
    #
    return [(1, 1, 2), (0, 1, 1), (0, 0, 0)]


class TestAdd(unittest.TestCase):

    # @parameterized.expand([(1, 1, 2), (0, 1, 1), (0, 0, 0)])
    @parameterized.expand(build_data)
    def test_add(self, x, y, expect):
        result = add(x, y)
        self.assertEqual(expect, result)

    # def test_add01(self):
    #     result = add(1, 1)
    #     self.assertEqual(2, result)
    #
    # def test_add02(self):
    #     result = add(0, 1)
    #     self.assertEqual(1, result)
    #
    # def test_add03(self):
    #     result = add(0, 0)
    #     self.assertEqual(0, result)
