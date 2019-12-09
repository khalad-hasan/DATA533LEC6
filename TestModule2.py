import unittest
from mod2 import multiplication as md2


class TestMultiplication(unittest.TestCase):

    def test_multiplication(self):
        self.assertEqual(md2(1,2),2)
        self.assertEqual(md2(1,5),5)
     
unittest.main()