import unittest
import math
def reverse(mylist):
    temp = 0
    for i in range(math.floor(len(mylist)/2)):
        temp = mylist[i]
        mylist[i] = mylist[len(mylist)-1 -i]
        mylist[len(mylist)-1-i] = temp
    return mylist

class test(unittest.TestCase):
    def testreverse1(self):
        self.assertEqual(reverse([1,2,3,4]), [4,3,2,1])
    def testreverse2(self):
        self.assertNotEqual(reverse([1,2,3,4]), [2,4,3,1])
    def testreverse3(self):
        self.assertIsNot(reverse([1,2,3,4]), [4,3,1,2])
    def testreverse4(self):
        self.assertEquals(reverse(['coding',5,'dojo',7]), [7,'dojo',5,'coding'])
    def testreverse5(self):
        self.assertNotEqual(reverse(['coding',2,3,4]), [2,4,3,'dojo'])

input = 'madam'
def Pstring(input):
    if input[::-1] == input:
        return True
    else:
        return False
class palindrome(unittest.TestCase):
    def test1_pal(self):
        self.assertEqual(Pstring(input), True)
    def test2_pal(self):
        self.assertEqual(Pstring('notpal'), False)
    def test3_pal(self):
        self.assertIs(Pstring(input), True)
    def test5_pal(self):
        self.assertIsNotNone(Pstring(input), True)
    def test6_pal(self):
        self.assertTrue(Pstring(input), True)
    def test7_pal(self):
        self.assertFalse(Pstring('racebike'), False)

def coins(given):
    chgInc = [25,10,5,1]
    q = 0
    r = 0
    for i in range(len(chgInc)):
        q, r = divmod(given, chgInc[i])
        q, chgInc[i] = chgInc[i], q
        given = r
    return chgInc

class CoinIncrements(unittest.TestCase):
    def testCoins1(self):
        self.assertEqual(coins(87), (3,1,0,2))
    def testCoins2(self):
        self.assertIsNot(coins(87), (3,8,17,87))
    def testCoins3(self):
        self.assertTrue(coins(87), (3,1,0,2))
    def testCoins4(self):
        self.assertEqual(coins(37), (1,1,0,2))

def coins2(given):
    quarters = 0
    dimes = 0
    nickles = 0
    pennies = 0
    while given > 0:
        while given >= 25:
            given -= 25
            quarters +=1
        while given >=10:
            given -= 10
            dimes += 1
        while given >=5:
            given -= 5
            nickles += 1
        while given >=1:
            given -= 1
            pennies += 1
        return quarters, dimes, nickles, pennies

class CoinIncrements(unittest.TestCase):
    def testCoins1(self):
        self.assertEqual(coins2(87), (3,1,0,2))
    def testCoins2(self):
        self.assertIsNot(coins2(87), (3,8,17,87))
    def testCoins3(self):
        self.assertTrue(coins2(87), (3,1,0,2))
    def testCoins4(self):
        self.assertEqual(coins2(37), (1,1,0,2))
if __name__ == '__main__':
    unittest.main()