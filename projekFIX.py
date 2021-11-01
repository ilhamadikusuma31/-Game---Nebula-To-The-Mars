import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU
import random as rd

print("Imports successful!")


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

pos_awal = 0

pos_x_pemain = 0
pos_y_pemain = 0

pos_x_peluru = pos_x_pemain 
pos_y_peluru = pos_y_pemain

kecepatan_peluru = 100

motion = 50
w,h= 1024,576


def init():
    print("huo")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-500.0, 500.0, -500.0, 500.0)

def pemain():
    global pos_x_pemain, pos_y_pemain
    print(pos_x_pemain, pos_y_pemain)
    # print("hopppi")
    glTranslated(pos_x_pemain, pos_y_pemain, 0)
    glColor3f(1.0, 1.0, 1.0) #RGB
    glBegin(GL_POLYGON)
    glVertex2f(-50,-340)
    glVertex2f(50,-340)
    glVertex2f(50,-310)
    glVertex2f(-50,-310)
    glEnd()

def peluru():
    global pos_x_peluru, pos_y_peluru, kecepatan_peluru
  
    pos_y_peluru += kecepatan_peluru
    if pos_y_peluru > 1000:
        pos_y_peluru = pos_awal 
    glTranslated(pos_x_peluru, pos_y_peluru, 0)
    glColor3f(1.0, 0, 1.0) #RGB
    glBegin(GL_POLYGON) 
    glVertex2f(-20,-100)
    glVertex2f(20,-100)
    glVertex2f(20,-50)
    glVertex2f(-20,-50)
    glEnd()


def meteor():
    glColor3f(0, 0, 1.0) #RGB
    glBegin(GL_QUADS) 
    glVertex2f(30,5)
    glVertex2f(45,15)
    glVertex2f(45,20)
    glVertex2f(30,10)
    glEnd()


def display():
    # print("hudd")
    glClear(GL_COLOR_BUFFER_BIT)
    # glColor3f(1.0,1.0,1.)
    # glBegin(GL_LINES)
    # glVertex2f(-500.0, 0.0)
    # glVertex2f(500.0, 0.0)
    # glVertex2f(0.0, 500.0)
    # glVertex2f(0.0, -500.0)
    # glEnd()
    glPushMatrix()
    pemain()
    # if peluru_aktif == True:
    peluru()
    # meteor()
    glPopMatrix()
    glFlush()


def input_keyboard(key,x,y):
    global pos_x_pemain, pos_y_pemain, pos_x_peluru, pos_y_peluru

    if key == GLUT_KEY_UP:
        pos_y_pemain += motion
        # print("Tombol Atas ditekan ", "x : ", pos_x, " y : ", pos_y)
    elif key == GLUT_KEY_DOWN:
        pos_y_pemain -= motion
        # print("Tombol Bawah ditekan ", "x : ", pos_x, " y : ", pos_y)
    elif key == GLUT_KEY_RIGHT:
        pos_x_pemain += motion
        # print("Tombol Kanan ditekan ", "x : ", pos_x, " y : ", pos_y)
    elif key == GLUT_KEY_LEFT:
        pos_x_pemain -= motion
        # print("Tombol Kiri ditekan ", "x : ", pos_x, " y : ", pos_y)
   
       
        # print("Tombol Kiri ditekan ", "x : ", pos_x, " y : ", pos_y)
        
    # Untuk Mengubah Warna backgorund window
    # Background Kiri Atas berubah warna menjadi Hijau
    # if pos_x < 0 and pos_y > 0:
    #     glClearColor(0.0, 1.0, 0.0, 1.0)
    # # Background Kanan Atas berubah warna menjadi Biru
    # if pos_x > 0 and pos_y > 0:
    #     glClearColor(0.0,0.0,1.0,1.0)
    # # Background Kanan Bawah berubah warna menjadi Merah
    # if pos_x > 0 and pos_y < 0:
    #     glClearColor(1.0, 0.0, 0.0, 1.0)
    # # Background Kiri Bawah berubah warna menjadi Hitam
    # if pos_x < 0 and pos_y < 0:
    #     glClearColor(0.0,0.0,0.0,1.0)



def update(value):
    glutPostRedisplay()
    glutTimerFunc(10,update,0)

def main():
    print("hui")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(w,h)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Eveng Handling Keyboard & Mouse")
    glutDisplayFunc(display)
    # glutKeyboardFunc((unsigned_char key,int x, int y))
    glutSpecialFunc(input_keyboard)
    glutTimerFunc(50, update, 0)
    init()
    glutMainLoop()

main()