import time
import sys, pygame
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *

# IMPORT OBJECT LOADER
from objloader_textures import *


attack0 = 'C:/Users/jcamargo/Desktop/Matias/comp/knigth-pyOpenGL/knight_attack_0.obj'
attack1 = 'C:/Users/jcamargo/Desktop/Matias/comp/knigth-pyOpenGL/knight_attack_1.obj'
attack2 = 'C:/Users/jcamargo/Desktop/Matias/comp/knigth-pyOpenGL/knight_attack_2.obj'
attack3 = 'C:/Users/jcamargo/Desktop/Matias/comp/knigth-pyOpenGL/knight_attack_3.obj'
attack4 = 'C:/Users/jcamargo/Desktop/Matias/comp/knigth-pyOpenGL/knight_attack_4.obj'
attack5 = 'C:/Users/jcamargo/Desktop/Matias/comp/knigth-pyOpenGL/knight_attack_5.obj'
attack6 = 'C:/Users/jcamargo/Desktop/Matias/comp/knigth-pyOpenGL/knight_attack_6.obj'
attack7 = 'C:/Users/jcamargo/Desktop/Matias/comp/knigth-pyOpenGL/knight_attack_7.obj'

box =  'C:/Users/jcamargo/Desktop/Matias/comp/knigth-pyOpenGL/box_texturas.obj'



pygame.init()
viewport = (800,600)
hx = viewport[0]/2
hy = viewport[1]/2
srf = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)


glEnable(GL_TEXTURE_2D)

texID =  ReadTexture('C:/Users/jcamargo/Desktop/Matias/comp/knigth-pyOpenGL/knight.png')

boxTexID =  ReadTexture('C:/Users/jcamargo/Desktop/Matias/comp/knigth-pyOpenGL/box.png')


glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0))
glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
glEnable(GL_LIGHT0)
glEnable(GL_LIGHTING)
glEnable(GL_COLOR_MATERIAL)
glEnable(GL_DEPTH_TEST)
glShadeModel(GL_SMOOTH)           # most obj files expect to be smooth-shaded
glActiveTexture(GL_TEXTURE0)



# LOAD OBJECT AFTER PYGAME INIT

obj0 = OBJ(attack0, swapyz=True)
obj1 = OBJ(attack1, swapyz=True)
obj2 = OBJ(attack2, swapyz=True)
obj3 = OBJ(attack3, swapyz=True)
obj4 = OBJ(attack4, swapyz=True)
obj5 = OBJ(attack5, swapyz=True)
obj6 = OBJ(attack6, swapyz=True)
obj7 = OBJ(attack7, swapyz=True)

boxObj = OBJ(box, swapyz=True)

objArray = []

objArray.append(obj0)
objArray.append(obj1)
objArray.append(obj2)
objArray.append(obj3)
objArray.append(obj4)
objArray.append(obj5)
objArray.append(obj6)
objArray.append(obj7)


#muchos obj cargados aca...
#hacer funcion nombre de modelo nombre de funcion y cant de cuadrads
clock = pygame.time.Clock()
glClearColor(1,1,1,1)



glMatrixMode(GL_PROJECTION)
glLoadIdentity()
width, height = viewport
gluPerspective(90.0, width/float(height),1, 100.0)
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_MODELVIEW)

rx, ry = (-110,-10)
tx, ty = (0,0)
zpos = 42
rotate = move = False
sec = 0
while 1:
    clock.tick(30)
    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit()
        elif e.type == KEYDOWN and e.key == K_ESCAPE:
            sys.exit()
        elif e.type == MOUSEBUTTONDOWN:
            if e.button == 4: zpos = max(1, zpos-1)
            elif e.button == 5: zpos += 1
            elif e.button == 1: rotate = True
            elif e.button == 3: move = True
        elif e.type == MOUSEBUTTONUP:
            if e.button == 1: rotate = False
            elif e.button == 3: move = False
        elif e.type == MOUSEMOTION:
            i, j = e.rel
            if rotate:
                rx += i
                ry += j
            if move:
                tx += i
                ty -= j
        elif e.type == KEYUP:
        #for sec2 in range(8):
            pygame.mixer.music.load('C:/Users/jcamargo/Desktop/Matias/comp/knigth-pyOpenGL/knight.mp3')
            print(sec)
            start_time = pygame.time.get_ticks()
            time_since_enter = pygame.time.get_ticks() - start_time
            #print(time_since_enter)
            if(sec < 7):
                glCallList(objArray[sec].gl_list)
                
                pygame.mixer.music.play(0)
                pygame.display.flip()
                sec+=1
            else:
                sec = 0
            #glDeleteLists(objArray[i].gl_list,0)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glBindTexture(GL_TEXTURE_2D, texID)    
    #glBindTexture(GL_TEXTURE_2D, boxTexID)
    


    # RENDER OBJECT
    glTranslate(tx/20., ty/20., - zpos)
    glRotate(ry, 1, 0, 0)
    glRotate(rx, 0, 1, 0)

 
    
    #glCallList(boxObj.gl_list)

    #glCallList(obj0.gl_list)
    glCallList(objArray[sec].gl_list)

    pygame.display.flip()
   
   
    

