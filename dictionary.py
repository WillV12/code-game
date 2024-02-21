import os
import time
TITLE_CARD = """       _   _____   _____ _____   ____       _      ____    _____  __   __
      | | | ____| |  ___|  ___| |  _ \\     / \\    |  _ \\  |_   _| \\ \\ / /
   _  | | |  _|   | |_  | |_    | |_) |   / _ \\   | |_) |   | |    \\ V / 
  | |_| | | |___  |  _| |  _|   |  __/   / ___ \\  |  _ <    | |     | |  
   \\___/  |_____| |_|   |_|     |_|     /_/   \\_\\ |_| \\_\\   |_|     |_|  """
TREBECK = """   

                       ██                             
                 ▓████████████                        
                ▓█▓█▓▓▓▓▓▓▓████                       
              ██▓▓▓▓█▓▓▓▓▓█▓█████                     
              ██▓▓▓▓▓▓▓█▓▓▓▓▓████                     
             ███▓██████████▓▓████                     
             ███████████████▓████                     
             █▓▓███████████▓▓████                     
             ▓▓▓████████████▓▓▓▓▓                     
              █▓▓▓▒▒▓█▓▓▓▒▒▓▓▓▓▓▓                     
              █▓█████████████▓▓▓▓                     
               ████████▓█████▓▓▓                      
                ████▓▓▓▓▓███▓▓▓                       
                ███▓█████▓██▓▓▓░                      
                █▓█████████▓▓▓█▒░░                    
                 ▒▒███████▓▓███░░░░░░░                
            ░░░░░░▒██▓▓▒▒▒▓███▓░░░░░░░░░░░▒▒          
       ░░░░░░░░░░░░████▒▓█████░░░░░░░░░░░░░░░░░░░     
   ░░░░░░░░░░░░░░░▒██▒▒▒░▒███▓░░░░░░░░░░░░░░░░░░░░▒   
   ░░░░░░░░░░░░░░░▒███▒░▒████▒░░░░░░░░░░░░░░░░░░░░▒   
   ░░░░░░░░░░░░░░░▓██▒░▒▓███▒░░░░░░░░░░░░░░░░░░░░░░   
   ░░░░░░░░░░░░░░░▓█▒▒▒▒▒███░░░░░░░░░░░░░░░░░░░░░░░   
  ░░░░░░░░░░░░░░░░▓▓▒▒▒▒▒██▒░░░░░░░░░░░░░░░░░░░░░░░▒  
 ░░░░░░░░░░░░░░░░░▒▒▒▒▓▒▒█▓░░░░░░░░░░░░░░░░░░░░░░░░░  
 ░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▓░░░░░░░░░░░░░░░░░░░░░░░░░░▒ 
░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓
░░░░░░░░░░░░░░░░░░░▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒
░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒"""
POINT = 100
types = ["Floating Point", "Integer", "String", "Value"]
def_types = ["A type that represents numbers with fractional parts.", "A type that represents whole numbers.",
             "A type that represents sequences of characters.",
             "A category of values. The types we have seen so far are integers (type int), "
             "floating-point numbers (type float), and strings (type str)."]

operations = ["Assignment", "Concatenate", "Evaluate", "Statement"]
def_operations = ["A statement that assigns a value to a variable.", "To join two operands end to end.",
                  "To simplify an expression by performing the operations in order to yield a single value.",
                  "A section of code that represents a command or action. So far, the statements we have seen are "
                  "assignments and print expression statement."]

aspects = ["Variable" "Operand", "Operator", "Keyword", "Expression"]
def_aspects = ["A name that refers to a value.", "One of the values on which an operator operates.",
               "A special symbol that represents a simple computation like addition, multiplication, "
               "or string concatenation.", "A reserved word that is used by the compiler to parse a program; "
               "you cannot use keywords like if, def, and while as variable names.",
               "A combination of variables, operators, and values that represents a single result value."]

misc = ["Mnemonic", "Rules of Precedence", "Comment", "Modulus Operator"]
def_misc = ["A memory aid. We often give variables mnemonic names to help us remember what is stored in the variable.",
            "The set of rules governing the order in which expressions involving multiple operators and operands are "
            "evaluated.", "Information in a program that is meant for other programmers (or anyone reading the source "
                          "code) and has no effect on the execution of the program.", "An operator, denoted with a "
            "percent sign (%), that works on integers and yields the remainder when one number is divided by another."]

category = ["Types", "Operations", "Aspects", "Misc"]
questions = [def_types, def_operations, def_aspects, def_misc]
answers = [types, operations, aspects, misc]
move_on = True
user_score = 0


def print_title(num_categories, num_questions):
    print(TITLE_CARD)
    time.sleep(.6)
    print("epic graphic")
    print(num_questions, num_questions)

# The prior block of code should remove the question and or category if the category is out of questions
def run_through(category_choice, question_choice, score):
    os.system("cls")
    answer = answers[category_choice][question_choice]
    time.sleep(.5)
    for x in TREBECK.splitlines():
        print(x)
        time.sleep(.045)
    print(f"Let's get started\n\tPlayer, for {POINT * (question_choice + 1)} points, your question is...")
    print(f"{category[category_choice]}-{question_choice + 1}: {questions[category_choice][question_choice]}:\n")
    user_input = input("What is a(n):\t").upper()
    print("\n\n\n")
    if user_input == answer.upper():
        add = POINT * (question_choice + 1)
        score += add
        print(f"Correct!!!\nYou gained {add} points")

    else:
        print(f"Sorry that wasn't right\n The correct answer was...\nWhat is: {answer}")
    return score


while move_on is True:
    os.system("cls")
    time.sleep(.5)
    print_title(len(category), len(questions))
    for x in TREBECK.splitlines():
        print(x)
        time.sleep(.045)
    cat_choice = int(input(f"HI there folks, welcome to jeopardy\n\tMy name is Alex Trebeck, Player, please choose your\
 category (1-4):\n"))
    cat_choice -= 1
    print(f"You chose category '{category[cat_choice]}'")
    time.sleep(.5)
    q_choice = int(input("Now, player, Which question do you want? (1-4):\n"))
    q_choice -= 1
    user_score = run_through(cat_choice, q_choice, user_score)
    print("\n\n\n\n\n")
    end = input("Do you want to end?\nPress X to end\nelse press any key to continue").upper()
    if end == "X" or len(questions) == 0:
        move_on = False
else:
    print(f"Your final score = {user_score}")