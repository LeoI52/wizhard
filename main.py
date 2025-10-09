"""
@author : Léo Imbert & Yael Ennon
@created : 11/09/25
@updated : 08/10/25
"""

#? -------------------- IMPORTATIONS -------------------- ?#

import colorsys
import random
import pyxel
import math
import time

#? -------------------- UTILS -------------------- ?#

FONT_DEFAULT = {
    " ":[[0,0,0,0]],
    "A":[[0,0,0,0,0,0],[0,0,1,1,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,1,1,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1]],
    "B":[[0,0,0,0,0,0,0],[1,1,1,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[1,1,1,1,1,1,0]],
    "C":[[0,0,0,0,0,0,0],[0,0,1,1,1,1,0],[0,1,1,0,0,1,1],[1,1,0,0,0,0,0],[1,1,0,0,0,0,0],[1,1,0,0,0,0,0],[0,1,1,0,0,1,1],[0,0,1,1,1,1,0]],
    "D":[[0,0,0,0,0,0,0],[1,1,1,1,1,0,0],[0,1,1,0,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,1,1,0],[1,1,1,1,1,0,0]],
    "E":[[0,0,0,0,0,0,0],[1,1,1,1,1,1,1],[0,1,1,0,0,0,1],[0,1,1,0,1,0,0],[0,1,1,1,1,0,0],[0,1,1,0,1,0,0],[0,1,1,0,0,0,1],[1,1,1,1,1,1,1]],
    "F":[[0,0,0,0,0,0,0],[1,1,1,1,1,1,1],[0,1,1,0,0,0,1],[0,1,1,0,1,0,0],[0,1,1,1,1,0,0],[0,1,1,0,1,0,0],[0,1,1,0,0,0,0],[1,1,1,1,0,0,0]],
    "G":[[0,0,0,0,0,0,0],[0,0,1,1,1,1,0],[0,1,1,0,0,1,1],[1,1,0,0,0,0,0],[1,1,0,0,0,0,0],[1,1,0,0,1,1,1],[0,1,1,0,0,1,1],[0,0,1,1,1,1,1]],
    "H":[[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,1,1,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1]],
    "I":[[0,0,0,0,0,0],[1,1,1,1,1,1],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[1,1,1,1,1,1]],
    "J":[[0,0,0,0,0,0,0],[0,0,0,1,1,1,1],[0,0,0,0,1,1,0],[0,0,0,0,1,1,0],[0,0,0,0,1,1,0],[1,1,0,0,1,1,0],[1,1,0,0,1,1,0],[0,1,1,1,1,0,0]],
    "K":[[0,0,0,0,0,0,0],[1,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,1,1,0],[0,1,1,1,1,0,0],[0,1,1,0,1,1,0],[0,1,1,0,0,1,1],[1,1,1,0,0,1,1]],
    "L":[[0,0,0,0,0,0,0],[1,1,1,1,0,0,0],[0,1,1,0,0,0,0],[0,1,1,0,0,0,0],[0,1,1,0,0,0,0],[0,1,1,0,0,0,1],[0,1,1,0,0,1,1],[1,1,1,1,1,1,1]],
    "M":[[0,0,0,0,0,0,0],[1,1,0,0,0,1,1],[1,1,1,0,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,0,1,0,1,1],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1]],
    "N":[[0,0,0,0,0,0,0],[1,1,0,0,0,1,1],[1,1,1,0,0,1,1],[1,1,1,1,0,1,1],[1,1,0,1,1,1,1],[1,1,0,0,1,1,1],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1]],
    "O":[[0,0,0,0,0,0,0],[0,0,1,1,1,0,0],[0,1,1,0,1,1,0],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1],[0,1,1,0,1,1,0],[0,0,1,1,1,0,0]],
    "P":[[0,0,0,0,0,0,0],[1,1,1,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,1,1,1,0],[0,1,1,0,0,0,0],[0,1,1,0,0,0,0],[1,1,1,1,0,0,0]],
    "Q":[[0,0,0,0,0,0,0],[0,0,1,1,1,0,0],[0,1,1,0,1,1,0],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1],[1,1,0,1,1,0,1],[1,1,0,0,1,1,0],[0,1,1,1,0,1,1]],
    "R":[[0,0,0,0,0,0,0],[1,1,1,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,1,1,1,0],[0,1,1,0,1,1,0],[0,1,1,0,0,1,1],[1,1,1,0,0,1,1]],
    "S":[[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,0,0],[0,1,1,1,1,0],[0,0,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "T":[[0,0,0,0,0,0],[1,1,1,1,1,1],[1,0,1,1,0,1],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,1,1,1,1,0]],
    "U":[[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "V":[[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0],[0,0,1,1,0,0]],
    "W":[[0,0,0,0,0,0,0],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1],[1,1,0,1,0,1,1],[1,1,1,1,1,1,1],[1,1,1,0,1,1,1],[1,1,0,0,0,1,1]],
    "X":[[0,0,0,0,0,0,0],[1,1,0,0,0,1,1],[0,1,1,0,1,1,0],[0,0,1,1,1,0,0],[0,0,1,1,1,0,0],[0,1,1,0,1,1,0],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1]],
    "Y":[[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,1,1,1,1,0]],
    "Z":[[0,0,0,0,0,0,0],[1,1,1,1,1,1,1],[1,1,0,0,0,1,1],[1,0,0,0,1,1,0],[0,0,0,1,1,0,0],[0,0,1,1,0,0,1],[0,1,1,0,0,1,1],[1,1,1,1,1,1,1]],
    "a":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,1,1,1,0,0],[0,0,0,0,1,1,0],[0,1,1,1,1,1,0],[1,1,0,0,1,1,0],[0,1,1,1,0,1,1]],
    "b":[[0,0,0,0,0,0,0],[1,1,1,0,0,0,0],[0,1,1,0,0,0,0],[0,1,1,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[1,1,0,1,1,1,0]],
    "c":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,0,0],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "d":[[0,0,0,0,0,0,0],[0,0,0,1,1,1,0],[0,0,0,0,1,1,0],[0,1,1,1,1,1,0],[1,1,0,0,1,1,0],[1,1,0,0,1,1,0],[1,1,0,0,1,1,0],[0,1,1,1,0,1,1]],
    "e":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,1,1,1,1],[1,1,0,0,0,0],[0,1,1,1,1,0]],
    "f":[[0,0,0,0,0,0],[0,0,1,1,1,0],[0,1,1,0,1,1],[0,1,1,0,0,0],[1,1,1,1,0,0],[0,1,1,0,0,0],[0,1,1,0,0,0],[1,1,1,1,0,0]],
    "g":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,1],[0,0,0,0,1,1],[1,1,1,1,1,0]],
    "h":[[0,0,0,0,0,0,0],[1,1,1,0,0,0,0],[0,1,1,0,0,0,0],[0,1,1,0,1,1,0],[0,1,1,1,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[1,1,1,0,0,1,1]],
    "i":[[0,0,0,0],[0,1,1,0],[0,0,0,0],[1,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0],[1,1,1,1]],
    "j":[[0,0,0,0,0,0],[0,0,0,0,1,1],[0,0,0,0,0,0],[0,0,0,1,1,1],[0,0,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "k":[[0,0,0,0,0,0,0],[1,1,1,0,0,0,0],[0,1,1,0,0,0,0],[0,1,1,0,0,1,1],[0,1,1,0,1,1,0],[0,1,1,1,1,0,0],[0,1,1,0,1,1,0],[1,1,1,0,0,1,1]],
    "l":[[0,0,0,0],[1,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0],[1,1,1,1]],
    "m":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,1,0,1,1,0],[1,1,1,1,1,1,1],[1,1,0,1,0,1,1],[1,1,0,1,0,1,1],[1,1,0,0,0,1,1]],
    "n":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,0,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1]],
    "o":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "p":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,0,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,1,1,1,0],[0,1,1,0,0,0,0],[1,1,1,1,0,0,0]],
    "q":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,1,1,0,1,1],[1,1,0,0,1,1,0],[1,1,0,0,1,1,0],[0,1,1,1,1,1,0],[0,0,0,0,1,1,0],[0,0,0,1,1,1,1]],
    "r":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,0,1,1,1,0],[0,1,1,1,0,1,1],[0,1,1,0,0,0,0],[0,1,1,0,0,0,0],[1,1,1,1,0,0,0]],
    "s":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,0,0],[0,1,1,1,1,0],[0,0,0,0,1,1],[1,1,1,1,1,0]],
    "t":[[0,0,0,0,0,0],[0,1,1,0,0,0],[0,1,1,0,0,0],[1,1,1,1,1,0],[0,1,1,0,0,0],[0,1,1,0,0,0],[0,1,1,0,1,1],[0,0,1,1,1,0]],
    "u":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,1]],
    "v":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0],[0,0,1,1,0,0]],
    "w":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,0,0,0,1,1],[1,1,0,1,0,1,1],[1,1,0,1,0,1,1],[1,1,1,1,1,1,1],[0,1,1,0,1,1,0]],
    "x":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,0,0,0,1,1],[0,1,1,0,1,1,0],[0,0,1,1,1,0,0],[0,1,1,0,1,1,0],[1,1,0,0,0,1,1]],
    "y":[[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,1],[0,0,0,0,1,1],[1,1,1,1,1,0]],
    "z":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,1,1,1,1],[1,0,0,1,1,0],[0,0,1,1,0,0],[0,1,1,0,0,1],[1,1,1,1,1,1]],
    "1":[[0,0,0,0,0,0],[0,0,1,1,0,0],[0,1,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[1,1,1,1,1,1]],
    "2":[[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[0,0,0,0,1,1],[0,1,1,1,1,0],[1,1,0,0,0,0],[1,1,0,0,1,1],[1,1,1,1,1,1]],
    "3":[[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[0,0,0,0,1,1],[0,0,1,1,1,0],[0,0,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "4":[[0,0,0,0,0,0,0],[0,0,0,1,1,1,0],[0,0,1,1,1,1,0],[0,1,1,0,1,1,0],[1,1,0,0,1,1,0],[1,1,1,1,1,1,1],[0,0,0,0,1,1,0],[0,0,0,1,1,1,1]],
    "5":[[0,0,0,0,0,0],[1,1,1,1,1,1],[1,1,0,0,0,1],[1,1,0,0,0,0],[1,1,1,1,1,0],[0,0,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "6":[[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,0,0],[1,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "7":[[0,0,0,0,0,0],[1,1,1,1,1,1],[1,1,0,0,1,1],[0,0,0,0,1,1],[0,0,0,1,1,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0]],
    "8":[[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "9":[[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,1],[0,0,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "0":[[0,0,0,0,0,0,0],[0,1,1,1,1,1,0],[1,1,0,0,0,1,1],[1,1,0,0,1,1,1],[1,1,0,1,0,1,1],[1,1,1,0,0,1,1],[1,1,0,0,0,1,1],[0,1,1,1,1,1,0]],
    "?":[[0,0,0,0],[1,1,1,0],[1,0,1,1],[0,0,1,1],[0,1,1,0],[0,0,0,0],[0,1,1,0],[0,1,1,0]],
    ",":[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,1,1,0],[0,1,1,0],[1,1,0,0]],
    ".":[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[1,1,0],[1,1,0]],
    ";":[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0],[0,1,1,0],[0,1,1,0],[1,1,0,0]],
    "/":[[0,0,0,0,0,0],[0,0,0,0,1,1],[0,0,0,0,1,0],[0,0,0,1,1,0],[0,0,1,1,0,0],[0,0,1,0,0,0],[0,1,1,0,0,0],[1,1,0,0,0,0]],
    ":":[[0,0],[0,0],[1,1],[1,1],[0,0],[1,1],[1,1],[0,0]],
    "!":[[0,0],[1,1],[1,1],[1,1],[1,1],[0,0],[1,1],[1,1]],
    "&":[[0,1,1,1,0,0,0],[1,0,0,0,1,0,0],[1,0,0,0,1,0,0],[0,1,1,1,0,0,0],[1,1,0,1,1,0,0],[1,0,0,0,1,0,1],[1,1,0,0,0,1,0],[0,1,1,1,1,0,1]],
    "é":[[0,0,0,1,1,0],[0,1,1,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,1,1,1,1],[1,1,0,0,0,0],[0,1,1,1,1,0]],
    "~":[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,1,1,0,1],[1,0,0,1,0]],
    '"':[[0,0,0,0],[0,1,0,1],[0,1,0,1],[1,0,1,0],[1,0,1,0]],
    "#":[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,1,0,1,0],[1,1,1,1,1],[0,1,0,1,0],[1,1,1,1,1],[0,1,0,1,0]],
    "'":[[0,0,0,0,0],[0,0,1,1,0],[0,0,1,1,0],[0,1,1,0,0],[0,1,1,0,0]],
    "{":[[0,0,0],[0,0,1],[0,1,0],[0,1,0],[1,0,0],[0,1,0],[0,1,0],[0,0,1]],
    "(":[[0,0,0],[0,0,1],[0,1,0],[1,0,0],[1,0,0],[1,0,0],[0,1,0],[0,0,1]],
    "[":[[0,0,0],[1,1,1],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,1,1]],
    "-":[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,1,1,1],[1,1,1,1],[0,0,0,0],[0,0,0,0]],
    "|":[[1],[1],[1],[1],[1],[1],[1],[1]],
    "è":[[0,1,1,0,0,0],[0,0,0,1,1,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,1,1,1,1],[1,1,0,0,0,0],[0,1,1,1,1,0]],
    "_":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,1,1,1,1]],
    "ç":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,0,0],[1,1,0,0,1,1],[0,1,1,1,1,0],[0,0,0,1,0,0],[0,0,1,0,0,0]],
    "à":[[0,0,1,1,0,0,0],[0,0,0,0,1,1,0],[0,0,0,0,0,0,0],[0,1,1,1,1,0,0],[0,0,0,0,1,1,0],[0,1,1,1,1,1,0],[1,1,0,0,1,1,0],[0,1,1,1,0,1,1]],
    "@":[[0,0,0,0,0,0,0],[0,0,1,1,1,1,0],[0,1,0,0,0,0,1],[1,0,0,1,1,0,1],[1,0,1,0,0,1,1],[1,0,1,0,0,1,1],[1,0,0,1,1,0,0],[0,1,0,0,0,0,1],[0,0,1,1,1,1,0]],
    "°":[[1,1,1],[1,0,1],[1,1,1]],
    ")":[[0,0,0],[1,0,0],[0,1,0],[0,0,1],[0,0,1],[0,0,1],[0,1,0],[1,0,0]],
    "]":[[0,0,0],[1,1,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[1,1,1]],
    "+":[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[1,1,1,1,1],[0,0,1,0,0],[0,0,1,0,0]],
    "=":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,1,1,1,1],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,1,1,1,1],[0,0,0,0,0,0]],
    "}":[[0,0,0],[1,0,0],[0,1,0],[0,1,0],[0,0,1],[0,1,0],[0,1,0],[1,0,0]],
    "*":[[0,0,0],[1,0,1],[0,1,0],[1,0,1]],
    "%":[[0,1,0,0,0,0,0],[1,0,1,0,1,1,0],[0,1,0,0,1,0,0],[0,0,0,1,1,0,0],[0,0,1,1,0,0,0],[0,0,1,0,0,1,0],[0,1,1,0,1,0,1],[1,1,0,0,0,1,0]],
    "€":[[0,0,0,0,0,0],[0,0,1,1,1,0],[0,1,0,0,0,1],[0,1,1,1,0,0],[1,0,0,0,0,0],[0,1,1,1,0,0],[0,1,0,0,0,1],[0,0,1,1,1,0]],
    "$":[[0,0,1,0,0],[0,1,1,1,0],[1,0,1,0,1],[1,0,1,0,0],[0,1,1,1,0],[0,0,1,0,1],[1,0,1,0,1],[0,1,1,1,0],[0,0,1,0,0]],
    "^":[[0,0,0],[0,1,0],[1,0,1]]
}

