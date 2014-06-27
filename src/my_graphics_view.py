'''
Created on Jun 16, 2014

@author: keisano1
'''

from PyQt4 import QtGui, QtCore
    
class MyGraphicsView(QtGui.QGraphicsView):
    '''
    classdocs
    '''


    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(MyGraphicsView, self).__init__()
        self.setAcceptDrops(True)
        self.panning = False
        self.mouse_pos = None
        self.scale_factor = 1
        self.min_factor = 0.3
        self.max_factor = 2.5
        
    def wheelEvent(self, event):
        self.setTransformationAnchor(self.AnchorUnderMouse)
        factor = 1.1
        if event.delta() < 0:
            factor = 1.0/factor
        if (self.scale_factor*factor > self.min_factor and 
            self.scale_factor*factor < self.max_factor):
            self.scale_factor *= factor
            self.scale(factor, factor)
        
    def mousePressEvent(self, event):
        super(MyGraphicsView, self).mousePressEvent(event)
        if event.button() == QtCore.Qt.MiddleButton:            
            self.panning = True
            self.mouse_pos = event.pos()
        
            
    def mouseReleaseEvent(self, event):
        super(MyGraphicsView, self).mouseReleaseEvent(event)
        self.panning = False
        self.mouse_pos = None
        
        
    def mouseMoveEvent(self, event):
        super(MyGraphicsView, self).mouseMoveEvent(event)
        if self.panning:
            diff = event.pos() - self.mouse_pos
            self.mouse_pos = event.pos()
            self.verticalScrollBar().setValue(self.verticalScrollBar().value()-
                                              diff.y())
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value()-
                                              diff.x())
            self.scene().update()
            
    
        