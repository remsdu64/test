#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-
 	
import espeak
from gtts import gTTS
import os
Freq = 2500 # Set Frequency To 2500 Hertz
Dur = 1000 # Set Duration To 1000 ms == 1 second

es = espeak.ESpeak()
es.voice = 'fr'
es.speed = 200
i=0
ii = 0
mot1 = 0
u = 0
perso = []
text = []
listepersos = []
final = "Vous avez fini !!! BRAVO"


with open("persos.txt", "r") as f:
    data1 = f.readlines()

while ii < len(data1):
    ii+=1


for line1 in data1:
    line1.replace('\n', '')
    words1 = line1.split(" | ")

while mot1 < len(words1):
    listepersos.append(words1[mot1])
    mot1 += 1

listepersos2 = 'Comment s\'appelle votre personnage ? Vous avez le choix entre : ' + ", ".join(map(str, listepersos)) + "--->"
try:
    with open("config.txt", "r") as c:
        data2 = c.readlines()
    for iii in data2:
        iii.replace('\n', '')
        words2 = iii.split(" | ")
    try:
        persocourant = words2[0]
    except:
        persocourant = input(listepersos2)
    try:
        apprentissage = str(words2[1])
    except:
        apprentissage = input("Êtes vous en phase d'apprentissage (oui/non)")
    
except:
    persocourant = input(listepersos2)
    apprentissage = input("Êtes vous en phase d'apprentissage (oui/non)")
"""
with open("config.txt", "r") as c:
    data2 = c.readlines()
for iii in data2:
    words2 = iii.split(" | ")
persocourant = words2[0]
"""
if apprentissage == "oui":
    final = "BRAVO, vous venez de finir une séance d'apprentissage du texte"

with open("dialogue.txt", "r") as f:
    data = f.readlines()

while i < len(data):
    i+=1


for line in data:
    line.replace("\n", "")
    words = line.split(" : ")
    perso.append(words[0])
    text.append(words[1])


while u < len(perso):
    encours = perso[u]
    if encours == persocourant:
        if apprentissage != 'oui':
            gjnioejgh = input("C'est à vous --> pressez 'Entrer' pour continuer !!")
            u += 1
            continue
        if apprentissage == 'oui':
            #adire = text[u]
            tts = gTTS(text=text[u], lang='fr')
            tts.save("temp.mp3")
            os.system("mplayer temp.mp3")
            es.say("A vous")
            zzx = 'VOUS ------------->' + encours + " : " + text[u]
            input(zzx)

    else:
        #print(encours, ' | ', persocourant)
        print(encours, " : ", text[u])
        tts = gTTS(text=text[u], lang='fr', slow=True)
        tts.save("temp.mp3")
        os.system("mplayer temp.mp3")
    u += 1