NORMAL_COLOR_MODE = 0
ROTATING_COLOR_MODE = 1
RANDOM_COLOR_MODE = 2

ANCHOR_TOP_LEFT = 0
ANCHOR_TOP_RIGHT = 1
ANCHOR_BOTTOM_LEFT = 2
ANCHOR_BOTTOM_RIGHT = 3
ANCHOR_LEFT = 4
ANCHOR_RIGHT = 5
ANCHOR_TOP = 6
ANCHOR_BOTTOM = 7
ANCHOR_CENTER = 8

BOTTOM = 0
TOP = 1
LEFT = 2
RIGHT = 3

class Transition:

    def __init__(self, new_scene_id:int, speed:int, transition_color:int, new_camera_x:int=0, new_camera_y:int=0, action=None):
        self.new_scene_id = new_scene_id
        self.speed = speed
        self.transition_color = transition_color
        self.new_camera_x = new_camera_x
        self.new_camera_y = new_camera_y
        self.action = action
        self.direction = 1

class TransitionRectangle(Transition):

    def __init__(self, new_scene_id:int, duration:float, transition_color:int, dir:int=LEFT, new_camera_x:int=0, new_camera_y:int=0, action=None, fps:int=60):
        speed = pyxel.width / (duration / 2 * fps) if dir in [LEFT, RIGHT] else pyxel.height / (duration / 2 * fps)
        super().__init__(new_scene_id, speed, transition_color, new_camera_x, new_camera_y, action)
        self.dir = dir
        self.w = 0
        self.x = pyxel.width if dir == RIGHT else 0
        self.y = pyxel.height if dir == BOTTOM else 0

    def update(self, pyxel_manager):
        if self.dir in [RIGHT, LEFT]:
            self.w += self.speed * self.direction

            if (self.direction == 1 and self.dir == RIGHT) or (self.direction == -1 and self.dir == LEFT):
                self.x = self.x - self.speed if self.dir == RIGHT else self.x + self.speed
            if self.w > pyxel.width and self.direction == 1:
                self.direction = -1
                pyxel_manager.change_scene(self.new_scene_id, self.new_camera_x, self.new_camera_y, self.action)
                self.x = 0
            if self.w < 0 and self.direction == -1:
                pyxel_manager.finish_transition()
                return
        elif self.dir in [TOP, BOTTOM]:
            self.w += self.speed * self.direction

            if (self.direction == 1 and self.dir == BOTTOM) or (self.direction == -1 and self.dir == TOP):
                self.y = self.y - self.speed if self.dir == BOTTOM else self.y + self.speed
            if self.w > pyxel.height and self.direction == 1:
                self.direction = -1
                pyxel_manager.change_scene(self.new_scene_id, self.new_camera_x, self.new_camera_y, self.action)
                self.y = 0
            if self.w < 0 and self.direction == -1:
                pyxel_manager.finish_transition()
                return

    def draw(self, pyxel_manager):
        if self.dir in [RIGHT, LEFT]:
            pyxel.rect(pyxel_manager.camera_x + self.x, pyxel_manager.camera_y, self.w, pyxel.height, self.transition_color)
        elif self.dir in [TOP, BOTTOM]:
            pyxel.rect(pyxel_manager.camera_x, pyxel_manager.camera_y + self.y, pyxel.width, self.w, self.transition_color)

