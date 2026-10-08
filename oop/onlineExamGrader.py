from abc import ABC, abstractmethod

class Question(ABC):
    def __init__(self, text, correct_answer):
        self.text = text
        self.correct_answer = correct_answer

    @abstractmethod
    def check_answer(self, student_answer):
        pass


class MCQQuestion(Question):
    def check_answer(self, student_answer):
        return student_answer.strip().lower() == self.correct_answer.strip().lower()


class TrueFalseQuestion(Question):
    def check_answer(self, student_answer):
        student_bool = student_answer.strip().lower() in ("true", "t", "yes")
        correct_bool = self.correct_answer.strip().lower() in ("true", "t", "yes")
        return student_bool == correct_bool


def main():
    questions = []

    while True:
        q_type = input("Question type (mcq/tf, or 'done' to finish): ")
        if q_type == "done":
            break

        text = input("Question text: ")
        correct = input("Correct answer: ")
        student = input("Student answer: ")

        if q_type == "mcq":
            q = MCQQuestion(text, correct)
        elif q_type == "tf":
            q = TrueFalseQuestion(text, correct)
        else:
            print("Unknown question type, skipping.")
            continue

        q._student_answer = student
        questions.append(q)

    score = 0
    for i, q in enumerate(questions, start=1):
        if q.check_answer(q._student_answer):
            print(f"Q{i}: Correct!")
            score += 1
        else:
            print(f"Q{i}: Incorrect. Correct answer: {q.correct_answer}")

    print(f"Final Score: {score}/{len(questions)}")


if __name__ == "__main__":
    main()
