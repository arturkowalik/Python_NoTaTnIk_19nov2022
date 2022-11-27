import datetime
import os 
import random
from pathlib import Path
import climage
from termcolor import colored
import fuzzywuzzy
from rapidfuzz import fuzz


#variables#
global main_menu
main_menu = False
cytaty = []

#funkcje#

def print_images(img_index, size):              #funkcja ta drukuje obrazky w konsolecie
    images=[]           #create list of files
    for entry in os.scandir('.'):       #scan the folder and add elements to list images[]
        if entry.name.startswith('q_img_') and entry.is_file():        #include _img files
            images.append(entry.name)           #append list
    #print(images)
    img = climage.convert(images[img_index], is_unicode=True, width=size)   
    print(img)

def skaner_plikow():        #skanuje directory i zapisuje je do entry i drukuje go.
    files_list = [] 
    print("Oto lista plików w tym folderze: ")
    print(" ")
    for entry in os.scandir('.'):
        if not entry.name.startswith('notepad.py') and not entry.name.startswith('q') and entry.is_file():
            files_list.append(entry.name)
            print("*"+entry.name)

    print(" ")

def powitanie():        #generuję nam date i godzinę
    datetime_object = datetime.datetime.now()
    print(" ")
    print(10*" "+"-=-=-=-=-=   " + "Witaj w NoTaTnIkUv0.03!    " + str(datetime_object) + "   =-=-=-=-=-"+10*" " ) 
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
        if entry.name.startswith('q') and entry.is_file() and entry.name.endswith((".txt", ".TXT")) and not entry.name.startswith("qq"):
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
    f = open("qhelp.txt", "r", encoding="utf-8")
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
    #PL menu1 = input("Chcesz stworzyć (n)owy plik, czy (o)tworzyć już istniejący*? (*read only)   ")
    defauly_text = colored("(N)ew note, (o)pen note, (d)isplay, (s)earch, (del)ete, (x) random quote, (c)lear console, (h)elp, (q)uit",'yellow' ,attrs=["reverse"]) + "    " 
    menu1 = input(defauly_text)


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
        print_images(4, 100)

      
        
    elif menu1 =="d":
        skaner_plikow()
       
        
    elif menu1 =="h" or menu1=="help":           
        help()
       
        
    elif menu1 =="q":       
        exit()
        
    elif menu1 =="s":
        search()
    
    elif menu1 =="g":
        skanuj_gsi()

    elif menu1 =="gs":
        skanuj_gsi_posortowane()
        
        
    else:  
        print("command unknown. Try entering 'h' for help. ")   


