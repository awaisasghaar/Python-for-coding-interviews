# Hash map

map = {}
map['Awais'] = 'BC230200789'
map['Umair'] = 'BC234566788'
print(map)
print(f'Length of map values are {len(map)}')

# Changing the value
map['Awais'] = 'BC230200788'
print(map['Awais'])
print(map)

# checking if the key exists
print('Awais' in map) # True
print('Steve' in map) # False

# We can also pop the Key
map.pop('Umair')
print(map)

# Intialize the Hash map
map = {'Awais': ('BC230200789'), 'Umair': ('BC234566788')}
print(map)
print(f'Length of map is {len(map)}')

# Dict comprehension
map = {i: 2*i for i in range(7)}
print(map)

# Loop through map
map = {'Awais': 22, 'Umair': 23, 'Sufyan': 21}
for key in map:
    print(key, map[key])

map = {'Awais': 22, 'Umair': 23, 'Sufyan': 21}
for value in map.values():
    print(value)

for key, value in map.items():
    print(key, value)

# Tuples are like arrays but immutable
tup = (1, 2, 3, 4)
print(tup)
print(f'tuple is {tup[0]}')
print(f'tuple is {tup[1]}')
print(f'tuple is {tup[2]}')
print(f'tuple is {tup[3]}')

# But we can't modify tuple because it is immutable
# tup[0] = 3
# print(tup) # Output: TypeError: 'tuple' object does not support item assignment

# Tuples can be used for key as Hah map/set
# hash map
map = {(1, 2, 3): 'Computer science'}
print(map[(1, 2, 3)]) # Output: Computer Science

# hash set
set = set()
set.add((1, 2, 3))
print((1, 2, 3) in set) # Output True
print((1, 2) in set) # Output False

# List can't be key
# map[[3, 4, 5]] = 6 # Output: TypeError: unhashable type: 'list'










