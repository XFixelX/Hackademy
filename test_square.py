import unittest
import production

class TestProduction(unittest.TestCase):
    def test_square(self):
        input = [2]
        output = [4]
        self.assertEqual(output, production.square(input))

if __name__ =="__main__":
    unittest.main()
