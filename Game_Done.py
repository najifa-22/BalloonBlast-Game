from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math
import random
import time
score=0
m_x=0
m_y=0
game_over=False
outside=False
temp=0
dy=0
dx=0
arr3=[]
arr4=[]
d=0
bx=0
by=0
bullet=[]
bullet_dir=[]
NE=0
E=0
c_x1=0
c_x2=0
c_x=0
c_y=0
a=0
c_y1=0
c_y2=0
rx=0
ry=0
pause=False
limit=False
arr=[]
arr2=[]
speed=0.01
x_move=5
y_move=50
rotate="left"
gun=[[200,250],[300,250],[200,220],[300,220],[230,220],[250,220],[230,180],[250,180]]
zone=0
radius=[3,3,3,3]
center=[[50,400],[400,50],[50,50],[400,400]]
n=0
hit=False
def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    glutPostRedisplay()


def find_zone(x_1,y_1,x_2,y_2):
    arr=[]
    global dx,dy,d,E,NE,c_x1, c_x2, c_y1, c_y2,zone
    dy=y_2-y_1
    dx=x_2-x_1
    if abs(dx)>abs(dy):
        if dx>0 and dy>0:
            c_x1=x_1
            c_y1=y_1
            c_x2=x_2
            c_y2=y_2
            zone=0
        elif dx<0 and dy>0:
            c_x1=-x_1
            c_y1=y_1
            c_x2=-x_2
            c_y2=y_2
            zone=3
        elif dx<0 and dy<0:
            c_x1=-x_1
            c_y1=-y_1
            c_x2=-x_2
            c_y2=-y_2
            zone=4
        elif dx>0 and dy<0:
            c_x1=x_1
            c_y1=-y_1
            c_x2=x_2
            c_y2=-y_2
            zone=7
        if dx>0 and dy==0:
            c_x1=x_1
            c_y1=y_1
            c_x2=x_2
            c_y2=y_2
            zone=0
        elif dx<0 and dy==0:
            c_x1=-x_1
            c_y1=y_1
            c_x2=-x_2
            c_y2=y_2
            zone=3
    else:
        if dx>0 and dy>0:
            c_x1=y_1
            c_y1=x_1
            c_x2=y_2
            c_y2=x_2
            zone=1
        elif dx<0 and dy>0:
            c_x1=y_1
            c_y1=-x_1
            c_x2=y_2
            c_y2=-x_2
            zone=2
        elif dx<0 and dy<0:
            c_x1=-y_1
            c_y1=-x_1
            c_x2=-y_2
            c_y2=-x_2
            zone=5
        elif dx>0 and dy<0:
            c_x1=-y_1
            c_y1=x_1
            c_x2=-y_2
            c_y2=x_2
            zone=6
        elif dx==0 and dy>0:
            c_x1=y_1
            c_y1=x_1
            c_x2=y_2
            c_y2=x_2
            zone=1
        elif dx==0 and dy<0:
            c_x1=-y_1
            c_y1=x_1
            c_x2=-y_2
            c_y2=x_2
            zone=6
    dy=c_y2-c_y1
    dx=c_x2-c_x1
    d=2*dy-dx
    E=2*dy
    NE=2*dy-2*dx
    while c_x1<c_x2:
        if d>0:
            d=d+NE
            c_x1+=1
            c_y1+=1
        else:
            d=d+E
            c_x1+=1 
        if zone==0:
            arr.append((c_x1,c_y1))
        elif zone==1:
            arr.append((c_y1,c_x1))
        elif zone==2:
            arr.append((-c_y1,c_x1))
        elif zone==3:
            arr.append((-c_x1,c_y1))
        elif zone==4:
            arr.append((-c_x1,-c_y1))
        elif zone==5:
            arr.append((-c_y1,-c_x1))
        elif zone==6:
            arr.append((c_y1,-c_x1))
        elif zone==7:
            arr.append((c_x1,-c_y1))
    for x,y in arr:

        glPointSize(1) 
        glBegin(GL_POINTS)
        glVertex2f(x,y)
        glEnd()
        
        
