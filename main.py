#
# Gavin McKenzie
# 2/19/24
# Main function and GUI for python game
from time import sleep
from colorama import Fore, Back, Style
import dictionary

TITLE_CARD = """       _   _____   _____ _____   ____       _      ____    _____  __   __
      | | | ____| |  ___|  ___| |  _ \\     / \\    |  _ \\  |_   _| \\ \\ / /
   _  | | |  _|   | |_  | |_    | |_) |   / _ \\   | |_) |   | |    \\ V / 
  | |_| | | |___  |  _| |  _|   |  __/   / ___ \\  |  _ <    | |     | |  
   \\___/  |_____| |_|   |_|     |_|     /_/   \\_\\ |_| \\_\\   |_|     |_|  """
categories = ['Assaignment', 'Operations', 'Data Types', 'Misc']
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
    user_category, user_points = input_checking()


def print_tile():
    print("""________________________________________________________________________________
|     Assaignment     |     Operations     |     Data Types     |     Misc     |
|_____________________|____________________|____________________|______________|
|         100         |        100         |        100         |     100      |
|_____________________|____________________|____________________|______________|
|         200         |        200         |        200         |     200      |
|_____________________|____________________|____________________|______________|
|         300         |        300         |        300         |     300      |
|_____________________|____________________|____________________|______________|
|         400         |        400         |        400         |     400      |
|_____________________|____________________|____________________|______________|
|         500         |        500         |
|_____________________|____________________|\n""")


def input_checking():
    points_vals = [100, 200, 300, 400, 500]
    category = input("What category would you like to choose?\n\t")
    category = category.title()
    while category not in categories:
        print("Trebeck will remember this...")
        sleep(3)
        category = input("What category would you like to choose?\n\t")
        category = category.title()
    for x in trebeck.splitlines():
        print(x)
        sleep(.045)
    print(f"{Style.BRIGHT}Hi there folks, I'm Alex Trebeck")
    sleep(.8)
    print(f"{Style.BRIGHT}Player, you chose the category: {category}, how many points do you want to go for?")
    points = int(input("\t(100, 200, 300, 400, or 500, if you can):  "))
    while points not in points_vals:
        print("Trebeck is getting angry....")
        sleep(4)
        points = int(input("\tHow many points do you want to go for?:  "))
    if category == ("Data Types" or "Misc") and points == 500:
        points = int(input("\tHow many points do you want to go for? (400 or less):  "))
    return category, points


main()