class PyxelManager:

    def __init__(self, width:int, height:int, scenes:list, default_scene_id:int=0, fps:int=60, fullscreen:bool=False, mouse:bool=False, quit_key:int=pyxel.KEY_ESCAPE, camera_x:int=0, camera_y:int=0, debug_background_color:int=0, debug_text_color:int=7):
        
        self.__scenes_dict = {scene.id:scene for scene in scenes}
        self.__current_scene = self.__scenes_dict[default_scene_id]
        self.__transition = None

        self.__cam_x = self.__cam_tx = camera_x
        self.__cam_y = self.__cam_ty = camera_y
        self.__cam_bounds = (-float("inf"), -float("inf"), float("inf"), float("inf"))
        self.__shake_amount = 0
        self.__shake_decay = 0

        self.__flash = {}

        self.__fps = fps
        self.__previous_frame_time = time.time()
        self.__current_fps = 0

        self.debug = False
        self.debug_background_color = debug_background_color
        self.debug_text_color = debug_text_color

        pyxel.init(width, height, fps=fps, quit_key=quit_key)
        pyxel.fullscreen(fullscreen)
        pyxel.mouse(mouse)

        if self.__current_scene.pyxres_path:
            pyxel.load(self.__current_scene.pyxres_path)
        pyxel.title(self.__current_scene.title)
        pyxel.screen_mode(self.__current_scene.screen_mode)
        pyxel.colors.from_list(self.__current_scene.palette)

    @property
    def camera_x(self)-> int|float:
        return self.__cam_x
    
    @property
    def camera_y(self)-> int|float:
        return self.__cam_y

    @property
    def mouse_x(self)-> int:
        return self.__cam_x + pyxel.mouse_x
    
    @property
    def mouse_y(self)-> int:
        return self.__cam_y + pyxel.mouse_y
    
    def set_camera(self, new_camera_x:int, new_camera_y:int):
        self.__cam_x = self.__cam_tx = max(self.__cam_bounds[0], min(new_camera_x, self.__cam_bounds[2] - pyxel.width))
        self.__cam_y = self.__cam_ty = max(self.__cam_bounds[1], min(new_camera_y, self.__cam_bounds[3] - pyxel.height))

    def move_camera(self, new_camera_x:int, new_camera_y:int):
        self.__cam_tx = max(self.__cam_bounds[0], min(new_camera_x, self.__cam_bounds[2] - pyxel.width))
        self.__cam_ty = max(self.__cam_bounds[1], min(new_camera_y, self.__cam_bounds[3] - pyxel.height))

    def set_camera_bounds(self, min_x:int, min_y:int, max_x:int, max_y:int):
        self.__cam_bounds = (min_x, min_y, max_x, max_y)
        self.__cam_tx = max(self.__cam_bounds[0], min(self.__cam_tx, self.__cam_bounds[2] - pyxel.width))
        self.__cam_ty = max(self.__cam_bounds[1], min(self.__cam_ty, self.__cam_bounds[3] - pyxel.height))
        self.__cam_x = max(self.__cam_bounds[0], min(self.__cam_x, self.__cam_bounds[2] - pyxel.width))
        self.__cam_y = max(self.__cam_bounds[1], min(self.__cam_y, self.__cam_bounds[3] - pyxel.height))

    def shake_camera(self, amount:int, decay:float):
        self.__shake_amount = amount
        self.__shake_decay = decay

    def flash(self, lifespan:int, color:int, intensity:float):
        self.__flash = {"life":lifespan, "color":color, "intensity":intensity}

    def change_scene(self, new_scene_id:int, new_camera_x:int=0, new_camera_y:int=0, action=None):
        self.set_camera(new_camera_x, new_camera_y)

        self.__current_scene = self.__scenes_dict[new_scene_id]
        if action:
            action()

        #if self.__current_scene.pyxres_path:
            #pyxel.load(self.__current_scene.pyxres_path)
        #pyxel.colors.from_list(self.__current_scene.palette)
        pyxel.title(self.__current_scene.title)
        pyxel.screen_mode(self.__current_scene.screen_mode)

    def change_scene_transition(self, transition:Transition):
        self.__transition = transition

    def finish_transition(self):
        self.__transition = None

    def apply_palette_effect(self, effect_function, **kwargs):
        pyxel.colors.from_list(effect_function(self.__current_scene.palette, kwargs))

    def reset_palette(self):
        pyxel.colors.from_list(self.__current_scene.palette)

    def update(self):
        if self.__transition:
            self.__transition.update(self)

        self.__cam_x += (self.__cam_tx - self.__cam_x) * 0.1
        self.__cam_y += (self.__cam_ty - self.__cam_y) * 0.1

        if self.__shake_amount > 0:
            a = self.__shake_amount
            pyxel.camera(self.__cam_x + random.uniform(-a, a), self.__cam_y + random.uniform(-a, a))
            self.__shake_amount = max(0, self.__shake_amount - self.__shake_decay)
        else:
            pyxel.camera(self.__cam_x, self.__cam_y)

        if not self.__transition:
            self.__current_scene.update()

    def draw(self):
        self.__current_scene.draw()
        if self.__transition:
            self.__transition.draw(self)

        if self.__flash:
            pyxel.dither(self.__flash["intensity"])
            pyxel.rect(self.__cam_x, self.__cam_y, pyxel.width, pyxel.height, self.__flash["color"])
            pyxel.dither(1)
            self.__flash["life"] -= 1
            if self.__flash["life"] == 0:
                self.__flash = {}

        if self.debug:
            pyxel.rect(self.__cam_x + 1, self.__cam_y + 1, 66, 27, self.debug_background_color)
            pyxel.text(self.__cam_x + 3, self.__cam_y + 3, f"Scene[{self.__current_scene.id}]", self.debug_text_color)
            pyxel.text(self.__cam_x + 3, self.__cam_y + 9, f"Screen[{pyxel.mouse_x},{pyxel.mouse_y}]", self.debug_text_color)
            pyxel.text(self.__cam_x + 3, self.__cam_y + 15, f"World[{self.mouse_x:.0f},{self.mouse_y:.0f}]", self.debug_text_color)
            pyxel.text(self.__cam_x + 3, self.__cam_y + 21, f"Fps[{self.__current_fps:.0f}]", self.debug_text_color)

        if pyxel.frame_count % self.__fps == 0:
            self.__current_fps = 1 / (time.time() - self.__previous_frame_time)
        self.__previous_frame_time = time.time()

    def run(self):
        pyxel.run(self.update, self.draw)

