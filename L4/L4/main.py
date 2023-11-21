import turtle

from Aufgabe1 import *

def add_file1(word, file_name):
    f = open(file_name, "a")
    f.write(word)
    f.close()
def vorne():
    t.forward(10)
    add_file1("w\n", "wasd.txt")
def hinten():
    t.backward(10)
    add_file1("s\n", "wasd.txt")
def links():
    t.left(45)
    add_file1("a\n", "wasd.txt")
def rechts():
    t.right(45)
    add_file1("d\n", "wasd.txt")
def oben():
    t.up()
    add_file1("f\n", "wasd.txt")

def unten():
    t.down()
    add_file1("g\n", "wasd.txt")

def clear():
    t.reset()

def retur():
    turtle.Screen().bye()
    add_file1("Enter", "wasd.txt")
    turtle.done()