import datetime
import os 
import random



#variables#
global main_menu
main_menu = False
cytaty = []

#funkcje#
def skaner_plikow():        #skanuje directory i zapisuje je do entry i drukuje go.
    print("Oto lista plików w tym folderze: ")
    print(" ")
    for entry in os.scandir('.'):
        if not entry.name.startswith('notepad.py') and not entry.name.startswith('q') and entry.is_file():
            print("*"+entry.name)
    print(" ")

def powitanie():        #generuję nam date i godzinę
    datetime_object = datetime.datetime.now()
    print(" ")
    print(25*" "+"-=-=-=-=-=   " + "Witaj w NoTaTnIkUv0.03!    " + str(datetime_object) + "   =-=-=-=-=-"+25*" " ) 
    print("")
    print("Wciśnij [h] i enter aby uzyskać pomoc.")
    global main_menu
    main_menu = True

def losuj_cytat():            #otwiera losowo jeden z plików których nazwa zaczyna się na q(liczba)
    rq = random.choice(cytaty)
    f = open(rq, "r")
    print("_  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  \n")
    print(f.read()) 
    print("_  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  \n")
    print("")
    
def scan_quotes_to_list():
    for entry in os.scandir('.'):
        if entry.name.startswith('q') and entry.is_file() and entry.name.endswith((".txt", ".TXT")):
            cytaty.append(entry.name)


def open_note():        #otwiera notkę o wybranje nazwie
    skaner_plikow()
    nazwa_wpisu = input("Wybierz nazwę pliku (bez.txt): ")
    if os.path.exists(nazwa_wpisu+".txt"):
        f = open(nazwa_wpisu+(".txt"), "r")#, encoding="utf-8")
        print("_  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  \n")
        print(f.read()) 
        print("_  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  \n")
        print("")
    else: print("Ten plik nie istnieje w tym folderze.")

def new_note():         #tworzy plik nowa notatka
    datetime_object = datetime.datetime.now()
    print("")  
    nazwa = input("Wybierz nazwę pliku...   ")
    if not nazwa == "q":
        f = open(nazwa +".txt", "x")
        tresc = input("Wpisz tutaj treść...   ")
        f.write(str(datetime_object) + "\n" + tresc)
        print("Plik " + nazwa + " został pomyślnie stworzony!")  
        print("") 
    else: print("Zaniechano!")

def help():         #otwiera pomoc
    f = open("_help.txt", "r", encoding="utf-8")
    print("_  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  \n")
    print(f.read()) 
    print("_  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  \n")
    print("")

def file_delete():
    x_file = input("Który plik pragniesz skasować? Wpisz kompletną nazwę pliku razem z końcówką .txt!   ")
    if os.path.exists(x_file):
        os.remove(x_file)
        print("Plik  " + x_file + "  został pomyślnie skasowany!   " )
        print("")
    else: print("Ten plik nie istnieje w tym folderze.   ")

def exit(): #wychodzi z programu
    quit()
    q = input("Czy na pewno chcesz wyjść? Wciśnij 'q' ponownie zatem!")
    if q == "q":
        quit()
    else : print("Nie zdecydowałeś się wyjść z programu!   ")

def cls():      #czyści terminal 
    os.system('cls' if os.name=='nt' else 'clear')

def mainLoop():         #główna pętla programu. zajmuję się danymi wejściowymi do menu 
    menu1 = input("Chcesz stworzyć (n)owy plik, czy (o)tworzyć już istniejący*? (*read only)   ")


    if menu1 == "n":    
        new_note()

        
    elif menu1 == "o":     
        open_note()
        
    elif menu1 == "del":
        skaner_plikow()
        file_delete()
        
    elif menu1 == "x" or menu1=="cytat":    
        losuj_cytat()
        
        
    elif menu1 =="c":
        cls()
      
        
    elif menu1 =="d":
        skaner_plikow()
       
        
    elif menu1 =="h" or menu1=="help":           
        help()
       
        
    elif menu1 =="q":       
        exit()
        
        
    else:  
        print("Nie rozumiem. wpisz 'o' albo 'n'! Wpisz 'q' jeśli chcesz wyjść!   ")   


#właściwy program#

scan_quotes_to_list()
powitanie()
while main_menu == True:
    mainLoop()    
    
    
    




    


