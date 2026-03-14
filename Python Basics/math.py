'''Division in Python is decimal by default'''
print(f'{100 / 2:.1f}')

'''Double slash round down'''
print(f'{100 // 2:.1f}')

'''Negative numbers wil also round down'''
print(f'{-100 // 2:.1f}')

# Moddling in Python

print(f'{100 % 3:.0f}')
print(f'{-100 % 3:.0f}')

import math
print(math.floor(3/ 2))
print(math.ceil(3 / 2))
print(f'{math.sqrt(2):.3f}')
print(math.pow(2, 3))

# Max/Min Int

float('inf')
float('-inf')

'''Python numbers are infinit so they never overflow'''
import math
print(math.pow(2, 200))
print(math.pow(2, 200) < float('inf'))
print(math.pow(2, 200) < float('-inf'))

