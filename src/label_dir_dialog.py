'''
Created on Jun 24, 2014

@author: keisano1
'''

from PyQt4 import QtGui
from label_file_dialog import LabelFileDialog


class LabelDirDialog(LabelFileDialog):
    """Reimplementation of file dialog. Select directories instead of files.
    Reimplemented functions:
        openDialog
        setFileName
    """

    def __init__(self):
        """Call the super and just set a proper label text."""
        super(LabelDirDialog, self).__init__()
        self.label.setText("No directory selected")

    def openDialog(self):
        """Open the dialog for selecting directories. If selected
        call setFileName to change label."""
        filename = QtGui.QFileDialog.getExistingDirectory(self, "Select folder",
                   "/home/keisano1/Project/pyvafm-master/src")
        if filename:
            self.setFileName(filename)

    def setFileName(self, path):
        """Set label to show the last two directories of the path."""
        self.file_path = path
        split = path.split("/")
        length = len(split)
        self.label.setText(split[length-2] + '/' + split[length-1])
