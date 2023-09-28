import random


quiz_questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["A) London", "B) Berlin", "C) Paris", "D) Rome"],
        "correct_answer": "C",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "correct_answer": "B",
    },
    {
        "question": "What is the largest mammal in the world?",
        "choices": ["A) Elephant", "B) Giraffe", "C) Blue Whale", "D) Dolphin"],
        "correct_answer": "C",
    },
]


def run_quiz(questions):
    score = 0


    random.shuffle(questions)

    for question_data in questions:
        print(question_data["question"])
        for choice in question_data["choices"]:
            print(choice)

        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        if user_answer == question_data["correct_answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Sorry, the correct answer is {question_data['correct_answer']}.\n")

    return score


def main():
    print("Welcome to the Quiz Game!")
    print("Answer the following questions:")

    # Run the quiz and get the user's score
    final_score = run_quiz(quiz_questions)

    # Display the user's score and performance message
    print(f"Your Score: {final_score}/{len(quiz_questions)}")

    if final_score == len(quiz_questions):
        print("Congratulations! You got a perfect score!")
    elif final_score >= len(quiz_questions) // 2:
        print("Good job! You did well.")
    else:
        print("Keep practicing. You can do better next time.")


if __name__ == "__main__":
    main()
