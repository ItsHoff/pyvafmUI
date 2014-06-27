'''
Created on Jun 13, 2014

@author: keisano1
'''

from PyQt4 import QtGui, QtCore

class MyScrollArea(QtGui.QScrollArea):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(MyScrollArea, self).__init__()
        self.mouse_pos = None
        self.panning = False
        
    def wheelEvent(self, event):
        factor = 1.1
        pos = event.pos()
        if event.delta() < 0:
            factor = 1.0/factor
        self.scale(factor, event)
        
    def scale(self, factor, event):
        print event.pos().x(), event.pos().y()
    
    def mousePressEvent(self, event):
        event.accept()
        if event.button() == QtCore.Qt.RightButton:            
            self.panning = True
            self.mouse_pos = event.pos()
            
    def mouseReleaseEvent(self, event):
        self.panning = False
        self.mouse_pos = None
        
    def mouseMoveEvent(self, event):
        if self.panning:
            diff = event.pos() - self.mouse_pos
            self.mouse_pos = event.pos()
            self.verticalScrollBar().setValue(self.verticalScrollBar().value()-
                                              diff.y())
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value()-
                                              diff.x())
    
        