import random

emojis = {
    'r' : '🪨' ,
    'p' : '📃' ,
    's' : '✂️'
}
choices = tuple(emojis.keys())

def get_user_choice():

    while True:
        user_choice = input('Rock , Papers or Scissors (r/p/s) ?: ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid choice')    
def display_choices(user_choice , computer_choice):
    print(f'Your chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

def win_or_lose(user_choice , computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif (
        (user_choice == 'r' and computer_choice == 's') or 
        (user_choice == 's' and computer_choice == 'p') or 
        (user_choice == 'p' and computer_choice == 'r')):
        print('You Win!') 
    else:
        print('You lose!')

def playing():

    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)
    
        display_choices(user_choice , computer_choice)

        win_or_lose(user_choice , computer_choice)

        should_continue = input('You wanna continue or not (y/n)?: ').lower()

        if should_continue == 'n':
            break


if __name__ == '__main__':

    playing()