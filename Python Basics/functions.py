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
   print("\n           Student Details")

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

def marks():
    for _ in range(3):
        total_marks = 100

        # Title
        title = '\n          Subject wise marks calculation'
        print(title)

        # Print total marks of Maths
        print(f"\nTotal Math marks are {total_marks}")

        # User Input
        obt_marks = int(input("Enter Obtained marks in Maths: "))
   
        # Condition Statements
        if obt_marks > 100:
            raise ValueError(f"{obt_marks} exceed total marks {total_marks}")
        elif obt_marks >= 80:
            print(f"Grade A")
        elif obt_marks >=70:
            print(f"Grade B")
        elif obt_marks >= 50:
            print(f"Grade C")
        elif obt_marks < 50:
            print(f"Feed back: You need to wrok hard.")

        # Print Obtained marks
        print(f"Obtained marks in Maths {obt_marks}")
        # Marks percantage calculation
        total_cal_1 = obt_marks / total_marks * 100
        print(f"Percentage of Math is {total_cal_1:.1f}")
        print('       <-------->      ')

        # Print total marks of Computer Science 
        print(f"\nTotal Marks in Computer Science {total_marks}")

        # User Input
        obt_marks = int(input("Enter Obtained marks in Computer Science: "))
           
        # Condition Statements
        if obt_marks > 100:
           raise ValueError(f"{total_marks} are total marks "
            f"Therefore, {obt_marks} you enter is invalid.")
        elif obt_marks >= 80:
         print(f"Grade A")
        elif obt_marks >=70:
           print(f"Grade B")
        elif obt_marks >= 50:
           print(f"Grade C")
        elif obt_marks < 50:
           print(f"Feedback: You need to work hard.")

        # Print Obtained marks
        print(f"Obtained marks in Computer Science {obt_marks}")
        # Marks percentage calculation
        total_cal_2 = obt_marks / total_marks * 100
        print(f"Percentage of Computer Science is {total_cal_2:.1f}")
        print('       <-------->      ')

        # Print total marks of English
        print(f"\nTotal Marks in English {total_marks}")

        # User Input
        obt_marks = int(input("Enter Obtained marks in English: "))
    
        # Condition Statements
        if obt_marks > 100:
           raise ValueError(f"{total_marks} are total marks "
                 f"Therefore {obt_marks} you enter is invalid.")
        elif obt_marks >= 80:
         print(f"Grade A")
        elif obt_marks >=70:
           print(f"Grade B")
        elif obt_marks >= 50:
           print(f"Grade C")
        elif obt_marks < 50:
           print(f"Feedback: You need to work hard.")

        # Print Obtained marks
        print(f"Obtained marks in English {obt_marks}")
        # Marks percentage calculation
        total_cal_3 = obt_marks / total_marks * 100
        print(f"Percentage of English is {total_cal_3:.1f}")
        print('       <-------->      ')

        return total_cal_1, total_cal_2, total_cal_3, total_marks

def total(total_cal_1, total_cal_2, total_cal_3, total_marks):
    # Total
    print("\n   --------- Total ---------   ")
    Total_marks = total_cal_1 + total_cal_2 + total_cal_3 
    print(f"Obtained marks: {Total_marks:.0f}")
    TOTAL_MARKS = 300
    print(f"Total marks: {TOTAL_MARKS}")
    Total = (total_cal_1 + total_cal_2 + total_cal_3) / (total_marks * 3) * 100
    print(f"Overall percentage is {Total:.1f}")
    perct = Total
    if perct >= 90:
       print(f"Grade A")
    elif perct >=75:
       print(f"Grade A")
    elif perct >=50:
       print("Grade C")
    elif perct < 50:
       print("Fail!")
    

if __name__ == '__main__':
#    fun()
#    ask()
#    cal()

   Student_details()
   try:
    total_cal_1, total_cal_2, total_cal_3, total_marks = marks()
   except ValueError as e:
      print(f'{e}')

   try:
    total(total_cal_1, total_cal_2, total_cal_3, total_marks)
   except NameError as n:
      print(f'{n}')
