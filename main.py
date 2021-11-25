#imports
import os
import time
import colorama as cr
import math
import sys


cr.init(autoreset=True)


#clears the console every now and then
def clearConsole():
    command = 'clear'
    os.system(command)


#the actual code :noooooo:

print(f"{cr.Fore.GREEN}this part is crucial to do") 
time.sleep(3)
clearConsole()

print("Loading main.py {⬜         } 20%") #Loading
time.sleep(2)
clearConsole()
print("Loading main.py {⬜⬜       } 40%") #Loading
time.sleep(2)
clearConsole()
print("Loading main.py {⬜⬜⬜     } 60%") #Loading
time.sleep(2)
clearConsole()
print("Loading main.py {⬜⬜⬜⬜   } 80%") #Loading
time.sleep(2)
clearConsole()
print("Loading main.py {⬜⬜⬜⬜⬜} 100%") #Loading
time.sleep(2)
clearConsole()

user = input(f"{cr.Fore.GREEN}USER? : ")
time.sleep(1)
clearConsole()

print(f"{cr.Fore.GREEN}Mysterious:Wake up " + user + ".")
time.sleep(0.5)
print(f"{cr.Fore.GREEN}Mysterious:You don't have enough time to WASTE.")

time.sleep(2)
print(f"{cr.Fore.LIGHTBLUE_EX}Respond With: | What. | Where am I? |")
time.sleep(1)

user_input1 = input(f"{cr.Fore.LIGHTRED_EX} " + user + " : ")

time.sleep(2)

if user_input1=="What.":
    print(f"{cr.Fore.GREEN}Mysterious:Wait Did You Lose Your Memory?")

if user_input1=="Where am I?":
    print(f"{cr.Fore.GREEN}Mysterious:Wait Did You Lose Your Memory?")

if user_input1.lower() == "what" or user_input1.lower() == 'where am i?':
    print(f"{cr.Fore.GREEN}Mysterious:Wait Did You Lose Your Memory?")

else:
    print(f"{cr.Fore.RED}Game.Console: '" + user_input1 +"' Considered to be a input Error. Please restart game. :(")
    sys.exit("")
time.sleep(2)