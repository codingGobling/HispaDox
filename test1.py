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
    print"""OPCIONES
1)Modo dia
2)Modo nocturno
99)Atras"""
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

    print """Bienvenido a Hispadox beta
==========================
1)Doxing
2)Text
3)Text
4)Text
5)Opciones
99)Salir"""
    mainMenuChoice=(raw_input())

    if mainMenuChoice == "1":
        DoxingMenu()
    elif mainMenuChoice == "5":
        Options()
    elif mainMenuChoice == "99":
        exit
    else:
        MainMenu()
#DOXING
def DoxingMenu():
    cls()
    print """1)Busqueda por usuario
2)Busqueda por nombre
99)Atras"""
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
    print """Recuerda que algunas redes sociales no aceptan espacios en los nombres de usuario
Buscar por usuario:"""
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
    print """Recuerda que los nombres completos suelen dar resultados mas precisos
Busqueda por nombre:"""
    name=(raw_input())
    webbrowser.open('https://duckduckgo.com/' + name)
    webbrowser.open('https://plus.google.com/s/' + name + '/top')
    webbrowser.open('https://www.facebook.com/public/' + name)
    webbrowser.open(happyHuntingImage)
    MainMenu()   
MainMenu()







