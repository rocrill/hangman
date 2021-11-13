import gspread
from google.oauth2.service_account import Credentials
import random 

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
    print("Enter your letter guess here.\n")

    data_str = input("Enter your guess here: ")
    print(f"The data provided is {data_str}")
    return data_str



def play_game():
    """
    Plays game steps
    """
    answer = select_word() 
    image = HANGMANPICS[0]
    print(image)
    print(answer)
    print()
    print ('_ ' * len(answer))
    checks_guess(answer)    


def checks_guess(answer):
    """
    Checks if guessed letter is in answer word.
    """
    guess = get_user_guess()
    if guess in answer:
        print(f'{guess} is a letter of the word!')
    else:
        print(f'{guess} is not a letter of the word :(')


play_game()
get_user_guess()
checks_guess()