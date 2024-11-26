def start_test(questions):
    marks = 0
    for i, qstn in enumerate(questions, start=1):
        print(f"Question {i}: {qstn['prompt']}")
        for optn in qstn['options']:
            print(optn)
        answer = input("Enter your answer (A, B, C, or D) or 'Q' to quit: ").upper().strip()
        
        if answer == 'Q':
            print("\nYou chose to quit the test.")
            print(f"You answered {marks} out of {i-1 } questions.")
            return
        
        if answer == qstn['answer']:
            print("Correct!\n")
            marks += 1
        else:
            print("Wrong! The correct answer was", qstn["answer"], "\n")
    
    print(f"\nYou completed the test! You got {marks} out of {len(questions)} questions.")


questions = [
    {
        "prompt": "What is the largest planet in our Solar System?",
        "options": ["A. Earth", "B. Jupiter", "C. Saturn", "D. Neptune"],
        "answer": "B"
    },
    {
        "prompt": "Who painted the Mona Lisa?",
        "options": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo"],
        "answer": "C"
    },
    {
        "prompt": "What is the chemical symbol for water?",
        "options": ["A. H2O", "B. CO2", "C. NaCl", "D. O2"],
        "answer": "A"
    },
    {
        "prompt": "Which continent is the Sahara Desert located in?",
        "options": ["A. Asia", "B. Africa", "C. Australia", "D. South America"],
        "answer": "B"
    },
    {
        "prompt": "What is the square root of 64?",
        "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
        "answer": "C"
    },
    {
        "prompt": "Who is known as the Father of Computers?",
        "options": ["A. Alan Turing", "B. Charles Babbage", "C. Bill Gates", "D. Steve Jobs"],
        "answer": "B"
    },
    {
        "prompt": "Which animal is known as the King of the Jungle?",
        "options": ["A. Tiger", "B. Elephant", "C. Lion", "D. Cheetah"],
        "answer": "C"
    },
    {
        "prompt": "What is the main ingredient in sushi?",
        "options": ["A. Rice", "B. Bread", "C. Pasta", "D. Potato"],
        "answer": "A"
    },
    {
        "prompt": "What is the currency of Japan?",
        "options": ["A. Yen", "B. Won", "C. Dollar", "D. Euro"],
        "answer": "A"
    },
    {
        "prompt": "Which is the smallest continent by land area?",
        "options": ["A. Europe", "B. Australia", "C. Antarctica", "D. South America"],
        "answer": "B"
    }
]

start_test(questions)
