# Functions in Python
def match():
    dict = {1: 'Pakistan', 2: 'New Zealand', 3: 'Australia', 4: 'South Africa'}
    for key, value in dict.items():
       print(key, value)
    n1 = input(f'Enter the team1 name: ')
    n2 = input(f'Enter the team2 name: ')

    if n1 in dict.values():
        print(f'{n1} vs {n2}')
    elif n2 in dict.values():
        print(f'{n1} vs {n2}')
    else:
        print(f'{n1} and {n2} are not in the dictionary')
    
def players():
    try:
        n = str(input("What's your favorite teams: "))
        if n == 'Pakistan' or n == 'PAKISTAN':
            print(f"Ummm {n} are actualy not so good")
        elif  n == 'New Zealand' or n == 'NEW ZEALAND':
               print(f"Yeah! {n} are very good team")
        elif  n == 'Australia' or n == 'australia':
               print(f'{n} are world champions.')
        elif  n == 'South Africa' or n == 'south africa':
               print(f'{n} are world champions.')
        else:
             print(f'{n} is not in the dictionary')

    except ValueError:
        print('Enter valid inputs only.')


if __name__ == '__main__':
    match()
    players()
    
