import turtle # Bibliothek turtle imortieren
import PIL # Bibliothek pillow importieren 
from PIL import Image # Funktion Image von Bibliothek pillow importieren
import random

yzombi = random.randint(-250,250) # y-Zufallposition
speedzomb = random.randint(1.0,2.0)

# Bild Gr0ße ändern
mywidth=100 # gewunschte Bereite (100)
myheight=100 # gewunschte Höhe (100)
img=Image.open('zombie1.gif') # Bild importieren oder öfnen 
img = img.resize((mywidth,myheight),PIL.Image.ANTIALIAS) # Gr0ße ändern
img = img.transpose(Image.FLIP_LEFT_RIGHT) # umkehren
img.save('resize.gif') # speichern

# screen importieren und dessen Eigentschaften bestimmen
win = turtle.Screen() # funktion Screen von Bibliothek turtle wird zu bildschirm abgekürzt
win.setup(width=800,height=600) # die Bereite und Höhe von virtuelle Screen 
win.bgpic('h.gif') # Hintergrundbild 

# Bilder aus Festplatte importieren
win.addshape('resize.gif')  # das geänderte Bild bringen wir in Python 

zombkopie = [] # eine Zombieliste erstellen

# importierte Bilder als Figur und kopieren
for i in range(3):
    zomb = turtle.Turtle()  # eine Figur bringen wir und zomb nennen wir sie
    zomb.shape('resize.gif') # das geäenderte Bild nehmen wir als Figur zomb ( Zombie )
    zomb.penup()
    zomb.speed(0)
    zomb.setposition(350,(random.randint(-250,250)))
    zomb.speed(random.randint(1.0,2.0))
    zombkopie.append(zombkopie)

turtle.done()