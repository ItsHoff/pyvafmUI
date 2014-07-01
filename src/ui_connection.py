'''
Created on Jun 18, 2014

@author: keisano1
'''

from PyQt4 import QtGui, QtCore 

class UIConnection(QtGui.QGraphicsPathItem):
    '''
    classdocs
    '''


    def __init__(self, origin, mouse_pos, parent=None):
        '''
        Constructor
        '''
        
        self.input_ = None
        self.output = None
        self.start = origin.scenePos()+QtCore.QPointF(0.5*origin.xsize, 0.5*origin.ysize)
        self.end = mouse_pos
        if origin.io_type == "in":
            if origin.nConnections() >= 1:
                raise ValueError("Input can only have one connection.")
            else:
                self.input_ = origin
        else:
            self.output = origin
        super(UIConnection, self).__init__(parent)
        pen = QtGui.QPen(QtGui.QColor(0, 255, 0))
        pen.setWidth(2)
        self.setPen(pen)
        path = QtGui.QPainterPath(self.start)
        path.lineTo(self.end)
        self.setPath(path)
        self.setZValue(1)
        
    def addContextActions(self, menu):
        remove = QtGui.QAction("Remove connection from "+self.input_.name + " to "+ self.output.name, menu)
        QtCore.QObject.connect(remove, QtCore.SIGNAL("triggered()"), 
                               self.removeConnection)
        
        menu.addAction(remove)
        
    def removeConnection(self):
        self.scene().removeConnection(self)
        
    def addIO(self, io):
        if io.io_type == "in" and self.input_ == None and io.nConnections()<1:
            self.input_ = io
            print "connected " + self.input_.name + " and "+ self.output.name
        elif io.io_type == "out" and self.output == None:
            self.output = io
            print "connected " + self.input_.name + " and "+ self.output.name
        else:
            return False
        self.updatePath()
        return True
            
    def updateMousePos(self, scenePos):
        self.end = scenePos
        path = QtGui.QPainterPath(self.start)
        path.lineTo(self.end)
        self.setPath(path)
        
    def updatePath(self):
        self.start = self.input_.scenePos()+QtCore.QPointF(0.5*self.input_.xsize, 0.5*self.input_.ysize)
        self.end = self.output.scenePos()+QtCore.QPointF(0.5*self.output.xsize, 0.5*self.output.ysize)
        path = QtGui.QPainterPath(self.start)
        path.lineTo(self.end)
        self.setPath(path)

        
