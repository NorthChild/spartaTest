#################################### NOTE ####################################
#################################### NOTE ####################################

# This is the testing for the solutions to the tasks, going by memory so i apologise if outputs are slightly different
# IMPORTANT: to run the testing, make sure to run this script ('test_solutions.py') and remember to keep both scripts in the same folder


#################################### NOTE ####################################
#################################### NOTE ####################################

import unittest
import solutions




class Test_Solutions(unittest.TestCase):

    # testing the calculator [TASK 1]
    print('Testing Solution to TASK 1')

    def test_add(self):
        self.assertEqual(solutions.add(5, 5), 10)
        self.assertEqual(solutions.add(-5, 5), 0)
        self.assertEqual(solutions.add(-5, -5), -10)

    def test_subtract(self):
        self.assertEqual(solutions.subtract(5, 5), 0)
        self.assertEqual(solutions.subtract(-5, 10), -15)
        self.assertEqual(solutions.subtract(-5, -5), 0)

    def test_multiply(self):
        self.assertEqual(solutions.multiply(1, 5), 5)
        self.assertEqual(solutions.multiply(-5, 5), -25)
        self.assertEqual(solutions.multiply(-5, -5), 25)

    def test_divide(self):
        self.assertEqual(solutions.divide(5, 1), 5)
        self.assertEqual(solutions.divide(-5, 10), -0.5)
        self.assertEqual(solutions.divide(-5, -5), 1)

        with self.assertRaises(ValueError):
            solutions.divide(10, 0)




    # testing the string element counter [TASK 2]
    print('Testing Solution to TASK 2')
    def test_string_counter(self):
        self.assertEqual(solutions.string_counter('CCTGGGACGTCGTAAGCTAGCTGTATGCTGAGTGTCTAGTCGTAGCGT'),(f'C:{10},A:{8},T:{14},G:{16}'))
        self.assertEqual(solutions.string_counter('ACTGGGACTTCGTAATGTAGCTGTCTGCTGAGTGTCTAGTCGTAGCGT'),(f'C:{9},A:{8},T:{16},G:{15}'))
        self.assertEqual(solutions.string_counter('ACTGGGACCTCGTAGTGTAGCTGTCTGCTGAGTGTCTAGTCGTACCGT'),(f'C:{11},A:{7},T:{15},G:{15}'))




    # testing the scrabble counter [TASK 3]
    print('Testing Solution to TASK 3')
    def test_scrabble_counter(self):
        self.assertEqual(solutions.scrabble_counter('zoo'),('zoo', 12))
        self.assertEqual(solutions.scrabble_counter('scrabble'),('scrabble', 14))
        self.assertEqual(solutions.scrabble_counter('faraday'),('faraday', 14))








if __name__ == '__main__':
    unittest.main()
