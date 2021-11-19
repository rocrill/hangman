import gspread
import random
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

def select_word():
    """
    Selects random word from Google Sheet database.
    """
    words = SHEET.worksheet("words").col_values(1)

    return random.choice(words)


def get_user_guess():
    """
    Get user letter guess for word.
    """
    
    data_str = input("Enter your guess here: ")
    return data_str

def is_game_active(wrong_guess_count, game_points, answer):
    if wrong_guess_count == 6 or game_points == len(answer):
        return False
    return True    

def play_game():
    """
    Plays game steps
    """
    wrong_guess_count = 0
    correct_guesses = ''
    answer = select_word() 
    game_active = True
    while game_active:
        image = HANGMANPICS[wrong_guess_count]
        print(image)
        #print(answer) #to be removed when game ready
        print()
        game_points = 0
        for letter in answer:
            if letter in correct_guesses:
                print(letter +' ', end='')
                game_points += 1
            else: 
                print('_ ', end='')    
        print()   
        """
        Variable to check if the game is active or not. 
        Every loop, we check to see if the game is active or not. 
        """   
        game_active = is_game_active(wrong_guess_count, game_points, answer) 
        """
        if wrong_guess_count == 6:
            print("GAME OVER!")
            print(answer)
            return
        elif game_points == len(answer):
            print("Congratulations, you won!")
            return """
        guess = get_user_guess()
        print(f"Guesses made so far are: {correct_guesses}")
        if guess in answer:
            correct_guesses += guess
            print(f'{guess} is a letter of the word!')
        else:
            print(f'{guess} is not a letter of the word :(')
            wrong_guess_count += 1




play_game()

