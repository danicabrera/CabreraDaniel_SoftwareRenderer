#Universidad del Valle de Guatemala
#Daniel Cabrera 20289
#Gráficas por Computadora
#Base de Carlos Alonso

from gl import Renderer, color, V2, V3
from OBJ import Obj
import random

width = 1920
height = 1080
rend = Renderer(width, height)
rend.glLoadModel("tree.obj",
                 translate= V3(width/2, height/6, 0),
                 scale = V3(30, 30, 30))

rend.glFinish("output.bmp")