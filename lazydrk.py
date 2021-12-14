#!/usr/bin/python3

#####################################################
## LazyDrk (lDrk)                                  ##
## Made to connect all of my scripts in one.       ##
## https://voidsecurity.ml                         ##
## Coded by: drk                                   ##
#####################################################

# Imports
import os
import time
from termcolor import colored


# Global Variables
discord = "drk#1337"
tooldir = "./assets/tools"

# Defines
def enter():
    input("Press enter to continue.")

def banner():
    print(colored("""
     _                     _____       _    
    | |                   |  __ \     | |   
    | |     __ _ _____   _| |  | |_ __| | __
    | |    / _` |_  / | | | |  | | '__| |/ /
    | |___| (_| |/ /| |_| | |__| | |  |   < 
    |______\__,_/___|\__, |_____/|_|  |_|\_\\
                    __/ |                 
                    |___/                  

    {---          Coded by drk           ---}
    """, "yellow"))

def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')
def drktools():
    clearcmd()
    print(colored("""
     _______             __       ________                   __           
    /       \           /  |     /        |                 /  |          
    $$$$$$$  |  ______  $$ |   __$$$$$$$$/______    ______  $$ |  _______ 
    $$ |  $$ | /      \ $$ |  /  |  $$ | /      \  /      \ $$ | /       |
    $$ |  $$ |/$$$$$$  |$$ |_/$$/   $$ |/$$$$$$  |/$$$$$$  |$$ |/$$$$$$$/ 
    $$ |  $$ |$$ |  $$/ $$   $$<    $$ |$$ |  $$ |$$ |  $$ |$$ |$$      \ 
    $$ |__$$ |$$ |      $$$$$$  \   $$ |$$ \__$$ |$$ \__$$ |$$ | $$$$$$  |
    $$    $$/ $$ |      $$ | $$  |  $$ |$$    $$/ $$    $$/ $$ |/     $$/ 
    $$$$$$$/  $$/       $$/   $$/   $$/  $$$$$$/   $$$$$$/  $$/ $$$$$$$/  
                                                                                                                      
    """, "red"))
    
    print("""
    [1] DrkAccountManager
    [2] EnVoid
    [3] Coming soon.
    [4] Coming soon.

    [5] Settings
    [6] Go back
    
    """)
    option = input("Option: ")
    if option == "1":
        read = exec(open(f"{tooldir}/accountmanager/manager.py").read())
        print(read)
        time.sleep(3)

    elif option == "2":
        pass
    elif option == "3":
        pass
    elif option == "4":
        pass
    elif option == "5":
        pass
    elif option == "6":
        usage()
    elif option == "drk":
        print(colored("Epic.", "green"))
        time.sleep(1.5)
        drktools()

def drkgames():
    pass
def usage():
    clearcmd()
    banner()
    print("""
    [1] Misc
    [2] Drk Tools
    [3] Drk Games
    [4] Coming soon.
    [5] Status
    [6] State
    
    [7] Settings
    [8] Quit   
    
    """)
    option = input("Option: ")
    if option == "1":
        pass
    elif option == "2":
        drktools()
    elif option == "3":
        pass
    elif option == "4":
        pass
    elif option == "5":
        pass
    elif option == "6":
        pass
    elif option == "7":
        pass
    elif option == "8":
        print(colored("Quitting.", "red"))
        time.sleep(1)
        clearcmd()
        quit()
    
    elif option == "1337":
        print("You're", colored("elite.", "green"))
        time.sleep(2)
        usage()
    else:
        print("Did not reckognize", colored(option, "red"))
        enter()
        usage()
        

# Main Code
def main():
    usage()

main()
