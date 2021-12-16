import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU
import random as rd
import os
import time
import json

print("Imports successful!")


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

pos_awal = 0


border_x = 450
border_y = 500

pos_x_pemain = 0
pos_y_pemain = -500


pos_x_peluru = 0
pos_y_peluru  = pos_y_pemain


pos_x_meteor = 0
pos_y_meteor = border_y

kecepatan_peluru = 0
kecepatan_meteor = 10
kecepatan_damage  = 10
damagenya = 0

kondisi_tembak = False
kondisi_damage = False
kondisi_pecah = False

darah = 380
batu  = 1
hit_meteor = 10
counter_batu = 1000

penambah_loading = 0.0000001
loading = False
mulai = True
jalan = False
selesai = False
muncul_tangga = False
delta_tangga = 0

mati = False
motion = 10
motion_tangga = 0.01
w,h= 1280,720

jumlah_bintang = 1000

jedag, jedug = 1,1

detik = 1
penambah_detik = 2600//60

def init():
    glClearColor(0.067,0.09,0.11, 1)
    gluOrtho2D(-500.0, 500.0, -500.0, 500.0)
        
def bintang():
    glPushMatrix()
    glPointSize(0.5)
    glRotated(180,0,0,0)
    glColor3f(1.0, 1.0, 1.0) #RGB
    glBegin(GL_POINTS)
    y = 1000
    for i in range(jumlah_bintang):
        x = rd.randrange(-1000,1000)
        glVertex2f(x,y)
        if y != 1000:
            x = x
        y -= 100

    glEnd()
    glPopMatrix()

def peluru():
    global pos_x_peluru, pos_y_peluru, kecepatan_peluru, pos_x_pemain,pos_y_pemain, kondisi_tembak
    
    glPushMatrix()
    
    rgb = [1,0,0.5] #warna pink
    pos_y_peluru += kecepatan_peluru

    #jika peluru melewati batas atas maka akan diset ke posisi awal (tepat didepan pesawat)
    if pos_y_peluru > 1000:
        kecepatan_peluru = 0
        kondisi_tembak = False
        pos_y_peluru = pos_y_pemain
        pos_x_peluru = pos_x_pemain 
        
    
    if kecepatan_peluru == 0:
        pos_x_peluru = pos_x_pemain
        pos_y_peluru = pos_y_pemain
        rgb = [0.067,0.09,0.11] #warna hitam
    
    
    glTranslated(pos_x_peluru, pos_y_peluru+300, 0)
    glColor3f(rgb[0], rgb[1], rgb[2]) #RGB
    glBegin(GL_POLYGON) 
    glVertex2f(-5,-100)
    glVertex2f(5,-100)
    glVertex2f(5,-50)
    glVertex2f(-5,-50)
    glEnd()

    glPopMatrix()

