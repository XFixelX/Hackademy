import unittest
import divisible

class TestDivisible(unittest.TestCase): 
    def test_divisible(self): 
        a = 1
        b = 10
        c = 2 
        output = [2,4,6,8,10] 
        self.assertEqual(output, divisible.divisible(a,b,c)) 
 
if __name__ =="__main__": 
    unittest.main() 
