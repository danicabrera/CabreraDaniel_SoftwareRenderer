#Universidad del Valle de Guatemala
#Daniel Cabrera 20289
#Gráficas por Computadora
#Base de Carlos Alonso
import random
from gl import Renderer

width = 960
height = 540
rend = Renderer(width, height)
rend.glClearColor(0,0,0)

rend.glClear()
    #rend.glViewPort(100,100,312,312)
    #rend.glPoint(100,100)

for x in range(width):
    for y in range(height):
        rend.glColor(random.random(), random.random(), random.random())

        if random.random() > 0.999:
            size = random.randrange(0,3)
            if size == 0:
                rend.glPoint(x,y)
                rend.glColor(0, 0, 0)

            elif size == 1:
                rend.glPoint(x, y)
                rend.glPoint(x + 1, y)
                rend.glPoint(x, y+1)
                rend.glPoint(x+1, y+1)
            elif size == 2:
                rend.glPoint(x, y)
                rend.glPoint(x, y+1)
                rend.glPoint(x, y-1)
                rend.glPoint(x+1, y)
                rend.glPoint(x-1, y)

            else:
                rend.glColor(1, 1, 1)
                rend.glPoint(x, y)

rend.glFinish("output.bmp")