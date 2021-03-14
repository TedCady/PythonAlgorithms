# #1
# def biggie(mylist):
#     for x in range(len(mylist)):
#         if mylist[x] > 0:
#             mylist[x] = ("Big")
#     return mylist
# x = [-1, 2, -38, 41]
# print(biggie(x))

# #2
# def sumpos(mylist):
#     sum = 0
#     for x in range(len(mylist)):
#         if mylist[x] > 0:
#             sum = sum + 1
#     mylist[len(mylist)-1] = sum
#     return mylist
# mylist = [-1, 3, 0, -6, 4]
# print(sumpos(mylist))

# #3
# def sumtotal(mylist):
#     total = 0
#     for x in range(len(mylist)):
#         total = total + mylist[x]
#     return total
# mylist = [1,2,3,4,5]
# print(sumtotal(mylist))

# #4
# def avg(mylist):
#     sum = 0
#     for x in range(len(mylist)):
#         sum = sum + mylist[x]
#     return sum/len(mylist)
# mylist = [1,2,3,4]
# print(avg(mylist))

# #5
# def length(mylist):
#     for x in range(len(mylist)):
#         return len(mylist)
#     if len(mylist) < 1:
#         return False
# mylist = [2,3,4,55,22,3,8]
# print(length(mylist))

# #6
# def min(mylist):
#     if len(mylist) < 1:
#         return False
#     min = mylist[0]
#     for x in range(len(mylist)):
#         if mylist[x]< min:
#             min = mylist[x]
#     return min
# mylist = [4,5,7,8,3,5,5,4]
# print(min(mylist))

# #7
# def max(mylist):
#     if len(mylist) < 1:
#         return False
#     max = mylist[0]
#     for x in range(len(mylist)):
#         if mylist[x] > max:
#             max = mylist[x]
#     return max
# mylist = [3,4,5,7,9,5,3]
# print(max(mylist))

# #8
# def ultimate_analysis(mylist):
#     sum = 0
#     avg = 0
#     min = mylist[0]
#     max = mylist[0]
#     for x in range(len(mylist)):
#         sum = sum + mylist[x]
#         avg = sum/len(mylist)
#     for x in range(len(mylist)):
#         if mylist[x] > max:
#             max = mylist[x]
#     for x in range(len(mylist)):
#         if mylist[x]< min:
#             min = mylist[x]
#     outputdict = {'sumtotal': sum, 'avg': avg, 'minimum': min, 'maximum': max, 'length': len(mylist)}
#     return outputdict
# mylist = [5,-3,7,33,-12]
# print(ultimate_analysis(mylist))

#9
# def reverse(mylist):
#     mylist.reverse()
#     return mylist
# mylist = [1,2,3,4]
# print(reverse(mylist))

#9.1
import math
def reverse2(mylist):
    temp = 0
    for i in range(math.floor(len(mylist)/2)):
        temp = mylist[i]
        mylist[i] = mylist[len(mylist)-1 -i]
        mylist[len(mylist)-1-i] = temp
    return mylist
mylist = [1,2,3,4,5,6]
print(reverse2(mylist))

# given = 83
# def change(given):
#     chgInc = [25,10,5,1]
#     q = 0
#     r = 0
#     for i in range(len(chgInc)):
#         q, r = divmod(given, chgInc[i])
#         q, chgInc[i] = chgInc[i], q
#         given = r
#     return chgInc

# print(change(given))

# def coins(given):
#     quarters = 0
#     dimes = 0
#     nickles = 0
#     pennies = 0
#     while given > 0:
#         while given >= 25:
#             given -= 25
#             quarters +=1
#         while given >=10:
#             given -= 10
#             dimes += 1
#         while given >=5:
#             given -= 5
#             nickles += 1
#         while given >=1:
#             given -= 1
#             pennies += 1
#         return quarters, dimes, nickles, pennies
# print(coins(given))

# string = 'racecar'
# def palindromeString(string):
#     if string[::-1] == string:
#         return True
#     else:
#         return False