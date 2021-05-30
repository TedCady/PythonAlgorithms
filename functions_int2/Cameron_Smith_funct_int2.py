#1
#1A
x = [ [5,2,3], [10,8,9] ]
def nestlist(input):
    input[1][0] = 15
    return input
print(nestlist(x))

#1B
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
def nameSwap(input):
    input[0]['last_name'] = 'Bryant'
    return input
print(nameSwap(students))

#1C
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
def dirSwap(input):
    input['soccer'][0] = 'Andres'
    return input
print(dirSwap(sports_directory))

#1D
z = [ {'x': 10, 'y': 20} ]
def valSwap(input):
    input[0]['y'] = 30
    return input
print(valSwap(z))

#2
def iterateDictionary(mylist):
    for i in range(len(mylist)):
        print("first_name -", mylist[i]['first_name'],"last_name -", mylist[i]['last_name'])
students = [{'first_name':  'Michael,', 'last_name' : 'Jordan'},
            {'first_name' : 'John,', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark,', 'last_name' : 'Guillen'},
            {'first_name' : 'KB,', 'last_name' : 'Tonel'}]
iterateDictionary(students)

#3
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
def iterateDictionary2(a, list):
    for i in range(len(list)):
        print(list[i][a])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
#4.0
def printInfo(lib):
    for i in range(len(lib)-1):
        numL = len(lib['locations'])
        print(numL, 'LOCATIONS')
    for i in range(len(lib['locations'])):
        print(lib['locations'][i])
    for i in range(len(lib)-1):
        numI = len(lib['instructors'])
        print(numI, 'INSTRUCTORS')
    for i in range(len(lib['instructors'])):
        print(lib['instructors'][i])
printInfo(dojo)


#4.1
def printInfo(lib):
    for i in lib:
        print(len(lib[i]), i.upper())
        for list in lib[i]:
            print(list)
printInfo(dojo)
