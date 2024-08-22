import csv
from random import randrange

def get_codes(file_name):

    # This function takes the csv file and uses the keys country and code to get 
    # a list of airport codes in the USA only.

    with open(file_name, encoding='UTF-8') as airport_list:
        codes = []
        dict_reader = csv.DictReader(airport_list)
        for dict in dict_reader:
            if dict['country'] == 'US':
                codes.append(dict['code'])
        return codes

def wordle_player(code):
    #This function is ran to actually use the wordle logic and game rules
    print('A code has been selected! \nThe game will now begin!')
    code_dict = {code[i]: i for i in range(len(code))}
    incorrect_letters = []
    present_letters = []
    guessed_code = ['_', '_', '_']
    attempts = 0

    while True:

        if attempts == 6:
            print(f'You lost! You could not get the code within 5 attemps. The correct code was {code}.')
            return 
        
        print(f'The current guessed code is {guessed_code} \n you have the letters {present_letters} in the code but not in the correct spot \n {incorrect_letters} are letters that are not present that you have guessed. You are on your number {attempts} attempt. \n')
        guess = input('\nEnter in your guess: ').strip().upper()
        
        if len(guess) == 3:
            attempts += 1
            if guess == code:
                print(f"Congratulations! You've guessed the code correctly: {code}, within {attempts} attemps.")
                return 
            else:
                for idx, letter in enumerate(guess):
                    if letter in code and idx == code_dict[letter]:
                        guessed_code[idx] = letter
                    elif letter in code:
                        present_letters.append(letter)
                    else:
                        incorrect_letters.append(letter)
        else:
            print('The code has to be 3 letters.')


def start_game(file_name):

    # This function starts the actual game 

    playing = True
    while playing:
        user_plays = input("Do you want to play airportle, a version of wordle that uses USA's 3 letter airport codes instead of words? ").strip().lower()
        if user_plays == 'yes':
            list_of_codes = get_codes(file_name)
            chosen_code = list_of_codes[randrange(0,len(list_of_codes))]
            wordle_player(chosen_code)

        else:
            print('Ok!')
            continue

start_game('airports.csv')