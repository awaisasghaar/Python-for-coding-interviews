# Hash set

my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(3)
print(my_set)
print(f"Length of set is {len(my_set)}")

print(1 in my_set)
print(2 in my_set)
print(3 in my_set)

my_set.remove(2)
print(my_set, 2 in my_set)

# List to set
print(set([1, 2 ,3]))

# Set Comprehension
my_set = {i for i in range(6)}
print(my_set)



