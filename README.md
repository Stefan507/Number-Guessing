 # Number Guessing
 Welcome to the wonderfull game of guessing the number. How many points can you score?
 
 ## How the game works
 In this game, the user can guess a number between 1 and 10. 
 The user can guess 4 times.
 There are 5 rounds, in wich the user can score points, 1 for each correct answer.
 There will be hints. The hints are:
 Smaller, larger

 ## Workflow
 When the program is run:
 - Initialize games counter, set counter to 0
 - Initialize round to 0
 - Set the score to 0
 - Welcome the user to the game
 - Print in which game the user currently is
    - Generate random integer
    - Let the user guess the number
        - If correct -> 1 point
        - If incorrect -> Give hint
        - If correct -> 1 point
        - If incorrect -> Give hint
        - If correct -> 1 point
        - If incorrect -> Give hint
        - If correct -> 1 point
        - If incorrect -> Show answer + award 0 points
    - Increment the games counter with 1
- Repeat above step 4 more times
- Ouput the score of the user

    