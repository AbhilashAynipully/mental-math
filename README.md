# Mental Math

Mental Math is a terminal game which is Python based, it runs on a mock terminal on Heroku made by Code Institute.

User of the game needs to solve a set of 10 mathematical questions, the intention is to resolve them mentally rather than using any aid like a calculator or by writing down on paper. The motive is to test ones mathematical skills and ultimately have fun solving these questions.

[ >>> Click here for live version of project <<<](https://mental-math-466801bbea0a.herokuapp.com/)

![website homescreen on different platforms](assets/images/mental-math-responsive.png)


## How to play

- The game starts by displaying the rules and instructions for the game.
- Player can continue to start playing the game by typing in Y or y after reading instructions.
- Players need to enter their name before starting the game which will be saved along with score once the game ends.
- Name has to be Alphanumeric (a to z , A to Z or 0 to 9) and should have maximum 30 characters. No special characters.
- After entering name, one question along with 4 options (A,B,C,D) will appear on screen at a time .
- Player can confirm their answer by typing in A,B,C,D or a,b,c,d. Other inputs will show Invalid Input notification.
- After entering an answer the console will display if the answer is correct, if not it will display the correct answer.
- After each question score will be displayed and the player can press enter to continue to next question.
- After 10th (last) question user will see the final result and an option to restart the game if they wish to.


## Features

### Existing Features

- Welcome message with game instructions

  ![welcome message and instructions](assets/images/welcome-instructions.png)


- Invalid input detection and notification

  ![invalid inputs](assets/images/invalid-response.png)


- Maintains and notifies score throughout the game

  ![current score display](assets/images/score-update.png)

  ![final score](assets/images/end-score.png)


- Records Player Name and Score on score worksheet

  ![score record](assets/images/score-record.png)

  [Scores Link](https://docs.google.com/spreadsheets/d/e/2PACX-1vRHtH1L6v7yLg2khtr9KpUW0DvZkV6rLFUJ38s1zkc5puSi6OsAw86cUR9_G9OlBzierRb28KjHE8Hm/pubhtml?gid=323336629&single=true)

### Future Features

- Options to selected number of questions
- Introduce time limit to answer each question
- Provide new set of questions if user restarts game


## Process Flow

Please find below the process flow diagram

![Process Flow](assets/images/process-flow.png)


## Testing

The following tests were done to check the projects proper functionality

    - There were no errors found on https://pep8ci.herokuapp.com/ (PEP8 linter)
    - Invalid user inputs were caught and displayed by the game
    - Successfully tested on local terminal , github and Code Institute Heroku terminal 

### Bugs

#### Solved Bugs

    - When the code was initially tested on PEP8 linter, errors were found due to length of certain line of codes. As there is a limit of 79 characters per line, these were restructured.
    - Data on spreadsheet and question_session_handler function were restructured in order to avoid exceeding the google API request quotas, this was leading to read request errors initially. 
    - Data (Questions) on the spreadsheet had to be reformatted for it to appear properly on the Heroku terminal as they had text content longer than 80 characters.

#### Unsolved Bugs

    - No unsolved bugs remaining

### Validator Testing

    - No errors found on pep8ci.herokuapp.com


## Deployment

The project was deployed using mock terminal on Heroku made by Code Institute.

### Deployment Steps
    - Fork or clone this repository
    - New app was created on Heroku
    - Buildpacks were set to Python and NodeJS in that order
    - The Heroku app was linked to repository
    - Click on Deploy


## Credits

- Thanks to Mr Anthony Ugwu for being a great mentor. He guided me through this projects with his feedback and suggestions. 
- Thanks to Code Institute for providing with template and deployment terminal.
- All codes were written by me.
