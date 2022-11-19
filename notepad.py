import datetime
import os 


datetime_object = datetime.datetime.now()
global main_menu
main_menu = False

def skaner_plikow():
    
    print("Oto lista plików w tym folderze: ")
    print(" ")
    #skanuje directory i zapisuje je do entry. Następnie dl akażego pliku który nie zaczyna się na notepad drukuje go.
    for entry in os.scandir('.'):
        if not entry.name.startswith('notepad.py') and entry.is_file():
            print("*"+entry.name)
    print(" ")

def powitanie():
    #generuję nam date i godzinę
    print(" ")
    print(25*" "+"-=-=-=-=-=   " + "Witaj w NoTaTnIkUv0.01!    " + str(datetime_object) + "   =-=-=-=-=-"+25*" " ) 
    print("")
    skaner_plikow()
    global main_menu
    main_menu = True

def mainLoop():
    #zapytaj czy chcesz stworzyc nowy plik czy otworzyc stary
    menu1 = input("Chcesz stworzyć (n)owy plik, czy (o)tworzyć już istniejący*? (*read only) ")
    #jesli nowy plik to stwórz nowy plik
    print(menu1)
   

   
    if menu1 == "n": 
        nazwa = input("Wybierz nazwę pliku...   ")
        f = open(nazwa +".txt", "x")
        tresc = input("Wpisz tutaj treść...   ")
        f.write(str(datetime_object) + "\n" + tresc)
        print("")

        
    elif menu1 == "o":
        numer_wpisu = input("Wybierz nazwę pliku (bez.txt): ")
        f = open(numer_wpisu+(".txt"), "r")
        print("_  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  \n")
        print(f.read()) 
        print("_  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  \n")
        print("")
        
    elif menu1 =="q":       #zajmuje się wyjściem z aplikacji
        q = input("Czy na pewno chcesz wyjść? Wciśnij 'q' ponownie zatem!")
        if q == "q":
            quit()
        else : print("Nie zdecydowałeś się wyjść z programu!")
        
    else:  
        print("Nie rozumiem. wpisz 'o' albo 'n'! Wpisz 'q' jeśli chcesz wyjść!")   


        

#tutaj jest właściwy program:

powitanie()  #skanuje pliki i czyta powitanie 

while main_menu == True: #główna pętla która zajmuję się całą funkcjonalnością
    mainLoop()    
    
    
    




    


