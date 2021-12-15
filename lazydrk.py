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
import subprocess

# Global Variables
discord = "drk#1337"
tooldir = "./assets/tools"

# Defines
def enter():
    input("Press enter to continue.")

def notwrk():
    print("This is currently under development. /drk")
    time.sleep(3)
    usage()

def misc():
    clearcmd()
    print(colored("""
     _______             __        __       __  __                     
    /       \           /  |      /  \     /  |/  |                    
    $$$$$$$  |  ______  $$ |   __ $$  \   /$$ |$$/   _______   _______ 
    $$ |  $$ | /      \ $$ |  /  |$$$  \ /$$$ |/  | /       | /       |
    $$ |  $$ |/$$$$$$  |$$ |_/$$/ $$$$  /$$$$ |$$ |/$$$$$$$/ /$$$$$$$/ 
    $$ |  $$ |$$ |  $$/ $$   $$<  $$ $$ $$/$$ |$$ |$$      \ $$ |      
    $$ |__$$ |$$ |      $$$$$$  \ $$ |$$$/ $$ |$$ | $$$$$$  |$$ \_____ 
    $$    $$/ $$ |      $$ | $$  |$$ | $/  $$ |$$ |/     $$/ $$       |
    $$$$$$$/  $$/       $$/   $$/ $$/      $$/ $$/ $$$$$$$/   $$$$$$$/ 
                                                                    
    """, "red"))
    print("""
    [1] Ifconfig
    [2] Whoami
    [3] Netstat
    [4] Coming soon.
    [5] Coming soon.
    [6] Coming soon.
    [7] Coming soon.
    [8] Coming soon.

    [9] Go back
    """)
    USERIN = input("Option: ")
    if USERIN == "1":
        print("-----------------")
        print("OUTPUT:")
        os.system('ipconfig' if os.name == 'nt' else 'ifconfig')
        print("-----------------")
        input("\nPress enter to continue.")
        misc()

    elif USERIN == "2":
        print("-----------------")
        print("OUTPUT:\n")
        os.system('whoami' if os.name == 'nt' else 'whoami')
        print("-----------------")
        input("\nPress enter to continue.")
        misc()

    elif USERIN == "3":
        print("-----------------")
        print("OUTPUT:\n")
        os.system('netstat' if os.name == 'nt' else 'netstat')
        print("-----------------")
        input("\nPress enter to continue.")
        misc()

    elif USERIN == "4":
        notwrk()

    elif USERIN == "5":
        notwrk()

    elif USERIN == "6":
        notwrk()

    elif USERIN == "7":
        notwrk()

    elif USERIN == "8":
        notwrk()

    elif USERIN == "9":
        usage()

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
        notwrk()
    elif option == "2":
        notwrk()
    elif option == "3":
        notwrk()
    elif option == "4":
        notwrk()
    elif option == "5":
        notwrk()
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
        misc()
    elif option == "2":
        drktools()
    elif option == "3":
        notwrk()
    elif option == "4":
        notwrk()
    elif option == "5":
        notwrk()
    elif option == "6":
        notwrk()
    elif option == "7":
        notwrk()
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
