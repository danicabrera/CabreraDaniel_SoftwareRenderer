#Universidad del Valle de Guatemala
#Daniel Cabrera 20289
#Gráficas por Computadora
#Base de Carlos Alonso

from gl import Renderer, color, V2, V3
from OBJ import Obj
from shader import flat, gourad, unlit, toon, glow, textureBlend, toon2, Ice, Intense, Black, Comic
from texture import Texture


width = 960
height = 540
rend = Renderer(width, height)
rend.active_shader = gourad
rend.background = Texture("Fondo.bmp")
rend.glClearBackground()
rend.dirLight = V3(0.75, - 0.5, 0.5)
# rend.active_texture = Texture("Cabana.bmp")
# rend.glLoadModel("cabana.obj",
#                  translate= V3(3, 0, -10),
#                  scale = V3(0.1, 0.1, 0.1))

# rend.active_texture = Texture("Road.bmp")
# rend.active_shader = glow
# rend.glLoadModel("road.obj",
#                  translate= V3(24, 0, -10),
#                  rotate= V3(0,90,0),
#                  scale = V3(10, 10, 10))

rend.active_shader = unlit
#rend.active_texture = Texture("Brasil1.bmp")
rend.active_texture = Texture("textures/Cabana.bmp")
rend.glLoadModel("models/cabana.obj",
                 translate= V3(-8.5, -2, -15),
                 rotate= V3(0,180,0),
                 scale = V3(0.38, 0.38, 0.38))

rend.active_shader = Black
rend.active_texture = Texture("textures/piel1.bmp")
rend.glLoadModel("models/girl.obj",
                 translate= V3(3, -3, -10),
                 rotate= V3(0,65,0),
                 scale = V3(3, 3, 3))

rend.active_shader = toon2
rend.active_texture = Texture("textures/wood4.bmp")
rend.glLoadModel("models/tree.obj",
                 translate= V3(8.5, -2.5, -10),
                 scale = V3(0.5, 0.5, 0.5))

rend.active_shader = Comic
rend.active_texture = Texture("textures/Penguin0.bmp")
rend.glLoadModel("models/Penguin.obj",
                 translate= V3(4, -2.5, -11),
                 scale = V3(1.75, 1.75, 1.75))

rend.active_texture = Texture("textures/rosa0.bmp")
rend.active_shader = Ice
rend.glLoadModel("models/rose.obj",
                 translate= V3(2.75, 0, -8),
                 rotate= V3(0,0,-10),
                 scale = V3(0.01, 0.01, 0.01))

rend.active_shader = glow
rend.active_texture = Texture("textures/Gris0.bmp")
rend.glLoadModel("models/Tumba.obj",
                 translate= V3(4.5, -2, -8),
                 rotate= V3(0,45,0),
                 scale = V3(0.3, 0.3, 0.3))

rend.glFinish("output.bmp")
