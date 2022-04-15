import unittest
from deque import Deque

class MyTests(unittest.TestCase):

    def test_add_front(self):
        dq = Deque()
        for i in range(100):
            dq.addFront(i)
            self.assertEqual(i,dq.removeTail())

    def test_add_tail(self):
        dq = Deque()
        for i in range(100):
            dq.addTail(i)
            self.assertEqual(i,dq.removeTail())

    def test_remove_front(self):
        dq = Deque()
        self.assertEqual(None,dq.removeFront())
        for i in range(101):
            dq.addFront(i)
        for j in range(100,-1,-1):
            self.assertEqual(j,dq.removeFront())
        self.assertEqual(0,dq.size())
    def test_remove_tail(self):
        dq = Deque()
        self.assertEqual(None,dq.removeTail())
        for i in range(100):
            dq.addTail(i)
        for j in range(99,-1,-1):
            self.assertEqual(j,dq.removeTail())
        self.assertEqual(0,dq.size())

if __name__ == '__main__':
    unittest.main()