def pemain():
    # glutTimerFunc(25, update, 0)
    global pos_x_pemain, pos_y_pemain, kondisi_tembak, pos_y_peluru, kecepatan_peluru, selesai, delta_tangga, muncul_tangga, motion_tangga, motion, penambah_detik
    glPushMatrix()

    #batas agar pemain tidak keluar dari layar
    if not selesai:
        if pos_x_pemain > border_x:
            pos_x_pemain = border_x
        if pos_x_pemain < -border_x:
            pos_x_pemain = -border_x

        if pos_y_pemain > border_y-200:
            pos_y_pemain = border_y-200
        if pos_y_pemain < -border_y:
            pos_y_pemain = -border_y

      
    ketinggian = 0
       

    #ketika permainan selesai, pemain akan di set di ketinggian 800
    if selesai:
        pengurangan = 1
        pos_y_pemain -= pengurangan
        if ketinggian != 800:
            ketinggian = 800    
        if pos_y_pemain < -953: #ketika menyentuh permukaan mars
            pos_y_pemain = -953
            muncul_tangga = True
            motion = 0
        
    glTranslated(pos_x_pemain, pos_y_pemain + ketinggian, 0)
    glScaled(15*0.5,30*0.5,0)

    #body
    glColor3f(0.859,0.851,0.843) #RGB
    glBegin(GL_POLYGON)
    glVertex2f(-4,2) #A
    glVertex2f(-4,4) #B
    glVertex2f(-3,6) #C
    glVertex2f(-2,9) #D
    glVertex2f(-1,11) #E
    glVertex2f(0,12) #F
    glVertex2f(1,11) #G
    glVertex2f(2,9) #H
    glVertex2f(3,6) #I
    glVertex2f(4,4) #J
    glVertex2f(4,2) #K
    glVertex2f(-4,2) #A
    glEnd()

    #jendela
    glColor3f(0.369,0.361,0.349)
    glBegin(GL_QUADS)
    glVertex2f(-1,10)
    glVertex2f(-1,9)
    glVertex2f(1,9)
    glVertex2f(1,10)
    glEnd()

    #jet kiri
    glColor3f(0.478,0.471,0.463)
    glBegin(GL_POLYGON)
    glVertex2f(-3,2.5)#T
    glVertex2f(-1,2.5)#W
    glVertex2f(-1,1)#v
    glVertex2f(-3,1)#U
    glEnd()

    #jet kanan
    glBegin(GL_POLYGON)
    glVertex2f(1,2.5)#A1
    glVertex2f(3,2.5)#B1
    glVertex2f(3,1)#C
    glVertex2f(1,1)#Z
    glEnd()


    #left part
    glColor3f(0.871,0.545,0.216)
    glBegin(GL_POLYGON)
    glVertex2f(-4,2) #A
    glVertex2f(-4,4) #B
    glVertex2f(-3,6) #C
    glVertex2f(-3,4) #C
    glVertex2f(-1.5,4) #I1
    glVertex2f(-1.5,4) #P
    glVertex2f(-1.5,2.5) #T
    glVertex2f(-3,2.5) #D1
    glVertex2f(-4,2) #A
    glEnd()

    #Right part
    glBegin(GL_POLYGON)
    glVertex2f(1.5,2.5) #M
    glVertex2f(1.5,4) #J1
    glVertex2f(3,4) #K1
    glVertex2f(3,6) #I
    glVertex2f(4,4) #I
    glVertex2f(4,2) #K
    glVertex2f(3,2) #G1
    glVertex2f(3,2.5) #G1
    glVertex2f(1.5,2.5) #M
    glEnd()

    #Tail
    glColor3f(0.988,0.157,0.325)
    glBegin(GL_QUADS)
    glVertex2f(-0.2,5) #L1
    glVertex2f(0.2,5) #N1
    glVertex2f(0.2,3) #O1
    glVertex2f(-0.2,3) #M1

    glEnd()

   
    #Tangga dan Bendera
    if muncul_tangga == True:
        if delta_tangga > 1.7:
            penambah_detik = 0
            motion_tangga = 0
            y = rd.uniform(0.1, 0.3)
            glColor3f(0,1,1)
            glBegin(GL_TRIANGLES)#tiang
            glVertex2f(18,8) 
            glVertex2f(18.2,8) 
            glVertex2f(18.2,-20) 
            glEnd()


            glColor3f(1,0,0)
            glBegin(GL_POLYGON)
            glVertex2f(18.2,8)
            glVertex2f(19.4334835576925,7.6561960413823+y)
            glVertex2f(20.3404552675945,7.6295204028558+y)
            glVertex2f(21.3141160738128,7.9896415229639+y)
            glVertex2f(22.0877095910821,8.4297895586517+y)

            glVertex2f(22.941330023931,8.4297895586517-y)
            glVertex2f(24.1150581190983,7.8696011495946-y)
            glColor3f(1,1,1)
            glVertex2f(24,4.8-y)

            glVertex2f(24,4-y)
            glVertex2f(23.1700489039573,4.37948305611540-y)
            glVertex2f(22.4869041871991,4.4770751585094-y)
            glVertex2f(21.5500200042165,4.0281514874969-y)
            glVertex2f(20.5545805597974,3.5597093960056-y)

            glVertex2f(19.402993751548,3.4621172936116+y)
            glVertex2f(18.1163394283617, 3.9975682226151+y)
            glVertex2f(18.2,8)
            
            glVertex2f(18.2,-20) 
            glEnd()

        delta_tangga += motion_tangga
        glTranslated(delta_tangga-2,0,0)
        glColor3f(1,1,1)
        glBegin(GL_POLYGON)
        glVertex2f(4,3.8) 
        glVertex2f(6,3.8) 
        glVertex2f(8,0.8) 
        glVertex2f(8,0.3) 
        glVertex2f(7.3,0.3) 
        glVertex2f(5.6,0.3) 
        glVertex2f(4,3) 
        glEnd()

        glBegin(GL_LINES)
        glVertex2f(4,4) 
        glVertex2f(6,4) 
        glVertex2f(6,4) 
        glVertex2f(8,1) 
        glEnd()


    glPopMatrix()

