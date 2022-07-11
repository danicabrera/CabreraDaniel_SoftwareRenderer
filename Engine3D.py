#Universidad del Valle de Guatemala
#Daniel Cabrera 20289
#Gráficas por Computadora
#Base de Carlos Alonso

from gl import Renderer

rend = Renderer(512, 512)
rend.glClearColor(0,0.5,0.5)
rend.glColor(1,1,1)
rend.glClear()
rend.glViewPort(100,100,312,312)
rend.glPoint(100,100)
for i in range(512):
    rend.glPoint(i,i)

rend.glFinish("output.bmp")