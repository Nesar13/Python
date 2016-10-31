'''
Created on Jan 20, 2015

@author: Brian Borowski

CS115 - Lab 1 Test Script
'''
import unittest
import Lab_1_Going_Natural

class Test(unittest.TestCase):

    def testInverse1(self):
        self.assertAlmostEqual(Lab_1_Going_Natural.inverse(1), 1, 6)

    def testInverse2(self):
        self.assertAlmostEqual(Lab_1_Going_Natural.inverse(2), 0.5, 6)

    def testInverse3(self):
        self.assertAlmostEqual(Lab_1_Going_Natural.inverse(3), 0.3333333333333333, 6)

    def testInverse4(self):
        self.assertAlmostEqual(Lab_1_Going_Natural.inverse(-3), -0.3333333333333333, 6)

    def testE1(self):
        self.assertAlmostEqual(Lab_1_Going_Natural.e(1), 2, 6)

    def testE2(self):
        self.assertAlmostEqual(Lab_1_Going_Natural.e(2), 2.5, 6)

    def testE3(self):
        self.assertAlmostEqual(Lab_1_Going_Natural.e(10), 2.718281801146385, 10)

    def testE4(self):
        self.assertAlmostEqual(Lab_1_Going_Natural.e(100), 2.7182818284590455, 10)

    def testError1(self):
        self.assertAlmostEqual(Lab_1_Going_Natural.error(1), 0.7182818284590451, 10)

    def testError2(self):
        self.assertAlmostEqual(Lab_1_Going_Natural.error(2), 0.2182818284590451, 10)

    def testError3(self):
        self.assertAlmostEqual(Lab_1_Going_Natural.error(10), 2.7312660133560485e-08, 10)

    def testError4(self):
        self.assertAlmostEqual(Lab_1_Going_Natural.error(100), 4.440892098500626e-16, 10)

if __name__ == "__main__":
    unittest.main()
