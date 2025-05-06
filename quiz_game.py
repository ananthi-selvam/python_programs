"""
EXPLANATION: In this progarm, computer ask few questions to user. Based on the user's answer, display user score.
Simple QUIZZ game written on python
"""

questions = [
    {"prompt": "What is the capital of INDIA? ",
     "Options": ["A: New Delhi", 'B: Mumbai', 'C: Kolkata', 'D: Chennai'],
     'Answer': 'A'},
    {'prompt': 'What is the capital of France? ',
     'Options': ['A: berlin', 'B: Madrid', 'C: Paris', 'D: Rome'],
     'Answer': "C"
    },
    {'prompt': 'What is the capital of Japan? ',
     'Options': ["A: Seoul", "B: Tokyo", "C: Beijing", "D: Bangkok"],
     'Answer': "B"
    },
    {'prompt': 'Which planet is known as the Red Planet? ',
     'Options': ["A: Charles Dickens", "B: William Shakespeare", "C: Mark Twain", "D: Jane Austen"],
     'Answer': "B"
    },
    {'prompt': "Which element has the chemical symbol 'O'? ",
     'Options': ['A: Gold", "B: Oxygen", "C: Osmium", "D: Ozone'],
     'Answer': "B"
    }
]

def quizz(questions):
    score = 0
    for question in questions:
        print(question['prompt'])
        for option in question['Options']:
            print(option)
        user_choice = input('Enter answer Select (A, B, C, D): ').upper()
        if user_choice in question['Answer']:
                if user_choice == question['Answer']:
                    score+=1
                    print("Right answer!! \n")
                else:
                    print(f'Sorry! wrong answer. The right answer is {question['Answer']}')
        else:
            print('invalid option you have entered!!')
            should_continue = input('You want to continue? (Y/N): ').lower()
            if should_continue == 'y':
                continue
            else:
                break
            
    print(f'your score is {score} out of {len(questions)}')


quizz(questions)
