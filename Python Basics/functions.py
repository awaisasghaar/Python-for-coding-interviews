# Functions in Python

def fun():
    a = input("\nEnter -> 'Hey or Hello': ")
    name = str(input("Enter your name: "))
    age = int(input("Enter your age: "))

    if a == 'Hey':
        print(f'{a}, My name is {name} and my age is {age}.')
    elif a == 'Hello':
        print(f'{a}, My name is {name} and my age is {age}.')
    else:
        print(f"{a} is not valid")

def ask():
    print("\nEnter Yes or No")
    b = input("Would you like to answer the questions?: ")
    if b == 'Yes' or b == 'yes':
        answer = input('Are you sure?: ')
        if answer in ('Yes', 'yes'):
            print("Ok Great! let's proceed")
        elif answer in ('No', 'no'):
            print('Ok see you next time.')
    elif b == 'No' or b == 'no':
        print("Ok, we won't ask questions to you.")
    
def cal():
    a = int(input("\nWhat's the Number: "))
    for i in range(1, 11):
       print(f"{a} * {i} = {a * i}")

if __name__ == '__main__':
   fun()
   ask()
   cal()
