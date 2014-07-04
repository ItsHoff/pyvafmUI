'''
Created on Jun 19, 2014

@author: keisano1
'''

from PyQt4 import QtGui, QtCore


class MyCheckBox(QtGui.QCheckBox):
    """Simple checkbox that changes its text based on its state."""

    def __init__(self, state=True):
        """Create the checkbox and connect it."""
        super(MyCheckBox, self).__init__()
        self.setChecked(state)
        self.setText(str(state))
        QtCore.QObject.connect(self, QtCore.SIGNAL("stateChanged(int)"), self.changeText)

    def changeText(self):
        """Change text to match the state of the checkbox."""
        self.setText(str(self.isChecked()))
