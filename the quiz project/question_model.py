class Question:
    """
    A simple class to model a single quiz question.
    It holds the text of the question and its correct answer.
    """

    def __init__(self, q_text, q_answer):
        """
        Initializes a Question object with text and an answer.

        Args:
            q_text (str): The text of the question.
            q_answer (str): The correct answer to the question.
        """
        self.text = q_text
        self.answer = q_answer