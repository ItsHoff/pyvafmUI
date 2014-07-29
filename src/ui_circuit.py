'''
Created on Jun 12, 2014

@author: keisano1
'''

from PyQt4 import QtGui, QtCore
from ui_IO import UIIO
from parameter_window import ParameterWindow


class UICircuit(QtGui.QGraphicsItem):

    def __init__(self, x, y, circuit_info, parent=None):
        """Create a circuit defined by the circuit_info and
        place it into the at (x, y)
        """
        super(UICircuit, self).__init__()
        self.setX(x)
        self.setY(y)
        # self.setFlag(self.ItemIsMovable, True)
        # self.setFlag(self.ItemSendsScenePositionChanges, True)
        self.xsize = 130
        self.ysize = 100
        self.circuit_info = circuit_info
        self.parameter_window = None
        self.save_state = None
        if parent:
            self.name = circuit_info.circuit_type + str(parent.circuit_index)
        else:
            self.name = circuit_info.circuit_type
        self.dragged = False
        self.parameters = {"Name": self.name}
        self.inputs = []
        self.outputs = []

    def addIO(self):
        """Add inputs and outputs defined in circuit info
        into the scene.
        """
        for name in self.circuit_info.inputs:
            new_input = UIIO(name, "in", self)
            self.inputs.append(new_input)
        for name in self.circuit_info.outputs:
            new_output = UIIO(name, "out", self)
            self.outputs.append(new_output)
        self.positionIO()

    def addLoadedIO(self, save_state):
        io = UIIO(save_state.name, save_state.io_type, self)
        save_state.loaded_item = io
        if save_state.io_type == "in":
            self.inputs.append(io)
        else:
            self.outputs.append(io)

    def positionIO(self):
        """Position the circuits inputs and outputs such that
        they're evenly spaced, inputs on left and outputs on right.
        """
        extra = 25
        io_max = max(len(self.inputs), len(self.outputs))
        self.ysize = (io_max/6 + 1)*100
        in_offset = round(self.ysize+extra)/(len(self.inputs)+1)
        out_offset = round(self.ysize+extra)/(len(self.outputs)+1)
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
        """Add circuit specific context actions into the menu."""
        remove = QtGui.QAction("Remove "+self.name, menu)
        QtCore.QObject.connect(remove, QtCore.SIGNAL("triggered()"),
                               self.remove)

        menu.addAction(remove)

    def remove(self):
        """Call the scene to remove the circuit."""
        self.scene().removeCircuit(self)

    def setParameters(self, parameters):
        """Save the parameters given by parameter window."""
        for label, value in parameters.iteritems():
            if value is not None and value != "":
                self.parameters[label] = value
        if "Name" in self.parameters:
            self.name = self.parameters["Name"]
            self.parameter_window.setWindowTitle(self.name + " parameters")

    def getSaveState(self):
        """Return the current state of the circuit without the Qt bindings
        for saving.
        """
        if self.save_state is None:
            self.save_state = SaveCircuit(self)
        else:
            self.save_state.update(self)
        return self.save_state

    def loadSaveState(self, save_state):
        self.setX(save_state.x)
        self.setY(save_state.y)
        self.circuit_info = save_state.circuit_info
        self.name = save_state.name
        self.parameters = save_state.parameters
        for input_ in save_state.inputs:
            self.addLoadedIO(input_)
        for output in save_state.outputs:
            self.addLoadedIO(output)
        self.positionIO()

    def boundingRect(self):
        """Return the bounding rectangle of the circuit.
        Required by the scene.
        """
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
        """If left mouse button is pressed down start dragging
        the circuit.
        """
        if event.button() == QtCore.Qt.LeftButton:
            self.dragged = True
        # super(UICircuit, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        """End drag when mouse is released."""
        if event.button() == QtCore.Qt.LeftButton:
            self.dragged = False
            self.ensureVisible()
            self.scene().updateSceneRect()
        super(UICircuit, self).mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        """If circuit is being dragged try to set the circuits
        positions to the mouse position. Circuit will be
        snapping to 100x100 grid.
        """
        if self.dragged:
            old_pos = self.pos()
            pos = event.scenePos()
            pos.setX(pos.x() - pos.x() % 100)
            pos.setY(pos.y() - pos.y() % 100)
            self.setPos(pos)
            # If new position collides with other circuit
            # return to old position.
            for circuit in self.scene().circuits:
                if (self.collidesWithItem(circuit) and
                   circuit != self):
                    self.setPos(old_pos)
                    break
            # Update the connections since some of them might
            # have to be moved with the circuit.
            self.scene().updateConnections()
            self.scene().updateMovingSceneRect()
            self.scene().views()[0].autoScroll(event.scenePos())
            self.scene().update()
        # super(UICircuit, self).mouseMoveEvent(event)

    def mouseDoubleClickEvent(self, event):
        """Open the parameter window when circuit is double
        clicked.
        """
        if event.button() == QtCore.Qt.LeftButton:
            if self.parameter_window is None:
                self.parameter_window = ParameterWindow(self)
                self.parameter_window.showWindow()
            else:
                self.parameter_window.show()
                self.parameter_window.showWindow()
        # super(UICircuit, self).mouseDoubleClickEvent(event)


class SaveCircuit(object):
    """Container for UICircuit state without Qt bindings. Used for saving."""

    def __init__(self, circuit):
        pos = circuit.pos()
        self.x = pos.x()
        self.y = pos.y()
        self.circuit_info = circuit.circuit_info
        self.name = circuit.name
        self.parameters = circuit.parameters
        self.inputs = []
        for input_ in circuit.inputs:
            self.inputs.append(input_.getSaveState())
        self.outputs = []
        for output_ in circuit.outputs:
            self.outputs.append(output_.getSaveState())
        self.loaded_item = None         # Do not set this before saving

    def update(self, circuit):
        self.__init__(circuit)
