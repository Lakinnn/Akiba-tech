print("===== Quiz Engine ======")
def display_question(number, question_data):
    print(f"\nQuestion {number}: {question_data['question']}")

    for index, option in enumerate(question_data["options"], start=1):
        print(f"{index}. {option}")


def validate_answer(answer, number_of_options):
    answer = answer.strip()

    if not answer.isdigit():
        return None

    answer_number = int(answer)

    if 1 <= answer_number <= number_of_options:
        return answer_number

    return None


def check_answer(answer, correct_answer):
    return answer == correct_answer


def update_score(score, is_correct):
    if is_correct:
        return score + 1

    return score


def get_result_category(percentage):
    if percentage >= 80:
        return "Excellent"
    elif percentage >= 60:
        return "Good"
    elif percentage >= 40:
        return "Needs Improvement"
    else:
        return "Keep Practicing"


def display_final_results(score, total_questions):
    incorrect = total_questions - score
    percentage = (score / total_questions) * 100
    category = get_result_category(percentage)

    print("\n--- Final Results ---")
    print(f"Correct answers: {score}")
    print(f"Incorrect answers: {incorrect}")
    print(f"Final score: {score}/{total_questions}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Category: {category}")


def run_quiz(questions):
    score = 0

    for number, question_data in enumerate(questions, start=1):
        display_question(number, question_data)

        while True:
            answer = input("Enter your answer: ")
            valid_answer = validate_answer(
                answer,
                len(question_data["options"])
            )

            if valid_answer is not None:
                break

            print("Invalid option. Please try again.")

        if check_answer(valid_answer, question_data["correct_answer"]):
            print("Correct!")
            score = update_score(score, True)
        else:
            print(
                f"Incorrect. The correct answer was "
                f"{question_data['correct_answer']}."
            )

    display_final_results(score, len(questions))


questions = [
    {
        "question": "What is the capital city of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "correct_answer": 3
    },
    {
        "question": "Which language is commonly used for web page structure?",
        "options": ["Python", "HTML", "SQL", "Java"],
        "correct_answer": 2
    },
    {
        "question": "How many days are in a leap year?",
        "options": ["364", "365", "366", "367"],
        "correct_answer": 3
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Venus", "Mars", "Jupiter"],
        "correct_answer": 3
    },
    {
        "question": "What is 7 multiplied by 3?",
        "options": ["18", "21", "24", "27"],
        "correct_answer": 2
    }
]


def main():
    print("Welcome to the Quiz!")

    while True:
        run_quiz(questions)

        play_again = input(
            "\nWould you like to play again? (yes/no): "
        ).strip().lower()

        if play_again not in ["yes", "y"]:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
