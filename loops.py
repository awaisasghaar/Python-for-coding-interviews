# Use of for loop with list
print('For loop is executed \n')
a = [1, 2, 3, 4, 5, 6] 
for num in a:
    if num in [1, 2, 3, 4, 5, 6]:
        print(f"{num} is at index {a.index(num)} \n")

# While loop
a = str(input('Enter your name: '))
print(f"Hello, {a} \n")
num = 0
while num < 8:
       print('While loop executed')
       num += 1
       print(num)