class Scene:

    def __init__(self, id:int, title:str, update, draw, pyxres_path:str, palette:list, screen_mode:int=0):
        self.id = id
        self.title = title
        self.update = update
        self.draw = draw
        self.pyxres_path = pyxres_path
        self.palette = palette
        self.screen_mode = screen_mode

class Text:

    def __init__(self, text:str, x:int, y:int, text_colors:int|list, font_size:int=0, font:dict=FONT_DEFAULT, anchor:int=ANCHOR_TOP_LEFT, relative:bool=False, color_mode:int=NORMAL_COLOR_MODE, color_change_time:int=5, wavy:bool=False, wave_speed:int=10, amplitude:int=3, shadow:bool=False, shadow_color:int=0, shadow_offset:int=1, outline:bool=False, outline_color:int=0, glitch_intensity:int=0):
        self.text = text
        self.x, self.y = x, y
        self.font_size = font_size
        self.font = font
        self.__anchor = anchor
        self.relative = relative
        self.wavy = wavy
        self.wave_speed = wave_speed
        self.amplitude = amplitude
        self.shadow = shadow
        self.shadow_color = shadow_color
        self.shadow_offset = shadow_offset
        self.outline = outline
        self.outline_color = outline_color
        self.glitch_intensity = glitch_intensity

        self.text_colors = [text_colors] if isinstance(text_colors, int) else text_colors
        self.original_text_colors = [x for x in self.text_colors]
        self.color_mode = color_mode
        self.color_change_time = color_change_time
        self.__last_change_color_time = pyxel.frame_count

        _, text_height = text_size(text, font_size, font)
        _, self.y = get_anchored_position(0, y, 0, text_height, anchor)

    def __draw_line(self, text:str, y:int, camera_x:int=0, camera_y:int=0):
        text_width, _ = text_size(text, self.font_size, self.font)
        x, _ = get_anchored_position(self.x, 0, text_width, 0, self.__anchor)

        if self.relative:
            x += camera_x
            y += camera_y

        if self.shadow:
            Text(text, x + self.shadow_offset, y + self.shadow_offset, self.shadow_color, self.font_size, self.font, wavy=self.wavy, wave_speed=self.wave_speed, amplitude=self.amplitude).draw()

        if self.outline:
            Text(text, x - 1, y, self.outline_color, self.font_size, self.font, wavy=self.wavy, wave_speed=self.wave_speed, amplitude=self.amplitude).draw()
            Text(text, x + 1, y, self.outline_color, self.font_size, self.font, wavy=self.wavy, wave_speed=self.wave_speed, amplitude=self.amplitude).draw()
            Text(text, x, y - 1, self.outline_color, self.font_size, self.font, wavy=self.wavy, wave_speed=self.wave_speed, amplitude=self.amplitude).draw()
            Text(text, x, y + 1, self.outline_color, self.font_size, self.font, wavy=self.wavy, wave_speed=self.wave_speed, amplitude=self.amplitude).draw()

        if self.font_size > 0:
            for char_index, char in enumerate(text):
                    x += random.uniform(-self.glitch_intensity, self.glitch_intensity)
                    char_y = y + math.cos(pyxel.frame_count / self.wave_speed + char_index * 0.3) * self.amplitude if self.wavy else y
                    char_y += random.uniform(-self.glitch_intensity, self.glitch_intensity)

                    if char in self.font:
                        char_matrix = self.font[char]
                        char_width = len(char_matrix[0]) * self.font_size
                        
                        for row_index, row in enumerate(char_matrix):
                            for col_index, pixel in enumerate(row):
                                if pixel:
                                    pyxel.rect(x + col_index * self.font_size, char_y + row_index * self.font_size + (1 * self.font_size if char in "gjpqy" else 0), self.font_size, self.font_size, self.text_colors[char_index % len(self.text_colors)])
                        
                        x += char_width + 1
        else:
            for char_index, char in enumerate(text):
                x += random.uniform(-self.glitch_intensity, self.glitch_intensity)
                char_y = y + math.cos(pyxel.frame_count / self.wave_speed + char_index * 0.3) * self.amplitude if self.wavy else y
                char_y += random.uniform(-self.glitch_intensity, self.glitch_intensity)
                pyxel.text(x, char_y, char, self.text_colors[char_index % len(self.text_colors)])
                x += 4

    def update(self):
        if self.color_mode != NORMAL_COLOR_MODE and pyxel.frame_count - self.__last_change_color_time >= self.color_change_time:
            if self.color_mode == ROTATING_COLOR_MODE:
                self.__last_change_color_time = pyxel.frame_count
                self.text_colors = [self.text_colors[-1]] + self.text_colors[:-1]
            elif self.color_mode == RANDOM_COLOR_MODE:
                self.__last_change_color_time = pyxel.frame_count
                self.text_colors = [random.choice(self.original_text_colors) for _ in range(len(self.text))]

    def draw(self, camera_x:int=0, camera_y:int=0):
        if "\n" in self.text:
            lines = self.text.split("\n")
            for i, line in enumerate(lines):
                if self.font_size > 0:
                    self.__draw_line(line, self.y + i * (11 * self.font_size), camera_x, camera_y)
                else:
                    self.__draw_line(line, self.y + i * 9, camera_x, camera_y)
        else:
            self.__draw_line(self.text, self.y, camera_x, camera_y)

class Sprite:

    def __init__(self, img:int, u:int, v:int, w:int, h:int, colkey:int=None):
        self.img = img
        self.u, self.v = u, v
        self.w, self.h = w, h
        self.colkey = 0 if colkey == 0 else colkey
        self.flip_horizontal = False
        self.flip_vertical = False

