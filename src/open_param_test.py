'''
Created on Jun 19, 2014

@author: keisano1
'''
import sys
from parameter_window import ParameterWindow
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)
param = ParameterWindow()
param.show()
sys.exit(app.exec_())