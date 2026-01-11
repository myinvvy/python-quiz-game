import time

questions = {
    "Question: How do you get the output 'Hello, world!'?\n" : "D",
    "Question: How do you declare a variable?\n" : "A",
    "Question: How do you interpolate variables into a strings?\n" : "D",
    "Question: How do you turn a string fully uppercase?\n" : "A",
    "Question: Which of these declare a function?\n" : "B",
    "Question: Which of these are lists, tuples and sets respectively?\n" : "B",
    "Question: Which of these will return an error?\n" : "A",
    "Question: Which of these can be very dangerous?\n" : "C",
}

options = [
    ['A: cout << "Hello, world!"','B: console.log("Hello, world!");','C: echo "Hello, world!"','D: print("Hello, world!")'],
    ['A: variable_name = True','B: let variable_name = True','C: bool variable_name = True','D: local variable_name = True'],
    ['A: "Hello," + variable"','B: "Hello, variable"','C: "Hello, $variable"','D: f"Hello, {{variable}}"'],
    ['A: str_variable.upper()','B: str_variable.capitalize()','C: upper(str_variable)','D: capitalize(str_variable)'],
    ['A: function_name()','B: def function_name()','C: create function_name()','D: import function_name()'],
    ['A: () [] {}','B: [] () {}','C: {} [] ()','D: {} () []'],
    ['A: 2nd = "Silver Medal"','B: result = 1 + 1.0','C: answer = True or False','D: name = input("What is your name? ")'],
    ['A: file.write()','B: os.remove()','C: shutil.rmtree()','D: os.rmdir()'],
]

valid_choices = ["A", "B", "C", "D"]

def quiz():
    print("Welcome to the Python quiz.\n")
    correct = 0

    for question_number, question in enumerate(questions):
        print(question)

        for option in options[question_number]:
            print(option)

        while True:
            choice = input("\nWhat is your choice? (A/B/C/D): ").upper()
            if choice in valid_choices:
                break
            print("Please type A, B, C or D.")

        correct += check_answer(choice, question)
        time.sleep(1)

    quiz_end(correct)

def check_answer(choice, question):
    if choice == (questions[question]):
        print("Your choice is correct!\n")
        return 1
    else:
        print("Your choice is wrong.\n")
        return 0
    
def quiz_end(correct):
    print(f"\nThank you for taking the quiz.\nYour final score is {round((correct / len(questions) * 100))}%")


while True:
    quiz()
    response = input('Would you like to retake the quiz? (Type "Yes" to continue): ').strip().lower()
    if response != "yes":
        break