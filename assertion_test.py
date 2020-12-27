import unittest

from assertion import assert_that


class AssertionTest(unittest.TestCase):

    def test_assert_that(self):
        assert_that(True, True)
        try:
            assert_that(True, False)
        except AssertionError as e:
            assert e.args[0] == '\n\texpected: True\n\tactual: False'