def damage():
    #efek-efek kerusakan listrik
    global pos_x_pemain, pos_y_pemain, kecepatan_damage, damagenya, border_y
    glColor3f(1,1,1)          
    glPushMatrix()
    damagenya -= kecepatan_damage
    if damagenya < pos_y_pemain or border_y:
        damagenya = -300
    glTranslated(0,damagenya,0)
    glBegin(GL_LINES)

    for i in range(5):
        glVertex2f(pos_x_pemain+rd.randrange(-10,10),rd.randrange(pos_y_pemain+300,pos_y_pemain+500)) 
        glVertex2f(pos_x_pemain+rd.randrange(-30,30),pos_y_pemain+400) 
    
    glEnd()
    glPopMatrix()

def jet():
    global pos_y_pemain, pos_x_pemain, selesai
    glPushMatrix()
    glPointSize(0.4)
    glColor3f(0.961,0.,0.) #RGB
    glBegin(GL_POINTS)

    jarak_jet = 0

    if selesai:
        jarak_jet = 800
    
    for i in range(500):
        angka_random = rd.randrange(pos_y_pemain-300, pos_y_pemain-100)
        if angka_random == pos_y_pemain:
            angka_random = rd.randrange(pos_y_pemain-300, pos_y_pemain-100)
        y = rd.randrange(angka_random, pos_y_pemain)
        x = rd.randrange(pos_x_pemain-20, pos_x_pemain-10)
        glVertex2f(x,y+jarak_jet)
        glVertex2f(x+31,y+jarak_jet)
        if not y < -1000:
            x = x
        y -= 100

    glEnd()
    glPopMatrix()

