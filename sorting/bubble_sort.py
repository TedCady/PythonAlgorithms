mylist = [1,8,4,3,9,5,6,2,7]

def bubblesort(input):
    for x in range(len(input)-1):
        for i in range(len(input)-1-x):
            if input[i] > input[i+1]:
                input[i], input[i+1] = input[i+1], input[i]
    return input
print(bubblesort(mylist))