import turtle # Bibliothek turtle imortieren
import PIL # Bibliothek pillow importieren 
from PIL import Image # Funktion Image von Bibliothek pillow importieren
import random
import time

yzombi = random.randint(-250,250) # y-Zufallposition
speedzomb = random.randint(1.0,2.0)
zombiname = ["zombie1.gif","zombie2.gif"]

x = 2

# Bild Gr0ße ändern

mywidth=100 # gewunschte Bereite (100)
myheight=100 # gewunschte Höhe (100)
img=Image.open('zombie1.gif') # Bild importieren oder öfnen 
img = img.resize((mywidth,myheight),PIL.Image.ANTIALIAS) # Gr0ße ändern
img = img.transpose(Image.FLIP_LEFT_RIGHT) # umkehren
img.save('resize.gif') # speichern

mywidth=100 # gewunschte Bereite (100)
myheight=100 # gewunschte Höhe (100)
img=Image.open('zombie2.gif') # Bild importieren oder öfnen 
img = img.resize((mywidth,myheight),PIL.Image.ANTIALIAS) # Gr0ße ändern
img.save('zombie2.gif') # speichern

# screen importieren und dessen Eigentschaften bestimmen
win = turtle.Screen() # funktion Screen von Bibliothek turtle wird zu bildschirm abgekürzt
win.setup(width=800,height=600) # die Bereite und Höhe von virtuelle Screen 
win.bgpic('h.gif') # Hintergrundbild 

# Bilder aus Festplatte importieren
win.addshape('resize.gif')  # das geänderte Bild bringen wir in Python 
win.addshape('zombie2.gif')

zombkopie = [] # eine Zombieliste erstellen

# Zombiebild importieren und duplizieren
def addzombi1():

    zomb = turtle.Turtle()  # eine Figur bringen wir und zomb nennen wir sie
    zomb.shape('resize.gif') # das geäenderte Bild nehmen wir als Figur zomb ( Zombie )
    zomb.hideturtle()
    zomb.penup() # damit die Figur keine Streife hinterlest
    zomb.speed(0) # maximume Geschwindigkeit
    zomb.setposition(350,(random.randint(-250,250))) # positionieren auf der rechten seite mit zufällige y-Position zwischen -250 und 250
    zomb.speed(random.randint(1.0,2.0)) # zufällige Geschwindigkeit
    zomb.showturtle()
    zombkopie.append(zombkopie) # eine Kopie wird in der Liste hinzugefügt
    
        
    
def addzombi2():

    zomb = turtle.Turtle()  # eine Figur bringen wir und zomb nennen wir sie
    zomb.hideturtle()
    zomb.shape('zombie2.gif') # das geäenderte Bild nehmen wir als Figur zomb ( Zombie )
    zomb.penup() # damit die Figur keine Streife hinterlest
    zomb.speed(0) # maximume Geschwindigkeit
    zomb.setposition(350,(random.randint(-250,250))) # positionieren auf der rechten seite mit zufällige y-Position zwischen -250 und 250
    zomb.speed(random.randint(1.0,2.0)) # zufällige Geschwindigkeit
    zomb.showturtle()
    zombkopie.append(zombkopie) # eine Kopie wird in der Liste hinzugefügt

while 1 :
    addzombi1()
    time.sleep(x)
    addzombi2()
    time.sleep(x)

turtle.done() # damit bleit das Fenster offen