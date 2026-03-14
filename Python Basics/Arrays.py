# '''Array in Python are called as list'''

# arr = [1, 2, 3, 4, 5]
# print(f'{arr} This is an example of an array in Python ')

# # Can also be used as stack
# arr.append(6) # Time complexity O(1)
# arr.append(7) # Time complexity O(1)
# print(arr) 

# arr.insert(7, 8) # Time complexity O(n)
# print(arr)


# arr[6] = 9 # Time complexity O(1)
# arr[7] = 10 # Time complexity O(1)
# print(arr) 

# # Initializing array of size n with default value of n
# n = 5
# arr = [2] * n
# print(len(arr))
# print(arr)

# # Indexing the array
# arr = [1, 2, 3]
# print(arr[0], arr[1], arr[2])

# # Indexing the negative value
# arr = [1, 2, 3]
# print(arr[-1], arr[-2], arr[-3])

# # Sublist (Slicing the array)
# arr = [1, 2, 3, 4, 5, 6]
# print(arr[0:5], arr[1:5], arr[1:4])

# # Unpacking
# a, b, c = [1, 2, 3]
# print(a, b, c)

# Loop using array 
'''Using Index'''
arr = [1, 2, 3, 4, 5, 6]
for i in range(len(arr)):
    print('\n', arr[i])

'''Without Index'''
for i in arr:
    print('\n', i)

'''With Index and Value'''
for i, arr in enumerate(arr):
    print(f'{i} is the Index and {arr} is Value')

# Loop through Multiple arrays with unpacking
arr_1 = [1, 2, 3]
arr_2 = [4, 5, 6]
for num_1, num_2 in zip(arr_1, arr_2):
    print(f'first array {num_1}, Second array {num_2}')

# Reverse the array
arr = [1, 2, 3, 4, 5, 6]
arr.reverse()
print(f'Rverse the array {arr}')

# Sorting in ascending order 
arr = [13, 43, 24, 261, 78, 0, 12]
arr.sort()
print(f'Sorted the array {arr}')

# Sorting in descending order
arr = [13, 43, 24, 261, 78, 0, 12]
arr.sort(reverse=True)
print(f'Sorted the array {arr}')

# Sorting on strings
str = ['Awais', 'Hamza', 'Usman']
str.sort()
print(str)

# Custom sort (by length of string)
str.sort(key=lambda x:len(x))
print(str)

# List Comprehension
arr = [i for i in range(4)]
print(arr)

arr = [i+i for i in range(4)]
print(arr)

# 2-D List
arr = [[2 * 4 for i in range(4)]]
print(arr)





