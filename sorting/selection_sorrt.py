def selSort(input):
    for i in range(len(input)):
        min = i
        for x in range(i+1, len(input)):
            if input[min] > input[x]:
                min = x
        temp = input[i]
        input[i] = input[min]
        input[min] = temp
    return input
x = [7,4,5,-3,2,6]
print(selSort(x))