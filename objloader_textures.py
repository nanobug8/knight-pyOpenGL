from PIL import Image
import numpy
import pygame
from OpenGL.GL import *
#from loadTextures import *

class OBJ:
    
    def __init__(self, filename, swapyz=False):
        """Loads a Wavefront OBJ file. """
        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []

        material = None
        for line in open(filename, "r"):
            if line.startswith('#'): continue
            values = line.split()
            if not values: continue
            if values[0] == 'v':
                v = list(map(float, values[1:4]))
                if swapyz:
                    v = v[0], v[2], v[1]
                self.vertices.append(v)
            elif values[0] == 'vn':
                v = list(map(float, values[1:4]))
                if swapyz:
                    v = v[0], v[2], v[1]
                self.normals.append(v)
                #print(self.normals)
            elif values[0] == 'vt':
                vt = list(map(float, values[1:3]))
                self.texcoords.append(vt)
            elif values[0] == 'f':
                face = []
                texcoords = []
                norms = []
                for v in values[1:]:
                    w = v.split('/')
                    face.append(int(w[0]))
                    if len(w) >= 2 and len(w[1]) > 0:
                        norms.append(int(w[1]))
                    else:
                        norms.append(0)
                    if len(w) >= 3 and len(w[2]) > 0:
                        texcoords.append(int(w[2]))
                    else:
                        texcoords.append(0)
                self.faces.append((face, norms, texcoords, material))
        self.gl_list = glGenLists(1)
        glNewList(self.gl_list, GL_COMPILE)

        glEnable(GL_TEXTURE_2D)
        glFrontFace(GL_CCW)
        for face in self.faces:
            vertices, normals, texture_coords, material = face
            glBegin(GL_POLYGON)
            for i in range(len(vertices)):
                if normals[i] > 0:
                    glNormal3fv(self.normals[normals[i] - 1])
                if texcoords[i] > 0:
                    glTexCoord2fv(self.texcoords[texture_coords[i] - 1])
                glVertex3fv(self.vertices[vertices[i] - 1])
                #aca va el texture de 2f
            glEnd()
        glEndList()

        
def ReadTexture(filename):
      #pygame.init()
      #display = (800,600)
      #pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
      # PIL can open BMP, EPS, FIG, IM, JPEG, MSP, PCX, PNG, PPM
      # and other file types.  We convert into a texture using GL.
      print('trying to open', filename)
      try:
         image = Image.open(filename)
      except IOError as ex:
         print('IOError: failed to open texture file')
         message = template.format(type(ex).__name__, ex.args)
         print(message)
         return -1
      print('opened file: size=', image.size, 'format=', image.format)
      imageData = numpy.array(list(image.getdata()), numpy.uint8)

      textureID = glGenTextures(1)
      glPixelStorei(GL_UNPACK_ALIGNMENT, 4)
      glBindTexture(GL_TEXTURE_2D, textureID)
      glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_BASE_LEVEL, 0)
      glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAX_LEVEL, 0)
      glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.size[0], image.size[1],
         0, GL_RGB, GL_UNSIGNED_BYTE, imageData)
      glBindTexture(GL_TEXTURE_2D, 0)

      #image.close()
      print(textureID)
      #pygame.quit()
      #quit()
      return textureID