def find_zone2(x_1,y_1,x_2,y_2): #bullet
    global dx,dy,d,E,NE,c_x1, c_x2, c_y1, c_y2,zone, arr3,arr2
    arr3=[]
    dy=y_2-y_1
    dx=x_2-x_1
    if abs(dx)>abs(dy):
        if dx>0 and dy>0:
            c_x1=x_1
            c_y1=y_1
            c_x2=x_2
            c_y2=y_2
            zone=0
        elif dx<0 and dy>0:
            c_x1=-x_1
            c_y1=y_1
            c_x2=-x_2
            c_y2=y_2
            zone=3
        elif dx<0 and dy<0:
            c_x1=-x_1
            c_y1=-y_1
            c_x2=-x_2
            c_y2=-y_2
            zone=4
        elif dx>0 and dy<0:
            c_x1=x_1
            c_y1=-y_1
            c_x2=x_2
            c_y2=-y_2
            zone=7
        if dx>0 and dy==0:
            c_x1=x_1
            c_y1=y_1
            c_x2=x_2
            c_y2=y_2
            zone=0
        elif dx<0 and dy==0:
            c_x1=-x_1
            c_y1=y_1
            c_x2=-x_2
            c_y2=y_2
            zone=3
    else:
        if dx>0 and dy>0:
            c_x1=y_1
            c_y1=x_1
            c_x2=y_2
            c_y2=x_2
            zone=1
        elif dx<0 and dy>0:
            c_x1=y_1
            c_y1=-x_1
            c_x2=y_2
            c_y2=-x_2
            zone=2
        elif dx<0 and dy<0:
            c_x1=-y_1
            c_y1=-x_1
            c_x2=-y_2
            c_y2=-x_2
            zone=5
        elif dx>0 and dy<0:
            c_x1=-y_1
            c_y1=x_1
            c_x2=-y_2
            c_y2=x_2
            zone=6
        elif dx==0 and dy>0:
            c_x1=y_1
            c_y1=x_1
            c_x2=y_2
            c_y2=x_2
            zone=1
        elif dx==0 and dy<0:
            c_x1=-y_1
            c_y1=x_1
            c_x2=-y_2
            c_y2=x_2
            zone=6
    dy=c_y2-c_y1
    dx=c_x2-c_x1
    d=2*dy-dx
    E=2*dy
    NE=2*dy-2*dx
    while c_x1<c_x2:
        if d>0:
            d=d+NE
            c_x1+=1
            c_y1+=1
        else:
            d=d+E
            c_x1+=1 
        if zone==0:
            arr3.append((c_x1,c_y1))
        elif zone==1:
            arr3.append((c_y1,c_x1))
        elif zone==2:
            arr3.append((-c_y1,c_x1))
        elif zone==3:
            arr3.append((-c_x1,c_y1))
        elif zone==4:
            arr3.append((-c_x1,-c_y1))
        elif zone==5:
            arr3.append((-c_y1,-c_x1))
        elif zone==6:
            arr3.append((c_y1,-c_x1))
        elif zone==7:
            arr3.append((c_x1,-c_y1))
    for x,y in arr3:

        glPointSize(5) 
        glBegin(GL_POINTS)
        glVertex2f(x,y)
        glEnd()
 
def keyboardListener(key,x,y):

    global gun, rx1,ry1,rx2,rx3,rx4,rx5,rx6,rx7,rx8,ry2,ry3,ry4,ry5,ry6,ry7,ry8, rotate, bx, by, bullet, bullet_dir, pause, game_over
    
    if key==b' ' and rotate=="left" and pause==False and game_over==False:
        bx=gun[1][0]
        by=(gun[1][1]+gun[3][1])/2
        bullet.append([bx,by])
        bullet_dir.append("left")
    if key==b' ' and rotate=="right" and pause==False and game_over==False:
        bx=gun[1][0]
        by=(gun[1][1]+gun[3][1])/2
        bullet.append([bx,by])
        bullet_dir.append("right")
    if key==b'r' and rotate=="left" and pause==False and game_over==False:
        gun[0],gun[1]=gun[1],gun[0]
        gun[2],gun[3]=gun[3],gun[2]
        gun[4][0]=gun[4][0]+40
        gun[4],gun[5]=gun[5],gun[4]
        gun[6][0]=gun[6][0]+40
        gun[6],gun[7]=gun[7],gun[6]
        rotate="right"
    
    elif key==b'r' and rotate=="right" and pause==False and game_over==False: 
        gun[0],gun[1]=gun[1],gun[0]
        gun[2],gun[3]=gun[3],gun[2]
        gun[5][0]=gun[5][0]-40
        gun[4],gun[5]=gun[5],gun[4]
        gun[7][0]=gun[7][0]-40
        gun[6],gun[7]=gun[7],gun[6]
        rotate="left"
        
