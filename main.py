import os 
from SafeSleepClearr import safe_sleep_clear 

Names = ['Dan']
Types = ['Dog']
Ages = ['20.0']
Temperaments = ['Friendly']

def main():
    os.system('clear')
    os.system('clear')
    print('-- Pet Adoption Centre --\n')
    print('''Would you like to...
    (A) View all pets already in the shelter?
    (B) Add a new pet to the shelter?\n''')
    user = input(': ').upper()

    if user == 'A':
        os.system('clear')
        print('-- Pet Adoption Centre --\n')
        if Names:
            for i in range(len(Names)):
                print(f'Name: {Names[i]}')
                print(f'Type: {Types[i]}')
                print(f'Age: {Ages[i]}')
                print(f'Temperament: {Temperaments[i]}')
                print('---')
                
        else:
            print('No pets in the shelter yet!')
        input('\nPress Enter to continue...')

    elif user == 'B':
        os.system('clear')
        print('-- Pet Adoption Centre --\n')
        print('Please enter your pets name.')
        name = input(': ').capitalize()
        if len(name) > 15:
            print('Please shorten the name in some way.')
            safe_sleep_clear(3)
            main()
        else:
            Names.append(name)

        os.system('clear')
        print('-- Pet Adoption Centre --\n')
        print('Please enter your pets type (dog, cat, rabbit, bird).')
        ptype = input(': ').capitalize()
        if ptype not in ['Dog','Cat','Rabbit','Bird']:
            print('Only dogs, cats, rabbits and birds are able to be brought here.')
            safe_sleep_clear(4.5)
            main()
        else:
            Types.append(ptype)

        os.system('clear')
        print('-- Pet Adoption Centre --\n')
        print('Please enter your pets age.')
        age = float(input(': '))
        if age > 20:
            print('Too old.')
            safe_sleep_clear(2)
            main()
        else:
            Ages.append(age)

        os.system('clear')
        print('-- Pet Adoption Centre --\n')
        print('Please enter your pets usual temperament.')
        print('Friendly, Shy, Playful or Aggressive...')
        temperament = input(': ').capitalize()
        if temperament not in ['Friendly','Shy','Playful','Aggressive']:
            print('Invalid temperament')
            safe_sleep_clear(2)
            main()
        else:
            Temperaments.append(temperament)

        os.system('clear')
        print('-- Pet Added Successfully! --')
        safe_sleep_clear(2)

    else:
        print('Invalid option selected.')
        safe_sleep_clear(2)

while True:
    main()
    print('\nRestarting in...')
    for i in range(3, 0, -1):
        print(f'{i}...')
        safe_sleep_clear(1)
    os.system('clear')