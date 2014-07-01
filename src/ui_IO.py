'''
Created on Jun 17, 2014

@author: keisano1
'''

from PyQt4 import QtGui, QtCore
from ui_connection import UIConnection

class UIIO(QtGui.QGraphicsItem):
    '''
    classdocs
    '''


    def __init__(self, name, io_type, parent):
        '''
        Constructor
        '''
        self.name = name
        self.circuit = parent
        self.xsize = 18
        self.ysize = 18
        self.io_type = io_type
        self.drag = False 
        super(UIIO, self).__init__(parent)
        
    def nConnections(self):
        n = 0
        for connection in self.scene().connections:
            if connection.input_ == self or connection.output == self:
                n += 1
        return n
        
    def addContextActions(self, menu):
        remove = QtGui.QAction("Remove all connections from "+self.name, menu)
        QtCore.QObject.connect(remove, QtCore.SIGNAL("triggered()"), 
                               self.removeConnections)
        
        menu.addAction(remove)
        
    def removeConnections(self):
        self.scene().removeConnectionsFrom(self)
        
    def boundingRect(self):
        return QtCore.QRectF(0, 0, self.xsize, self.ysize)
    
    def paint(self, painter, options, widget):
        pen = QtGui.QPen(QtGui.QColor(0, 0, 0))
        pen.setWidth(1)
        painter.setPen(pen)
        painter.setFont(QtGui.QFont("", 6))
        if  self.io_type == "in":
            painter.setBrush(QtGui.QColor(12, 169, 255))
        else:
            painter.setBrush(QtGui.QColor(255, 62, 66))
        painter.drawRect(0, 0, self.xsize, self.ysize)
        if self.io_type == "in":
            painter.drawText(-self.xsize-4, -1, self.name)
        else:
            painter.drawText(self.xsize+1, -1, self.name)
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawPoint(0.5*self.xsize, 0.5*self.ysize)
        
    def mousePressEvent(self, event):
        if (event.button() == QtCore.Qt.LeftButton and
            self.contains(event.pos())):               #otherwise context menu does weird stuff
            if self.scene().new_connection == None:
                self.scene().createNewConnection(self, event.scenePos())
            else:
                if self.scene().new_connection.addIO(self):
                    self.scene().addConnection()
                else:
                    self.scene().deleteNewConnection()
                    
                    
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drag = False
        
    def dropEvent(self, event):
        data = event.mimeData()
        print data.text()