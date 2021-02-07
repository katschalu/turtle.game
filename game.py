import turtle # Bibliothek turtle imortieren
import PIL # Bibliothek pillow importieren 
from PIL import Image # Funktion Image von Bibliothek pillow importieren
import random
import time
import os
yzombi = random.randint(-250,250) # y-Zufallposition
xp = -350
yp = 100

# Bild Bearbeitung
mywidth=100 # gewunschte Bereite (100)
myheight=100 # gewunschte Höhe (100)
img=Image.open('zombie1.gif') # Bild importieren oder öfnen 
img = img.resize((mywidth,myheight),PIL.Image.ANTIALIAS) # Gr0ße ändern
img = img.transpose(Image.FLIP_LEFT_RIGHT) # umkehren
img.save('resize.gif') # speichern


mywidth=100 # gewunschte Bereite (100)
myheight=100 # gewunschte Höhe (100)
img=Image.open('zombie2.gif') # Bild importieren 
img = img.resize((mywidth,myheight),PIL.Image.ANTIALIAS) # Gr0ße ändern
img.save('zombie2.gif') # speichern

mywidth=120 # gewunschte Bereite (150)
myheight=130 # gewunschte Höhe (160)
img=Image.open('soldier1.gif') # Bild importieren 
img = img.resize((mywidth,myheight),PIL.Image.ANTIALIAS) # Gr0ße ändern
img.save('soldier1.gif') # speichern

mywidth=20 # gewunschte Bereite (150)
myheight=10 # gewunschte Höhe (160)
img=Image.open('bullet1.gif') # Bild importieren 
img = img.resize((mywidth,myheight),PIL.Image.ANTIALIAS) # Gr0ße ändern
img.save('billet1.gif') # speichern



# screen importieren und dessen Eigentschaften bestimmen
win = turtle.Screen() # funktion Screen von Bibliothek turtle wird zu bildschirm abgekürzt
win.setup(width=800,height=600) # die Bereite und Höhe von virtuelle Screen 
win.bgpic('h.gif') # Hintergrundbild 


# Bilder aus Festplatte importieren
win.addshape('resize.gif')  # das geänderte Bild bringen wir in Python 
win.addshape('zombie2.gif')
win.addshape('soldier1.gif')
win.addshape('bullet1.gif')

# Figur Soldier im Spiel
soldier = turtle.Turtle()
soldier.hideturtle()
soldier.penup()
soldier.shape('soldier1.gif')
soldier.setposition(xp,yp)
soldier.showturtle()

# Figur Bullet im Spiel
bullet = turtle.Turtle()
bullet.hideturtle()
bullet.penup()
bullet.shape('bullet1.gif')
bullet.setposition((xp+40),(yp+40))
bullet.showturtle()

# Figur Zombie im Spiel
def addzombi1():
    zomb = turtle.Turtle()  # neue Figur bringen wir und zomb nennen wir sie
    zomb.shape('resize.gif') # das geäenderte Bild nehmen wir als Figur zomb ( Zombie )
    zomb.hideturtle()
    zomb.penup() # damit die Figur keine Streife hinterlest
    zomb.speed(0) # maximume Geschwindigkeit
    zomb.setposition(350,(random.randint(-250,250))) # positionieren auf der rechten seite mit zufällige y-Position zwischen -250 und 250
    zomb.speed(random.randint(0,1)) # zufällige Geschwindigkeit
    zomb.showturtle()
    zomb.backward(800)
    
        
    
def addzombi2():
    zomb = turtle.Turtle()  # eine Figur bringen wir und zomb nennen wir sie
    zomb.hideturtle()
    zomb.shape('zombie2.gif') # das geäenderte Bild nehmen wir als Figur zomb ( Zombie )
    zomb.penup() # damit die Figur keine Streife hinterlest
    zomb.speed(0) # maximume Geschwindigkeit
    zomb.setposition(350,(random.randint(-250,250))) # positionieren auf der rechten seite mit zufällige y-Position zwischen -250 und 250
    zomb.speed(random.randint(0,1)) # zufällige Geschwindigkeit
    zomb.showturtle()
    zomb.backward(800)
    
def oben():
    soldier.setheading(90)
    soldier.forward(30)
def unten():
    soldier.setheading(-90)
    soldier.forward(30)
def schiessen():
    bullet.forward(750)

# Tastatur   
turtle.listen()
turtle.onkey(oben, "w")
turtle.onkey(unten, "s")
turtle.onkey(schiessen, "d")

 


   

turtle.done() # damit bleit das Fenster offen