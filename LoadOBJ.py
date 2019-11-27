import time
import sys, pygame
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
# IMPORT OBJECT LOADER
from objloader_textures import *
from settings import *


settings = Conf('C:/Users/Usuario/Documents/Compgra/V2/knigth-pyOpenGL/knight_settings.txt')


box =  settings.path + settings.model1


pygame.init()
viewport = (settings.height,settings.width)
hx = viewport[0]/2
hy = viewport[1]/2
srf = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)


glEnable(GL_TEXTURE_2D)

texID =  ReadTexture(settings.path + settings.tex1)

boxTexID =  ReadTexture(settings.path + settings.tex2)


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

objArray = []

#attacks
for ite in range(len(settings.attack)):

    obj = OBJ(settings.path + settings.attack[ite], swapyz=True)
    objArray.append(obj)

#movesForward
for ite in range(len(settings.walk)):

    obj = OBJ(settings.path + settings.walk[ite], swapyz=True)
    objArray.append(obj)

#movesFallback
for ite in range(len(settings.fallback)):

    obj = OBJ(settings.path + settings.fallback[ite], swapyz=True)
    objArray.append(obj)



boxObj = OBJ(box, swapyz=True)

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
fstep = 13

animation = False
walk = False
fallback = False
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
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_d:
                kz += 5
                walk = True
            elif e.key == pygame.K_a:
                kz -= 5
                walk = True
            elif e.key == pygame.K_w:
                kx += 5
                fallback = True
                pygame.mixer.music.load(settings.path + settings.sound_back)
                pygame.mixer.music.play(0)
                
            elif e.key == pygame.K_s:
##                pygame.mixer.music.load(settings.path + settings.sound_voy)
##                pygame.mixer.music.play(0)
                walk = True
                pygame.mixer.music.load(settings.path + settings.step_sound)
                pygame.mixer.music.play(0)
                kx -= 10
            elif e.key == pygame.K_p:
                animation = True
                pygame.mixer.music.load(settings.path + settings.attack_sound)
                pygame.mixer.music.play(0)
            
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

    if fallback:
        stand = False
        animation = False
        
        glCallList(objArray[fstep].gl_list)

        time_since_enter = pygame.time.get_ticks() - start_time
        
        if time_since_enter >= 1:
            fstep +=1
            start_time = pygame.time.get_ticks()
        if fstep == 17:
            fstep = 13
            fallback = False
            stand = True
            
    if animation:
        stand = False
        glCallList(objArray[sec].gl_list)
        time_since_enter = pygame.time.get_ticks() - start_time

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
   
   
    

