import random


def generate_random_integer(min_value, max_value):
    """
    Generate a random integer between min_value and max_value (inclusive).
    """
    return random.randint(min_value, max_value)


def generate_random_operator():
    """
    Generate a random mathematical operator (+, -, *).
    """
    return random.choice(['+', '-', '*'])


def generate_math_problem():
    """
    Generate a random math problem with two operands and an operator.
    """
    operand1 = generate_random_integer(1, 10)
    operand2 = generate_random_integer(1, 5)
    operator = generate_random_operator()

    problem = f"{operand1} {operator} {operand2}"
    answer = calculate_answer(operand1, operand2, operator)

    return problem, answer


def calculate_answer(num1, num2, operator):
    """
    Calculate the answer for a given math problem.
    """
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    else:
        raise ValueError("Invalid operator")


def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, correct_answer = generate_math_problem()
        print(f"\nQuestion: {problem}")
        
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            user_answer = None

        if user_answer is not None:
            if user_answer == correct_answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()

