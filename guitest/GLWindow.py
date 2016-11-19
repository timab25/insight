from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PyQt4.QtOpenGL import *
from PyQt4.QtCore import *
import numpy as np

class GLWindow(QGLWidget):

    def __init__(self, parent=None):
        QGLWidget.__init__(self, parent)
        self.setMinimumSize(640, 480)
        glutInit()
        self.x = 0
        self.y = 0
        self.z = -10

        self.robot_x = 0
        self.robot_y = 0
        self.robot_z = 0

        self.robot_roll = 0
        self.robot_pitch = 0
        self.robot_yaw = 0

        self.detections = np.empty()

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        print('here')
        glTranslated(self.x, self.y, self.z)

        glColor4f(0.0, 1.0, 1.0, 1.0)
        glBegin(GL_LINES)
        for i in range(-25,25):
            glVertex3f(i, 0.0, -25)
            glVertex3f(i, 0.0, 25)
            glVertex3f(-25, 0.0, i)
            glVertex3f(25, 0.0, i)
        glEnd()

        glPushMatrix()
        glTranslated(self.robot_x, self.robot_y, self.robot_z)
        glutSolidCube(1)
        glPopMatrix()

        glFlush()

        self.emit(SIGNAL('render'))

    def initializeGL(self):
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)

        glClearColor(0, 0, 0, 1)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)

        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LESS)

        glEnable(GL_LIGHT0)
        glEnable(GL_NORMALIZE)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_LIGHTING)

        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.0, 0.0, 0.0, 1.0])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
        glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
        glLightfv(GL_LIGHT0, GL_POSITION, [2.0, 5.0, 5.0, 0.0])

        glMaterialfv(GL_FRONT, GL_AMBIENT, [0.7, 0.7, 0.7, 1.0])
        glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.8, 0.8, 0.8, 1.0])
        glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
        glMaterialfv(GL_FRONT, GL_SHININESS, 100.0)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60.0,1.33,0.0001, 100000000.0)
        glMatrixMode(GL_MODELVIEW)

    def moveLeft(self, units):
        self.x = self.x + units
        self.update()

    def moveRight(self, units):
        self.x = self.x - units
        self.update()

    def moveForward(self, units):
        self.z = self.z + units
        self.update()

    def moveBack(self, units):
        self.z = self.z - units
        self.update()

    def moveUp(self, units):
        self.y = self.y + units
        self.update()

    def moveDown(self, units):
        self.y = self.y - units
        self.update()

    def updatePosition(self, x, y, z):
        self.robot_x = x
        self.robot_y = y
        self.robot_z = z
        self.update()

    def updatePose(self, roll, pitch, yaw):
        self.robot_roll = roll
        self.robot_pitch = pitch
        self.robot_yaw = yaw
        self.update()

    def clearDetections(self):
        self.detections = []
        self.update()

    def addDetection(self, bearing, range_m, r, g, b):
        self.detections.append([bearing, range_m, r, g, b])
        self.update()




