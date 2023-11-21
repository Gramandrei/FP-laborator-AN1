from Aufgabe1 import *

from main import *

def add_file(word, file_name):
    f = open(file_name, "a")
    f.write(word)
    f.close()

def wort():
    word = input("Schreibe ein Wort: ")
    add_file(word, "file.txt")
    word = word.lower()
    linie_noua()
    for ch in word:
        alfa[ch]()

def new_word():

    nw = input("Schreibe ein neues Zeichen:" )
    clear()
    if nw not in alfa:
        alfa[nw] = nw
        # print(alfa)
        while True:
            turtle.onkey(vorne, "w")
            turtle.onkey(hinten, "s")
            turtle.onkey(links, "a")
            turtle.onkey(rechts, "d")
            turtle.onkey(oben, "f")
            turtle.onkey(unten, "g")
            turtle.onkey(retur, "Return")
            turtle.listen()
            turtle.done()
    else:
        print("Das Zeichen ist schon in die Liste")

def main():
    wort()
    new_word()

main()