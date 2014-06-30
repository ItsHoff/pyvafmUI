'''
Created on Jun 6, 2014

@author: keisano1
'''

import sys
from PyQt4 import QtGui, QtCore
from machine_widget import MachineWidget
from my_scroll_area import MyScrollArea
from my_graphics_view import MyGraphicsView
from parameter_window import ParameterWindow
from ui_circuit import UICircuit
import circuit_info
import circuits
import script





class MainWindow(QtGui.QMainWindow):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(MainWindow, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(100, 100, 800, 500)
        self.setWindowTitle('PyVAFM')
        
        self.setCentralWidget(MainWidget())
        
        self.show()


class MainWidget(QtGui.QWidget): 
    def __init__(self):
        super(MainWidget, self).__init__()
        self.param_window_style = circuits.machine_param_window_style
        self.parameters = {}
        self.initWidget()

    def initWidget(self):
        "Set up the left area of the UI"
        left_area = QtGui.QVBoxLayout()             
        
        "Set up machine parameter grid on the top left of the UI"
        machine_param_grid = QtGui.QGridLayout()    
        create_button = QtGui.QPushButton("Create Script")
        run_button = QtGui.QPushButton("Create + Run")
        self.parameter_button = QtGui.QPushButton("Machine Parameters")
        
        QtCore.QObject.connect(create_button, QtCore.SIGNAL("clicked()"), self.createScript)
        QtCore.QObject.connect(run_button, QtCore.SIGNAL("clicked()"), self.createRun)
        QtCore.QObject.connect(self.parameter_button, QtCore.SIGNAL("clicked()"), self.showParameters)
        
        """label1 = QtGui.QLabel("Temp")
        label2 = QtGui.QLabel("Temp")
        label3 = QtGui.QLabel("Temp")
        label4 = QtGui.QLabel("Temp")
        label5 = QtGui.QLabel("Temp")
        machine_param_grid.addWidget(label1, 0, 0)
        machine_param_grid.addWidget(label2, 1, 0)
        machine_param_grid.addWidget(label3, 2, 0)
        machine_param_grid.addWidget(label4, 3, 0)
        machine_param_grid.addWidget(label5, 4, 0)"""
        #machine_param_grid.addWidget(self.param_window, 0, 0, 1, 2)
        machine_param_grid.addWidget(create_button, 2, 0)
        machine_param_grid.addWidget(run_button, 2, 1)
        machine_param_grid.addWidget(self.parameter_button, 1, 0, 1,  2)
        
        
        tree_widget = QtGui.QTreeWidget(self)
        tree_widget.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        tree_widget.setHeaderLabel("Circuits")
        tree_widget.setDragEnabled(True)
        tree_widget.setFocusPolicy(QtCore.Qt.NoFocus)
        
        self.load_circuits(tree_widget)
        
        left_area.addLayout(machine_param_grid)
        left_area.addWidget(tree_widget)
        
        
        """scroll_area = MyScrollArea()       #Right side scroll area
        
        scroll_area.setWidget(machine_widget)
        scroll_area.setAlignment(QtCore.Qt.AlignCenter)
        scroll_area.verticalScrollBar().setValue(
                    0.5*scroll_area.verticalScrollBar().maximum())
        scroll_area.horizontalScrollBar().setValue(
                    0.5*scroll_area.horizontalScrollBar().maximum())"""
        
        graphics_view = MyGraphicsView()
        self.machine_widget = MachineWidget(tree_widget, graphics_view)
        graphics_view.setScene(self.machine_widget)
        
        
        main_layout = QtGui.QHBoxLayout()
        main_layout.addLayout(left_area)
        #main_layout.addWidget(scroll_area)
        main_layout.addWidget(graphics_view)
        self.setLayout(main_layout)
        
    def showParameters(self):
        self.parameter_window = ParameterWindow(self, True)
        
    def setParameters(self, parameters):
        for label, value in parameters.iteritems():
            if value or value == False:
                self.parameters[label] = value 
        
   
    def load_circuits(self, tree_widget):
        "Loads all the circuits from the circuits file to the tree_widget"
        groups = {}
        for group in circuit_info.groups:
            top_item = QtGui.QTreeWidgetItem(tree_widget)
            top_item.setText(0, group)
            top_item.setFlags(top_item.flags()&~QtCore.Qt.ItemIsDragEnabled
                              &~QtCore.Qt.ItemIsSelectable)
            groups[group] = top_item
        for name, info in circuits.circuits.iteritems():
            group = info.io_type
            sub_item = QtGui.QTreeWidgetItem(groups[group])
            sub_item.setText(0, name)
            
    def createScript(self):
        print self.parameters
        savefile = QtGui.QFileDialog.getSaveFileName(self, "Save script", "")
        if not savefile:
            return
        blocks = [""]*5
        with open("formats/machine.format", "r") as f:
            script.createFromFormat(blocks, f, self.parameters)
        
        for circuit in self.machine_widget.circuits:
            print circuit.name
            print circuit.circuit_info.script_format
            if circuit.circuit_info.script_format:
                print circuit.name
                print circuit.circuit_info.script_format
                with open(circuit.circuit_info.script_format, "r") as f:
                    script.createFromFormat(blocks, f, circuit.parameters)
            else:
                raise NotImplementedError("Circuit "+ circuit.name+ " doesn't have proper script format implemented!")
        
        for connection in self.machine_widget.connections:
            with open("formats/connect.format", "r") as f:
                output = connection.output.circuit.name+"."+connection.output.name
                input = connection.input.circuit.name+"."+connection.input.name
                print output, input
                script.createFromFormat(blocks, f, {"output":output, "input":input})
                    
        print blocks
        with open(savefile, 'w') as f:
            i = 0
            for block in blocks:
                f.write("'Block #"+str(i)+"'\n")
                f.write(block)
                f.write('\n\n')
                i += 1
        return savefile
        
    def createRun(self):
        savefile  = self.createScript()
        if savefile:
            with open(str(savefile), 'r') as f:
                print f
                exec(f)
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())        

if __name__ == "__main__":
    main()
