#Universidad del Valle de Guatemala
#Daniel Cabrera 20289
#Gráficas por Computadora
#Base de Carlos Alonso


class Obj(object):
    def __init__(self, filename):
        with open(filename, "r") as file:
            self.lines = file.read().splitlines()

        self.vertices = []
        self.texcoords = []
        self.normals = []
        self.faces = []

        for line in self.lines:
            try:
                prefix, value = line.split(' ', 1)
            except:
                continue
            try:
                if prefix == 'v': # Se leen vertices
                    self.vertices.append( list(map(float,value.split(' '))))
                elif prefix == 'vt': # Se leen coordenadas
                    self.texcoords.append( list(map(float, value.split(' '))))
                elif prefix == 'vn': # Se leen normales
                    self.normals.append( list(map(float, value.split(' '))))
                elif prefix == 'f': # Se leen caras
                    self.faces.append([  list(map(int, vert.split('/'))) for vert in value.split(' ')] )
            except:
                continue
