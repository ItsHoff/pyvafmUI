'''
Created on Jun 19, 2014

@author: keisano1
'''

from PyQt4 import QtGui, QtCore
from my_check_box import MyCheckBox
from my_file_dialog import MyFileDialog
from my_dir_dialog import MyDirDialog

class ParameterWindow(QtGui.QDialog):
    '''
    classdocs
    '''


    def __init__(self, circuit = None, machine = False):
        '''
        Constructor
        '''
        
        self.circuit = circuit
        self.machine = machine
        if not self.machine:
            super(ParameterWindow, self).__init__(circuit.scene().parent().window())
            self.setWindowTitle(self.circuit.name)
            self.addWidgets(self.circuit.circuit_info.param_window_style)
            self.initUI()
        else:
            super(ParameterWindow, self).__init__(circuit)
            self.setWindowTitle("Machine")
            self.addWidgets(self.circuit.param_window_style)
            self.initUI()
        
    def initUI(self):
        self.show()
        self.raise_()
        self.activateWindow()
        
    def addWidgets(self, param_window_style):
        grid = QtGui.QGridLayout()
        self.setLayout(grid)
        
        widgets = []
        
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
                print "Incorrect widget type on circuit " +  self.circuit.name
        
        row = 0
        for widget_row in widgets:
            if isinstance(widget_row, QtGui.QLayout):
                grid.addLayout(widget_row, row, 0, 1, 2)
                
            else:
                col = 0
                for widget in widget_row:
                    grid.addWidget(widget, row, col)
                    col += 1
            row += 1
            
        ok_button = QtGui.QPushButton("OK")
        QtCore.QObject.connect(ok_button, QtCore.SIGNAL("clicked()"), self.setParameters)
        cancel_button = QtGui.QPushButton("Cancel")
        QtCore.QObject.connect(cancel_button, QtCore.SIGNAL("clicked()"), self.cancel)
        grid.addWidget(ok_button, row, 0)
        grid.addWidget(cancel_button, row, 1)

            
    def createLineEdit(self, label_text):
        label = QtGui.QLabel(label_text)
        text_edit = QtGui.QLineEdit()
        if self.circuit.parameters.has_key(label_text):
            text_edit.setText(self.circuit.parameters[label_text])
        return [label, text_edit]
        
    def createCheckBox(self, label_text):
        label = QtGui.QLabel(label_text)
        check_box = MyCheckBox()
        if self.circuit.parameters.has_key(label_text):
            check_box.setChecked(bool(self.circuit.parameters[label_text]))
        return [label, check_box]
    
    def createFileDialog(self, label_text):
        label = QtGui.QLabel(label_text)
        file_dialog = MyFileDialog()
        if self.circuit.parameters.has_key(label_text):
            file_dialog.setFileName(self.circuit.parameters[label_text])
        return [label, file_dialog]
    
    def createDirDialog(self, label_text):
        label = QtGui.QLabel(label_text)
        file_dialog = MyDirDialog()
        if self.circuit.parameters.has_key(label_text):
            file_dialog.setFileName(self.circuit.parameters[label_text])
        return [label, file_dialog]
    
    def changeCheckBoxState(self, check_box):
        check_box.setText(str(check_box.isChecked()))
        
    def setParameters(self):
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
        self.close()
        