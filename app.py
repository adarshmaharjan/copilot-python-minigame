import random


#  create me a function that accepts the input from user as rock , paper or sisors form the given options
#  and return the output as win or lose or tie based on the random selection of computer
#  and also return the computer selection
# if te option is invalid return the message as invalid option
def game_with_computer(user):
    options = ['rock', 'paper', 'scissors']
    computer = random.choice(options)
    if user in options:
        if user == computer:
            return 'tied', computer
        elif user == 'rock':
            if computer == 'paper':
                return 'lose', computer
            else:
                return 'win', computer
        elif user == 'paper':
            if computer == 'scissors':
                return 'lose', computer
            else:
                return 'win', computer
        elif user == 'scissors':
            if computer == 'rock':
                return 'lose', computer
            else:
                return 'win', computer
    else:
        return 'invalid option', computer


# crate me a function that ask user to continue or discontinue the game 
# if user select continue then ask the user to enter the choice
# if user select discontinue then exit the game

def game():
    while True:
        user = input('Do you want to continue (yes/no): ')
        if user.lower() == 'no':
            break
        elif user.lower() == 'yes':
            user = input('Enter your choice (rock, paper, scissors): ')
            result, computer = game_with_computer(user)
            print(f'You {result}! Computer selected {computer}')
        else:
            print('Invalid option!') 

def main():
    user = input('Enter your choice (rock, paper, scissors): ')
    result, computer = game_with_computer(user)
    print(f'You {result}! Computer selected {computer}')
    game();

if __name__ == '__main__':
    main()