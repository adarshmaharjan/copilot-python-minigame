import random


#  create me a function that accepts the input from user as rock , paper or sisors form the given options
#  and return the output as win or lose or tie based on the random selection of computer
#  and also return the computer selection
def game_with_computer(user):
    options = ['rock', 'paper', 'scissors']
    computer = random.choice(options)
    if user == computer:
        return 'tie', computer
    elif user == 'rock' and computer == 'scissors':
        return 'win', computer
    elif user == 'paper' and computer == 'rock':
        return 'win', computer
    elif user == 'scissors' and computer == 'paper':
        return 'win', computer
    else:
        return 'lose', computer
    

def main():
    user = input('Enter your choice (rock, paper, scissors): ')
    result, computer = game_with_computer(user)
    print(f'You {result}! Computer selected {computer}')

if __name__ == '__main__':
    main()