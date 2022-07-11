#Universidad del Valle de Guatemala
#Daniel Cabrera 20289
#Gráficas por Computadora
#Base de Carlos Alonso

import struct

def char(c):
    return struct.pack('=c' , c.encode('ascii'))

def word(w):
    return struct.pack('=h', w)

def dword(d):
    return struct.pack('=l', d)

def color(r, g, b):
    return bytes([int(b * 255),
                  int(g * 255),
                  int(r * 255)])

class Renderer(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.Xinicial = 0
        self.Yinicial = 0
        self.Xfinal = width
        self.Yfinal = height
        self.clearColor = color(0,0,0)
        self.currColor = color(1,1,1)

        self.glClear()

    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height

    def glClearColor(self, r, g, b):
        self.clearColor = color(r, g, b)

    def glColor(self, r, g, b):
        self.currColor = color(r, g, b)

    def glPoint(self, x, y, clr = None):
        if (self.Xinicial <= x < self.Xfinal) and (self.Yinicial <= y < self.Yfinal):
            self.pixels[x][y] = clr or self.currColor

    def glClear(self):
        self.pixels = [[ self.clearColor for y in range (self.height) ]
                       for x in range (self.width)]

    def glViewPort(self, x, y, width, height):
        self.Xinicial = x
        self.Yinicial = y
        self.Xfinal = x + width
        self.Yfinal = y + height

    def glFinish(self, filename):
        with open(filename, "wb") as file:
            # Header
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))
            file.write(dword(14 + 40 + (self.width * self.height * 3)))
            file.write(dword(0))
            file.write(dword(14 + 40))

            #InfoHeader
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0))
            file.write(dword(self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            #Color Table
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.pixels[x][y])