class Animation:

    def __init__(self, sprite:Sprite, total_frames:int=1, frame_duration:int=20, loop:bool=True):
        self.sprite = sprite
        self.__total_frames = total_frames
        self.frame_duration = frame_duration
        self.__loop = loop
        self.__start_frame = pyxel.frame_count
        self.current_frame = 0
        self.__is_finished = False

    def is_finished(self)-> bool:
        return self.__is_finished and not self.__loop
    
    def is_looped(self)-> bool:
        return self.__loop
    
    def reset(self):
        self.__start_frame = pyxel.frame_count
        self.current_frame = 0
        self.__is_finished = False

    def update(self):
        if self.is_finished():
            return
        
        if pyxel.frame_count - self.__start_frame >= self.frame_duration:
            self.__start_frame = pyxel.frame_count
            self.current_frame += 1
            if self.current_frame >= self.__total_frames:
                if self.__loop:
                    self.current_frame = 0
                else:
                    self.__is_finished = True
                    self.current_frame = self.__total_frames - 1

    def draw(self, x:int, y:int, anchor:int=ANCHOR_TOP_LEFT):
        x, y = get_anchored_position(x, y, self.sprite.w, self.sprite.h, anchor)

        w = -self.sprite.w if self.sprite.flip_horizontal else self.sprite.w
        h = -self.sprite.h if self.sprite.flip_vertical else self.sprite.h
        pyxel.blt(x, y, self.sprite.img, self.sprite.u + self.current_frame * abs(self.sprite.w), self.sprite.v, w, h, self.sprite.colkey)

class Particle:

    def __init__(self, x:int, y:int, lifespan:int, speed:int, target:tuple, friction:tuple=(1, 1), acceleration:tuple=(0, 0), dither_duration:int=0, wooble:bool=False):
        self.x, self.y = x, y
        self.lifespan = lifespan
        self.fx, self.fy = friction
        self.ax, self.ay = acceleration
        self.dither = 1
        self.dither_duration = max(dither_duration, 0)
        self.wooble = wooble
        self.wooble_offset = random.random() * 1000 if wooble else 0

        dx = target[0] - x
        dy = target[1] - y
        mag = (dx ** 2 + dy ** 2) ** 0.5
        self.vx = dx / mag * speed if mag != 0 else 0
        self.vy = dy / mag * speed if mag != 0 else 0

    def update(self):
        self.lifespan -= 1

        self.vx *= self.fx
        self.vy *= self.fy
        self.vx += self.ax
        self.vy += self.ay
        self.x += self.vx
        self.y += self.vy

        if self.wooble:
            self.x += math.sin(self.wooble_offset + pyxel.frame_count * 0.1)
            self.y += math.cos(self.wooble_offset + pyxel.frame_count * 0.1)

        if self.lifespan <= self.dither_duration and self.dither_duration:
            self.dither -= 1 / self.dither_duration

class ShapeParticle(Particle):

    def __init__(self, x:int, y:int, w:int, h:int, colors:int|list, lifespan:int, speed:int, target:tuple, friction:tuple=(1, 1), acceleration:tuple=(0, 0), grow:tuple=(1, 1), dither_duration:int=0, hollow:bool=False, wooble:bool=False):
        super().__init__(x, y, lifespan, speed, target, friction, acceleration, dither_duration, wooble)
        self.w, self.h = w, h
        self.colors = [colors] if isinstance(colors, int) else colors
        self.colors_length = len(self.colors)
        self.current_color = 0
        self.lifespan = round(lifespan / self.colors_length) * self.colors_length
        self.initial_lifespan = self.lifespan
        self.gw, self.gh = grow
        self.hollow = hollow

    def update(self):
        super().update()

        self.w *= self.gw
        self.h *= self.gh

        if self.w < 1 or self.h < 1:
            self.lifespan = 0

        if self.lifespan > 0 and self.lifespan % (self.initial_lifespan / self.colors_length) == 0:
            self.current_color = (self.current_color + 1) % self.colors_length

class StarParticle(ShapeParticle):

    def __init__(self, x:int, y:int, radius:int, points:int, colors:int|list, lifespan:int, speed:int, target:tuple, friction:tuple=(1,1), acceleration:tuple=(0,0), grow:int=1, dither_duration:int=0, hollow:bool=False, rotating:bool=False, rotation_speed:float=1):
        super().__init__(x, y, radius, radius, colors, lifespan, speed, target, friction, acceleration, (grow, grow), dither_duration, hollow)
        self.points = max(5, points)
        self.angle = 0
        self.rotating = rotating
        self.rotation_speed = rotation_speed

    def update(self):
        super().update()

        if self.rotating:
            self.angle += self.rotation_speed

    def draw(self):
        pyxel.dither(self.dither)
        step = 360 / self.points
        r_outer = self.w
        r_inner = self.w / 2
        coords = []
        for i in range(self.points * 2):
            r = r_outer if i % 2 == 0 else r_inner
            ang = math.radians(self.angle + step / 2 * i)
            coords.append((self.x + r * math.cos(ang), self.y + r * math.sin(ang)))

        for i in range(len(coords)):
            x1, y1 = coords[i]
            x2, y2 = coords[(i + 1) % len(coords)]
            if self.hollow:
                pyxel.line(x1, y1, x2, y2, self.colors[self.current_color])
            else:
                pyxel.tri(self.x, self.y, x1, y1, x2, y2, self.colors[self.current_color])
        pyxel.dither(1)

class LineParticle(ShapeParticle):

    def __init__(self, x:int, y:int, lenght:int, colors:int|list, lifespan:int, speed:int, target:tuple, friction:tuple=(1, 1), acceleration:tuple=(0, 0), dither_duration:int=0, wooble:bool=False):
        super().__init__(x, y, 1, 1, colors, lifespan, speed, target, friction, acceleration, (1, 1), dither_duration, False, wooble)
        self.lenght = lenght

    def draw(self):
        vx2 = self.vx * self.fx + self.ax
        vy2 = self.vy * self.fy + self.ay
        mag = (vx2 ** 2 + vy2 ** 2) ** 0.5
        x2 = self.x + (vx2 / mag * self.lenght) if mag != 0 else self.x
        y2 = self.y + (vy2 / mag * self.lenght) if mag != 0 else self.y

        pyxel.dither(self.dither)
        pyxel.line(self.x, self.y, x2, y2, self.colors[self.current_color])
        pyxel.dither(1)

class ParticleManager:

    def __init__(self):
        self.particles = []

    def reset(self):
        self.particles = []

    def add_particle(self, new_particle):
        self.particles.append(new_particle)

    def update(self):
        for particle in self.particles:
            particle.update()

        self.particles = [particle for particle in self.particles if particle.lifespan > 0]

    def draw(self):
        for particle in self.particles:
            particle.draw()

def get_anchored_position(x:int, y:int, width:int, height:int, anchor:int)-> tuple:
    if anchor in [ANCHOR_TOP_RIGHT, ANCHOR_BOTTOM_RIGHT, ANCHOR_RIGHT]:
        x -= width
    if anchor in [ANCHOR_BOTTOM_LEFT, ANCHOR_BOTTOM_RIGHT, ANCHOR_BOTTOM]:
        y -= height
    if anchor in [ANCHOR_TOP, ANCHOR_BOTTOM, ANCHOR_CENTER]:
        x -= width // 2
    if anchor in [ANCHOR_LEFT, ANCHOR_RIGHT, ANCHOR_CENTER]:
        y -= height // 2
        
    return x, y

def text_size(text:str, font_size:int=1, font:dict=FONT_DEFAULT)-> tuple:
    lines = text.split("\n")
    if font_size == 0:
        return (max(len(line) * 4 for line in lines), 9 * len(lines))
    text_width = max(sum(len(font[char][0]) * font_size + 1 for char in line) - 1 for line in lines)
    text_height = (11 * font_size + 1) * len(lines)

    return (text_width, text_height)

def clamp(value:int|float, min_value:int|float, max_value:int|float)-> int|float:
    return max(min_value, min(value, max_value))

def collision_rect_rect(x1:int, y1:int, w1:int, h1:int, x2:int, y2:int, w2:int, h2:int)-> bool:
    return not (x1 + w1 < x2 or x2 + w2 < x1 or y1 + h1 < y2 or y2 + h2 < y1)

#? -------------------- CONSTANTS -------------------- ?#

