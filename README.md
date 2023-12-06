 # How the game works
 In this game, the user can guess a number between 1 and 10. 
 The user can guess 4 times, each time the score will decrease
 There are 5 rounds, in wich the user can score points, from 0 to 3
 If the guess is correct in the first guess, the user will get 3 points
 On the second attempt this will be 2, then 1 and finally 0.5
 There will be hints. The hints are:
 Smaller, larger

 ## Workflow
 When the program is run:
 - Initialize games counter, set counter to 0
 - Initialize round to 0
    - Generate random integer
    - Let the user guess the number
        - If correct -> 3 points
        - If incorrect -> Give hint
        - If correct -> 2 points
        - If incorrect -> Give hint
        - If correct -> 1 points
        - If incorrect -> Give hint
        - If correct -> 0.5 points
        - If incorrect -> Show answer + award 0 points
    - Increment the games counter with 1
- Repeat above step 4 more times
- Ouput the score of the user

    