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
def Student_details():
   print("\n"
    "  --------- Marks Sheet ---------  ")
   a = "    Student Details"
   width = len(a) + 9
   print("\n" + "     " + "*" * width)
   print(f"     |   {a}    |") 
   print("     " + "*" * width)

   # Exception Handling
   try:
    a = input("\nEnter name: ").strip()
    if not a.isalpha():
      raise ValueError(f"{a} is not a string")
    b = int(input("Enter roll no: "))
   except ValueError as t:
    print(f'{t}')
   else:
    print(f"\nCandidate name is {a}")
    print(f"Candidate roll no is {b}")
    print('       <-------->      ')

def main():
   subjects = {'Maths': None, 'Computer Science': None, 'English': None}
   num = 100
   for subject in subjects.keys():
       a = int(input(f'\nEnter Marks in {subject}: '))
       print(f"The marks in {subject} are {a}")
       print(f"Total marks in {subject} are {num}")
       subjects[subject] = a

      # Calculating the percentage 
       per = a / 100 * 100
       print(f"Percentage is {per:.1f} %")
       
       if a > 100:
           raise ValueError(f"The value {a} is greater than {num} "
                            f"So therefore, it is invalid")
       elif a < 0:
           raise ValueError(f"The value {a} is negative number "
                            f"So therefore, it is invalid")
       elif a >= 85:
           print('Grade A')
       elif a >= 75:
           print("Grade B+")
       elif a >= 65:
           print('Grade B')
       elif a > 50:
           print("Grade C")
       elif a < 50:
           print("Fail")
       
       print('\n        <--------->   \n')
       print(subjects)
       
   return subjects
   
total = 300  
a = 'Result'
width = len(a) + 9
def call(subjects):  
    print("\n" + "     " + "*" * width)
    print(f"     |   {a}    |") 
    print("     " + "*" * width)
    total_marks = sum(subjects.values())
    perc = total_marks / total * 100
    print(f"\nObtained marks are {total_marks}")
    print(f"Total marks are {total}")
    print(f"Overall percentage is {perc:.1f}")
   
    if perc >= 85:
           print('Grade A')
    elif perc >= 75:
           print("Grade B+")
    elif perc >= 65:
           print('Grade B')
    elif perc > 50:
           print("Grade C")
    elif perc < 50:
           print("Fail")
  

if __name__ == '__main__':
    Student_details()
    try:
       subjects = main()
    except ValueError as e:
        print(f"{e}")
    try:
        call(subjects)
    except NameError as e:
        print(f"{e}")