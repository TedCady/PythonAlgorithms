x = [4,5,3,2,6]

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
print(selSort(x))

# my_arr = [-64, 25, -12, 22, 11]

# for i in range(len(my_arr)):
#     min_idx = i
#     for j in range(i+1, len(my_arr)):
#         if my_arr[min_idx] > my_arr[j]:
#             min_idx = j
#     temp = my_arr[i]
#     my_arr[i] = my_arr[min_idx]
#     my_arr[min_idx] = temp

# print(my_arr)