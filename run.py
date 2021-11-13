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
    Selects random word from Google Sheet database
    """
    words = SHEET.worksheet("words").col_values(1)

    return random.choice(words)


def get_user_guess():
    """
    Get user letter guess for word
    """
    print("Enter your letter guess here.\n")

    data_str = input("Enter your guess here: ")
    print(f"The data provided is {data_str}")

def play_game():
    """
    Plays game steps
    """
    answer = select_word() 
    image = HANGMANPICS[0]
    print(image)
    print ('_' * len(answer))

play_game()
