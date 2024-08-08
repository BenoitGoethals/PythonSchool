import random
import uuid
class Question:
    def __init__(self, category=None,type=None,difficulty=None,incorrect_answers=None,correct_answer=None, question=None):
        self.question = question
        self.category = category
        self.incorrect_answers = incorrect_answers
        self.type = type
        self.correct_answer = correct_answer
        self.difficulty = difficulty
        self.guid=uuid.uuid4()
        self.personal_anser=""

class QuestionMachine:
    def __init__(self,questions:[]=None):
        self.questions  = questions

    def StartQuestion(self,difficulty):
        max=len(self.questions)
        already_chosen_questions=[]
        counter=0
        while(max>counter):
           choice=random.randint(0,max-1)
           question=self.questions[choice]
           if question not in already_chosen_questions:
            already_chosen_questions.append(question)
            print(question.question.question)
            answer=input("Answer")
            if answer==question.correct_answer:
                print("Correct")
            else:
                print("Incorrect")

class QuestionPopulator:
    @staticmethod
    def construct_question(questions:[{}]):
        list_of_questions = []
        for question in questions:
            temp=Question()
            temp.question=question.get("question")
            temp.difficulty=question.get("difficulty")
            temp.category=question.get("category")
            temp.incorrect_answers=question.get("incorrect_answers")
            temp.type=question.get("type")
            temp.correct_answer=question.get("correct_answer")
            list_of_questions.append(temp)
        return list_of_questions