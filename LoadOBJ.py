import time
import sys, pygame
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *

# IMPORT OBJECT LOADER
from objloader_textures import *


attack0 = 'C:/Users/Usuario/Documents/Compgra/V2/knigth-pyOpenGL/knight_attack_0.obj'
attack1 = 'C:/Users/Usuario/Documents/Compgra/V2/knigth-pyOpenGL/knight_attack_1.obj'
attack2 = 'C:/Users/Usuario/Documents/Compgra/V2/knigth-pyOpenGL/knight_attack_2.obj'
attack3 = 'C:/Users/Usuario/Documents/Compgra/V2/knigth-pyOpenGL/knight_attack_3.obj'
attack4 = 'C:/Users/Usuario/Documents/Compgra/V2/knigth-pyOpenGL/knight_attack_4.obj'
attack5 = 'C:/Users/Usuario/Documents/Compgra/V2/knigth-pyOpenGL/knight_attack_5.obj'
attack6 = 'C:/Users/Usuario/Documents/Compgra/V2/knigth-pyOpenGL/knight_attack_6.obj'
attack7 = 'C:/Users/Usuario/Documents/Compgra/V2/knigth-pyOpenGL/knight_attack_7.obj'

walk0 = 'C:/Users/Usuario/Documents/Compgra/V2/knigth-pyOpenGL/knight_run_0.obj'
walk1 = 'C:/Users/Usuario/Documents/Compgra/V2/knigth-pyOpenGL/knight_run_1.obj'
walk2 = 'C:/Users/Usuario/Documents/Compgra/V2/knigth-pyOpenGL/knight_run_2.obj'
walk3 = 'C:/Users/Usuario/Documents/Compgra/V2/knigth-pyOpenGL/knight_run_3.obj'
walk4 = 'C:/Users/Usuario/Documents/Compgra/V2/knigth-pyOpenGL/knight_run_4.obj'
walk5 = 'C:/Users/Usuario/Documents/Compgra/V2/knigth-pyOpenGL/knight_run_5.obj'




box =  'C:/Users/Usuario/Documents/Compgra/V2/knigth-pyOpenGL/box_texturas2.obj'



pygame.init()
viewport = (800,600)
hx = viewport[0]/2
hy = viewport[1]/2
srf = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)


glEnable(GL_TEXTURE_2D)

texID =  ReadTexture('C:/Users/Usuario/Documents/Compgra/V2/knigth-pyOpenGL/knight.png')

boxTexID =  ReadTexture('C:/Users/Usuario/Documents/Compgra/V2/knigth-pyOpenGL/box.png')


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

wlk0 = OBJ(walk0, swapyz=True)
wlk1 = OBJ(walk1, swapyz=True)
wlk2 = OBJ(walk2, swapyz=True)
wlk3 = OBJ(walk3, swapyz=True)
wlk4 = OBJ(walk4, swapyz=True)
wlk5 = OBJ(walk5, swapyz=True)


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
objArray.append(wlk0)
objArray.append(wlk1)
objArray.append(wlk2)
objArray.append(wlk3)
objArray.append(wlk4)
objArray.append(wlk5)

##wlkArray = []
##
##wlkArray.append(wlk0)
##wlkArray.append(wlk1)
##wlkArray.append(wlk2)
##wlkArray.append(wlk3)
##wlkArray.append(wlk4)
##wlkArray.append(wlk5)


clock = pygame.time.Clock()
glClearColor(1,1,1,1)



glMatrixMode(GL_PROJECTION)
glLoadIdentity()
width, height = viewport
gluPerspective(90.0, width/float(height),1, 200.0)
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_MODELVIEW)

rx, ry = (-180,0)
rxBox, ryBox = (45,15)
tx, ty = (0,0)
txBox, tyBox = (0,0)
zpos = 80
rotate = move = False
sec = 0
step = 7
animation = False
walk = False
stand = True
start_time = 0

kx,kz = (0,0)


while 1:
    clock.tick(10)
    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit()
        elif e.type == KEYDOWN and e.key == K_ESCAPE:
            sys.exit()
        elif e.type == MOUSEBUTTONDOWN:
            #if e.button == 4: zpos = max(1, zpos-1)
            #elif e.button == 5: zpos += 1
            if e.button == 1: rotate = True
            if e.button == 3: move = True
        elif e.type == MOUSEBUTTONUP:
            if e.button == 1: rotate = False
            elif e.button == 3: move = False
        elif e.type == MOUSEMOTION:
            i, j = e.rel
            if rotate:
                rx += i
                #ry += j
            if move:
                tx += i
                ty -= j
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_d:
                kz += 5
                walk = True
            elif e.key == pygame.K_a:
                kz -= 5
                walk = True
            elif e.key == pygame.K_w:
                          
                kx += 5
                walk = True
                #pygame.mixer.music.load('C:/Users/Usuario/Documents/Compgra/V2/knigth-pyOpenGL/knight.mp3')
                #print(sec)
            
                #print(time_since_enter)
                #if(sec < 7):
                #glCallList(objArray[sec].gl_list)

                start_time = pygame.time.get_ticks()

                #pygame.mixer.music.play(0)
                
            elif e.key == pygame.K_s:
                kx -= 5
                walk = True
            elif e.key == pygame.K_p:
                #for sec2 in range(8):
                animation = True
                pygame.mixer.music.load('C:/Users/Usuario/Documents/Compgra/V2/knigth-pyOpenGL/knight.mp3')
                #print(sec)
            
                #print(time_since_enter)
                #if(sec < 7):
                #glCallList(objArray[sec].gl_list)
                start_time = pygame.time.get_ticks()

                pygame.mixer.music.play(0)
            #pygame.display.flip()
            #sec+=1
            #else:
            #sec = 0
            #glDeleteLists(objArray[i].gl_list,0)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()


    # RENDER OBJECT BOX
    glTranslate(tx/20., ty/20., -70)
    glRotate(ryBox, 1, 0, 0)
    glRotate(rxBox, 0, 1, 0)

 
    glBindTexture(GL_TEXTURE_2D, boxTexID)

    glCallList(boxObj.gl_list)



    
    glBindTexture(GL_TEXTURE_2D, texID)    

    glLoadIdentity()


    # RENDER OBJECT knight
    glTranslate(tx/20., ty/20., - zpos)
    glRotate(ryBox, 1, 0, 0)
    glRotate(rxBox, 0, 1, 0)
    #otra traslacion
    glTranslate(kx, -11.5, kz)
    glRotate(ry, 1, 0, 0)
    glRotate(rx, 0, 1, 0)

    #glCallList(objArray[sec].gl_list)
    #sec = step


    if walk:
        stand = False
        animation = False
        
        glCallList(objArray[step].gl_list)

        time_since_enter = pygame.time.get_ticks() - start_time
        
        if time_since_enter >= 200:
            step +=1
            start_time = pygame.time.get_ticks()
        if step == 13:
            step = 7
            walk = False
            stand = True
            
    if animation:
        stand = False
        glCallList(objArray[sec].gl_list)

        time_since_enter = pygame.time.get_ticks() - start_time
        #print(time_since_enter)
        if time_since_enter >= 200:
            sec +=1
            start_time = pygame.time.get_ticks()
        if sec == 7:
            sec = 0
            animation = False
            stand = True

    if stand:
        glCallList(objArray[0].gl_list)
        time_since_enter = pygame.time.get_ticks() - start_time
        

    pygame.display.flip()
   
   
    