def meteor():
    
    global pos_x_meteor,pos_y_meteor,kecepatan_meteor, pos_x_pemain, pos_y_pemain,pos_x_peluru, pos_y_peluru,border_y ,darah, hit_meteor, batu, counter_batu, kondisi_damage, kondisi_pecah
    glPushMatrix()
    
    pos_y_meteor -= kecepatan_meteor 
    #jika meteor melewati layar maka akan direset ke posisi awal (diatas)
    
    #Toggle animasi jika sudah direset ke atas, seperti animasi semula
    if pos_y_meteor < -border_y:
        pos_y_meteor = border_y
        pos_x_meteor = rd.randrange(pos_x_pemain-100, pos_x_pemain+50) 
        kondisi_pecah = False
        kondisi_damage = False

    if kondisi_pecah == True and pos_y_meteor > -border_y:
        kondisi_pecah = True

    
    #colision Meteor dengan Pemain
    offset = 50
    if pos_y_meteor in range (pos_y_pemain-offset, pos_y_pemain+offset) and  pos_x_meteor in range (pos_x_pemain-offset, pos_x_pemain+offset):
        darah -= hit_meteor
        kondisi_damage = True
        
    #colision Meteor dengan Peluru
    offset = 50
    if pos_y_meteor in range (pos_y_peluru-offset, pos_y_peluru+offset) and  pos_x_meteor in range (pos_x_peluru-offset, pos_x_peluru+offset):
        batu += counter_batu
        kondisi_pecah= True
        
    rgb = [0.6,0.341,0.043]
    glTranslated(pos_x_meteor, pos_y_meteor, 0)
    glScaled(5,10,0)
    glColor3f(float(rgb[0]),float(rgb[1]),float(rgb[2])) #RGB


    if kondisi_pecah == False:
    # glRotated(-270,0,0,0)
        glBegin(GL_POLYGON) 
        glVertex2f(-5.69,2.07)
        glVertex2f(-4.75,3.11)
        glVertex2f(-4.41,3.97)
        glVertex2f(-3.33,4.73)
        glVertex2f(-1.41,5.09)
        glVertex2f(1.09,4.35)
        glVertex2f(3.03,2.71)
        glVertex2f(2.69,1.39)

        glVertex2f(1.61,0.51)
        glVertex2f(0.29,-1.23)
        glVertex2f(-2,-2)
        glVertex2f(-4.61,-1.61)
        glVertex2f(-6.15,-1.07)
        glVertex2f(-6.39,0.61)
        glVertex2f(-5.69,2.07)
        glEnd()
    if kondisi_pecah == True:
        glRotatef(rd.randrange(0,45),0,0,0)
        glTranslated(rd.randrange(-5,5),0,0)
        glBegin(GL_POLYGON) 
        glVertex2f(-5.69,2.07)
        glVertex2f(-4.75,3.11)
        glVertex2f(-4.41,3.97)
        glVertex2f(-3.33,4.73)
        glVertex2f(-1.41,5.09)
        glVertex2f(1.09,4.35)
        glVertex2f(3.03,2.71)
        glVertex2f(2.69,1.39)
        glEnd()
        glRotatef(rd.randrange(0,45),0,0,0)
        glTranslated(rd.randrange(-5,5),0,0)
        glBegin(GL_POLYGON) 
        glVertex2f(1.61,0.51)
        glVertex2f(0.29,-1.23)
        glVertex2f(-2,-2)
        glVertex2f(-4.61,-1.61)
        glVertex2f(-6.15,-1.07)
        glVertex2f(-6.39,0.61)
        glVertex2f(-5.69,2.07)
        glEnd()
       
    glPopMatrix()
    
