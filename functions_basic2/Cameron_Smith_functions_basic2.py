#1
def ctdwn(a):
    for x in range(a, -1, -1):
        list.append(x)
    print(list)
list = []
ctdwn(5)

#2
def PandR(a,b):
    print(a)
    return(b)
var = PandR(1,2)
print(var)

#3
def first_plus_len(a):
    return (a[0] + len(a))
list = first_plus_len([5,3,4,2,3])
print(list)

#4
def vgt_second(a):
    for x in range (len(a)):
        if len(a) < 2:
            return False
        if a[x] > a[1]:
            list.append(a[x])
    print(len(list))
    return list
a = [3,2,4,1,1,0,5]
list = []
print(vgt_second(a))

#5
def L_and_V(size,value):
    list = []
    for x in range(size):
        list.append(value)
    print(list)
L_and_V(7,2)