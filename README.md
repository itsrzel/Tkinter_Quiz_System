# Atlas Pinas

* Name: Rezelle Vedeja Filomeno
* Section: BS Information Technology - Software engineering 3-A
* Topic: Philippine Geography

## Features Completed
✓ 10 multiple-choice questions

✓ Random question order

✓ 15-second countdown timer

✓ Answer checking and time-out handling

✓ Score and percentage

✓ Answer review

✓ High score saved in a text file

✓ Restart button

  
## How the Questions Are Stored and Shuffled
The questions are stored in a list, with each question containing the choices and correct answer. The random.shuffle() function is used to mix the order of the questions every time the quiz starts, making the game different for each attempt.


## How the Timer Works
Each question has a 15-second countdown timer. The timer decreases every second using Tkinter's after() function. When the time reaches zero, the program automatically marks the question as unanswered and moves on. The timer also stops when the player submits an answer or leaves the question.
How the Program Identifies the Correct Answer
The program checks the player's selected answer and compares it with the correct answer stored in the question list. If they match, the answer is marked correct. Otherwise, it is marked incorrect.


## How the Score and High Score Work
The score increases for every correct answer. After the quiz, the program calculates the percentage by dividing the score by the total number of questions and multiplying it by 100. The highest score is saved in a text file named high_score.txt. When the program opens again, it reads the file to display the previous highest score. A new high score is saved if the player gets a higher score.


## Function Explanations
Function	Purpose	Called when
show_start_screen()	Displays the welcome screen and start button.	When the program opens or returns to the home screen.
start_quiz()	Starts the quiz and prepares the questions.	When the player clicks Start.
show_question()	Displays the current question and choices.	When a new question appears.
start_timer()	Starts the 15-second countdown.	When a question is displayed.
update_timer()	Updates the countdown every second.	While the player is answering.
submit_answer()	Checks the selected answer.	When the player submits an answer.
get_high_score()	Reads the saved highest score from the text file.	When the program needs to display the high score.
save_high_score()	Saves a new highest score in the text file.	When the player gets a higher score.
show_results()	Displays the final score, percentage, and answer review.	After all questions are answered.

## Screenshots
See the uploaded screenshots the screenshot folder uploaded in this repository.

## Challenges I Faced
One of the challenges I faced was making the timer work correctly without affecting the other parts of the quiz. I also had difficulty saving and displaying the highest score. I solved these by using Tkinter's after() function for the countdown and a text file to store the highest score. I also tested the program several times to make sure the buttons, answers, and scoring worked properly.

