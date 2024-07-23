HANGMANPICS = {
    'stage1': 
    ''' 
  +---+ 
  |   | 
      | 
      | 
      | 
      | 
=========''',
    'stage2': 
    ''' 
  +---+ 
  |   | 
  O   | 
      | 
      | 
      | 
=========''',
    'stage3': 
    ''' 
  +---+ 
  |   | 
  O   | 
  |   | 
      | 
      | 
=========''',
    'stage4': 
    ''' 
  +---+ 
  |   | 
  O   | 
 /|   | 
      | 
      | 
=========''',
    'stage5': 
    ''' 
  +---+ 
  |   | 
  O   | 
 /|\  | 
      | 
      | 
=========''',
    'stage6': 
    ''' 
  +---+ 
  |   | 
  O   | 
 /|\  | 
 /    | 
      | 
=========''',
    'stage7': 
    ''' 
  +---+ 
  |   | 
  O   | 
 /|\  | 
 / \  | 
      | 
========='''
}

import random

word_bank = [
    "apple",  # 5 letters
    "grape",  # 5 letters
    "peach",  # 5 letters
    "mango",  # 5 letters
    "berry",  # 5 letters
    "orange",  # 6 letters
    "banana",  # 6 letters
    "tomato",  # 6 letters
    "carrot",  # 6 letters
    "pickle"   # 6 letters
]

# Display the word bank


while True:
    correct_letters = []
    wrong_letters = []
    hangman_stage = 0
    play = input('Would you like to play hangman? ').lower()
    if play == 'no':
        print('Ok bye')
        break
    else: 
        word = word_bank[random.randint(0, (len(word_bank)-1))]
        print("We have chosen a word, we are starting.")
        while True:
             choice = input('Guess a letter: ').lower()
             if choice in word:
                 print('Correct')
                 correct_letters.append(choice)
                 if len(correct_letters) == len(word):
                     print('You guessed the correct word: ' + word + '!')
                     break
                 print('Here are your correct choices: ' + str(correct_letters))
                 print('Here are your incorrect choices: ' + str(wrong_letters))
             else: 
                 hangman_stage += 1
                 formated = 'stage' + str(hangman_stage)
                 wrong_letters.append(choice)
                 print(HANGMANPICS[formated])
                 print('That letter is not in the word!')
                 print('So far your correct letters have been ' + str(correct_letters))
                 print('Here are your incorrect choices: ' + str(wrong_letters))
                 if hangman_stage == 7:
                     print('You LOST!')
                     break
                 
                 
                 

            
            
       
