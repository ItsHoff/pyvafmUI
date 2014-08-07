'''
Created on Jun 12, 2014

@author: keisano1
'''

from PyQt4 import QtGui, QtCore
from ui_IO import UIIO
from parameter_window import ParameterWindow


class UICircuit(QtGui.QGraphicsItem):
    """Graphics item that represents the circuits of the machine."""

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
        self.parameters = circuit_info.default_values.copy()
        self.parameters["Name"] = self.name
        self.ios = []

    def addIO(self):
        """Add inputs and outputs defined in circuit info
        into the scene.
        """
        info_ios = self.circuit_info.inputs + self.circuit_info.outputs
        for name in info_ios:
            if name in self.circuit_info.inputs:
                io_type = "in"
            else:
                io_type = "out"
            number_index = name.find("#")
            if number_index != -1:
                parameter = name[number_index+1:]
                n_io = self.parameters[parameter]
                self.changeNofIO(name, 0, n_io)
            else:
                new_input = UIIO(name, io_type, self)
                self.ios.append(new_input)
        self.positionIO()

    def changeNofIO(self, name, old_n, new_n):
        """Change the number of ios matching name from old to new."""
        if name in self.circuit_info.inputs:
            io_type = "in"
        else:
            io_type = "out"
        number_index = name.find("#")
        if new_n > old_n:
            for i in range(old_n, new_n):
                new_io = UIIO(name[:number_index]+str(i+1), io_type, self)
                insert_index = None
                io_name = name[:number_index]+str(i)
                io = self.findMatchingIO(io_name)
                if io is not None:
                    insert_index = self.ios.index(io)+1
                    self.ios.insert(insert_index, new_io)
                else:
                    self.ios.append(new_io)
        elif new_n < old_n:
            for i in range(new_n, old_n):
                io_name = name[:number_index]+str(i+1)
                io_to_remove = self.findMatchingIO(io_name)
                self.removeIO(io_to_remove)

    def findMatchingIO(self, name):
        """Find IO matching the name."""
        for io in self.ios:
            if io.name == name:
                return io
        return None

    def updateIO(self, new_parameters):
        """Update the amount of io if the relevant parameters
        have been changed.
        """
        info_ios = self.circuit_info.inputs + self.circuit_info.outputs
        for name in info_ios:
            number_index = name.find("#")
            if number_index != -1:
                parameter = name[number_index+1:]
                if parameter in new_parameters:
                    new_n = int(new_parameters[parameter])
                    old_n = int(self.parameters[parameter])
                    if new_n == old_n:
                        continue
                    else:
                        self.changeNofIO(name, old_n, new_n)
        self.positionIO()
        self.scene().updateSceneRect()
        self.scene().updateConnections()

    def removeIO(self, io_to_remove):
        """Remove io_to_remove from the circuit."""
        self.scene().removeConnectionsFrom(io_to_remove)
        self.ios.remove(io_to_remove)
        parameter_name = "INPUT:"+io_to_remove.name
        if parameter_name in self.parameters:
            del self.parameters[parameter_name]
        self.scene().removeItem(io_to_remove)

    def addLoadedIO(self, save_state):
        """Add io matching the save state to the circuit."""
        io = UIIO(save_state.name, save_state.io_type, self)
        save_state.loaded_item = io
        io.save_state = save_state
        self.ios.append(io)

    def positionIO(self):
        """Position the circuits inputs and outputs such that
        they're evenly spaced, inputs on left and outputs on right.
        """
        extra = 25
        inputs = []
        outputs = []
        for io in self.ios:
            if io.io_type == "in":
                inputs.append(io)
            else:
                outputs.append(io)
        io_max = max(len(inputs), len(outputs))
        self.ysize = (io_max/6 + 1)*100
        in_offset = round(self.ysize+extra)/(len(inputs)+1)
        out_offset = round(self.ysize+extra)/(len(outputs)+1)
        iny = in_offset-0.5*extra
        outy = out_offset-0.5*extra
        for inp in inputs:
            inp.setPos(-0.5*inp.xsize, iny-0.5*inp.ysize)
            iny += in_offset
        for outp in outputs:
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
        status_bar = self.scene().parent().window().statusBar()
        self.updateIO(parameters)
        for label, value in parameters.iteritems():
            if value is not None and value != "" and value != []:
                self.parameters[label] = value
            elif label != "Name" and label in self.parameters:
                del self.parameters[label]
        if self.name != self.parameters["Name"]:
            self.name = self.parameters["Name"]
            self.parameter_window.setWindowTitle(self.name + " parameters")
        status_bar.showMessage("Set parameters for %s"%self.name, 2000)

    def updateParameters(self):
        """Update the parameters of the circuit to match the current state."""
        if self.parameter_window is not None:
            self.parameter_window.setParameters()

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
        """Load the state given in save_state."""
        save_state.loaded_item = self
        self.save_state = save_state
        self.setX(save_state.x)
        self.setY(save_state.y)
        self.circuit_info = save_state.circuit_info
        self.name = save_state.name
        self.parameters = save_state.parameters
        for io in save_state.ios:
            self.addLoadedIO(io)
        self.positionIO()

    def boundingRect(self):
        """Return the bounding rectangle of the circuit.
        Required by the scene.
        """
        return QtCore.QRectF(0, 0, self.xsize, self.ysize)

    def paint(self, painter, options, widget):
        """Paint the circuit. Called automatically by the scene."""
        pen = QtGui.QPen(QtGui.QColor(0, 0, 0))
        pen.setWidth(2)
        painter.setBrush(QtGui.QColor(222, 244, 251))
        painter.setPen(pen)
        painter.drawRoundedRect(0, 0, self.xsize, self.ysize,
                                10, 10)
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
        self.ios = []
        for io in circuit.ios:
            self.ios.append(io.getSaveState())
        self.loaded_item = None         # Do not set this before saving

    def update(self, circuit):
        """Update the save state to match the current state."""
        self.__init__(circuit)
