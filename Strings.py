# Strings are similar to arrays
s = 'abc'
print(s[0:2])

# IT creates a new string
s += 'efghk'
print(s)

# Strings can be converted into Integers
a = (int('1234') + int('5678'))
print(a)

b = (str(123) + str(456))
print(b)

# If ASCIi value is needed
print(ord('a'))
print(ord('b'))
print(ord('c'))
print(ord('d'))

# Combine a list of string with empty string
strings = ['ab', 'cd', 'ef']
print(' '.join(strings))
