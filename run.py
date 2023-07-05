import gspread
import time
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('mental_math')

def welcome_and_instructions():
    """
    Prints welcome message on console
    Prints instructions for the user to follow
    """
    print("Welcome to Mental Math Game!!!")
    print("-------------------------------")
    print("-------------------------------\n")
    time.sleep(1.5)
    print("Please read the below instructions carefully :")
    print("**********************************************\n")
    print("- There will be a total of 10 questions\n")
    print("- Each question will have 4 options 'A','B','C,'D'\n")
    print("- To choose option 'A' as answer type A or a and press enter\n")
    print("- There are no negative marking for wrong answers\n")

