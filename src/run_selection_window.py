"""
Contains all the classes for the run selection window.
Classes:
    - RunSelectionWindow
    - RunSelectionTree
    - RunSelectionTreeItem
"""

from PyQt4 import QtGui, QtCore
import sys
import drag_selection_window
import circuits


class RunSelectionWindow(drag_selection_window.DragSelectionWindow):
    """Subclass of DragSelection window used for selecting the runtime
    operations of the pyvafm."""

    def __init__(self, main_widget):
        self.main_widget = main_widget
        super(RunSelectionWindow, self).__init__(main_widget)
        self.setWindowTitle("Select runtime operations")
        self.selection_tree = RunSelectionTree()
        self.selection_tree.setHeaderLabel("Selected operations")
        self.layout().addWidget(self.selection_tree, 0, 1)

    def loadOptions(self):
        """Add all the circuits with runtime operations to the option tree."""
        for circuit in self.main_widget.machine_widget.circuits:
            circuit_type = circuit.circuit_info.circuit_type
            if circuit_type in circuits.run_time_functions:
                new_item = QtGui.QTreeWidgetItem(self.option_tree)
                new_item.setText(0, circuit.name)
                new_item.setData(0, QtCore.Qt.UserRole, circuit)
                new_item.setFlags(new_item.flags() &
                                  ~QtCore.Qt.ItemIsDragEnabled)
                for function in circuits.run_time_functions[circuit_type]:
                    sub_item = QtGui.QTreeWidgetItem(new_item)
                    sub_item.setText(0, function)

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
            widget = self.selection_tree.itemWidget(top_item, 0)
            widget.updateText()


class RunSelectionTree(drag_selection_window.SelectionTree):
    """Subclass of the selection tree to be used in run selection
    window.
    """

    def __init__(self):
        super(RunSelectionTree, self).__init__()

    def createNewItem(self, dropped_item, parent_item):
        """Create a empty tree widget item and a custom widget to use
        with the item.
        """
        new_item = QtGui.QTreeWidgetItem()
        circuit = parent_item.data(0, QtCore.Qt.UserRole).toPyObject()
        item_widget = RunSelectionTreeItem(circuit, dropped_item.text(0))
        # Set the tree item size hint to match the widget size hint.
        size_hint = item_widget.sizeHint()
        new_item.setSizeHint(0, size_hint)
        return new_item, item_widget


class RunSelectionTreeItem(QtGui.QWidget):
    """Custom widget to be used in run selection tree. Holds label telling the
    function and a line edit to edit the function parameters."""

    def __init__(self, circuit, function):
        self.circuit = circuit
        self.function = function
        super(RunSelectionTreeItem, self).__init__()
        main_layout = QtGui.QHBoxLayout()
        self.label = QtGui.QLabel()
        self.line_edit = QtGui.QLineEdit()
        close = QtGui.QLabel(')')

        main_layout.addWidget(self.label)
        main_layout.addWidget(self.line_edit)
        main_layout.addWidget(close)
        self.setLayout(main_layout)
        self.updateText()

    def setEdit(self, text):
        """Set the value of the line edit to match text."""
        self.line_edit.setText(text)

    def updateText(self):
        """Update the text of the widget to match the current name of
        self.circuit.
        """
        self.label.setText(self.circuit.name + '.' + self.function + '(')

    def text(self):
        """Reimplementation. Return the text of the labels and parameters
        given in line edit as one string.
        """
        self.updateText()
        return self.label.text() + self.line_edit.text() + ')'

    def copy(self):
        """Return a copy of the widget. Needed when moving widgets around."""
        new_item = RunSelectionTreeItem(self.circuit, self.function)
        new_item.label.setText(self.label.text())
        new_item.line_edit.setText(self.line_edit.text())
        return new_item

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = RunSelectionWindow()
    sys.exit(app.exec_())