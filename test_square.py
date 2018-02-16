import unittest
import production

class TestProduction(unittest.TestCase):
    def test_square(self):
        output = [0,1,4,9,16,25,36,49,64,81,100]
        self.assertEqual(output, production.square())

if __name__ =="__main__":
    unittest.main()
