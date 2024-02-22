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

print_tile()



for i in range(10):
    x = input()
    y = int(input())
    title[x][title[x].index(y)] = "   "
    print_tile()