def bar_darah():
    global darah, hit_meteor, mati

    if darah < 60:
        hit_meteor = 0
        mati = True



    glPushMatrix()
    glTranslated(100,400, 0)
    glColor3f(0.016,0.761,0.027) #RGB
    glBegin(GL_QUADS) 
    glVertex2f(60,60)
    glVertex2f(1+darah,60)
    glVertex2f(1+darah,80)
    glVertex2f(60,80)
    glEnd()

    glBegin(GL_LINE_LOOP) 
    glVertex2f(60,60)
    glVertex2f(381,60)
    glVertex2f(381,80)
    glVertex2f(60,80)
    glEnd()
    
    glScaled(1,1.2,0)
    glTranslated(10,50,0)
    glBegin(GL_POLYGON)
    glVertex2f(20,10)
    glVertex2f(20,20)
    glVertex2f(30,20)
    glVertex2f(30,10)
    glVertex2f(40,10)
    glVertex2f(40,0)
    glVertex2f(30,0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(20,10)
    glVertex2f(10,10)
    glVertex2f(10,0)
    glVertex2f(20,0)
    glVertex2f(20,-10)
    glVertex2f(30,-10)
    glVertex2f(30,0)
    glEnd()


  

    glPopMatrix()

def bar_batu():
    global batu, counter_batu, jalan, selesai
    if batu > 320:
        jalan = False
        selesai = True
        counter_batu = 0
        
    
    glPushMatrix()
    glTranslated(100,300, 0)
    glColor3f(0.988,0.749,0.137) #RGB
    glBegin(GL_QUADS) 
    glVertex2f(60,60)
    glVertex2f(batu+60,60)
    glVertex2f(batu+60,80)
    glVertex2f(60,80)
    glEnd()

    glBegin(GL_LINE_LOOP) 
    glVertex2f(60,60)
    glVertex2f(381,60)
    glVertex2f(381,80)
    glVertex2f(60,80)
    glEnd()

    
    glTranslated(40, 60, 0)
    glScaled(2.5,5,0)
    glBegin(GL_POLYGON) 
    glVertex2f(-5.69,2.07)
    glVertex2f(-4.75,3.11)
    glVertex2f(-4.41,3.97)
    glVertex2f(-3.33,4.73)
    glVertex2f(-1.41,5.09)
    glVertex2f(1.09,4.35)
    glVertex2f(3.03,2.71)
    glVertex2f(2.69,1.39)

    glVertex2f(1.61,0.51)
    glVertex2f(0.29,-1.23)
    glVertex2f(-2,-2)
    glVertex2f(-4.61,-1.61)
    glVertex2f(-6.15,-1.07)
    glVertex2f(-6.39,0.61)
    glVertex2f(-5.69,2.07)
    glEnd()
    

    glPopMatrix()

def mars():
    glPushMatrix()
    glScaled(50,50,0)
    glTranslated(0,-5,0)
    glBegin(GL_POLYGON) 
    glColor3f(1.,0.667,0.231)
    glVertex2f(-12,2)
    glVertex2f(12,2)
    glColor3f(0.741,0.498,0.184)
    glVertex2f(12,-10)
    glColor3f(0.478,0.271,0.)
    glVertex2f(-12,-10)
    glEnd()

    
    glPopMatrix()

def tulis_json(value):
    penampung = [{'waktu':str(value)}]
    with open('waktuTerbaik.json','w') as berkas:
        json.dump(penampung, berkas, indent = 4)

def baca_json():
    penampung = [] 
    try:
        with open ('waktuTerbaik.json','r') as berkas:
                data = json.load(berkas)
                for i in data:
                    penampung.append(i)

    except:
        penampung = [{'waktu':'9999'}]
        with open('waktuTerbaik.json','w') as berkas:
            json.dump(penampung, berkas, indent = 4)

    waktu = int(penampung[0]['waktu'])
    return waktu

def waktu():
    global detik, penambah_detik
    glPushMatrix()
    detik += penambah_detik

    if penambah_detik == 0:
        if detik//1000 < baca_json():
            tulis_json(detik//1000)

    
    glTranslated(-450,260,0)
    glScaled(2,2,0)
    glColor3f(0.706,0.878,0.388)
    glBegin(GL_QUADS)
    glVertex2f(-10,80)
    glVertex2f(50,80)
    glVertex2f(50,110)
    glVertex2f(-10,110)
    glEnd()

    glColor3f(0.016,0.812,0.282)
    glBegin(GL_QUADS)
    glVertex2f(-10,80-40)
    glVertex2f(50,80-40)
    glVertex2f(50,110-40)
    glVertex2f(-10,110-40)
    glEnd()
    glColor3f(1,1,1)
    glRasterPos(30,90)
    for c in str(detik//1000):
        glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )

    glRasterPos(-4,90)
    for c in "TIME:":
        glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )

    glRasterPos(30,50)
    for c in str(baca_json()):
        glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )

    glRasterPos(-4,50)
    for c in "BEST:":
        glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )




    glPopMatrix()

def loading_bar():
    global loading, penambah_loading , jalan, mulai
    glPushMatrix()
    if loading:
        penambah_loading += 5

    if penambah_loading > 360:
        loading = False
        jalan   = True
        mulai   = False
    glScaled(2.5,2.5,0)
    glColor3f(0.573,0.706,0.988)
    glTranslated(-200,-200,0)
    glBegin(GL_QUADS)
    glVertex2f(20,20)
    glVertex2f(20+penambah_loading,20)
    glVertex2f(20+penambah_loading,30)
    glVertex2f(20,30)
    glEnd()
    glPopMatrix()
    
