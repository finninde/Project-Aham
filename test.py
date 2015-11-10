import unittest
from optimizer import *

class OptimizerTest(unittest.TestCase):
    
    def test_sorted(self):
        opt = Optimizer(elementer=[7,5,8,1,4,3,2,9,11,50,17,22,34,11,5,99,1,42,24])
        self.assertEqual(opt.solveSA(), [1, 1, 2, 3, 4, 5, 5, 7, 8, 9, 11, 11, 17, 22, 24, 34, 42, 50, 99])

    def test_listempty(self):
        opt = Optimizer(elementer=[7,5,8,1,4,3,2,9,11,50,17,22,34,11,5,99,1,42,24])
        self.assertIsNotNone(opt.solveSA())
    
    def test_listlengths(self):
        opt = Optimizer(elementer=[7,5,8,1,4,3,2,9,11,50,17,22,34,11,5,99,1,42,24])
        self.assertEqual(len(opt.solveSA()), len(opt.elementer))
    

if __name__ == "__main__":
    unittest.main()
