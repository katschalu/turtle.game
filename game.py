import turtle # Bibliothek turtle imortieren
import PIL # Bibliothek pillow importieren 
from PIL import Image # Funktion Image von Bibliothek pillow importieren
import random
import time


# Y-Zufallposition
yzombi = random.randint(-250,250) 

# Soldier Y-Position
syp = []

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

mywidth=60 # gewunschte Bereite (150)
myheight=60 # gewunschte Höhe (160)
img=Image.open('bullet1.gif') # Bild importieren 
img = img.resize((mywidth,myheight),PIL.Image.ANTIALIAS) # Gr0ße ändern
img.save('bullet1.gif') # speichern

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
soldier.setposition(-350,100)
soldier.showturtle()

# Figur Bullet im Spiel
bullet = turtle.Turtle()
bullet.hideturtle()
bullet.penup()
bullet.shape('bullet1.gif')
bullet.setposition((-310),(140))
bullet.speed(0)

zomb1 = turtle.Turtle()  # neue Figur bringen wir und zomb nennen wir sie

# Figur Zombie im Spiel
def addzombi1():
    zomb1.hideturtle()
    zomb1.shape('resize.gif') # das geäenderte Bild nehmen wir als Figur zomb ( Zombie )
    zomb1.penup() # damit die Figur keine Streife hinterlest
    zomb1.speed(100) # maximume Geschwindigkeit
    zomb1.setposition(350,(random.randint(-230,250))) # positionieren auf der rechten seite mit zufällige y-Position zwischen -250 und 250
    zomb1.speed(random.randint(0,1)) # zufällige Geschwindigkeit
    zomb1.showturtle()
    zomb1.backward(800)
    
zomb = turtle.Turtle()  # eine Figur bringen wir und zomb nennen wir sie 
        
def addzombi2():
    zomb.hideturtle()
    zomb.shape('zombie2.gif') # das geäenderte Bild nehmen wir als Figur zomb ( Zombie )  
    zomb.penup() # damit die Figur keine Streife hinterlest
    zomb.speed(100) # minimume Geschwindigkeit
    zomb.setposition(350,(random.randint(-230,250))) # positionieren auf der rechten seite mit zufällige y-Position zwischen -250 und 250
    zomb.speed(random.randint(0,1)) # zufällige Geschwindigkeit
    zomb.showturtle()
    zomb.backward(800)
   
def oben():
    if soldier.ycor() < 220:
        soldier.setheading(90)
        soldier.forward(40)
        soldier.ycor()
        syp.append(soldier.ycor())
    
def unten():
    if soldier.ycor() >= -200:
        soldier.setheading(-90)
        soldier.forward(40)
        syp.append(soldier.ycor())
    
def schiessen():     
    bullet.goto(-310,(syp[-1]+40))  
    bullet.showturtle()
    for i in range(65):
        bullet.forward(10) 
        if bullet.distance(zomb) < 45:
            zomb.hideturtle()
            bullet.hideturtle()     
        elif bullet.distance(zomb1) < 45 :
            zomb1.hideturtle()
            zomb1.speed(100)
            bullet.hideturtle()   
    bullet.hideturtle()

# Tastatur   
turtle.listen()
turtle.onkey(oben, "w")
turtle.onkey(unten, "s")
turtle.onkey(schiessen, "d")
while 1 :
    addzombi1()
    addzombi2()

turtle.done() # damit bleit das Fenster offen