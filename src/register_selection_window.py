"""
Contains all the classes for the register selection window.
Classes:
    - RegisterSelectionWindow
    - RegisterSelectionTree
    - RegisterSelectionTreeItem
    - GlobalDummy
"""

from PyQt4 import QtGui, QtCore
import sys
import drag_selection_window
import circuits


class RegisterSelectionWindow(drag_selection_window.DragSelectionWindow):
    """Subclass of DragSelectionWindow for selecting channels to
    register for the output.
    """

    def __init__(self, main_widget, parent=None):
        self.main_widget = main_widget
        super(RegisterSelectionWindow, self).__init__(parent)
        self.setWindowTitle("Select channels to register")
        self.selection_tree = RegisterSelectionTree()
        self.selection_tree.setHeaderLabel("Selected channels")
        self.layout().addWidget(self.selection_tree, 0, 1)

    def loadOptions(self):
        """Load the global channels that can be registered and all the
        outputs of the circuits to the option tree.
        """
        global_item = QtGui.QTreeWidgetItem(self.option_tree)
        global_item.setText(0, "global")
        global_item.setData(0, QtCore.Qt.UserRole, GlobalDummy())
        global_item.setFlags(global_item.flags() &
                             ~QtCore.Qt.ItemIsDragEnabled)
        for channel in circuits.global_channels:
            sub_item = QtGui.QTreeWidgetItem(global_item)
            sub_item.setText(0, channel)
        for circuit in self.main_widget.machine_widget.circuits:
            if circuit.outputs:
                new_item = QtGui.QTreeWidgetItem(self.option_tree)
                new_item.setText(0, circuit.name)
                new_item.setData(0, QtCore.Qt.UserRole, circuit)
                new_item.setFlags(new_item.flags() &
                                  ~QtCore.Qt.ItemIsDragEnabled)
                for output in circuit.outputs:
                    sub_item = QtGui.QTreeWidgetItem(new_item)
                    sub_item.setText(0, output.name)

    def loadSelections(self):
        """Currently not required since window should never have to be
        deleted and loaded again.
        """
        pass

    def updateNames(self):
        """Update the circuit names that might have changed since the
        window was last opened.
        """
        self.option_tree.clear()
        self.loadOptions()
        for i in range(self.selection_tree.topLevelItemCount()):
            top_item = self.selection_tree.topLevelItem(i)
            top_item.updateText()


class RegisterSelectionTree(drag_selection_window.SelectionTree):
    """Subclass of the selection tree to be used in register selection
    window.
    """

    def __init__(self):
        super(RegisterSelectionTree, self).__init__()

    def createNewItem(self, dropped_item, parent_item):
        """Create a new tree item for the tree. Return new_item, None since
        no custom widget is used.
        """
        circuit = parent_item.data(0, QtCore.Qt.UserRole).toPyObject()
        new_item = RegisterSelectionTreeItem(circuit, dropped_item.text(0))
        return new_item, None


class RegisterSelectionTreeItem(QtGui.QTreeWidgetItem):
    """Tree widget item used on register selection tree."""

    def __init__(self, circuit, channel):
        # Save references to the circuit and channel for easy updates
        self.circuit = circuit
        self.channel = channel
        super(RegisterSelectionTreeItem, self).__init__()
        self.updateText()

    def updateText(self):
        """Update the text of the item to match the current name of
        self.circuit.
        """
        self.setText(0, self.circuit.name + '.' + self.channel)


class GlobalDummy(object):
    """Dummy class used with global channels to pass as a global circuit."""

    def __init__(self):
        self.name = "global"


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = RegisterSelectionWindow()
    sys.exit(app.exec_())
