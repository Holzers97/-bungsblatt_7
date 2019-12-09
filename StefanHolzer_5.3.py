# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 14:01:11 2019

@author: stefa
"""
# imortieren vom random Parket:
import random as rm
# Spielbeschreibung ausgeben
print('*****Schere, Stein, Papier*** \n ****auf drei Gewinnt***')


# Definieren einer Funktion, die Input verlangt:
def Snik():
    input_h = input('Gib ein: ')
    input_c = rm.randint(1, 3)
    # ausgeben der zufälligen Computer generierten Werte:
    if input_c == 1:
        print('Computer : Schere')
    elif input_c == 2:
        print('Computer : Stein')
    else:
        print('Computer : Papier')
    # Spielregeln X=Unentschieden, V=Verloren, G=Gewonnen:
    if input_h == 'Schere':
        if input_c == 1:
            ergebniss = 'X'
        elif input_c == 2:
            ergebniss = 'V'
        else:
            ergebniss = 'G'
    elif input_h == 'Stein':
        if input_c == 1:
            ergebniss = 'G'
        elif input_c == 2:
            ergebniss = 'X'
        else:
            ergebniss = 'V'
    elif input_h == 'Papier':
        if input_c == 1:
            ergebniss = 'V'
        elif input_c == 2:
            ergebniss = 'G'
        else:
            ergebniss = 'X'
    else:
        raise TypeError
    return str(ergebniss)
# Funktion Snik() verwenden, um den Spielablauf zu generieren:
person = 0
computer = 0
# while-Schleife: a = spieler(Eingabe), c = computer:
while person < 3 and computer < 3:
    try:
        x = Snik()
        if x == 'G':
            person = person + 1
            print('Gewonnen')
        elif x == 'V':
            computer = computer + 1
            print('Verloren')
        elif x == 'X':
            print('unentschieden')
    except TypeError:
        print('Gib es richtig ein!')
# Wer zuerst 3 Mal 'Gewinnt';
else:
    if person == 3:
        print('Yessa! Du hast gewonnen!')
    else:
        print('Nope! Das war nichts. Du hast gegen den Computer verloren.')
