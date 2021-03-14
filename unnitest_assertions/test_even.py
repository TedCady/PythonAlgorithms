import unittest

# def isEven(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
# class IsEvenTests(unittest.TestCase):
#     def testTwo(self):
#         # self.assertEqual(isEven(4), True)
#         self.assertTrue(isEven(4))
#     def testThree(self):
#         # self.assertEqual(isEven(5), False)
#         self.assertFalse(isEven(5))
#     def setUp(self):
#         print("running setUp")
#     def tearDown(self):
#         print("running tearDown tasks")
# if __name__ == '__main__':
#     unittest.main() # this runs our tests


import math
mylist = [1,2,3,4]
def reverse(mylist):
    mylist.reverse()
    return mylist

# print(reverse(mylist))

class test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse(mylist), [4,3,2,1])
    def testagain(self):
        self.assertNotEqual(reverse(mylist), [2,4,3,1])
    def test3(self):
        self.assertIsNot(reverse(mylist), [4,3,1,2])
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown tasks")

# string = 'racecar'
# def palindromeString(string):
#     pass
# class palindrome(unittest.TestCase):
#     def pal_test1(self):
#         self.assertEqual
if __name__ == '__main__':
    unittest.main()