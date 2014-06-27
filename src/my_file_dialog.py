'''
Created on Jun 19, 2014

@author: keisano1
'''

from PyQt4 import QtGui, QtCore

class MyFileDialog(QtGui.QWidget):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(MyFileDialog, self).__init__()
        self.file_path = None
        self.button = QtGui.QToolButton(self)
        self.button.setIcon(self.style().standardIcon(QtGui.QStyle.SP_DirIcon))
        self.label = QtGui.QLabel("No file selected", self)
        self.layout = QtGui.QHBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        QtCore.QObject.connect(self.button, QtCore.SIGNAL("clicked()"), self.openDialog)
        
    def openDialog(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, "Select file", "")
        if filename:
            self.setFileName(filename)
            
    def setFileName(self, path):
        self.file_path = path
        split = path.split("/")
        self.label.setText(split.last())
        