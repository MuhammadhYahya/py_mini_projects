def display_question(index, question):
    """Displays the question and its options."""
    print(f"Question {index}: {question['prompt']}")
    for option in question['options']:
        print(option)


def get_user_answer():
    """Gets a valid answer from the user."""
    valid_choices = {'A', 'B', 'C', 'D', 'Q'}
    while True:
        answer = input("Enter your answer (A, B, C, or D) or 'Q' to quit: ").upper().strip()
        if answer in valid_choices:
            return answer
        print("Invalid input! Please enter A, B, C, D, or Q.")


def calculate_result(marks, total_questions):
    """Calculates and displays the final result."""
    print(f"\nYou completed the test! You got {marks} out of {total_questions} questions.")


def add_incorrect_answer(incorrect_answers, question_number, question_prompt, user_answer, correct_answer):
    """Adds an incorrect answer to the list."""
    incorrect_answers.append((question_number, question_prompt, user_answer, correct_answer))


def review_incorrect_answers(incorrect_answers):
    """Displays the review of all incorrect answers."""
    if incorrect_answers:
        print("\nReview of incorrect answers:")
        for i, prompt, user_answer, correct_answer in incorrect_answers:
            print(f"Question {i}: {prompt}")
            print(f"Your Answer: {user_answer}")
            print(f"Correct Answer: {correct_answer}\n")


def start_test(questions):
    """Main function to run the test."""
    marks = 0
    incorrect_answers = []  # List to store incorrect answers

    for i, qstn in enumerate(questions, start=1):
        display_question(i, qstn)
        answer = get_user_answer()

        if answer == 'Q':
            print("\nYou chose to quit the test.")
            calculate_result(marks, i - 1)
            review_incorrect_answers(incorrect_answers)
            return

        if answer == qstn['answer']:
            print("Correct!\n")
            marks += 1
        else:
            print(f"Wrong! You selected {answer}, but the correct answer was {qstn['answer']}.\n")
            add_incorrect_answer(incorrect_answers, i, qstn['prompt'], answer, qstn['answer'])
    
    calculate_result(marks, len(questions))
    review_incorrect_answers(incorrect_answers)


# Questions for the test
questions = [
    {
        "prompt": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "prompt": "Which language is primarily spoken in Brazil?",
        "options": ["A. Spanish", "B. Portuguese", "C. English", "D. French"],
        "answer": "B"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    },
    {
        "prompt": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
        "answer": "A"
    }
]

# Start the test
start_test(questions)
