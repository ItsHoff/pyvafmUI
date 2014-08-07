'''
Created on Jun 6, 2014

@author: keisano1
'''

from PyQt4 import QtGui, QtCore

from ui_circuit import UICircuit
from ui_IO import UIIO
from ui_connection import UIConnection
import circuits


class MachineWidget(QtGui.QGraphicsScene):
    """Scene displaying the current state of the machine."""

    def __init__(self, tree_widget, parent=None):
        '''
        Constructor
        '''
        super(MachineWidget, self).__init__(parent)
        self.tree_widget = tree_widget
        self.circuits = []
        self.connections = []
        self.circuit_index = 1
        self.new_connection = None
        self.initWidget()

    def initWidget(self):
        """Initialise the UI of the widget."""
        self.addCircuits()
        self.updateSceneRect()
        self.update()

    def getNewSceneRect(self):
        """Return a new scene rectangle based on the bounding rectangle
        of all scene items.
        """
        rect = self.itemsBoundingRect()
        center = rect.center()
        rect.setHeight(rect.height() + 500)
        rect.setWidth(rect.width() + 500)
        rect.moveCenter(center)
        return rect

    def updateSceneRect(self):
        """Update the scene rect to the one given by getNewSceneRect."""
        rect = self.getNewSceneRect()
        self.setSceneRect(rect)

    def updateMovingSceneRect(self):
        """Update the scene rectangle but don't make it smaller. Used while
        moving circuits to avoid unwanted movement.
        """
        old_rect = self.sceneRect()
        new_rect = self.getNewSceneRect()
        new_rect = new_rect.united(old_rect)
        self.setSceneRect(new_rect)

    def addCircuits(self):
        """Add some circuits to the scene on startup."""
        pass

    def addCircuit(self, name, x, y):
        """Add a circuit with corresponding name to the scene
        and update the scene.
        """
        circuit = UICircuit(x-x%100, y-y%100, circuits.circuits[name], self)
        circuit.addIO()
        self.circuits.append(circuit)
        self.addItem(circuit)
        self.circuit_index += 1
        self.updateSceneRect()
        self.update()

    def addDroppedCircuit(self, dropped, pos):
        """Add the dropped circuit to the scene after a dropEvent."""
        name = str(dropped.text(0))
        self.addCircuit(name, pos.x(), pos.y())

    def addClickedCircuit(self, pos):
        """Add circuit selected from the main_window tree_widget
        to the scene. If nothing is selected do nothing.
        """
        item = self.tree_widget.currentItem()
        if item is None:
            return
        name = str(item.text(0))
        if item.parent():
            self.addToRecentlyUsed(item)
            self.addCircuit(name, pos.x(), pos.y())

    def addLoadedCircuit(self, save_state):
        """Add circuit loaded from save_state into the scene."""
        circuit = UICircuit(0, 0, save_state.circuit_info)
        self.circuits.append(circuit)
        self.addItem(circuit)
        circuit.loadSaveState(save_state)
        self.circuit_index += 1

    def createNewConnection(self, origin, mouse_pos):
        """Try to create a new connection starting from mouse_pos.
        Throw a ValueError if input under mouse is allready connected.
        Should be called by the input or output at the start of the
        connection.
        """
        status_bar = self.parent().window().statusBar()
        try:
            self.new_connection = UIConnection(origin, mouse_pos)
        except ValueError as e:
            status_bar.showMessage(e.message, 3000)
            return
        self.views()[0].setMouseTracking(True)
        self.addItem(self.new_connection)

    def addConnection(self):
        """Add a new valid connection. Should be called
        by the input or output at the end of connection.
        """
        status_bar = self.parent().window().statusBar()
        input_ = self.new_connection.input_
        output = self.new_connection.output
        message = "Connected %s.%s and %s.%s" % (output.circuit.name,
                  output.name, input_.circuit.name, input_.name)
        self.connections.append(self.new_connection)
        self.new_connection = None
        self.views()[0].setMouseTracking(False)
        status_bar.showMessage(message, 4000)

    def addLoadedConnection(self, save_state):
        """Add connection loaded from save_state into the scene."""
        output = save_state.output
        connection = UIConnection(output.loaded_item, output.loaded_item.pos())
        connection.loadSaveState(save_state)
        self.connections.append(connection)
        self.addItem(connection)

    def deleteNewConnection(self):
        """Delete unconnected new_connextion."""
        if self.new_connection is not None:
            status_bar = self.parent().window().statusBar()
            self.removeItem(self.new_connection)
            self.new_connection = None
            self.views()[0].setMouseTracking(False)
            status_bar.showMessage("Destroyed connection", 2000)

    def updateConnections(self):
        """Update paths for all required connections.
        Needed after some move events."""
        for connection in self.connections:
            connection.updatePath()

    def hasIOatPos(self, pos):
        """Check if there's input or output at position pos
        and return True if there is and False otherwise.
        """
        items = self.items(pos)
        for item in items:
            if isinstance(item, UIIO):
                return True
        return False

    def addContextActions(self, menu):
        """Add widget specific context actions to the
        context menu given as parameter.
        """
        clear_all = QtGui.QAction("Clear All", menu)
        QtCore.QObject.connect(clear_all, QtCore.SIGNAL("triggered()"),
                               self.clearAll)

        clear_connections = QtGui.QAction("Clear Connections", menu)
        QtCore.QObject.connect(clear_connections, QtCore.SIGNAL("triggered()"),
                               self.removeConnections)

        menu.addAction(clear_connections)
        menu.addAction(clear_all)

    def clearAll(self):
        """Clear everything from the scene."""
        status_bar = self.parent().window().statusBar()
        for circuit in self.circuits[:]:
            self.removeCircuit(circuit)
        # self.updateSceneRect()
        status_bar.showMessage("Cleared all", 3000)
        self.update()

    def removeConnections(self):
        """Clear all connections from the scene."""
        status_bar = self.parent().window().statusBar()
        for connection in self.connections:
            self.removeItem(connection)
        self.connections = []
        status_bar.showMessage("Removed all connections", 3000)
        self.update()

    def removeConnectionsFrom(self, IO):
        """Remove all connections from input or output
        given as parameter.
        """
        status_bar = self.parent().window().statusBar()
        for connection in self.connections[:]:
            if connection.input_ == IO or connection.output == IO:
                self.connections.remove(connection)
                self.removeItem(connection)
        status_bar.showMessage("Removed all connections from %s.%s"%
                (IO.circuit.name, IO.name), 3000)
        self.update()

    def removeConnection(self, connection):
        """Remove the specified connection from the scene."""
        status_bar = self.parent().window().statusBar()
        input_ = connection.input_
        output = connection.output
        message = "Removed connection from %s.%s to %s.%s" % (input_.circuit.name,
                input_.name, output.circuit.name, output.name)
        self.connections.remove(connection)
        self.removeItem(connection)
        status_bar.showMessage(message, 3000)

    def removeCircuit(self, circuit):
        """Remove the specified circuit from the scene.
        Also remove all the circuits inputs, outputs and connections
        from the scene.
        """
        status_bar = self.parent().window().statusBar()
        for io in circuit.ios:
            self.removeConnectionsFrom(io)
        self.circuits.remove(circuit)
        self.removeItem(circuit)
        status_bar.showMessage("Removed %s"%circuit.name, 3000)
        self.updateSceneRect()
        self.update()

    def drawBackground(self, qp, rect):
        """Draw the background white and call a grid draw"""
        qp.setPen(QtGui.QColor(255, 255, 255))
        qp.setBrush(QtGui.QColor(255, 255, 255))
        qp.drawRect(rect)
        self.drawGrid(qp, rect)

    def drawGrid(self, qp, rect):
        """Draw a grid with a spacing of 100 to the background."""
        tl = rect.topLeft()
        br = rect.bottomRight()
        solid_pen = QtGui.QPen(QtGui.QColor(0, 0, 0), 4, QtCore.Qt.SolidLine)
        faint_pen = QtGui.QPen(QtGui.QColor(150, 150, 150), 1, QtCore.Qt.SolidLine)
        qp.setPen(faint_pen)
        for x in range(int(tl.x() - tl.x() % 100),
                       int(br.x()), 100):
            for y in range(int(tl.y() - tl.y() % 100),
                           int(br.y()), 100):
                qp.drawLine(int(tl.x()), int(y), int(br.x()), int(y))
                qp.drawLine(int(x), int(tl.y()), int(x), int(br.y()))
        # Draw thicklines to the middle of the scene
        qp.setPen(solid_pen)
        qp.drawLine(0, int(tl.y()),
                    0, int(br.y()))
        qp.drawLine(int(tl.x()), 0,
                    int(br.x()), 0)

    def dragEnterEvent(self, event):
        """Accept event for drag & drop to work."""
        event.accept()

    def dragMoveEvent(self, event):
        """Accept event for drag & drop to work."""
        event.accept()

    def dropEvent(self, event):
        """Accept event and add the dropped circuit
        to the scene.
        """
        if event.source() is self.tree_widget:
            event.accept()
            dropped_item = event.source().currentItem()
            self.addDroppedCircuit(dropped_item, event.scenePos())
            self.addToRecentlyUsed(dropped_item)

    def addToRecentlyUsed(self, tree_item):
        """Add tree item under the recently used tab if it's not allready
        there.
        """
        recently = self.tree_widget.findItems("Recently Used",
                                              QtCore.Qt.MatchExactly)[0]
        for i in range(recently.childCount()):
            if recently.child(i).text(0) == tree_item.text(0):
                return
        clone = tree_item.clone()
        recently.addChild(clone)

    def mousePressEvent(self, event):
        """If user is holding down ctrl try to add circuit to the scene.
        Otherwise call the super function to send signal forward.
        """
        if (event.modifiers() & QtCore.Qt.ControlModifier and
                event.button() == QtCore.Qt.LeftButton):
            event.accept()
            self.addClickedCircuit(event.scenePos())
        else:
            super(MachineWidget, self).mousePressEvent(event)
            # If user was trying to create a new connection
            # and clicked something other than input or output
            # destroy the connection. Also non left clicks
            # destroy the connection.
            if (self.new_connection is not None and
                    (not self.hasIOatPos(event.scenePos()) or
                     event.button() != QtCore.Qt.LeftButton)):
                self.deleteNewConnection()

    def mouseMoveEvent(self, event):
        """If user is trying to create a connection update connections
        end point when mouse is moved. Remember to call super.
        """
        super(MachineWidget, self).mouseMoveEvent(event)
        if self.new_connection is not None:
            self.new_connection.updateMousePos(event.scenePos())
            self.update()

    def contextMenuEvent(self, event):
        """Create a new context menu and open it under mouse"""
        menu = QtGui.QMenu()
        # Insert actions to the menu from all the items under the mouse
        for item in self.items(event.scenePos()):
            item.addContextActions(menu)
        self.addContextActions(menu)
        # Show the menu under mouse
        menu.exec_(event.screenPos())
