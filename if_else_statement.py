a = [1, 2, 3, 4, 5, 6]
print(a)


val = int(input('Enter the number: '))

if val == 1 or val == 2 or val == 3:
    print(f'Value {val} ia at the list and its index is {a.index(val)}')
elif val == 4 or val == 5 or val == 6:
    print(f'Value {val} is at the list and its index is {a.index(val)}')
else:
    print(f'{val} is not in the list')

