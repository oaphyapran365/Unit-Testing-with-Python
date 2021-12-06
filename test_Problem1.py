import unittest
import Problem1


class TestProblem1(unittest.TestCase):

    def test_numberToWords(self):
        self.assertEqual(Problem1.numberToWords(542), "Five Hundred Forty Two")
        self.assertEqual(Problem1.numberToWords( 1334567891), "One Billion Three Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One")
        
        #self.assertEqual(Problem1.numberToWords(100), "Forty Two")

    


if __name__ == '__main__':
    unittest.main()