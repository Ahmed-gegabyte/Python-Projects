import random

playing = True
count = 0
number = random.randint(1 , 10)
while playing:

    
    try:
        guess = int(input('Enter a number between (1 - 10): '))

        if guess == number:
        
            print(f'Wallah you guessed the {number} in {count} tries ')
        
            playing = False
        elif guess > number:

            print('The guess is higher than the number')
            count = count + 1
        elif guess < number:
            print('The guess is less than the number')
            count = count + 1
    except ValueError:
        print('Your input is invalid')
        

    