def mulai_menu():
    global jedag,jedug
    glPushMatrix()
    glPointSize(4)
    glColor3f(1.0, 1.0, 1.0) #RGB
    glBegin(GL_POINTS)
    y = 1000
    for i in range(jumlah_bintang):
        x = rd.randrange(-1000,1000)
        glVertex2f(x,y)
        if y != 1000:
            x = x
        y -= 100
    glEnd()
   
   
    glScaled(0.5,0.5,0)
    glTranslated(-700,-500,0)

    


    #FONT
    glColor3f( 1, 1, 1 )   #-> kalo mau diubah warna nya bisa
    # glScaled(0.5,0.5,0)
    glRasterPos(900,0)
    for c in "CARA BERMAIN":
        glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
    glRasterPos(900,-100)
    for c in "1. Gunakan Panah Untuk Menggerakan Roket":
        glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )
    glRasterPos(900,-170)
    for c in "2. Gunakan F5 Untuk Menembak":
        glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )

   

    #N
    glTranslated(0,rd.randrange(-jedag,jedug),0)
    glBegin(GL_LINE_LOOP) 
    glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
    glVertex2f(138.853673411388,658.0901797485591)
    glVertex2f(222.5429790339964,659.1495380475794)
    glVertex2f(314.7071510487676,499.1864348955054)
    glVertex2f(277.629610583055,668.6837627387627)
    glVertex2f(357.0814830095819,684.5741372240681)#I
    glVertex2f(370.8531408968466,451.5153114395893)
    glVertex2f(289.282551872279,434.5655786552636)
    glVertex2f(220.4242624359557,576.5195907239915)
    glVertex2f(220.4242624359557,418.6752041699582)
    glVertex2f(135.675598514327,405.9629045817139)
    glVertex2f(138.853673411388,658.0901797485591)
    glEnd()
    #E
    glTranslated(0,rd.randrange(-jedag,jedug),0)
    glBegin(GL_LINE_LOOP) 
    glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
    glVertex2f(395.2183817743148,651.734029954437)
    glVertex2f(400,400)
    glVertex2f(560.4782764214908,413.3784126748564)
    glVertex2f(556.2014252421901,452.963922322901)
    glVertex2f(479.2378130063854,445.3759605531738)
    glVertex2f(470.5658566981257,475.7278076320827)
    glVertex2f(521.2820193577376,477.9992689150982)
    glVertex2f(521.2820193577376,507.6613012876683)
    glVertex2f(465.1360295096585,511.8987344837497)
    glVertex2f(455.6018048184753,579.6976656210526)
    glVertex2f(523.4007359557783,563.8072911357473) 
    glVertex2f(518.1039444606764,639.0217303661926)
    glVertex2f(395.2183817743148,651.734029954437)
    glEnd()
    #B
    glTranslated(0,rd.randrange(-jedag,jedug),0)
    glBegin(GL_LINE_LOOP) 
    glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
    glVertex2f(581.665442401898,662.3276129446406)
    glVertex2f(673.8296144166692,679.2773457289662)
    glVertex2f(706.825933238541,635.5385500586459)
    glVertex2f(681.9912994349481,553.5265035444559)
    glVertex2f(649.4643735392009,539.442050258279)
    glVertex2f(699.8953377584686,524.6490223774875)
    glVertex2f(732.8156662888125,501.5470374439129)
    glVertex2f(731.0830174187945,438.0165788765826)
    glVertex2f(584.385413090595,421.267639799741)
    glEnd()
    #U
    glTranslated(0,rd.randrange(-jedag,jedug),0)
    glBegin(GL_LINE_LOOP) 
    glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
    glVertex2f(769.2012925591933,634.3834508119671)
    glVertex2f(809.427476691275,652.7933882534574)
    glVertex2f(798.0787737261618,528.1143201175238)
    glVertex2f(823.1991345785398,462.1088944297929)
    glVertex2f(869.8108997354356,468.465044223915)
    glVertex2f(882.5231993236798,546.8575583514215)
    glVertex2f(853.9205252501301,643.2591635622741)
    glVertex2f(880.4044827256391,655.9714631505184)
    glVertex2f(918.541381490372,570.1634409298694)
    glVertex2f(909.5458510306598,479.0226021336777)
    glVertex2f(887.8199908187817,423.97199566506)
    glVertex2f(830.6146426716823,412.3190543758361)
    glVertex2f(754.7625519757091,514.253129157379)
    glVertex2f(769.2012925591933,634.3834508119671)
    glEnd()
    #L
    glTranslated(0,rd.randrange(-jedag,jedug),0)
    glBegin(GL_LINE_LOOP) 
    glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
    glVertex2f(954.5595636570642,690.9302870181903)
    glVertex2f(1000,700)
    glVertex2f(1012.8242701031839,568.0447243318287)
    glVertex2f(1001.17132881396,469.5244025229354)
    glVertex2f(1100,500)
    glVertex2f(1109.2258753140366,462.1088944297929)
    glVertex2f(1016.0023450002451,429.2687871601618)
    glVertex2f(939.9619715094864,434.2191585278784)
    glVertex2f(967.3714006181323,564.5810774592426)
    glVertex2f(954.5595636570642,690.9302870181903)
    glEnd()
    #A
    glTranslated(0,rd.randrange(-jedag,jedug),0)
    glBegin(GL_LINE_LOOP) 
    glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
    glVertex2f(1137.8285493875862,655.9714631505184)
    glVertex2f(1218.6143716494896,679.931623907601)
    glVertex2f(1321.0975351181085,426.0907122631007)
    glVertex2f(1253.2560004564257,428.931752025767)
    glVertex2f(1221.6531110185192,558.3820491464223)
    glVertex2f(1184.4403145444821,550.0356332484826)
    glVertex2f(1177.0248064513396,422.9126373660396)
    glVertex2f(1133.5911161915049,414.4377709738768)
    glVertex2f(1137.8285493875862,655.9714631505184)
    glEnd()
     
   
    glPopMatrix()   

