'''
Created on Jun 19, 2014

@author: keisano1
'''

from PyQt4 import QtGui, QtCore


class LabelFileDialog(QtGui.QWidget):
    """File dialog widget that contains label showing the current file
    and a button to open the dialog to select the file.
    """

    def __init__(self):
        """Create the label and the button for the widget and connect
        the button to open the dialog. Finally add them into a horizontal
        layout.
        """
        super(LabelFileDialog, self).__init__()
        self.file_path = None
        self.button = QtGui.QToolButton(self)
        self.button.setIcon(self.style().standardIcon(QtGui.QStyle.SP_DirIcon))
        self.label = QtGui.QLabel("No file selected", self)
        self.layout = QtGui.QHBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        QtCore.QObject.connect(self.button, QtCore.SIGNAL("clicked()"), self.openDialog)

    def openDialog(self):
        """Open a file dialog to select a file. If file was selected
        call setFileName to change the label.
        """
        filename = QtGui.QFileDialog.getOpenFileName(self, "Select file", "..")
        if filename:
            self.setFileName(filename)

    def setFileName(self, path):
        """Set label to match the selected file. Remove the path."""
        self.file_path = path
        split = path.split("/")
        self.label.setText(split.last())
