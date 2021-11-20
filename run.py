import gspread
import random 
import string
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_words')

HANGMANPICS = [
    '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def welcome_message():
    print("Welcome to hangman!") 

def select_difficulty_level():
    """
    User selects difficulty level.
    """
    level = None
    while level != 'e' and level != 'd':
        level = input("Please choose a difficulty level. Enter 'e' for easy or 'd' for difficult:\n")   
    return level 

def select_word(level):
    """
    Selects random word from Google Sheet database, based on user's chosen difficulty level.
    """
    if level == 'e':
        words = SHEET.worksheet("words").col_values(1)
        return random.choice(words)
    elif level == 'd':
        words = SHEET.worksheet("words").col_values(2)
        return random.choice(words)

def get_user_guess():
    """
    Get user letter guess for word.
    """
    
    data_str = input("Enter your guess here:\n")
    return data_str

def play_game():
    """
    Plays game steps
    """
    wrong_guess_count = 0
    correct_guesses = ''
    guess_list = []
    level = select_difficulty_level()
    answer = select_word(level).lower() 
    while True:
        image = HANGMANPICS[wrong_guess_count]
        print(image)
        print()
        game_points = 0
        for letter in answer:
            if letter in correct_guesses:
                print(letter +' ', end='')
                game_points += 1
            else: 
                print('_ ', end='')    
        print()        
        
        
        #Exit game condition.
        if wrong_guess_count == 6:
            if game_points == len(answer) - 1:
                print("Game over! You were so close though! Better luck next time :D") 
            else:
                print("Game over! Better luck next time!")
            print(f"The answer was: {answer}")
            return
        elif game_points == len(answer):
            if wrong_guess_count > 4:
                print("Congratulations, you won! You were cutting it close though...you must need more practice :P" )
            else:
                print("Congratulations, you won!")
            return     

        guess = get_user_guess()
        print('\n'*12)    

        #data validation.
        if len(guess)>1:
            print("Looks like you didn't enter a single letter! Please try again.")
            continue
        elif guess not in string.ascii_lowercase:
            print("Looks like you didn't enter a letter! Please try again.")
            continue

        if guess not in guess_list:
            guess_list.append(guess)

        if guess in answer:
            correct_guesses += guess
            print(f'{guess} is a letter of the word!')
        else:
            print(f'{guess} is not a letter of the word :(')
            wrong_guess_count += 1
        
        print("Guesses made so far are: " + ', '.join(guess_list))

welcome_message()
play_game()

