class QuizBrain:
    """
    Manages the flow of the quiz, including question navigation,
    scoring, and user interaction.
    """

    def __init__(self, q_list):
        """Initializes the QuizBrain with a list of questions."""
        self.question_number = 0  # Tracks the current question index.
        self.question_list = q_list # Stores the list of Question objects.
        self.counter = 0        # Tracks the user's correct score.

    def still_has_questions(self):
        """Checks if there are still questions remaining in the quiz."""
        # Returns True if the current question number is less than the total number of questions.
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Retrieves the next question, prompts the user for an answer,
        and checks if the answer was correct.
        """
        # Get the current question object from the list using the question_number index.
        current_question = self.question_list[self.question_number]
        # Increment the question_number to prepare for the next round.
        self.question_number += 1
        # Prompt the user for an answer.
        user_answer = input(f"Q.{self.question_number}:{current_question.text} (True or False): ")
        # Check the user's answer against the correct answer.
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """
        Compares the user's answer to the correct answer and provides feedback.
        """
        # Check if the user's answer (converted to lowercase) matches the correct answer.
        if user_answer == correct_answer.lower():
            # If correct, increment the score.
            self.counter += 1
            print("You get it right")
        else:
            # If incorrect, provide feedback.
            print("You get it wrong")
        # Print the correct answer for learning purposes.
        print(f"The correct answer was: {correct_answer}")
        # Print the user's current score.
        print(f"Your current score is: {self.counter}/{self.question_number}")
        # Print a newline for better formatting.
        print("\n")