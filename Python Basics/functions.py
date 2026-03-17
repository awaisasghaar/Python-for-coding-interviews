# Functions in Python

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
    
# def cal():
#     a = int(input("\nWhat's the Number: "))
#     for i in range(1, 11):
#        print(f"{a} * {i} = {a * i}")


def Student_details():
    print("\n"
    "  --------- Marks Sheet ---------  ")
    print("\n           Student Details")
    a = input("\nEnter name: ")
    b = input("Enter roll no: ")
    print(f"\nCandidate name is {a}")
    print(f"Candidate roll no is {b}")
    print('       <-------->      ')

def marks():
    for _ in range(1):
        total_marks = 100

        # Title
        title = '\n          Subject wise marks calculation'
        print(title)
        # Print total marks of Maths
        print(f"\nTotal Math marks are {total_marks}")
        obt_marks = int(input("Enter Obtained marks in Maths: "))
        
        # Condition Statements
        if obt_marks > 100:
            print(f"{total_marks} are total marks "
                  f"Therefore, {obt_marks} that you entered are invalid")
            
        elif obt_marks >= 80:
            print(f"Grade A")
        elif obt_marks >=70:
              print(f"Grade B")
        elif obt_marks >= 50:
              print(f"Grade C")
        elif obt_marks < 50:
              print(f"Alas! you are fail")

        # Print Obtained marks
        print(f"Obtained marks in Maths {obt_marks}")
        # Marks percantage calculation
        total_cal_1 = obt_marks / total_marks * 100
        print(f"Percentage of Math is {total_cal_1:.1f}")
        print('       <-------->      ')

        # Print total marks of Computer Science 
        print(f"\nTotal Marks in Computer Science {total_marks}")
        obt_marks = int(input("Enter Obtained marks in Computer Science: "))

        # Condition Statements
        if obt_marks > 100:
           print(f'''{total_marks} are total marks
                 Therefore, {obt_marks} you enter is invalid''')
        elif obt_marks >= 80:
         print(f"Grade A")
        elif obt_marks >=70:
           print(f"Grade B")
        elif obt_marks >= 50:
           print(f"Grade C")
        elif obt_marks < 50:
           print(f"Alas! you are fail")

        # Print Obtained marks
        print(f"Obtained marks in Computer Science {obt_marks}")
        # Marks percentage calculation
        total_cal_2 = obt_marks / total_marks * 100
        print(f"Percentage of Computer Science is {total_cal_2:.1f}")
        print('       <-------->      ')

        # Print total marks of English
        print(f"\nTotal Marks in English {total_marks}")
        obt_marks = int(input("Enter Obtained marks in English: "))

        # Condition Statements
        if obt_marks > 100:
           print(f'''{total_marks} are total marks
                 Therefore {obt_marks} you enter is invalid''')
        elif obt_marks >= 80:
         print(f"Grade A")
        elif obt_marks >=70:
           print(f"Grade B")
        elif obt_marks >= 50:
           print(f"Grade C")
        elif obt_marks < 50:
           print(f"Alas! you are fail")

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
    print(f"Total marks in three major subjects are {Total_marks}")
    Total = (total_cal_1 + total_cal_2 + total_cal_3) / (total_marks * 3) * 100
    print(f"Total Percentage is {Total:.1f}")


if __name__ == '__main__':
#    fun()
#    ask()
#    cal()
   Student_details()
   total_cal_1, total_cal_2, total_cal_3, total_marks = marks()
   total(total_cal_1, total_cal_2, total_cal_3, total_marks)
