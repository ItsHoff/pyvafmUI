'''
Created on Jun 6, 2014

@author: keisano1
'''

from PyQt4 import QtGui, QtCore
from ui_circuit import UICircuit
from ui_IO import UIIO
from ui_connection import UIConnection
import circuits
import random

class MachineWidget(QtGui.QGraphicsScene):
    '''
    classdocs
    '''


    def __init__(self, tree_widget, parent=None):
        '''
        Constructor
        '''
        super(MachineWidget, self).__init__(parent)
        self.tree_widget = tree_widget
        self.xsize = 1000
        self.ysize = 1000
        self.max_size = 2000
        self.circuits = []
        self.connections = []
        self.circuit_index = 1
        """self.scale_factor = 0.5
        self.max_factor = 3
        self.min_factor = 0.25"""
        self.font_size = 15
        self.new_connection = None
        self.add_circuits = False
        self.initWidget()
        
    def initWidget(self):
        self.addCircuits()
        self.update()
        
    def addCircuits(self):
        self.addCircuit("Scanner", 300, 500)
        self.addCircuit("3d Linear Interpolation", 500, 500)
        self.addCircuit("Output", 700, 500)
        """for i in range(1, 10):
            x = random.randint(0, self.xsize)
            y = random.randint(0, self.ysize)
            circuit = UICircuit(x - x%100, y -y%100, random.choice(circuits.circuits.values()), self)
            self.circuits.append(circuit)
            self.addItem(circuit)
            self.circuit_index += 1"""
        
    def addCircuit(self, name, x, y):
        circuit = UICircuit(x - x%100, y - y%100, circuits.circuits[name], self)
        self.circuits.append(circuit)
        
        self.addItem(circuit)
        self.circuit_index += 1
        self.update()
        
    def addDroppedCircuit(self, dropped, pos):
        name = str(dropped.text(0))
        self.addCircuit(name, pos.x(), pos.y())
        
    def addClickedCircuit(self, pos):
        item = self.tree_widget.currentItem()
        if item == None:
            return
        name = str(item.text(0))
        if item.parent():
            self.addCircuit(name, pos.x(), pos.y())
            
    def createNewConnection(self, origin, mouse_pos):
        try:
            self.new_connection = UIConnection(origin, mouse_pos)
        except ValueError as e:
            print e.message
            return
        self.views()[0].setMouseTracking(True)
        self.addItem(self.new_connection)
            
    def addConnection(self):
        self.connections.append(self.new_connection)
        self.new_connection = None
        self.views()[0].setMouseTracking(False)
        
    def deleteNewConnection(self):
        if self.new_connection != None:
            self.removeItem(self.new_connection)
            self.new_connection = None
            self.views()[0].setMouseTracking(False)
        
    def updateConnections(self):
        for connection in self.connections:
            connection.updatePath()
            
    def ioAt(self, pos):
        items = self.items(pos)
        for item in items:
            if isinstance(item, UIIO):
                return True
        return False
    
    def addContextActions(self, menu):
        clear_all = QtGui.QAction("Clear All", menu)
        QtCore.QObject.connect(clear_all, QtCore.SIGNAL("triggered()"), self.clearAll)
        
        clear_connections = QtGui.QAction("Clear Connections", menu)
        QtCore.QObject.connect(clear_connections, QtCore.SIGNAL("triggered()"), self.removeConnections)
        
        menu.addAction(clear_connections)
        menu.addAction(clear_all)
        
    
    def clearAll(self):
        self.connections = []
        self.circuits = []
        self.clear()
        self.update()
        
        
    def removeConnections(self):
        for connection in self.connections:
            self.removeItem(connection)
        self.connections = []
        self.update()
        
    def removeConnectionsFrom(self, IO):
        for connection in self.connections[:]:
            if connection.input == IO or connection.output == IO:
                self.connections.remove(connection)
                self.removeItem(connection)
        self.update()
        
    def removeConnection(self, connection):
        self.connections.remove(connection)
        self.removeItem(connection)
                
    def removeCircuit(self, circuit):
        for inp in circuit.inputs:
            self.removeConnectionsFrom(inp)
            self.removeItem(inp)
        for outp in circuit.outputs:
            self.removeConnectionsFrom(outp)
            self.removeItem(outp)
        self.circuits.remove(circuit)
        self.removeItem(circuit)
        self.update()
        
    """def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawBackground(qp)
        self.drawGrid(qp)
        self.drawCircuits(qp)
        qp.end()"""
        
    def drawBackground(self, qp, rect):
        qp.setPen(QtGui.QColor(255,255,255))
        qp.setBrush(QtGui.QColor(255, 255, 255))
        qp.drawRect(rect)
        self.drawGrid(qp, rect)
        
    def drawGrid(self, qp, rect):
        tl = rect.topLeft()
        br = rect.bottomRight()
        width = rect.width()
        height = rect.height()
        if width < 0.5*self.xsize:
            width = 0.5*self.xsize
        if height < 0.5*self.ysize:
            height = 0.5*self.ysize
        solid_pen = QtGui.QPen(QtGui.QColor(0,0,0), 4, QtCore.Qt.SolidLine)
        dashed_pen = QtGui.QPen(QtGui.QColor(150,150,150), 1, QtCore.Qt.SolidLine)
        qp.setPen(dashed_pen)
        for x in range(int(tl.x() - tl.x()%100), int(br.x() - br.x()%100 + 100), 100):
            for y in range(int(tl.y()- tl.y()%100), int(br.y()- br.y()%100+100), 100):
                qp.drawLine(int(tl.x()), int(y), int(br.x()), int(y))
                qp.drawLine(int(x), int(tl.y()), int(x), int(br.y()))
                qp.drawLine(int(tl.x()), int(-y+self.ysize), int(br.x()), int(-y+self.ysize))
                qp.drawLine(int(-x+self.xsize), int(tl.y()), int(-x+self.xsize), int(br.y()))
        qp.setPen(solid_pen)
        qp.drawLine(int(0.5*self.xsize), int(tl.y()), int(0.5*self.xsize), int(br.y()))
        qp.drawLine(int(tl.x()), int(0.5*self.ysize), int(br.x()), int(0.5*self.ysize)) 
    
    def drawCircuits(self, qp):
        
        pen = QtGui.QPen(QtGui.QColor(0, 0, 0))
        pen.setWidth(2)
        qp.setBrush(QtGui.QColor(50, 242, 255))
        qp.setPen(pen)
        qp.setFont(QtGui.QFont("", self.font_size))
        for circuit in self.circuits:
            qp.translate(-0.5*circuit.xsize, -0.5*circuit.ysize)
            qp.drawRoundedRect(circuit.x, circuit.y, circuit.xsize, circuit.ysize, 
                               0.15*circuit.xsize, 0.2*circuit.ysize)
            qp.drawText(circuit.x, circuit.y, circuit.xsize, circuit.ysize, 
                        QtCore.Qt.AlignCenter, circuit.name)
            qp.translate(0.5*circuit.xsize, 0.5*circuit.ysize)
            
            
    def dragEnterEvent(self, event):
        print "drag enter"
        event.accept()
        
        
            
    def dragMoveEvent(self, event):
        event.accept()
        
    def dropEvent(self, event):
        event.accept()
        dropped_item = event.source().currentItem()
        self.addDroppedCircuit(dropped_item, event.scenePos())
        
    def mousePressEvent(self, event):
        if self.add_circuits:
            event.accept()
            self.addClickedCircuit(event.scenePos())
        else:
            super(MachineWidget, self).mousePressEvent(event)
            if (self.new_connection != None and 
                not self.ioAt(event.scenePos())):
                self.deleteNewConnection()
                print "destroyed connection"
              
    def mouseMoveEvent(self, event):
        super(MachineWidget, self).mouseMoveEvent(event)
        if self.new_connection != None:
            self.new_connection.updateMousePos(event.scenePos())
            self.update()
                
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Control:
            self.add_circuits = True
            
    def keyReleaseEvent(self, event):
        if event.key() == QtCore.Qt.Key_Control:
            self.add_circuits = False
            
    def contextMenuEvent(self, event):
        self.deleteNewConnection()
        menu = QtGui.QMenu()
        
        for item in self.items(event.scenePos()):
            item.addContextActions(menu)
        self.addContextActions(menu)
        
        menu.exec_(event.screenPos())
            
    """def mouseReleaseEvent(self, event):
        super(MachineWidget, self).mouseReleaseEvent(event) 
        if event.button() == QtCore.Qt.LeftButton:
            self.dragged_object = None
        else:
            event.ignore()
        
    def mouseMoveEvent(self, event):
        super(MachineWidget, self).mouseMoveEvent(event) 
        if self.dragged_object:
            event.accept()
            pos = event.pos()
            x = pos.x()/self.scale_factor - 0.5*self.xsize
            y = pos.y()/self.scale_factor - 0.5*self.ysize
            self.dragged_object.x = x - x%100
            self.dragged_object.y = y - y%100
            self.update()
        else:
            event.ignore()
            
    def mouseDoubleClickEvent(self, event):
        super(MachineWidget, self).mouseDoubleClickEvent(event) 
        if event.button() == QtCore.Qt.LeftButton:
            clicked = self.itemAt(event.pos())
            print event.pos().x(), event.pos().y()
            if clicked:
                print "open param window for " + clicked.name
            else:
                print "Double clicked None" """
                
            
    """def objectAtPos(self, x, y):
        for circuit in self.circuits:
            if (circuit.x -0.5*circuit.xsize<x and
                circuit.x +0.5*circuit.xsize>x and
                circuit.y -0.5*circuit.ysize<y and
                circuit.y +0.5*circuit.ysize>y):
                return circuit"""
              
            
    """def wheelEvent(self, event):
        factor = 1.1
        pos = event.pos()
        if event.delta() < 0:
            factor = 1.0/factor
        self.(factor)"""
        
    
    def scale(self, factor):
        if factor < 1:
            if (self.xsize /factor < self.max_size and 
                self.ysize/factor < self.max_size):
                self.xsize /= factor
                self.ysize /= factor
            else:
                self.xsize = self.max_size
                self.ysize = self.max_size
        self.setSceneRect(0, 0, self.xsize, self.ysize)
        self.update()
        
    """def widgetPosToNormal(self, pos):
        x = pos.x()/self.scale_factor - 0.5*self.xsize
        y = pos.y()/self.scale_factor - 0.5*self.ysize
        return x, y"""
            
    """def drawRect(self, qp):
        qp.setBrush(QtGui.QColor(0, 0, 0))
        qp.drawRect(0, 0, 1000, 1000)
        qp.setBrush(QtGui.QColor(0, 255, 0))
        qp.drawRect(100, 100, 800, 800)
        qp.setBrush(QtGui.QColor(255, 0, 0))
        qp.drawRect(200, 200, 600, 600)
        qp.setBrush(QtGui.QColor(0, 0, 255))
        qp.drawRect(300, 300, 400, 400)
        qp.setBrush(QtGui.QColor(255, 255, 255))
        qp.drawRect(400, 400, 200, 200)"""
        
        