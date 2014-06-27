'''
Created on Jun 19, 2014

@author: keisano1
'''

from PyQt4 import QtGui, QtCore

class MyCheckBox(QtGui.QCheckBox):
    '''
    classdocs
    '''


    def __init__(self, state = True):
        '''
        Constructor
        '''
        super(MyCheckBox, self).__init__()
        self.setChecked(state)
        self.setText(str(state))
        QtCore.QObject.connect(self, QtCore.SIGNAL("stateChanged(int)"), self.changeText)
        
    def changeText(self):
        self.setText(str(self.isChecked()))
        
        