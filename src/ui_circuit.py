'''
Created on Jun 12, 2014

@author: keisano1
'''

from PyQt4 import QtGui, QtCore
from ui_IO import UIIO
from parameter_window import ParameterWindow

class UICircuit(QtGui.QGraphicsItem):
    '''
    classdocs
    '''


    def __init__(self, x, y, circuit_info, parent=None):
        '''
        Constructor
        '''
        super(UICircuit, self).__init__()
        self.setX(x) 
        self.setY(y)
        self.xsize = 140
        self.ysize = 100
        self.circuit_info = circuit_info
        if parent:
            self.name = circuit_info.circuit_name + str(parent.circuit_index)
        else:
            self.name = circuit_info.circuit_name
        self.dragged = False
        self.parameters = {"Name":self.name}
        self.inputs = []
        self.outputs = []
        self.addIO()
        
    def addIO(self):
        for name in self.circuit_info.inputs:
            new_input = UIIO(name, "in", self)
            self.inputs.append(new_input)
        for name in self.circuit_info.outputs:
            new_output = UIIO(name, "out", self)
            self.outputs.append(new_output)
        self.positionIO()
        
    def positionIO(self):
        extra = 30
        in_offset = (self.ysize+extra)/(len(self.inputs)+1)
        out_offset = (self.ysize+extra)/(len(self.outputs)+1)
        iny = in_offset-0.5*extra
        outy = out_offset-0.5*extra
        for inp in self.inputs:
            inp.setPos(-0.5*inp.xsize, iny-0.5*inp.ysize)
            iny += in_offset
        for outp in self.outputs:
            outp.setPos(self.xsize-0.5*outp.xsize, outy-0.5*outp.ysize)
            outy += out_offset
        self.update()
        
    def addContextActions(self, menu):
        remove = QtGui.QAction("Remove "+self.name, menu)
        QtCore.QObject.connect(remove, QtCore.SIGNAL("triggered()"), 
                               self.remove)
        
        menu.addAction(remove)

    def remove(self):
        self.scene().removeCircuit(self)
        
    def setParameters(self, parameters):
        for label, value in parameters.iteritems():
            if value or value == False:
                self.parameters[label] = value 
        if self.parameters.has_key("Name") and self.parameters["Name"]:
            self.name = self.parameters["Name"]

    def boundingRect(self):
        return QtCore.QRectF(0, 0, self.xsize, self.ysize)
    
    def paint(self, painter, options, widget):
        pen = QtGui.QPen(QtGui.QColor(0, 0, 0))
        pen.setWidth(2)
        painter.setBrush(QtGui.QColor(222, 244, 251))
        painter.setPen(pen)
        painter.drawRoundedRect(0, 0, self.xsize, self.ysize, 
                               0.07*self.xsize, 0.1*self.ysize)
        painter.drawText(0, 0, self.xsize, self.ysize, 
                        QtCore.Qt.AlignCenter, self.name)
        
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragged = True
        #super(UICircuit, self).mousePressEvent(event)
        
            
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragged = False
        super(UICircuit, self).mouseReleaseEvent(event)
        
        
    def mouseMoveEvent(self, event):
        if self.dragged:
            old_pos = self.pos()
            pos = event.scenePos()
            pos.setX(pos.x()-pos.x()%100)
            pos.setY(pos.y()-pos.y()%100)
            self.setPos(pos)
            for circuit in self.scene().circuits:
                if (self.collidesWithItem(circuit) and
                    circuit != self):
                    self.setPos(old_pos)
                    break
            self.scene().updateConnections()
            self.scene().update()
        super(UICircuit, self).mouseMoveEvent(event)
            
    def mouseDoubleClickEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.parameter_window = ParameterWindow(self)
            
        super(UICircuit, self).mouseDoubleClickEvent(event)    