PALETTE = [0x000000, 0x180d2f, 0x353658, 0x83769C, 0x686b72, 0xc5cddb, 0xffffff, 0x5ee9e9, 
           0x2890dc, 0x1831a7, 0x053239, 0x005f41, 0x08b23b, 0x47f641, 0xe8ff75, 0xfbbe82, 
           0xde9751, 0xb66831, 0x8a4926, 0x461c14, 0x1e090d, 0x720d0d, 0x813704, 0xda2424, 
           0xef6e10, 0xecab11, 0xece910, 0xf78d8d, 0xf94e6d, 0xc12458, 0x841252, 0x3d083b]

WIDTH, HEIGHT = 232, 144
FPS = 60

COLLISION_TILES = [1, 2]
COLLISION_TILES = [(x, y) for x in range(32) for y in COLLISION_TILES]
COLLISION_TILES += [(0,15)]

KILL_TILES = [(0,11),(1,11),(0,12),(1,12),(5,12),(6,12)]

ONE_WAY_TILES = [(0,9),(1,9),(2,9),(3,9)]

POT_TILE = (0, 13)
BROKEN_POT_TILE = (1, 13)

LEVER_TILES = [(0,14),(1,14)]

LEVERS_DICT = {
    #? Tile Coord : Activated, Block tile, Hollow tile, Block coords
    (17, 18):[False, (0,15), (1,15), [(13,16),(13,17),(13,18)]],
    (161, 10):[False, (0,15), (1,15), [(149,12),(148,14)]]
}

ANIMATED_TILES_DICT = {
    #? Torch
    (3,11):(4,11),(4,11):(5,11),(5,11):(3,11),
    #? Spikes
    (0,12):(1,12),(1,12):(2,12),(2,12):(3,12),(3,12):(4,12),(4,12):(5,12),(5,12):(6,12),(6,12):(0,12),
    #? Spider
    (7,12):(8,12),(8,12):(9,12),(9,12):(7,12),
    #? Candle
    (7,13):(8,13),(8,13):(9,13),(9,13):(7,13),
}

#? -------------------- CLASSES -------------------- ?#

