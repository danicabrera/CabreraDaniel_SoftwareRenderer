#Universidad del Valle de Guatemala
#Daniel Cabrera 20289
#Gráficas por Computadora
#Base de Carlos Alonso

from gl import Renderer, color, V2, V3
from OBJ import Obj
from shader import flat, gourad, unlit, toon, glow, textureBlend
from texture import Texture


width = 960
height = 540
rend = Renderer(width, height)
rend.active_shader = gourad
rend.active_texture = Texture("model.bmp")
rend.glLoadModel("model.obj",
                 translate= V3(0, 0, -10),
                 scale = V3(4, 4, 4))

rend.glFinish("venv/Shots/Medium.bmp")

width = 960
height = 540
rend = Renderer(width, height)
rend.active_shader = gourad
rend.active_texture = Texture("model.bmp")
rend.glLoadModel("model.obj",
                 translate= V3(0, 0, -10),
                 scale = V3(4, 4, 4),
                 rotate= V3(330,0,0))

rend.glFinish("venv/Shots/Low.bmp")

width = 960
height = 540
rend = Renderer(width, height)
rend.active_shader = gourad
rend.active_texture = Texture("model.bmp")
rend.glLoadModel("model.obj",
                 translate= V3(0, 0, -10),
                 scale = V3(4, 4, 4),
                 rotate= V3(60,0,0))

rend.glFinish("venv/Shots/HIGH.bmp")

width = 960
height = 540
rend = Renderer(width, height)
rend.active_shader = gourad
rend.active_texture = Texture("model.bmp")
rend.glLoadModel("model.obj",
                 translate= V3(0, 0, -10),
                 scale = V3(4, 4, 4),
                 rotate= V3(0,0,45))

rend.glFinish("venv/Shots/Dutch.bmp")



