# Import the necessary classes from our custom modules.
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# --- Data Preparation ---
# Create an empty list to hold our Question objects.
question_bank = []
# Loop through the raw data (a list of dictionaries).
for question in question_data:
   # Extract the text and answer for each question.
   question_text = question["question"]
   question_answer = question["correct_answer"]
   # Create a new Question object with the extracted data.
   new_question = Question(question_text, question_answer)
   # Add the newly created Question object to our question bank.
   question_bank.append(new_question)

# --- Quiz Initialization ---
# Create an instance of our QuizBrain, passing it the list of questions.
quiz = QuizBrain(question_bank)

# --- Main Game Loop ---
# The loop continues as long as there are questions left in the quiz.
while quiz.still_has_questions():
    # Advance to the next question in the quiz.
    quiz.next_question()
    # This variable was created but is not used in the final code.
    game_quiz = False

# --- End of Game ---
# Once the loop is finished, print the final results.
print("You've completed the quiz.")
print(f"Your final score was: {quiz.counter} / {quiz.question_number}")