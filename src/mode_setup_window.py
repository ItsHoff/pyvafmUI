"""Module containing all the parts for the ModeSetupWindow."""

from PyQt4 import QtGui, QtCore

from custom_line_edit import CustomLineEdit
import drag_selection_window


class ModeSetupButton(QtGui.QPushButton):
    """Button wrapper for the window. Its purpose is to give a common interface
    for all parameter window widgets."""

    def __init__(self, parent):
        super(ModeSetupButton, self).__init__("Setup Modes")
        self.window = ModeSetupWindow(parent)
        QtCore.QObject.connect(self, QtCore.SIGNAL("clicked()"),
                               self.window.showWindow)

    def getValue(self):
        """Return the save state of the window."""
        return self.window.getSaveState()

    def setValue(self, value):
        """Load the save state of the window."""
        self.window.loadSaveState(value)

    def clearValue(self):
        """Clear the value of the widget."""
        self.window.clearSelections()


class ModeSetupWindow(drag_selection_window.DragSelectionWindow):
    """Window for condiguring the modes for the advanced cantilever circuit."""

    def __init__(self, parent=None):
        super(ModeSetupWindow, self).__init__(parent)

    def initUI(self):
        self.setWindowTitle("Setup Modes")
        self.resize(600, 400)
        grid = QtGui.QGridLayout()
        self.selection_tree = ModeSetupTree()
        self.selection_tree.setHeaderLabel("Current Modes")

        done_button = QtGui.QPushButton("Done")
        QtCore.QObject.connect(done_button, QtCore.SIGNAL("clicked()"),
                               self.hide)
        addV_button = QtGui.QPushButton("Add Vertical Mode")
        QtCore.QObject.connect(addV_button, QtCore.SIGNAL("clicked()"),
                               self.selection_tree.addVerticalMode)
        addL_button = QtGui.QPushButton("Add Lateral Mode")
        QtCore.QObject.connect(addL_button, QtCore.SIGNAL("clicked()"),
                               self.selection_tree.addLateralMode)

        grid.addWidget(self.selection_tree, 0, 0)
        grid.addWidget(addV_button, 1, 0)
        grid.addWidget(addL_button, 2, 0)
        grid.addWidget(done_button, 3, 0)
        self.setLayout(grid)


class ModeSetupTree(drag_selection_window.SelectionTree):
    """Selection tree containing all the current modes."""

    def __init__(self):
        super(ModeSetupTree, self).__init__()

    def createNewItem(self):
        """Create a new empty tree item."""
        new_item = QtGui.QTreeWidgetItem()
        item_widget = ModeSetupTreeItem(self.window().parent().circuit)
        # Set the tree item size hint to match the widget size hint.
        size_hint = item_widget.sizeHint()
        new_item.setSizeHint(0, size_hint)
        return new_item, item_widget

    def createLoadedItem(self, save_state):
        """Create a new item matching the save state."""
        new_item = QtGui.QTreeWidgetItem()
        item_widget = ModeSetupTreeItem(save_state.circuit.loaded_item)
        size_hint = item_widget.sizeHint()
        new_item.setSizeHint(0, size_hint)
        item_widget.setText(save_state.edit_text)
        return new_item, item_widget

    def addVerticalMode(self):
        """Add a vertical mode to the tree."""
        new_item, widget = self.createNewItem()
        widget.setText("Vertical=True, k= , Q= , M= , f0= ")
        self.addTopLevelItem(new_item)
        self.setItemWidget(new_item, 0, widget)
        self.setCurrentItem(new_item)

    def addLateralMode(self):
        """Add a lateral mode to the tree."""
        new_item, widget = self.createNewItem()
        widget.setText("Vertical=False, k= , Q= , M= , f0= ")
        self.addTopLevelItem(new_item)
        self.setItemWidget(new_item, 0, widget)
        self.setCurrentItem(new_item)

    def getSaveState(self):
        """Return the save state of the tree."""
        save_state = ModeSetupSaveList()
        for i in range(self.topLevelItemCount()):
            top_item = self.topLevelItem(i)
            item_widget = self.itemWidget(top_item, 0)
            save_item = ModeSetupSaveItem(item_widget)
            save_state.append(save_item)
        return save_state


class ModeSetupTreeItem(QtGui.QWidget):
    """Widget used in the ModeSetupTree."""

    def __init__(self, circuit):
        super(ModeSetupTreeItem, self).__init__()
        self.circuit = circuit
        main_layout = QtGui.QHBoxLayout()
        self.label = QtGui.QLabel("AddMode(")
        self.line_edit = CustomLineEdit("ModeSetupLineEdit")
        close = QtGui.QLabel(')')

        main_layout.addWidget(self.label)
        main_layout.addWidget(self.line_edit)
        main_layout.addWidget(close)
        self.setLayout(main_layout)

    def getEdit(self):
        """Get the value of the text edit."""
        return self.line_edit.text()

    def setText(self, text):
        """Set the value of the text edit."""
        self.line_edit.setText(text)

    def copy(self):
        """Return a copy of the widget. Needed when moving widgets around."""
        new_item = ModeSetupTreeItem(self.circuit)
        new_item.label.setText(self.label.text())
        new_item.line_edit.setText(self.line_edit.text())
        return new_item


class ModeSetupSaveItem(object):
    """Container for ModeSetupTreeItem state without Qt bindings.
    Used for saving.
    """

    def __init__(self, tree_item):
        self.circuit = tree_item.circuit.getSaveState()
        self.edit_text = tree_item.getEdit()

    def update(self, tree_item):
        """Update the save state to match the current state."""
        self.__init__(tree_item)

    def __str__(self):
        return str(self.circuit.name + ".AddMode(" + self.edit_text + ")")


class ModeSetupSaveList(list):
    """List for saving all the individual save items."""

    def __init__(self):
        super(ModeSetupSaveList, self).__init__()

    def __str__(self):
        i = 0
        string = ""
        for item in self:
            if i != 0:
                string += "\n"
            string += str(item)
            i += 1
        return str(string)
