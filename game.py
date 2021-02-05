import turtle
import PIL
from PIL import Image

mywidth=100
myheight=100
img=Image.open('zombie1.gif')
img = img.resize((mywidth,myheight),PIL.Image.ANTIALIAS)
img.save('resize.gif')

win = turtle.Screen()
win.setup(width=800,height=600)
win.bgpic('h.gif')

win.addshape('resize.gif')


zomb = turtle.Turtle()
zomb.shape('resize.gif')

turtle.done()