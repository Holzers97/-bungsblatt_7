# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:47:06 2019

@author: stefan
"""
import random
import numpy as np
from rechteck import Rechteck
from Kreis import Kreis


class Formen:
    '''definiere Klasse Formen'''

    def flaeche(self):
        return

    def umfang(self):
        return

    def volumen(self):
        return 'Die Berechnung ist nicht näher definiert!'


class rechteck(Formen):
    '''definiere Klasse Rechteck inklusive geerbter Klasse Formen'''

    def __init__(self, laenge, breite):
        self.laenge = laenge
        self.breite = breite

# überschreibe Methoden von Formen
    def flaeche(self):
        area = self.laenge * self.breite
        return area

    def umfang(self):
        umf = 2 * self.breite + 2 * self.laenge
        return umf


class kreis(Formen):
    '''definiere Klasse kreismit geerbter Klasse Formen'''
    def __init__(self, radius):
        self. radius = radius

# überschreibe die Methoden flaeche, welche schon in Formen definiert wurden
    def flaeche(self):
        flae = (self.radius ** 2) * np.pi
        return flae

    def umfang(self):
        umf = 2 * (self.radius) * np.pi
        return umf


class Quader(Rechteck):
    '''definiere Quader,welcher Erbe von Rechteck und damit auch von Formen ist'''
    def __init__(self, laenge, breite, hohe):
        self.laenge = laenge
        self.breite = breite
        self.hohe = hohe

# überschreibe die Methode volumen
    def volumen(self):
        vol = self.laenge * self.breite * self.hohe
        return vol


print(Rechteck(1, 8).flaeche())
print(Rechteck(5, 1).umfang())
print(Kreis(2).Flaeche())
print(Kreis(5).Umfang())


# Zufallszahl zwischen 1 und 50 generieren:
def Number():
    return random.randint(1, 50)

# Liste mit zufälligen Kreisen und Rechtecken generieren:
List_10 = []
for i in range(10):
    Z = random.choice(['Rechteck', 'Kreis'])
    List_10.append(Z)

# Listen für A und U der erzeuten Rechtecke und Kreise:
Kreis_A = []
Kreis_U = []
Rechteck_A = []
Rechteck_U = []

# Über die List_10 interieren und ergebnisse mithilfe der importierten Klassen ausrechnen und in die eingefühten Listen anfügen.
for i in List_10:
    if i == 'Kreis':
        radius = Number()
        r = Kreis(radius)
        Kreis_A.append(r.Flaeche())
        Kreis_U.append(r.Umfang())
    elif i == 'Rechteck':
        breite = Number()
        laenge = Number()
        b = Rechteck(breite, laenge)
        Rechteck_A.append(b.flaeche())
        Rechteck_U.append(b.umfang())

print('Es sind ' + str(List_10.count('Kreis')) + ' Kreise und ' + str(List_10.count('Rechteck')) + ' Rechtecke erzeugt worden')
print('Der durchschnittliche Umfang der Keise beträgt ' + str(np.mean(Kreis_U)))
print('Der durchschnittliche Umfange der Rechtecke beträgt ' + str(np.mean(Rechteck_U)))
