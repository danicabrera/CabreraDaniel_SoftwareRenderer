#Universidad del Valle de Guatemala
#Daniel Cabrera 20289
#Gráficas por Computadora
#Base de Carlos Alonso

from gl import Renderer, color, V2, V3
from OBJ import Obj
from shader import flat, gourad, unlit, toon, glow, textureBlend, toon2, Ice, Intense
from texture import Texture


width = 960
height = 540
rend = Renderer(width, height)
rend.active_shader = gourad
rend.active_texture = Texture("model.bmp")
rend.glLoadModel("Penguin.obj",
                 translate= V3(3, 0, -10),
                 scale = V3(4, 4, 4))


rend.active_shader = Ice
rend.active_texture = Texture("Model.bmp")
rend.glLoadModel("model.obj",
                 translate= V3(-3, 0, -10),
                 scale = V3(4, 4, 4))


rend.glFinish("output.bmp")
