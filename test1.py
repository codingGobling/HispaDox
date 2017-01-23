import sys
import os
import webbrowser
import random

happyHuntingImage = "Banners\HPhunt.jpg"

os.system("color 0F") 

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def Banner():
    banner = random.choice(open('bannerList.txt').readlines())[:-1]
    myBanner = open(banner, 'r')
    bannerText = myBanner.read()
    myBanner.close()
    print bannerText
    
#OPTIONS
def Options():
    cls()
    print"""OPTIONS
1)Day Mode
2)Night mode
99)Back"""
    optionsChoice=(raw_input())
    if optionsChoice == "1":
        os.system("color F0")
        MainMenu()
    elif optionsChoice == "2":
        os.system("color 0F")
        MainMenu()
    elif optionsChoice == "99":
        MainMenu()
    else:
        Options()
        
#MAIN MENU
def MainMenu():
    cls()
    Banner()

    print """Welcome to advanced browser beta
===========================
1)Doxing
2)Text
3)Text
4)Delete yourself
5)Options
99)Exit"""
    mainMenuChoice=(raw_input())

    if mainMenuChoice == "1":
        DoxingMenu()
    elif mainMenuChoice == "4":
        DeleteYourselfMenu()
    elif mainMenuChoice == "5":
        Options()
    elif mainMenuChoice == "99":
        exit
    else:
        MainMenu()
#DOXING
def DoxingMenu():
    cls()
    print """1)Search by username
2)Search by name
99)Back"""
    DoxingMenuChoice=(raw_input())

    if DoxingMenuChoice == "1":
        SearchByUsername()
    elif DoxingMenuChoice == "2":
        SearchByName()
    elif DoxingMenuChoice == "99":
        MainMenu()
    else:
        DoxingMenu()


def SearchByUsername():
    cls()
    print """Remember that some social networks doesent allow spaces
Search username:"""
    username=(raw_input(""))
    webbrowser.open('https://duckduckgo.com/' + username)
    webbrowser.open('http://knowem.com/checkusernames.php?u=' + username)
    webbrowser.open('https://twitter.com/search?q=' + username)
    webbrowser.open('https://www.facebook.com/public/' + username)
    webbrowser.open('https://plus.google.com/s/' + username + '/top')
    webbrowser.open('https://www.youtube.com/results?search_query=' + username)
    webbrowser.open('http://steamcommunity.com/search/?text=&x=0&y=0#filter=users&text=' + username)
    webbrowser.open(happyHuntingImage)
    MainMenu()

def SearchByName():
    cls()
    print """Rembemer to use full names to find more accurate results"
Search by name:"""
    name=(raw_input())
    webbrowser.open('https://duckduckgo.com/' + name)
    webbrowser.open('https://plus.google.com/s/' + name + '/top')
    webbrowser.open('https://www.facebook.com/public/' + name)
    webbrowser.open(happyHuntingImage)
    MainMenu()

#DELETING YOURSELF
def DeleteYourselfMenu():
    cls()
    print "Delete me on:"
    print """
"""
    deleteYorselfMenuChoice=float(raw_input())
    MainMenu()
    
MainMenu()







