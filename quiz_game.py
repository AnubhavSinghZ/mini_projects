"""
QUIZ GAME
A simple multpile-choice quiz that tracks and shows your final score.
"""

# Each Question is a dictionary with the question, options, and correct answer

questions =[
    {
        "question": "What is the Capital of India ?",
        "options":["A. Kolkata", "B. Delhi", "C. New Delhi", "D. Mumbai"],
        "answer": "C"    
    },
    {
        "question": "Which language is used to build an Android apps traditionally ?",
        "options": ["A. Swift", "B. Java", "C. Pyhton", "D. RUby"],
        "answer": "C"
    },
    {
        "question": "Which of this is not a programming Language ?",
        "options": ["A. HTML", "B. Java", "C. Pyhton", "D. Cobra"],
        "answer": "D"
   },
   {
       "question": "What is the output of 2**3 in Python ?",
       "options": ["A. 6", "B. 8", "c. 10", "D. 12"],
       "answer": "B"
   }
],
def run_quiz(questions_list):
    score = 0
    total = len(questions_list)
 
    print("=" * 40)
    print("Welcome to the Quiz Game!")
    print("Answer by typing the letter (A, B, C, or D)")
    print("=" * 40)
 
    for i, q in enumerate(questions_list, start=1):
        print(f"\nQ{i}. {q['question']}")
        for option in q["options"]:
            print(option)
 
        user_answer = input("Your answer: ").strip().upper()
 
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")
 
    show_result(score, total)
 
 
def show_result(score, total):
    print("\n" + "=" * 40)
    print(f"Quiz over! You scored {score} out of {total}.")
 
    percentage = (score / total) * 100
    if percentage == 100:
        print("Perfect score! Amazing job!")
    elif percentage >= 60:
        print("Well done!")
    else:
        print("Keep practicing, you'll get better!")
    print("=" * 40)
 
 
if __name__ == "__main__":
    run_quiz(questions)