def search():
#program #
                                #search for strings inside a bigger strings
    global_files_search_index = []
    for entry in os.scandir('.'):
        if not entry.name.startswith('notepad') and not entry.name.startswith('q') and entry.is_file():
            
            global_files_search_index.append(entry.name) 
    
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
    lst = []
    lst = st.split()                                            #create a list from the user input, so each word is a sparate element
    #print("\n", sorted(lst))    
    search_input_question = colored("\n What word are you looking for?:", 'blue', attrs=["reverse"]) + "   "
    search_input = input(search_input_question)     #ask for the word to search for in the database
    search_input = search_input.lower()                         #lowercase the input
    if search_input == "q":
        return
    f = "info has been found in the index: "
    ff = "Wokół nastepujących słów: "
        
    def list_duplicates_of(seq,item):
        start_at = -1
        locs = []
        while True:
            try:
                loc = seq.index(item,start_at+1)
            except ValueError:
                break
            else:
                locs.append(loc)
                start_at = loc
        return locs

    fuzzy_list=[]
    
    for element in lst:
        if(fuzz.ratio(element, search_input)) > 90:
            fuzzy_list.append(element)
    
    
    print (fuzzy_list, "fuzzylist!")   
    fuzzy_list = list(dict.fromkeys(fuzzy_list))
    print (fuzzy_list, "fuzzylistdict!")

    globalMatches = []
    source = lst
    #print(list_duplicates_of(source, search_input))   
    globalMatches = list_duplicates_of(lst, search_input) 
    #print(globalMatches)
    
    if search_input in fuzzy_list:
        fuzzy_list.remove(search_input)
    
    if len(fuzzy_list) > 0:
        globalMatches1 = list_duplicates_of(lst, fuzzy_list[0]) 
    if len(fuzzy_list) > 1:
        globalMatches2 = list_duplicates_of(lst, fuzzy_list[1]) 
    if len(fuzzy_list) > 2:
        globalMatches3 = list_duplicates_of(lst, fuzzy_list[2]) 
    #print(globalMatches1)
    
    #print(globalMatches)
    total_counts = 0
    for index in globalMatches:
        total_counts += 1
        print("\n" + colored("▋", 'blue',attrs=[ "blink"])+"["+ colored(str(index), 'green')+"]  " + colored(search_input, attrs=["reverse"]))
        i=-13 
        print("...", end=' ')
        while i< 13:
            print(lst[index+i], end=" ")
            i += 1
            
            
        print("... \n")
    print("========== SEARCH FINISHED with "+ colored(str(total_counts), 'yellow', attrs=["bold", "blink", "reverse"]) +" results ! ========== \n \n" )   
    
    if len(fuzzy_list) >= 1:
        total_counts1 = 0
        for index in globalMatches1:
            
            total_counts1 += 1
            print("\n" + colored("▋", 'cyan',attrs=[ "blink"])+"["+ colored(str(index), 'green')+"]  " + colored(fuzzy_list[0], attrs=["reverse"]), colored("f", 'cyan'))
            i=-13 
            print("...", end=' ')
            while i< 13:
                print(lst[index+i], end=" ")
                i += 1
                
                
            print("... \n")
        print("========== FUZZY SEARCH FINISHED with "+ colored(str(total_counts1), 'yellow', attrs=["bold", "blink", "reverse"]) +" results! ========== \n \n" )   


    if len(fuzzy_list) >= 2:
        total_counts2 = 0
        for index in globalMatches2:
            
            total_counts2 += 1
            print("\n" + colored("▋", 'magenta',attrs=[ "blink"])+"["+ colored(str(index), 'green')+"]  " + colored(fuzzy_list[1], attrs=["reverse"]), colored("f", 'cyan' ))
            i=-13 
            print("...", end=' ')
            while i< 13:
                print(lst[index+i], end=" ")
                i += 1
                
                
            print("... \n")
        print("========== FUZZY SEARCH FINISHED with "+ colored(str(total_counts2), 'yellow', attrs=["bold", "blink", "reverse"]) +" results! ========== \n \n" )   


    if len(fuzzy_list) >= 3:
        total_counts3 = 0
        for index in globalMatches3:
            
            total_counts3 += 1
            print("\n" + colored("▋", 'yellow',attrs=[ "blink"])+"["+ colored(str(index), 'green')+"]  " + colored(fuzzy_list[2], attrs=["reverse"]), colored("f", 'cyan' ))
            i=-13 
            print("...", end=' ')
            while i< 13:
                print(lst[index+i], end=" ")
                i += 1
                
                
            print("... \n")
        print("========== FUZZY SEARCH FINISHED with "+ colored(str(total_counts2), 'yellow', attrs=["bold", "blink", "reverse"]) +" results! ========== \n \n" )   




    def search_index():
        index = input("search index? :")
        print("...", end=' ')
        i = -150
        while i< 150:
            print(lst[int(int(index) + i)], end=" ")
            i += 1              

        print("... \n")
    
    if total_counts>0:  search_index()    
#end of program



def skanuj_gsi():
    f = open('qGSI.txt', 'r')                                  #This is the text to search in ")               #take input form user in form of string as database to search in
    st = f.read()
    st = st.lower()                                             #lowercase  the list
    lst = st.split()                                            #create a list from the user input, so each word is a sparate element
    print(lst)

def skanuj_gsi_posortowane():
    f = open('qGSI.txt', 'r')                                  #This is the text to search in ")               #take input form user in form of string as database to search in
    st = f.read()
    st = st.lower()                                             #lowercase  the list
    lst = st.split()                                            #create a list from the user input, so each word is a sparate element
    lst = sorted(lst)
    print(lst)


#właściwy program#
print_images(3, 100)
scan_quotes_to_list()
powitanie()
while main_menu == True:
    mainLoop()    
    
    
    




    


