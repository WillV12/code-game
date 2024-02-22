import os
import time
from main import input_checking

POINT = 100

aspects = {100: ["Variable", "A name that refers to a value."],
           200: ["Operand", "One of the values on which an operator operates."],
           300: ["Operator", "A special symbol that represents a simple computation like addition, multiplication, or "
                             "string concatenation."],
           400: ["Keyword", "A reserved word that is used by the compiler to parse a program; you cannot use keywords "
                            "like if, def, and while as variable names."],
           500: ["Expression","A combination of variables, operators, and values that represents a single result value."]}

types = {100: ["Floating Point", "A type that represents numbers with fractional parts."],
         200: ["Integer", "A type that represents whole numbers."],
         300: ["String", "A type that represents sequences of characters."],
         400: ["Value", "A category of values. The types we have seen so far are integers (type int), floating-point "
                        "numbers (type float), and strings (type str)."]}

operations = {100: ["Assignment", "A statement that assigns a value to a variable."],
              200: ["Concatenate", "To join two operands end to end."],
              300: ["Evaluate", "To simplify an expression by performing the operations in order to yield a single "
                                "value."],
              400: ["Statement", "A section of code that represents a command or action. So far, the statements we "
                                 "have seen are assignments and print expression statement."]}

misc = {100: ["Mnemonic", "A memory aid. We often give variables mnemonic names to help us remember what is stored in "
                          "the variable."],
        200: ["Rules of Precedence", "The set of rules governing the order in which expressions involving multiple "
                                     "operators and operands are evaluated."],
        300: ["Comment", "Information in a program that is meant for other programmers (or anyone reading the source "
                         "code) and has no effect on the execution of the program."],
        400: ["Modulus Operator", "An operator, denoted with a percent sign (%), that works on integers and yields the "
                                  "remainder when one number is divided by another."]}



category = ["Types", "Operations", "Aspects", "Misc"]
answers = [types, operations, aspects, misc]
move_on = True
user_score = 0

# The prior block of code should remove the question and or category if the category is out of questions


def run_through(category_choice, question_choice, score):
    os.system("cls")
    answer = answers[category_choice][question_choice]
    time.sleep(.5)
    print(f"{category[category_choice]}-{question_choice}: {questions[category_choice][question_choice]}:\n")
    user_input = input("What is a(n):\t").upper()
    print("\n\n\n")
    if user_input == answer.upper():
        add = POINT*question_choice
        score += add
        print(f"Correct!!!\nYou gained {add} points")

    else:
        print(f"Sorry that wasn't right\n {answer}")
    return score





while move_on is True:
    os.system("cls")
    time.sleep(.5)
    cat_choice = int(input("Category choice:\n"))
    time.sleep(.5)
    q_choice = int(input("Question choice:\n"))
    user_score = run_through(cat_choice, q_choice, user_score)
    end = input("Do you want to end?\nPress X to end\nelse press any key to continue").upper()
    if end == "X" or len(questions) == 0:
        move_on = False
else:
    print(f"Your final score = {user_score}")