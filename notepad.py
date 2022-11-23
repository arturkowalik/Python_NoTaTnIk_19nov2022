import datetime
import os 
import random
from pathlib import Path


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
        
    elif menu1 =="s":
        search()
        
        
    else:  
        print("Nie rozumiem. wpisz 'o' albo 'n'! Wpisz 'q' jeśli chcesz wyjść!   ")   


def search():
#program #
                                #search for strings inside a bigger strings
    global_files_search_index = []
    for entry in os.scandir('.'):
        if not entry.name.startswith('notepad.py') and not entry.name.startswith('q') and entry.is_file():
            
            global_files_search_index.append(entry.name) 
    #print(global_files_search_index)
    
    # skaner_plikow()    
    # nazwa_wpisu = input("Wybierz nazwę pliku (bez.txt): ")
    # nazwaplikutxt = nazwa_wpisu+".txt"
    # if os.path.exists(nazwa_wpisu+".txt"):
    #     print("_  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  \n")
    #     search.x = Path(nazwaplikutxt).read_text()
    #     print(search.x)
    #     print("_  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  \n")
    #     print("")
    # else: print("Ten plik nie istnieje w tym folderze.")
    
    file_object  = open('qGSI.txt', 'a')
    file_object.truncate(0)

    #index wszystkich słów do jednego plikuj qGSI.txt
    for filenameinGFSI in global_files_search_index:
        file_object  = open('qGSI.txt', 'a')
        file_object.write("\n"+ filenameinGFSI+ "\n")
        file_object.write(Path(filenameinGFSI).read_text())
        file_object.write("\n\n==========\n \n")
        #file_object.close()
        
    
    
    f = open('qGSI.txt', 'r')                                  #This is the text to search in ")               #take input form user in form of string as database to search in
    st = f.read()
    st = st.lower()                                             #lowercase  the list

    lst = st.split()                                            #create a list from the user input, so each word is a sparate element
    #print(lst)    

    search_input = input("What word are you looking for? ")     #ask for the word to search for in the database
    search_input = search_input.lower()                         #lowercase the input
    f = "info has been found in the index: "
    ff = "Wokół nastepujących słów: "
    sindex = 0
    def lookFor():                                              #loop the database list with the question is the word there
        for word in lst:                                        #for every element in the list
            if word == search_input:                            #check if element is same as the searched word
                sindex = st.index(search_input)
                print("\n '" + search_input + "' was located in this context: " + "\n")
                i=-65 
                while i< 65:
                    print(st[sindex+i], end=" ")
                    i += 1
                print("\n")

                return True                                     #and return True + break out of loop
        print("The string  '" + search_input + "'  was not found in the Global Search Index")                                      #else print negative message
        
        
    lookFor()                                                   #exectue the loop once
#end of program


       


#właściwy program#

scan_quotes_to_list()
powitanie()
while main_menu == True:
    mainLoop()    
    
    
    




    


