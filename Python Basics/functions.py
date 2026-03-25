# # Functions in Python
# def fun():
#     a = input("\nEnter -> 'Hey or Hello': ")
#     name = str(input("Enter your name: "))
#     age = int(input("Enter your age: "))

#     if a == 'Hey':
#         print(f'{a}, My name is {name} and my age is {age}.')
#     elif a == 'Hello':
#         print(f'{a}, My name is {name} and my age is {age}.')
#     else:
#         print(f"{a} is not valid")

# def ask():
#     print("\nEnter Yes or No")
#     b = input("Would you like to answer the questions?: ")
#     if b == 'Yes' or b == 'yes':
#         answer = input('Are you sure?: ')
#         if answer in ('Yes', 'yes'):
#             print("Ok Great! let's proceed")
#         elif answer in ('No', 'no'):
#             print('Ok see you next time.')
#     elif b == 'No' or b == 'no':
#         print("Ok, we won't ask questions to you.")

# # Tables
# def cal():
#     a = int(input("\nWhat's the Number: "))
#     for i in range(1, 11):
#        print(f"{a} * {i} = {a * i}")

# Student marks sheet
def sheet():
    subjects = {'Maths': None, 'Computer Science': None, 'English': None}
    print('\n')
    for subject in subjects.keys():
        while True:
           a = input(f"Enter marks in {subject}: ")
           if a.isdigit():
              subjects[subject] = int(a)
              break
           else:
               print("Please enter a valid input")
    return subjects

#  Calculating the sum of subjects values   
def total_subject_marks(subjects):
    total = sum(subjects.values())
    print('\n')
    for subject, marks in subjects.items():
        print(f"Marks in {subject} are {marks}")
    print(f"\nTotal marks are {total}/300")
    return total
    
# Calulaing the percentage
def percentage(total):
    perc = total / 300 * 100
    print(f"Total Percentage is {perc:.2f}")
    if perc >= 90:
        return f"Grade A+ (Pass)"
    elif perc >= 80:
        return f"Grade A (Pass)"
    elif perc >= 70:
        return f"Grade B+ (Pass)"
    elif perc >= 60:
        return f"Grade B (Pass)"
    elif perc >= 50:
        return f"Grade C (Pass)"
    else:
        return f'Fail'


if __name__ == '__main__':
    try:
       subjects = sheet()
    except TypeError as e:
        print(f"{e}")
    total = total_subject_marks(subjects)
    result = percentage(total)
    print(f"Result: {result}")
     

