'''
Created on Jun 19, 2014

@author: keisano1
'''

from PyQt4 import QtGui, QtCore
from my_check_box import MyCheckBox
from my_file_dialog import MyFileDialog
from my_dir_dialog import MyDirDialog
import ui_circuit


class ParameterWindow(QtGui.QDialog):
    """Widget for editing parameters of the circuits.
    Normally opens a separate window, but can also be embedded
    by adding it to a layout.
    """

    def __init__(self, circuit):
        """Construct the window based on the circuit parameters.
        Circuit can also be the main machine in addition to regular
        circuits.
        """
        self.circuit = circuit
        if isinstance(self.circuit, ui_circuit.UICircuit):
            super(ParameterWindow, self).__init__(circuit.scene().parent().window())
            self.setWindowTitle(self.circuit.name + " parameters")
            self.addWidgets(self.circuit.circuit_info.param_window_style)
        else:
            super(ParameterWindow, self).__init__(circuit.window())
            self.setWindowTitle("Machine parameters")
            self.addWidgets(self.circuit.param_window_style)

    def showWindow(self):
        """Show the window and make sure it's activated and on top."""
        self.show()
        self.raise_()
        self.activateWindow()

    def addWidgets(self, param_window_style):
        """Add widgets specified in the param_window_style to the window."""
        grid = QtGui.QGridLayout()
        self.setLayout(grid)
        widgets = []
        # Create all the necessary widgets and add them to the temporary
        # widgets container.
        for name, widget_type in param_window_style.iteritems():
            if widget_type == "LineEdit":
                widgets.append(self.createLineEdit(name))
            elif widget_type == "CheckBox":
                widgets.append(self.createCheckBox(name))
            elif widget_type == "FileDialog":
                widgets.append(self.createFileDialog(name))
            elif widget_type == "DirDialog":
                widgets.append(self.createDirDialog(name))
            else:
                print "Incorrect widget type on circuit " + self.circuit.name
        # Add the widgets from the container into the window layout.
        row = 0
        for widget_row in widgets:
            col = 0
            for widget in widget_row:
                grid.addWidget(widget, row, col)
                col += 1
            row += 1
        # Create the buttons for the window and connect them.
        ok_button = QtGui.QPushButton("OK")
        QtCore.QObject.connect(ok_button, QtCore.SIGNAL("clicked()"), self.setParameters)
        cancel_button = QtGui.QPushButton("Cancel")
        QtCore.QObject.connect(cancel_button, QtCore.SIGNAL("clicked()"), self.cancel)
        grid.addWidget(ok_button, row, 0)
        grid.addWidget(cancel_button, row, 1)

    def createLineEdit(self, label_text):
        """Create a line edit and a label with label_text."""
        label = QtGui.QLabel(label_text)
        text_edit = QtGui.QLineEdit()
        if label_text in self.circuit.parameters:
            text_edit.setText(self.circuit.parameters[label_text])
        return [label, text_edit]

    def createCheckBox(self, label_text):
        """Create a check box and a label with label_text."""
        label = QtGui.QLabel(label_text)
        check_box = MyCheckBox()
        if label_text in self.circuit.parameters:
            check_box.setChecked(bool(self.circuit.parameters[label_text]))
        return [label, check_box]

    def createFileDialog(self, label_text):
        """Create a file dialog and a label with label_text."""
        label = QtGui.QLabel(label_text)
        file_dialog = MyFileDialog()
        if label_text in self.circuit.parameters:
            file_dialog.setFileName(self.circuit.parameters[label_text])
        return [label, file_dialog]

    def createDirDialog(self, label_text):
        """Create a directory dialog and a label with label_text."""
        label = QtGui.QLabel(label_text)
        file_dialog = MyDirDialog()
        if label_text in self.circuit.parameters:
            file_dialog.setFileName(self.circuit.parameters[label_text])
        return [label, file_dialog]

    def setParameters(self):
        """Collect all the parameters given and call the circuits
        setParameters to save them. Finally close the window.
        """
        print "set parameters"
        rows = self.layout().rowCount()
        parameters = {}
        for row in range(0, rows - 1):
            label = self.layout().itemAtPosition(row, 0).widget()
            edit = self.layout().itemAtPosition(row, 1).widget()
            if isinstance(edit, QtGui.QLineEdit):
                parameters[str(label.text())] = edit.text()
            elif isinstance(edit, MyCheckBox):
                parameters[str(label.text())] = edit.isChecked()
            elif isinstance(edit, MyFileDialog):
                parameters[str(label.text())] = edit.file_path
        self.circuit.setParameters(parameters)
        self.close()

    def cancel(self):
        """Close the window without action when cancel is pressed."""
        self.close()
