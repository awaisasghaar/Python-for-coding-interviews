# # Use of for loop with list
a = [1, 2, 3, 4, 5, 6]
a.append(7) 
print(f'{a}\n')
for num in a:
        print(f"{num} is at index {a.index(num)}")

# # Increment for loop
a = input('\nEnter -> (Increment) for loop: ')
for i in range(0, 10):
     if a == 'Increment' or a == 'increment':
          print(f'{a} the loop {i}')
     else:
          print('Please enter the given option only')
          break

# # Decrement the loop
b = input(f'\nEnter -> (Decrement) for loop: ')
for k in range(10, 0, -1):
     if b == 'Decrement' or b == 'decrement':
          print(f'{b} the loop {k}')
     else:
          print('Please enter the given option only')
          break
     
'''Use of input variable with 
using if and else statement before executing
while loop'''

a = str(input('\n Enter your name: '))
      
if a.isalpha():
    print(f"Hello, {a} \n")
else:
        print('Enter only alphabatic characters \n')

# While loop 
num = 0
while num <= 10:
       num += 1
       print(f'While loop executed {num}')

        
     
        


