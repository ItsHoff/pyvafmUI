'''
Created on Jun 16, 2014

@author: keisano1
'''

from PyQt4 import QtGui, QtCore


class MachineView(QtGui.QGraphicsView):
    """Graphics view that is used to show the contents of the
    machine_widget scene.
    """

    def __init__(self):
        """Call super and set the default flags and parameters."""
        super(MachineView, self).__init__()
        self.setAcceptDrops(True)
        self.panning = False
        self.mouse_pos = None
        self.scale_factor = 1
        self.min_factor = 0.3
        self.max_factor = 2.5

    def wheelEvent(self, event):
        """Scale the view when wheel is scrolled."""
        self.setTransformationAnchor(self.AnchorUnderMouse)
        factor = 1.1
        if event.delta() < 0:
            factor = 1.0/factor
        if (self.scale_factor*factor > self.min_factor and
           self.scale_factor*factor < self.max_factor):
            self.scale_factor *= factor
            self.scale(factor, factor)

    def mousePressEvent(self, event):
        """Start panning the scene if middle mouse button is pressed."""
        super(MachineView, self).mousePressEvent(event)
        if event.button() == QtCore.Qt.MiddleButton:
            self.panning = True
            self.mouse_pos = event.pos()

    def mouseReleaseEvent(self, event):
        """Stop panning if middle mouse button is released."""
        super(MachineView, self).mouseReleaseEvent(event)
        self.panning = False
        self.mouse_pos = None

    def mouseMoveEvent(self, event):
        """If user is panning, move the scene based on the
        movement of the mouse.
        """
        super(MachineView, self).mouseMoveEvent(event)
        if self.panning:
            diff = event.pos() - self.mouse_pos
            self.mouse_pos = event.pos()
            self.verticalScrollBar().setValue(
                self.verticalScrollBar().value() - diff.y())
            self.horizontalScrollBar().setValue(
                self.horizontalScrollBar().value() - diff.x())
            self.scene().update()
