import unittest
from collections import deque
from Matches import MatchDeque


class TestMatchDeque(unittest.TestCase):
    def test_is_empty(self):
        test_deque = MatchDeque([('(', 1), ('[', 2), (']', 2)])
        self.assertFalse(test_deque.is_empty())
        test_deque = MatchDeque()
        self.assertTrue(test_deque.is_empty())

    def test_deque_property(self):
        test_deque = MatchDeque([('(', 1), ('[', 2), (']', 2)])
        self.assertEqual(test_deque.deque, deque([('(', 1), ('[', 2), (']', 2)]))
        with self.assertRaises(AttributeError):
            test_deque.deque = deque([('(', 1)])


if __name__ == "__main__":
    unittest.main()
