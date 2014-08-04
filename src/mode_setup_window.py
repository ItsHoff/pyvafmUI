from PyQt4 import QtGui, QtCore

import drag_selection_window


class ModeSetupWindow(drag_selection_window.DragSelectionWindow):

    def __init__(self, parent=None):
        super(ModeSetupWindow, self).__init__(parent)

    def initUI(self):
        self.setWindowTitle("Setup Modes")
        self.resize(400, 400)
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

    def __init__(self):
        super(ModeSetupTree, self).__init__()

    def createNewItem(self):
        new_item = QtGui.QTreeWidgetItem()
        item_widget = ModeSetupTreeItem(self.window().parent().circuit)
        # Set the tree item size hint to match the widget size hint.
        size_hint = item_widget.sizeHint()
        new_item.setSizeHint(0, size_hint)
        return new_item, item_widget

    def createLoadedItem(self, save_state):
        new_item = QtGui.QTreeWidgetItem()
        item_widget = ModeSetupTreeItem(save_state.circuit.loaded_item)
        size_hint = item_widget.sizeHint()
        new_item.setSizeHint(0, size_hint)
        item_widget.setText(save_state.edit_text)
        return new_item, item_widget

    def addVerticalMode(self):
        new_item, widget = self.createNewItem()
        widget.setText("Vertical=True, k= , Q= , M= , f0= ")
        self.addTopLevelItem(new_item)
        self.setItemWidget(new_item, 0, widget)
        self.setCurrentItem(new_item)

    def addLateralMode(self):
        new_item, widget = self.createNewItem()
        widget.setText("Vertical=False, k= , Q= , M= , f0= ")
        self.addTopLevelItem(new_item)
        self.setItemWidget(new_item, 0, widget)
        self.setCurrentItem(new_item)

    def getSaveState(self):
        save_state = ModeSetupSaveList()
        for i in range(self.topLevelItemCount()):
            top_item = self.topLevelItem(i)
            item_widget = self.itemWidget(top_item, 0)
            save_item = ModeSetupSaveItem(item_widget)
            save_state.append(save_item)
        return save_state


class ModeSetupTreeItem(QtGui.QWidget):

    def __init__(self, circuit):
        super(ModeSetupTreeItem, self).__init__()
        self.circuit = circuit
        main_layout = QtGui.QHBoxLayout()
        self.label = QtGui.QLabel("AddMode(")
        self.line_edit = QtGui.QLineEdit()
        close = QtGui.QLabel(')')

        main_layout.addWidget(self.label)
        main_layout.addWidget(self.line_edit)
        main_layout.addWidget(close)
        self.setLayout(main_layout)

    def getEdit(self):
        return self.line_edit.text()

    def setText(self, text):
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
        self.__init__(tree_item)

    def __str__(self):
        return str(self.circuit.name + ".AddMode(" + self.edit_text + ")")


class ModeSetupSaveList(list):

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