def specialKeyListener(key, x, y):
    global x_move, game_over,GL_PASS_THROUGH_TOKEN, gun,pause, game_over

    if key==GLUT_KEY_RIGHT and pause==False and game_over==False:
        if gun[1][0]<=500:
            gun[0][0]=gun[0][0]+2
            gun[1][0]=gun[1][0]+2
            gun[2][0]=gun[2][0]+2
            gun[3][0]=gun[3][0]+2
            gun[4][0]=gun[4][0]+2
            gun[5][0]=gun[5][0]+2
            gun[6][0]=gun[6][0]+2
            gun[7][0]=gun[7][0]+2
    if key==GLUT_KEY_LEFT and pause==False and game_over==False:
        if gun[0][0]>=0:
            gun[0][0]=gun[0][0]-2
            gun[1][0]=gun[1][0]-2
            gun[2][0]=gun[2][0]-2
            gun[3][0]=gun[3][0]-2
            gun[4][0]=gun[4][0]-2
            gun[5][0]=gun[5][0]-2
            gun[6][0]=gun[6][0]-2
            gun[7][0]=gun[7][0]-2
    if key==GLUT_KEY_UP and pause==False and game_over==False:
        if gun[0][1]<=500:
            gun[0][1]=gun[0][1]+2
            gun[1][1]=gun[1][1]+2
            gun[2][1]=gun[2][1]+2
            gun[3][1]=gun[3][1]+2
            gun[4][1]=gun[4][1]+2
            gun[5][1]=gun[5][1]+2
            gun[6][1]=gun[6][1]+2
            gun[7][1]=gun[7][1]+2
    if key==GLUT_KEY_DOWN and pause==False and game_over==False:
        if gun[6][1]>=0:
            gun[0][1]=gun[0][1]-2
            gun[1][1]=gun[1][1]-2
            gun[2][1]=gun[2][1]-2
            gun[3][1]=gun[3][1]-2
            gun[4][1]=gun[4][1]-2
            gun[5][1]=gun[5][1]-2
            gun[6][1]=gun[6][1]-2
            gun[7][1]=gun[7][1]-2
        
        

    glutPostRedisplay()

def gun_position():
    global gun
    find_zone(gun[0][0],gun[0][1],gun[1][0],gun[1][1])
    find_zone(gun[2][0],gun[2][1],gun[3][0],gun[3][1])
    find_zone(gun[0][0],gun[0][1],gun[2][0],gun[2][1])
    find_zone(gun[1][0],gun[1][1],gun[3][0],gun[3][1])
    find_zone(gun[4][0],gun[4][1],gun[6][0],gun[6][1])
    find_zone(gun[5][0],gun[5][1],gun[7][0],gun[7][1])
    find_zone(gun[6][0],gun[6][1],gun[7][0],gun[7][1])
    find_zone(gun[4][0],gun[4][1],gun[5][0],gun[5][1])
    
    
    
def draw():
    global d,c_y,c_x,arr,limit,temp,arr3,arr4, hit, pause, score, game_over,speed
    arr2=[]
    for i in range(len(radius)):
        c_y=radius[i]
        d=1-c_y
        c_x=0
        while c_x<c_y:
            if d<0:
                d=d+(2*c_x)+3
                c_x+=1
            else:
                d=d+(2*c_x)-(2*c_y)+5
                c_x+=1
                c_y-=1
            if c_x+center[i][0]>500 or c_y+center[i][1]>500 or c_y+center[i][1]<0 or c_x+center[i][0]<0:
                limit=True
                game_over=True
            if c_x+center[i][0]>500 or -c_y+center[i][1]>500 or -c_y+center[i][1]<0 or c_x+center[i][0]<0:
                limit=True
                game_over=True
            if -c_x+center[i][0]>500 or -c_y+center[i][1]>500 or -c_y+center[i][1]<0 or -c_x+center[i][0]<0:
                limit=True
                game_over=True
            if -c_x+center[i][0]>500 or c_y+center[i][1]>500 or c_y+center[i][1]<0 or -c_x+center[i][0]<0:
                limit=True
                game_over=True
            if c_y+center[i][0]>500 or c_x+center[i][1]>500 or c_x+center[i][1]<0 or c_y+center[i][0]<0:
                limit=True
                game_over=True
            if -c_y+center[i][0]>500 or c_x+center[i][1]>500 or c_x+center[i][1]<0 or -c_y+center[i][0]<0:
                limit=True
                game_over=True
            if -c_y+center[i][0]>500 or -c_x+center[i][1]>500 or -c_x+center[i][1]<0 or -c_y+center[i][0]<0:
                limit=True
                game_over=True
            if c_y+center[i][0]>500 or -c_x+center[i][1]>500 or -c_x+center[i][1]<0 or c_y+center[i][0]<0:
                limit=True
                game_over=True
            if radius[i]>40:
                limit=True
                game_over=True
            for j in range(len(arr2)): #arr2_circle, arr3_bullet
                for k in range(len(arr3)):
                    if int(arr2[j][1]) == int(arr3[k][1]) and int(arr2[j][0]) == int(arr3[k][0]):
                        hit=True
                        limit=True
                        score+=radius[i]
                        speed+=0.01
                        print("score",score)
                        break

            if limit==False:
                arr2.append((c_x+center[i][0],c_y+center[i][1]))
                arr2.append((c_x+center[i][0],-c_y+center[i][1]))
                arr2.append((-c_x+center[i][0],-c_y+center[i][1]))
                arr2.append((-c_x+center[i][0],c_y+center[i][1]))
                arr2.append((c_y+center[i][0],c_x+center[i][1]))
                arr2.append((-c_y+center[i][0],c_x+center[i][1]))
                arr2.append((-c_y+center[i][0],-c_x+center[i][1]))
                arr2.append((c_y+center[i][0],-c_x+center[i][1]))

            else:
                radius.pop(i)
                center.pop(i)

                break
        if limit==False and game_over==False:
            for x,y in arr2:
                if radius[i]>=10:
                    
                    glColor3f(1, 0, 0)
                    glPointSize(1) 
                    glBegin(GL_POINTS)
                    glVertex2f(x,y)
                    glEnd()
                
                else:
                    glColor3f(0, 1, 0)
                    glPointSize(1) 
                    glBegin(GL_POINTS)
                    glVertex2f(x,y)
                    glEnd()
            if pause==False and game_over==False:
                temp=radius[i]
                temp+=speed
                radius[i]=temp
        
        else:
            limit=False
            break
        
        
 
 
