'''Arrays in Python are called as list'''

arr = [1, 2, 3, 4, 5]
print(f'{arr} This is an example of an array in Python ')

# Can also be used as stack
arr.append(6) # Time complexity O(1)
arr.append(7) # Time complexity O(1)
print(arr) 

arr.insert(7, 8) # Time complexity O(n)
print(arr)


arr[6] = 9 # Time complexity O(1)
arr[7] = 10 # Time complexity O(1)
print(arr) 