class Tilemap:

    def __init__(self, id:int, x:int, y:int, w:int, h:int, colkey:int):
        self.id = id
        self.x = x
        self.y = y
        self.w, self.h = w, h
        self.colkey = colkey

    def collision_rect_tiles(self, x:int, y:int, w:int, h:int, tiles:list)-> bool:
        start_tile_x = (x - self.x) // 8
        start_tile_y = (y - self.y) // 8
        end_tile_x = (x + w - self.x - 1) // 8
        end_tile_y = (y + h - self.y - 1) // 8

        start_tile_x = clamp(start_tile_x, 0, self.w // 8 - 1)
        start_tile_y = clamp(start_tile_y, 0, self.h // 8 - 1)
        end_tile_x = clamp(end_tile_x, 0, self.w // 8 - 1)
        end_tile_y = clamp(end_tile_y, 0, self.h // 8 - 1)

        for tile_y in range(int(start_tile_y), int(end_tile_y) + 1):
            for tile_x in range(int(start_tile_x), int(end_tile_x) + 1):
                tile_id = pyxel.tilemaps[self.id].pget(tile_x, tile_y)

                if tile_id in tiles:
                    return True
        
        return False
    
    def tiles_in_rect(self, x:int, y:int, w:int, h:int, tiles:list):
        result = []

        start_tile_x = (x - self.x) // 8
        start_tile_y = (y - self.y) // 8
        end_tile_x = (x + w - self.x - 1) // 8
        end_tile_y = (y + h - self.y - 1) // 8

        start_tile_x = clamp(start_tile_x, 0, self.w // 8 - 1)
        start_tile_y = clamp(start_tile_y, 0, self.h // 8 - 1)
        end_tile_x = clamp(end_tile_x, 0, self.w // 8 - 1)
        end_tile_y = clamp(end_tile_y, 0, self.h // 8 - 1)

        for tile_y in range(int(start_tile_y), int(end_tile_y) + 1):
            for tile_x in range(int(start_tile_x), int(end_tile_x) + 1):
                tile_id = pyxel.tilemaps[self.id].pget(tile_x, tile_y)
                if tile_id in tiles:
                    result.append((int(tile_x), int(tile_y)))

        return result

    def draw(self):
        pyxel.bltm(self.x, self.y, self.id, 0, 0, self.w, self.h, self.colkey)

class Player:

    def __init__(self, x:int, y:int, tilemap:Tilemap):
        self.x, self.y = x, y
        self.w, self.h = 7, 8

        #? Animations
        self.main_animation = Animation(Sprite(0, 0, 8, 8, 8, 27))
        self.crouch_animation = Animation(Sprite(0, 8, 8, 8, 8, 27))
        self.current_animation = self.main_animation

        #? Others
        self.particle_manager = ParticleManager()
        self.tilemap = tilemap
        self.n_pots = 0
        self.box = None

        #? Checkpoint
        self.checkpoint_x, self.checkpoint_y = x, y
        self.temp_collected = []

        #? Velocity
        self.velocity_x = 0
        self.velocity_y = 0
        self.max_velocity_y = 4
        self.gravity = 0.4
        self.friction = 0.8

        #? Movement
        self.speed = 1

        #? Jump
        self.coyote_timer = 0
        self.coyote_time = 6
        self.jump_speed = 2
        self.jump_power = 5.5
        self.jumping = False
        self.falling_timer = 0

        #? Flares
        self.facing_right = True
        self.on_ground = False
        self.dead = False
        self.free = False

    def reset_temp_collected(self):
        self.temp_collected = []

    def _update_velocity_x(self):
        if self.velocity_x != 0:
            step_x = 1 if self.velocity_x > 0 else -1
            for _ in range(int(abs(self.velocity_x))):
                if not self.tilemap.collision_rect_tiles(self.x + step_x, self.y, self.w, self.h, COLLISION_TILES):
                    self.x += step_x
                else:
                    self.velocity_x = 0
                    break

    def _update_velocity_y(self):
        if self.velocity_y == 0:
            return

        step_y = 1 if self.velocity_y > 0 else -1
        for _ in range(int(abs(self.velocity_y))):
            next_y = self.y + step_y

            if step_y < 0:
                if not self.tilemap.collision_rect_tiles(self.x, next_y, self.w, self.h, COLLISION_TILES):
                    self.y = next_y
                else:
                    self.velocity_y = 0
                    break
            else:
                solid_hits = self.tilemap.tiles_in_rect(self.x, next_y, self.w, self.h, COLLISION_TILES)
                if solid_hits:
                    top_tile_y = min(ty for _, ty in solid_hits)
                    tile_top_world = self.tilemap.y + top_tile_y * 8
                    self.y = tile_top_world - self.h
                    self.velocity_y = 0
                    break

                one_way_hits = self.tilemap.tiles_in_rect(self.x, next_y, self.w, self.h, ONE_WAY_TILES)
                if one_way_hits:
                    top_tile_y = min(ty for _, ty in one_way_hits)
                    tile_top_world = self.tilemap.y + top_tile_y * 8

                    feet_before = self.y + self.h
                    if feet_before <= tile_top_world:
                        self.y = tile_top_world - self.h
                        self.velocity_y = 0
                        break
                    else:
                        self.y = next_y
                else:
                    self.y = next_y

    def _handle_free_movement(self):
        if pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_Q):
            self.x -= 2
        if pyxel.btn(pyxel.KEY_D):
            self.x += 2
        if pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_Z):
            self.y -= 2
        if pyxel.btn(pyxel.KEY_S):
            self.y += 2

    def _die(self, pyxel_manager:PyxelManager):
        pyxel_manager.shake_camera(5, 0.2)
        pyxel_manager.flash(2, 23, 0.4)
        self.dead = True
        for _ in range(50):
            x = self.x + self.w // 2
            y = self.y + self.h // 2
            l = random.randint(2, 4)
            c = [random.choice([21, 23]) for _ in range(5)]
            s = random.uniform(0.25, 1.5)
            t = (x + random.randint(-3, 3), y + random.randint(-8, 0))
            self.particle_manager.add_particle(LineParticle(x, y, l, c, 50, s, t, acceleration=(0, random.uniform(0.04, 0.08)), dither_duration=10))

    def _handle_timers(self):
        self.coyote_timer = max(0, self.coyote_timer - 1)

        self.falling_timer = max(0, self.falling_timer - 1)
        if self.falling_timer > 0 and not self.tilemap.collision_rect_tiles(self.x, self.y + 2, self.w, self.h, COLLISION_TILES):
            self.y += 2

    def _is_on_ground(self):
        feet_y = self.y + self.h
        on_ground = False
        if self.tilemap.collision_rect_tiles(self.x, self.y + 1, self.w, self.h, COLLISION_TILES):
            on_ground = True
        else:
            if self.velocity_y >= 0:
                one_way_hits = self.tilemap.tiles_in_rect(self.x, self.y + 1, self.w, self.h, ONE_WAY_TILES)
                if one_way_hits:
                    top_tile_y = min(ty for _, ty in one_way_hits)
                    tile_top_world = self.tilemap.y + top_tile_y * 8
                    if feet_y <= tile_top_world:
                        on_ground = True
        return on_ground

    def _handle_movement(self):
        if pyxel.btn(pyxel.KEY_Q) or pyxel.btn(pyxel.KEY_A):
            self.velocity_x = -self.jump_speed if self.jumping and self.velocity_y < 0 else -self.speed
            self.facing_right = False
        if pyxel.btn(pyxel.KEY_D):
            self.velocity_x = self.jump_speed if self.jumping and self.velocity_y < 0 else self.speed
            self.facing_right = True

        if pyxel.btn(pyxel.KEY_S):
            self.velocity_x /= 1.1

    def _handle_jump(self):
        if pyxel.btn(pyxel.KEY_SPACE) and ((self.on_ground or self.coyote_timer > 0) and not self.jumping) and not isinstance(self.box, Box):
            self.velocity_y = -self.jump_power
            self.jumping = True

    def _handle_crouching(self):
        if pyxel.btnp(pyxel.KEY_S) and not self.tilemap.collision_rect_tiles(self.x, self.y + 1, self.w, self.h, COLLISION_TILES) and not self.jumping and not isinstance(self.box, Box):
            self.falling_timer = 8

        if pyxel.btn(pyxel.KEY_S):
            if self.current_animation != self.crouch_animation:
                self.current_animation = self.crouch_animation
        elif self.current_animation != self.main_animation:
            self.current_animation = self.main_animation

    def _handle_pots(self):
        tiles = self.tilemap.tiles_in_rect(self.x, self.y, self.w, self.h, [POT_TILE])
        if tiles and pyxel.btnp(pyxel.KEY_E):
            pyxel.tilemaps[0].pset(*tiles[0], BROKEN_POT_TILE)
            self.temp_collected.append(("Pot", tiles[0]))
            self.n_pots += 1
            for _ in range(10):
                x, y = self.x + self.w // 2, self.y + self.h // 2
                r = random.randint(1, 2)
                c = [random.choice([2, 3, 5]) for _ in range(5)]
                tx, ty = x + random.randint(-2, 2), y + random.randint(-2, 2)
                self.particle_manager.add_particle(StarParticle(x, y, r, 5, c, 60, random.uniform(0.1, 0.5), (tx, ty), dither_duration=10, rotating=True))

    def _handle_levers(self):
        tiles = self.tilemap.tiles_in_rect(self.x, self.y, self.w, self.h, LEVER_TILES)
        if tiles and pyxel.btnp(pyxel.KEY_E):
            activated, door_tile, hollow_tile, door_tiles = LEVERS_DICT[tiles[0]]
            u, v = pyxel.tilemaps[0].pget(*tiles[0])
            activated = not activated

            if activated:
                pyxel.tilemaps[0].pset(*tiles[0], (u + 1, v))
            else:
                pyxel.tilemaps[0].pset(*tiles[0], (u - 1, v))

            for tx, ty in door_tiles:
                if pyxel.tilemaps[0].pget(tx, ty) == door_tile:
                    pyxel.tilemaps[0].pset(tx, ty, hollow_tile)
                else:
                    pyxel.tilemaps[0].pset(tx, ty, door_tile)

            LEVERS_DICT[tiles[0]][0] = activated

    def _handle_box(self):
        if self.box == 1:
            self.box = None

        if self.box:
            self.box.x = self.x
            self.box.y = self.y - 10
            if pyxel.btnp(pyxel.KEY_E) and self.on_ground:
                self.box.y = self.y
                self.box = 1

    def _revoke_temp_collected(self):
        for t in self.temp_collected:
            if t[0] == "Pot":
                pyxel.tilemaps[0].pset(*t[1], POT_TILE)
                self.n_pots -= 1

        self.reset_temp_collected()

    def update(self, pyxel_manager:PyxelManager):
        self.particle_manager.update()
        self.current_animation.update()

        if pyxel.btnp(pyxel.KEY_F):
            self.free = not self.free

        if self.dead:
            self._revoke_temp_collected()
            self.x, self.y = self.checkpoint_x, self.checkpoint_y
            self.dead = False
            return
        
        if self.free:
            self._handle_free_movement()
            return
        
        if self.tilemap.collision_rect_tiles(self.x + 1, self.y + 2, 6, 5, KILL_TILES) and not self.free:
            self._die(pyxel_manager)

        self._handle_timers()
        
        self.velocity_y = min(self.velocity_y + self.gravity, self.max_velocity_y)
        self.velocity_x *= self.friction

        self.on_ground = self._is_on_ground()

        if self.on_ground:
            if not self.jumping:
                self.velocity_y = 0
            self.jumping = False
            self.coyote_timer = self.coyote_time

        self._handle_movement()
        self._handle_jump()
        self._handle_crouching()
        self._handle_pots()
        self._handle_levers()
        self._handle_box()

        self._update_velocity_y()
        self._update_velocity_x()

    def draw(self):
        self.current_animation.sprite.flip_horizontal = not self.facing_right
        self.current_animation.draw(self.x, self.y)

        if self.tilemap.collision_rect_tiles(self.x, self.y, self.w, self.h, [POT_TILE] + LEVER_TILES):
            Text("E", self.x + self.w // 2, self.y - 11, 6, 1, anchor=ANCHOR_TOP, wavy=True, wave_speed=20, amplitude=1, outline=True, outline_color=3).draw()

        self.particle_manager.draw()

class Box:

    def __init__(self, x:int, y:int):
        self.x, self.y = x, y

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 16, 8, 8, 0)

class BoxManager:

    def __init__(self, boxes:list):
        self.boxes = boxes

    def update(self, player:Player):
        for box in self.boxes:
            if collision_rect_rect(player.x, player.y, player.w, player.h, box.x, box.y, 8, 8) and pyxel.btnp(pyxel.KEY_E) and not player.box and not player.jumping and not player.falling_timer:
                player.box = box
                return

    def draw(self):
        for box in self.boxes:
            box.draw()

class AnimatedTilesManager:

    def __init__(self, animated_tiles_dict:dict):
        self.animated_tiles_dict = animated_tiles_dict
        self.update_timer = 0

    def update(self, camera_x:int, camera_y:int):
        self.update_timer += 1

        if self.update_timer == 20:
            self.update_timer = 0
            for y in range(pyxel.height // 8):
                for x in range(pyxel.width // 8):
                    tile_id = pyxel.tilemaps[0].pget(camera_x // 8 + x, camera_y // 8 + y)
                    if tile_id in self.animated_tiles_dict.keys():
                        pyxel.tilemaps[0].pset(camera_x // 8 + x, camera_y // 8 + y, self.animated_tiles_dict[tile_id])

class Room: 

    def __init__(self, u:int, v:int, left:int=None, right:int=None, up:int=None, down:int=None, on_enter=None, on_exit=None):
        self.u, self.v = u * 8, v * 8
        self.left, self.right = left, right
        self.up, self.down = up, down
        self.on_enter, self.on_exit = on_enter, on_exit

    def update(self, pyxel_manager:PyxelManager, player:Player, rooms:dict):
        if player.x + player.w <= self.u and self.left is not None:
            new_u = rooms.get(self.left).u
            new_v = rooms.get(self.left).v
            def action():
                if self.on_exit:    self.on_exit()
                player.x = new_u + pyxel.width - 8
                player.y = new_v + (player.y - self.v)
                player.checkpoint_x = player.x
                player.checkpoint_y = player.y
                player.reset_temp_collected()
                if rooms.get(self.left).on_enter:    rooms.get(self.left).on_enter()
            pyxel_manager.change_scene_transition(TransitionRectangle(0, 0.25, 0, LEFT, new_u, new_v, action))
            return self.left
        
        elif player.x >= self.u + pyxel.width and self.right is not None:
            new_u = rooms.get(self.right).u
            new_v = rooms.get(self.right).v
            def action():
                if self.on_exit:    self.on_exit()
                player.x = new_u
                player.y = new_v + (player.y - self.v)
                player.checkpoint_x = player.x
                player.checkpoint_y = player.y
                player.reset_temp_collected()
                if rooms.get(self.right).on_enter:    rooms.get(self.right).on_enter()
            pyxel_manager.change_scene_transition(TransitionRectangle(0, 0.25, 0, RIGHT, new_u, new_v, action))
            return self.right
        
        elif player.y + player.h <= self.v and self.up is not None:
            new_u = rooms.get(self.up).u
            new_v = rooms.get(self.up).v
            def action():
                if self.on_exit:    self.on_exit()
                player.x = new_u + (player.x - self.u)
                player.y = new_v + pyxel.height - 16
                player.checkpoint_x = player.x
                player.checkpoint_y = player.y
                player.reset_temp_collected()
                if rooms.get(self.up).on_enter:    rooms.get(self.up).on_enter()
            pyxel_manager.change_scene_transition(TransitionRectangle(0, 0.25, 0, TOP, new_u, new_v, action))
            return self.up
        
        elif player.y >= self.v + pyxel.height and self.down is not None:
            new_u = rooms.get(self.down).u
            new_v = rooms.get(self.down).v
            def action():
                if self.on_exit:    self.on_exit()
                player.x = new_u + (player.x - self.u)
                player.y = new_v
                player.checkpoint_x = player.x
                player.checkpoint_y = player.y
                player.reset_temp_collected()
                if rooms.get(self.down).on_enter:    rooms.get(self.down).on_enter()
            pyxel_manager.change_scene_transition(TransitionRectangle(0, 0.25, 0, BOTTOM, new_u, new_v, action))
            return self.down
        
class RoomManager:

    def __init__(self, rooms:dict, start_room_id:int):
        self.rooms = rooms
        self.current_room_id = start_room_id
        self.current_room = self.rooms.get(start_room_id)

    def update(self, pyxel_manager:PyxelManager, player:Player):
        id = self.current_room.update(pyxel_manager, player, self.rooms)
        if id is not None:
            self.current_room_id = id
            self.current_room = self.rooms.get(id)

#? -------------------- ROOMS -------------------- ?#

ROOMS = {
    0:Room(2, 2, down=1, left=9, up=7, right=8),
    1:Room(35, 2, up=0, left=2, right=2, down=3),
    2:Room(68, 2, left=1, right=1, down=4),
    3:Room(101, 2, up=1, left=4, right=4, down=5),
    4:Room(134, 2, left=3, right=3, up=2, down=8),
    5:Room(167, 2, up=3, left=6, right=6),
    6:Room(200, 2, left=5, right=5, down=7),
    7:Room(2, 24, down=0, up=6),
    8:Room(35, 24, up=4, right=9, left=0),
    9:Room(68, 24, right=0, left=8),
}

#? -------------------- GAME -------------------- ?#

class Game:

    def __init__(self):
        #? Scenes
        game_scene = Scene(0, "WizHard - Game", self.update_game, self.draw_game, "assets.pyxres", PALETTE)
        scenes = [game_scene]

        #? Init
        self.pyxel_manager = PyxelManager(WIDTH, HEIGHT, scenes, 0, FPS, True, True, camera_x=16, camera_y=16)

        #? Game Variables
        self.tilemap_0 = Tilemap(0, 0, 0, 256*8, 256*8, 0)
        self.tilemap_1 = Tilemap(1, 0, 0, 256*8, 256*8, 0)
        self.player = Player(15*8, 13*8, self.tilemap_0)
        self.animated_tiles_manager = AnimatedTilesManager(ANIMATED_TILES_DICT)
        self.room_manager = RoomManager(ROOMS, 0)
        self.box_manager = BoxManager([Box(22*8, 18*8), Box(20*8, 18*8)])

        #? Run
        self.pyxel_manager.run()

    def update_game(self):
        self.player.update(self.pyxel_manager)
        self.box_manager.update(self.player)
        self.animated_tiles_manager.update(self.pyxel_manager.camera_x, self.pyxel_manager.camera_y)
        self.room_manager.update(self.pyxel_manager, self.player)

        if pyxel.btnp(pyxel.KEY_B):
            self.pyxel_manager.debug = not self.pyxel_manager.debug

    def draw_game(self):
        pyxel.cls(0)
        
        self.tilemap_0.draw()
        self.box_manager.draw()
        self.player.draw()
        self.tilemap_1.draw()

        px, py, pw, ph = self.player.x, self.player.y, self.player.w, self.player.h

        #? Hide zone 0
        if not collision_rect_rect(px, py, pw, ph, 13*8, 3*8, 16, 8):
            pyxel.blt(13*8, 2*8, 1, 22*8, 8, 8, 8)
            pyxel.blt(13*8, 3*8, 1, 7*8, 8, 8, 8)
            pyxel.blt(13*8, 4*8, 1, 7*8, 8, 8, 8)
            pyxel.rect(14*8, 2*8, 16, 24, 0)

        #? Hide zone 2
        if not collision_rect_rect(px, py, pw, ph, 548, 141, 43, 15):
            pyxel.rect(548, 141, 43, 15, 0)
            pyxel.blt(73*8, 18*8, 1, 13*8, 8, 8, 8)
            pyxel.blt(73*8, 19*8, 1, 28*8, 8, 8, 8)

        #? Hide zon 4
        if not collision_rect_rect(px, py, pw, ph, 148*8, 10*8, 16, 15):
            pyxel.rect(147*8, 10*8, 32, 8, 0)
            pyxel.blt(148*8, 9*8, 1, 14*8, 8, 8, 8)
            pyxel.blt(149*8, 9*8, 1, 29*8, 8, 8, 8)
            pyxel.blt(148*8, 11*8, 1, 11*8, 8, 8, 8)
            pyxel.blt(149*8, 11*8, 1, 11*8, 8, 8, 8)
            pyxel.blt(150*8, 11*8, 1, 11*8, 8, 8, 8)

        #? Hide zone 5
        if not collision_rect_rect(px, py, pw, ph, 175*8, 12*8, 3*8, 3*8) and not collision_rect_rect(px, py, pw, ph, 171*8, 15*8, 9*8, 4*8):
            pyxel.blt(177*8, 11*8, 1, 26*8, 8, 8, 8)
            pyxel.blt(177*8, 12*8, 1, 13*8, 8, 8, 8)
            pyxel.blt(177*8, 13*8, 1, 28*8, 8, 8, 8)
            pyxel.rect(1364, 116, 80, 40, 0)
            pyxel.rect(1396, 92, 20, 24, 0)

        #? Hide zone 8
        if not collision_rect_rect(px, py, pw, ph, 356, 243, 80, 93) and not collision_rect_rect(px, py, pw, ph, 436, 268, 8, 46) and not collision_rect_rect(px, py, pw, ph, 324, 291, 32, 25):
            pyxel.rect(356, 243, 80, 93, 0)
            pyxel.rect(436, 268, 10, 46, 0)
            pyxel.rect(324, 291, 32, 25, 0)

        pyxel.text(self.pyxel_manager.camera_x + 2, self.pyxel_manager.camera_y + 2, f"{self.player.n_pots}", 6)

if __name__ == "__main__":
    Game()