def bullet_shot():
    global bullet,bullet_dir,x_move, hit, temp,outside, pause, game_over
    if len(bullet)==0:
        pass
    elif game_over==False:
        for i in range(len(bullet)):
            if bullet_dir[i]=="left":
                find_zone2(bullet[i][0],bullet[i][1],bullet[i][0]+x_move,bullet[i][1])
                if hit==True:
                    temp=i
                if bullet[i][0]>500:
                    outside=True
                    temp=i
                if pause==False:
                    bullet[i][0]=bullet[i][0]+x_move

            if bullet_dir[i]=="right":
                
                find_zone2(bullet[i][0],bullet[i][1],bullet[i][0]-x_move,bullet[i][1])
                if hit==True:
                    
                    temp=i
                if bullet[i][0]<0:
                    outside=True
                    temp=i
                if pause==False:
                    bullet[i][0]=bullet[i][0]-x_move
        if hit==True:
            bullet.pop(temp)
            bullet_dir.pop(temp)
            hit=False
        if outside==True:
            bullet.pop(temp)
            bullet_dir.pop(temp)
            outside=False
       
def circle_generate():
    global n,a,rx,ry
    if len(radius)<4:
        a=random.randint(3, 9)
        radius.append(a)
        rx=random.randint(100, 400)
        ry=random.randint(100, 400)
        center.append([rx,500-ry])
        draw()


def art_icons():
    global pause   
    glColor3f(1, 0, 0)        #
    find_zone(20,460,80,460)
    find_zone(20,460,55,490)
    find_zone(20,460,55,430)

    if pause==True:
        glColor3f(0, 1, 0)
        find_zone(230,490,230,430) 
        find_zone(230,430,280,460)
        find_zone(230,490,280,460)
    else:
        glColor3f(0, 1, 0)
        find_zone(240,490,240,430) 
        find_zone(270,490,270,430)
    glColor3f(1, 1, 0)
    find_zone(445,490,495,430) 
    find_zone(495,490,445,430)
    glColor3f(0, 0, 1)
    # find_zone(425,40,450,70)
    # find_zone(450,70,475,40)
    # find_zone(425,40,475,40)
    
    
def mouseListener(button, state, x, y):	
    global m_x,m_y,pause,game_over,score, center, radius, speed, bullet, bullet_dir, gun, rotate
    if button == GLUT_LEFT_BUTTON:
        if(state == GLUT_DOWN):
  
            m_x=x
            m_y=500-y
            if m_x>=445 and m_x<=495 and m_y>=430 and m_y<=490:
                print("Goodbye")
                glutLeaveMainLoop()
                
            if pause==False and m_x>=240 and m_x<=270 and m_y>=430 and m_y<=490:
            
                pause=True
            elif pause==True and m_x>=230 and m_x<=280 and m_y>=430 and m_y<=490:
                pause=False
            if m_x>=20 and m_x<=80 and m_y>=460 and m_y<=490:

                game_over=False
                score=0
                speed=0.01
                radius=[3,3,3,3]
                center=[[50,400],[400,50],[50,50],[400,400]]
                gun=[[200,250],[300,250],[200,220],[300,220],[230,220],[250,220],[230,180],[250,180]]
                bullet=[]
                bullet_dir=[]
                rotate="left"
                print("Starting over!")
                
                
def showScreen():
    global game_over,score,pause
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0)
    glLoadIdentity()
    iterate()
    art_icons()
    gun_position()
    circle_generate()
    draw()
    bullet_shot()
    glColor3f(1, 1, 1)
    
    score_text = f"SCORE: {round(score)}"
    glRasterPos2f(210, 20)  
    for char in score_text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))
    glutSwapBuffers()
    

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) 
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") 
glutDisplayFunc(showScreen)
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboardListener)
glutMouseFunc(mouseListener)
glutSpecialFunc(specialKeyListener)
glutMainLoop()