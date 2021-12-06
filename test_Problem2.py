import unittest
import Problem2


class TestCalculate(unittest.TestCase):

    def test_calculate(self):
        self.assertEqual(Problem2.calculate(" 2-1 + 2 "),  3)
        self.assertEqual(Problem2.calculate("(1+(4+5+2)-3)+(6+8)"),  23)

        #self.assertEqual(Problem2.calculate(" 2-1 + 8 "),  50)
        
        
if __name__ == '__main__':
    unittest.main()