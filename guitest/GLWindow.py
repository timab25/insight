from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PyQt4.QtOpenGL import *
from PyQt4.QtCore import *
import RobotDetection_pb2
from model_loader import *
import math

class GLWindow(QGLWidget):

    def __init__(self, parent=None):
        QGLWidget.__init__(self, parent)
        self.setMinimumSize(640, 480)
        glutInit()
        self.x = 0
        self.y = 0
        self.z = -10

        self.robot_x = 0.0
        self.robot_y = 0.0
        self.robot_z = 0.0

        self.robot_roll = 0.0
        self.robot_pitch = 0.0
        self.robot_yaw = 0.0

        self.rotation_y = 0;
        self.rotation_x = 0;

        self.past_positions = []
        self.detections = []

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glRotated(self.rotation_y, 0, 1, 0)
        glRotated(self.rotation_x, 1, 0, 0)
        glTranslated(self.x, self.y, self.z)

        glColor4f(0.0, 1.0, 1.0, 1.0)
        glLineWidth(1.0)
        glBegin(GL_LINES)
        for i in range(-25, 25):
            glVertex3f(i, 0.0, -25)
            glVertex3f(i, 0.0, 25)
            glVertex3f(-25, 0.0, i)
            glVertex3f(25, 0.0, i)
        glEnd()

        glPushMatrix()
        glRotated(self.robot_roll, 0, 0, 1)
        glRotated(self.robot_pitch, 1, 0, 0)
        glRotated(self.robot_yaw, 0, 1, 0)
        glTranslated(self.robot_x, self.robot_y, -self.robot_z)
        glutSolidCube(0.5)
        glPopMatrix()

        glPointSize(8.0)
        glBegin(GL_POINTS)
        for i in range(len(self.detections)):
            currPoint = self.detections[i]
            glColor3f(currPoint.red, currPoint.green, currPoint.blue)
            point_x = currPoint.robot_x + currPoint.range*math.sin(currPoint.bearing*0.0174533)
            point_y = currPoint.robot_y + currPoint.range*math.cos(currPoint.bearing*0.0174533)
            glVertex3f(point_x, 0, -point_y)
        glEnd()

        glColor4f(1.0, 1.0, 1.0, 1.0)
        glBegin(GL_LINE_STRIP)
        for i in range(len(self.past_positions)):
            pos = self.past_positions[i]
            glVertex3f(pos[0], pos[1], -pos[2])
        glEnd()

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
        self.past_positions.append([x, y, z])
        self.update()

    def updatePose(self, roll, pitch, yaw):
        self.robot_roll = roll
        self.robot_pitch = pitch
        self.robot_yaw = yaw
        self.update()

    def clearDetections(self):
        self.detections = []
        self.update()

    def addDetection(self, detect):
        self.detections.append(detect)
        self.update()

    def rotateLeft(self):
        self.rotation_y -= 1
        if self.rotation_y < 0:
            self.rotation_y = 360
        elif self.rotation_y > 360:
            self.rotation_y = 0
        self.update()

    def rotateRight(self):
        self.rotation_y += 1
        if self.rotation_y < 0:
            self.rotation_y = 360
        elif self.rotation_y > 360:
            self.rotation_y = 0
        self.update()

    def resetRotation(self):
        self.rotation_y = 0
        self.rotation_x = 0
        self.update()

    def rotateUp(self):
        self.rotation_x += 1
        if self.rotation_x < 0:
            self.rotation_x = 360
        elif self.rotation_x > 360:
            self.rotation_x = 0
        self.update()

    def rotateDown(self):
        self.rotation_x -= 1
        if self.rotation_x < 0:
            self.rotation_x = 360
        elif self.rotation_x > 360:
            self.rotation_x = 0
        self.update()



