# Functions in Python
def match():

    n1 = input(f'Enter the team1 name: ')
    n2 = input(f'Enter the team2 name: ')
    if n1.isalpha():
        print(f'{n1} vs {n2}')
    elif n2.isalpha():
        print('Okay')
    else:
        print('Invlaid name')
    
def players():
    try:
        n = str(input('Would you like to tell the rankings? '))
        if n == 'Yes' or n == 'yes':
            print(f"Okay let's get started!")
        elif  n == 'y' or n == 'Y':
               print(f"Okay let's get started!")
        elif  n == 'No' or n == 'no':
               print(f'game is done')
        else:
             print('Enter yes or no')

    except ValueError:
        print('Enter valid inputs only.')


if __name__ == '__main__':
    match()
    players()
    
