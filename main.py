#
# Gavin McKenzie
# 2/19/24
# Main function and GUI for python game
from time import sleep
from colorama import Fore, Back, Style
import os

TITLE_CARD = """       _   _____   _____ _____   ____       _      ____    _____  __   __
      | | | ____| |  ___|  ___| |  _ \\     / \\    |  _ \\  |_   _| \\ \\ / /
   _  | | |  _|   | |_  | |_    | |_) |   / _ \\   | |_) |   | |    \\ V / 
  | |_| | | |___  |  _| |  _|   |  __/   / ___ \\  |  _ <    | |     | |  
   \\___/  |_____| |_|   |_|     |_|     /_/   \\_\\ |_| \\_\\   |_|     |_|  """
categories = ['Aspects', 'Types', 'Operations', 'Misc']
trebeck = """   
                                                      
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


def main():
    print(f"{TITLE_CARD}")
    print_tile()
    while categories != 0:
        user_pnts = question_select(score)


def print_tile():
    print(f"""___________________________________________________________________________
|       Aspects       |     Types     |     Operations     |     Misc     |
|_____________________|_______________|____________________|______________|
|         {title['Aspects'][0]}         |      {title['Types'][0]}      |        {title['Operations'][0]}         |     {title['Misc'][0]}      |
|_____________________|_______________|____________________|______________|
|         {title['Aspects'][1]}         |      {title['Types'][1]}      |        {title['Operations'][1]}         |     {title['Misc'][1]}      |
|_____________________|_______________|____________________|______________|
|         {title['Aspects'][2]}         |      {title['Types'][2]}      |        {title['Operations'][2]}         |     {title['Misc'][2]}      |
|_____________________|_______________|____________________|______________|
|         {title['Aspects'][3]}         |      {title['Types'][3]}      |        {title['Operations'][3]}         |     {title['Misc'][3]}      |
|_____________________|_______________|____________________|______________|
|         {title['Aspects'][4]}         |               |                    |              |
|_____________________|_______________|____________________|______________|""")


title = {'Aspects': [100, 200, 300, 400, 500],
         'Types': [100, 200, 300, 400],
         'Operations': [100, 200, 300, 400],
         'Misc': [100, 200, 300, 400]}

# Dictionary Section
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
score = 0

# def input_checking(score):
#     points_vals = [100, 200, 300, 400, 500]
#     category = input("What category would you like to choose?\n\t").title()
#     while category not in categories:
#         print("Trebeck will remember this...")
#         sleep(3)
#         category = input(f"What category would you like to choose?\n\t").title()
#     for x in trebeck.splitlines():
#         print(x)
#         sleep(.045)
#     print(f"{Style.BRIGHT}Hi there folks, I'm Alex Trebeck")
#     sleep(.8)
#     print(f"{Style.BRIGHT}Player, you chose the category: {category}, how many points do you want to go for?")
#     try:
#         points = int(input("\t(100, 200, 300, 400, or 500, if you can):  "))
#     except:
#         print("Trebeck is getting angry....")
#         points = int(input("\t(100, 200, 300, 400, or 500, if you can):  "))
#
#     while points not in points_vals:
#         print("Trebeck is getting angry....")
#         sleep(4)
#         points = int(input("\tHow many points do you want to go for?:  "))
#     if category == ("Operations" or "Data Types" or "Misc") and points == 500:
#         points = int(input("\tHow many points do you want to go for? (400 or less):  "))
#    while len(categories) != 0:
#        user_pnts = question_select(category, points, score)


def question_select(score):
    os.system("cls")
    category = input(f"What category would you like to choose?\n\t").title()
    if category == "Aspects":
        print(f"Let's get started\n\tPlayer, for {int(point)} points, your question is...")
        if input(f"{aspects[int(point)][1]}\n\tWhat is: ").title() == aspects[int(point)][0]:
            print("Correct")
            score += int(point)
            return score
        else:
            print("Wrong")
            return score

    elif category == "Types":
        print(f"Let's get started\n\tPlayer, for {int(point)} points, your question is...")
        if input(f"{types[int(point)][1]}\n\tWhat is: ").title() == types[int(point)][0]:
            print("Correct")
        else:
            print("Wrong")
    elif category == "Operations":
        print(f"Let's get started\n\tPlayer, for {int(point)} points, your question is...")
        if input(f"{operations[int(point)][1]}\n\tWhat is: ").title() == operations[int(point)][0]:
            print("Correct")
        else:
            print("Wrong")
    elif category == "Misc":
        print(f"Let's get started\n\tPlayer, for {int(point)} points, your question is...")
        if input(f"{misc[int(point)][1]}\n\tWhat is: ").title() == misc[int(point)][0]:
            print("Correct")
        else:
            print("Wrong")

main()