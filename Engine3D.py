#Universidad del Valle de Guatemala
#Daniel Cabrera 20289
#Gráficas por Computadora
#Base de Carlos Alonso
import random
from gl import Renderer, color, V2

width = 1024
height = 1024
rend = Renderer(width, height)

pol1 = [ V2(150,200), V2(100,200),V2(125,300), V2(100,400), V2(150,400), V2(175,300), V2(200,400), V2(250,400),
        V2(225,300), V2(250,200), V2(200,200), V2(175,60)]

pol2 = [V2(240, 780), V2(200, 880), V2(340, 880), V2(300, 780)]

pol3 = [V2(350, 500), V2(420, 700), V2(480, 500), V2(420, 600), V2(350,500)]

pol4 = [V2(650, 700), V2(650, 900), V2(750, 1000), V2(850, 900), V2(850,700)]

pol5 = [V2(600, 100), V2(550, 100), V2(525, 300), V2(575, 300), V2(600,150), V2(625,300), V2(675,300), V2(700,150),
        V2(725,300), V2(775,300), V2(750,100), V2(700,100), V2(650,175)]

rend.gldrawPoli(pol1, color(1,0.5,0.5))
rend.gldrawPoli(pol2, color(0.5,1,0.5))
rend.gldrawPoli(pol3, color(0.5,0.5,1))
rend.gldrawPoli(pol4, color(1,1,1))
rend.gldrawPoli(pol5, color(1,1,0))

rend.glFinish("output.bmp")