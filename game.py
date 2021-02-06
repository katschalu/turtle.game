import turtle # Bibliothek turtle imortieren
import PIL # Bibliothek pillow importieren 
from PIL import Image # Funktion Image von Bibliothek pillow importieren

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

# importierte Bilder als Figur nehmen
zomb = turtle.Turtle()  # eine Figur bringen wir und zomb nennen wir sie
zomb.shape('resize.gif') # das geäenderte Bild nehmen wir als Figur zomb ( Zombie )

turtle.done()