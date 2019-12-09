# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 15:30:40 2019

@author: stefa
"""
# importieren von numpy
import numpy as np
# iportieren der Klassen rechteck, kreis, Quader
from formen import rechteck
from formen import kreis
from formen import Quader


# Testfunktionen erstellen und korrektheit anschließend in der Konsole prüfen
def test_for_rechteck_flaeche():
    assert rechteck(2, 2).flaeche() == 4


def test_for_rechteck_umfang():
    assert rechteck(2, 2).umfang() == 8


def test_for_kreis_flaeche():
    assert kreis(1).flaeche() == np.pi


def test_for_kreis_umfang():
    assert kreis(1).umfang() == 2*np.pi


def test_for_Quader_volumen():
    assert Quader(1, 1, 1).volumen() == 1

# Mit '!pytest' die Funktionalität der Methoden in der Konsole prüfen