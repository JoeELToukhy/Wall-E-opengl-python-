from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def draw():
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor(1,0.5,0)

    glBegin(GL_POLYGON)

    glEnd()

    glBegin(GL_POLYGON)
    glVertex2d(0.4, 0.4)
    glVertex2d(-0.4, 0.4)
    glVertex2d(-0.4, -0.4)
    glVertex2d(0.4, -0.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2d(0.08, 0.7)
    glVertex2d(-0.08, 0.7)
    glVertex2d(-0.08, 0.4)
    glVertex2d(0.08, 0.4)
    glEnd()

    glColor(0.42,0.42,0.42)
    glBegin(GL_POLYGON)

    glVertex2d(0.3, -0.2)
    glVertex2d(0.5, -0.2)
    glVertex2d(0.5, -0.6)
    glVertex2d(0.3, -0.6)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2d(-0.3, -0.2)
    glVertex2d(-0.5, -0.2)
    glVertex2d(-0.5, -0.6)
    glVertex2d(-0.3, -0.6)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2d(0.3, 0.3)
    glVertex2d(0.5, 0.3)
    glVertex2d(0.5, 0.1)
    glVertex2d(0.3, 0.1)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2d(-0.3, 0.3)
    glVertex2d(-0.5, 0.3)
    glVertex2d(-0.5, 0.1)
    glVertex2d(-0.3, 0.1)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2d(-0.008, 0.54)
    glVertex2d(-0.25, 0.45)
    glVertex2d(-0.25, 0.67)
    glVertex2d(-0.008, 0.75)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2d(0.008, 0.54)
    glVertex2d(0.25, 0.45)
    glVertex2d(0.25, 0.67)
    glVertex2d(0.008, 0.75)
    glEnd()

    #eyes
    glColor(0.2, 0.4, 0.8)
    glBegin(GL_POLYGON)
    r = 0.06
    for theta in np.arange(0, 2*pi, 0.01):
        x=r*cos(theta)+0.13
        y=r*sin(theta)+0.60
        glVertex2d(x, y)
    glEnd()

    glBegin(GL_POLYGON)
    r = 0.06
    for theta in np.arange(0, 2*pi, 0.01):
        x = r*cos(theta)-0.13
        y = r*sin(theta)+0.60
        glVertex2d(x, y)
    glEnd()

    glColor(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2d(0.3, -0.3)
    glVertex2d(0.5, -0.3)
    glEnd()

    glBegin(GL_LINES)
    glVertex2d(0.3, -0.4)
    glVertex2d(0.5, -0.4)
    glEnd()

    glBegin(GL_LINES)
    glVertex2d(0.3, -0.5)
    glVertex2d(0.5, -0.5)
    glEnd()

    glBegin(GL_LINES)
    glVertex2d(-0.3, -0.3)
    glVertex2d(-0.5, -0.3)
    glEnd()

    glBegin(GL_LINES)
    glVertex2d(-0.3, -0.4)
    glVertex2d(-0.5, -0.4)
    glEnd()

    glBegin(GL_LINES)
    glVertex2d(-0.3, -0.5)
    glVertex2d(-0.5, -0.5)
    glEnd()


    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"first open gl program")
glutDisplayFunc(draw)
glutMainLoop()