def game_over():
    glRasterPos(-50,0)
    for c in "GAME OVER":
        glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(c) )

def display():
    global  mulai, loading, jalan, selesai
    glClear(GL_COLOR_BUFFER_BIT)
    
    if mulai:
        mulai_menu()

    if loading:
        mulai_menu()
        loading_bar()


    if jalan:
        bintang()
        pemain()
        peluru()
        jet()
        if kondisi_damage:
            damage()
        meteor()
        bar_darah()
        bar_batu()
        waktu()

    if selesai:
        bintang()
        pemain()
        jet()
        mars()
        waktu()

    if mati:
        mulai = False
        loading = False
        jalan = False
        selesai = False
        bintang()
        game_over()
    
    glFlush()


def mouse(button, state, x, y):
    global jalan,mulai, loading
    if (button == GLUT_LEFT_BUTTON and state == GLUT_DOWN) and mulai == True:
        loading = True
        mulai = False
 

def input_keyboard(ch,x,y):
    global pos_x_pemain, pos_y_pemain, pos_x_peluru, pos_y_peluru, kecepatan_peluru, pos_x_peluru_sementara, pos_awal, kondisi_tembak

    if ch == GLUT_KEY_UP:
        pos_y_pemain += motion
    elif ch == GLUT_KEY_DOWN:
        pos_y_pemain -= motion
    elif ch == GLUT_KEY_RIGHT:
        pos_x_pemain += motion
    elif ch == GLUT_KEY_LEFT:
        pos_x_pemain -= motion
    elif ch == GLUT_KEY_F5:
        kondisi_tembak = not kondisi_tembak
        if kondisi_tembak == True:
            kecepatan_peluru = 50

        else:
            if pos_y_peluru > 1000 and kondisi_tembak == False:
                kecepatan_peluru = 0
       
    
    else:
        kecepatan_peluru = 0

def update(value):
    glutPostRedisplay()
    glutTimerFunc(25,update,0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(w,h)
    glutInitWindowPosition(0,0)
    glutCreateWindow("NEBULA - TO THE MARS")
    glutDisplayFunc(display)
    # glutKeyboardFunc(input_keyboard)
    glutMouseFunc(mouse)
    glutSpecialFunc(input_keyboard)
    glutTimerFunc(25, update, 0)
    init()
    glutMainLoop()

main()
