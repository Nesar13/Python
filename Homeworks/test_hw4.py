''' "I pledge my honor that I have abided by the Stevens Honor System." 


@author: Nesar Ahmed
Created on Feb 24, 2016
'''
import unittest
import hw4_pascal

class Test(unittest.TestCase):

    def test01(self):
        self.assertEqual(hw4_pascal.pascal_row(-1),float("inf"))
    
    def test02(self):
        self.assertEqual(hw4_pascal.pascal_row((0)),[1])  
                           
    def test03(self): 
        self.assertEqual(hw4_pascal.pascal_row((1)),[1,1]) 
        
    def test04(self):
        self.assertEqual(hw4_pascal.pascal_row((5)),[1, 5, 10, 10, 5, 1])
    
    def test05(self):
        self.assertEqual(hw4_pascal.pascal_row((3)),[1,3,3,1])
    
    def test06(self):
        self.assertEqual(hw4_pascal.pascal_triangle((5)),[[1], [1, 1], \
        [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]])
    
    def test07(self):
        self.assertEqual(hw4_pascal.pascal_triangle((0)),[[1]])
        
    def test08(self):
        self.assertEqual(hw4_pascal.pascal_triangle((-1)),float("inf"))
        
    def test09(self):
        self.assertEqual(hw4_pascal.pascal_triangle((1)),[[1], [1, 1]])
        
    def test10(self):
        self.assertEqual(hw4_pascal.pascal_triangle((2)),[[1], [1, 1], [1, 2, 1]])

if __name__ == "__main__":
    unittest.main()