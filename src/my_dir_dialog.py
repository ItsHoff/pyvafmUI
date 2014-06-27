'''
Created on Jun 24, 2014

@author: keisano1
'''

from PyQt4 import QtGui, QtCore
from my_file_dialog import MyFileDialog

class MyDirDialog(MyFileDialog):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(MyDirDialog, self).__init__()
        self.label.setText("No directory selected")
        
    def openDialog(self):
        filename = QtGui.QFileDialog.getExistingDirectory(self, "Select folder", "/home/keisano1/Project/pyvafm-master/src")
        if filename:
            self.setFileName(filename)
            
    def setFileName(self, path):
        self.file_path = path
        split = path.split("/")
        length = len(split)
        self.label.setText(split[length-2]+'/'+split[length-1])