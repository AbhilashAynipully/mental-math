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

def start():
    """
    If user inputs Y/y starts the game and asks for name
    If user inputs N/n ends the game and shows end message
    For invalid input shows error promt and informs customer
    Returns user name
    """
    response = input("Press Y or y to continue, N or n to exit :")
    if response == "Y" or response == "y":
        print("\n\n\nGreat!!! Lets start the game... \n\n")
        time.sleep(1.5)
        while True:
            name = input(
                "Enter your Name (Aplhanumeric and max 30 characters):\n")
            if name.isalnum() is not True:
                print(" >>> Invalid Response!!! <<<")
                print(
                    "\n>> No special characters including 'space' <<\n")
            elif len(name) > 30:
                print(" >>> Invalid Response!!! <<<")
                print("\n >> Only 30 characters allowed <<\n")
            else:
                break
        print(f"\n\n\nHi {name}, are you ready?")
        print("\n\nHere comes the first question!\n\n\n")
        time.sleep(2)
    elif response == "N" or response == "n":
        time.sleep(1.5)
        print("\nSorry to see you leave :( \n")
        time.sleep(1)
        print("Please do come back whenever you are ready :)")
        exit()
    else:
        print(f"\nPlease enter a valid response!, you entered: {response} \n")
        start()
    return name

def question_session_handler(name):
    """
    Creates score variable and stores user name and score in it
    Generates questions and options from spreadsheet to terminal
    Validates user input and notifies invalid response
    For valid input using answer_checker provides response to user
    Updates score (using scorer function) and prints the score on terminal
    Returns score
    """
    score = [name, 0]

    questions_sheet = SHEET.worksheet("questions")
    for num in range(2, 12):
        question_number = (num - 1)
        question = questions_sheet.cell(num, 2).value
        print(f"Q{question_number}) {question}\n")

        valid_options = ("A", "a", "B", "b", "C", "c", "D", "d",)
        while True:
            answer_given = input(
                "Please type your answer (A,B,C,D or a,b,c,d)\n")
            if answer_given not in valid_options:
                print(
                    f"\nInvalid response! you entered {answer_given}\n\n")
            else:
                break
        actual_answer = questions_sheet.cell(num, 3).value
        is_correct = answer_checker(answer_given, actual_answer)

        scorer(score, is_correct)
        time.sleep(1)
        if question_number < 10:
            print(
                f"Your Current Score : {int(score[1])} / {question_number} \n")
        input("Press any key to continue\n\n")

    return score

def answer_checker(given, actual):
    """
    Takes user input (given) and spreadsheet data (actual) for comparison
    Checks and prints error on console if invalid entry made by user
    Notifies user of right / wrong answer
    Returns correct variable if right answer enered by user
    """
    if given == actual or given.upper() == actual:
        print(
            f"\n\n>>> Well done! Your answer is Correct! <<<\n\n")
        return 'correct'
    else:
        print(
            f"\n\n>> Thats wrong :( Correct answer is option {actual} <<\n\n")

def main():
    welcome_and_instructions()
    name = start()
    final = question_session_handler(name)

main()

