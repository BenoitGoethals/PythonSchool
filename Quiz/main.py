from Quiz.data import question_data
from Quiz.model import QuestionMachine, QuestionPopulator


def main():
    qm=QuestionMachine(QuestionPopulator.construct_question(question_data))

if __name__ == '__main__':
    main()