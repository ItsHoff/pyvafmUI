"""Module containing the custom line edit and all the regular expressions
it uses.
"""

from PyQt4 import QtGui, QtCore

from parameter_completer import ParameterCompleter
from parameter_completion_model import ParameterCompletionModel


DOUBLER = "((%s),\s?)(%s)"
TRIPLER = "((%s),\s?){2}(%s)"
BOOL_REGEXP = "True|False"
TRIPLE_BOOL_REGEXP = TRIPLER % (BOOL_REGEXP, BOOL_REGEXP)
FLOAT_REGEXP = "[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?"
DOUBLE_FLOAT_REGEXP = DOUBLER % (FLOAT_REGEXP, FLOAT_REGEXP)
TRIPLE_FLOAT_REGEXP = TRIPLER % (FLOAT_REGEXP, FLOAT_REGEXP)
DIM_REGEXP = "[x-z]=[0-9.]+"
TRIPLE_DIM_REGEXP = TRIPLER % (DIM_REGEXP, DIM_REGEXP)
INT_REGEXP = "[0-9]+"
DOUBLE_INT_REGEXP = DOUBLER % (INT_REGEXP, INT_REGEXP)
TRIPLE_INT_REGEXP = TRIPLER % (INT_REGEXP, INT_REGEXP)
BIT_REGEXP = "1|0"
NAME_REGEXP = "[\d\w]+"
FILE_REGEXP = "[\d\w\./]+"


class CustomLineEdit(QtGui.QLineEdit):
    """Line edit that comes with multiple preset completion and validation
    modes that can be accessed with its subtypes."""

    def __init__(self, subtype):
        """Initialise the line edit and setup the completion and validation
        according to the given subtype"""
        super(CustomLineEdit, self).__init__()

        model = None
        if subtype == "TripleBoolLineEdit":
            completion_list = ["True", "False"]
            model = ParameterCompletionModel(completion_list)
            validator_regexp = QtCore.QRegExp(TRIPLE_BOOL_REGEXP)
            self.setPlaceholderText("bool, bool, bool")
        elif subtype == "ThreeDimensionLineEdit":
            completion_list = ["x=", "y=", "z="]
            model = ParameterCompletionModel(completion_list)
            validator_regexp = QtCore.QRegExp(TRIPLE_DIM_REGEXP)
            self.setPlaceholderText("x=float, y=float, z=float")
        elif subtype == "FloatLineEdit":
            self.setPlaceholderText("float")
            validator_regexp = QtCore.QRegExp(FLOAT_REGEXP)
        elif subtype == "DoubleFloatLineEdit":
            self.setPlaceholderText("float, float")
            validator_regexp = QtCore.QRegExp(DOUBLE_FLOAT_REGEXP)
        elif subtype == "TripleFloatLineEdit":
            self.setPlaceholderText("float, float, float")
            validator_regexp = QtCore.QRegExp(TRIPLE_FLOAT_REGEXP)
        elif subtype == "IntLineEdit":
            self.setPlaceholderText("int")
            validator_regexp = QtCore.QRegExp(INT_REGEXP)
        elif subtype == "DoubleIntLineEdit":
            self.setPlaceholderText("int, int")
            validator_regexp = QtCore.QRegExp(DOUBLE_INT_REGEXP)
        elif subtype == "TripleIntLineEdit":
            self.setPlaceholderText("int, int, int")
            validator_regexp = QtCore.QRegExp(TRIPLE_INT_REGEXP)
        elif subtype == "NameLineEdit":
            self.setPlaceholderText("string")
            validator_regexp = QtCore.QRegExp(NAME_REGEXP)
        elif subtype == "FileLineEdit":
            self.setPlaceholderText("filename")
            validator_regexp = QtCore.QRegExp(FILE_REGEXP)
        elif subtype == "BitLineEdit":
            self.setPlaceholderText("1/0")
            validator_regexp = QtCore.QRegExp(BIT_REGEXP)
        else:
            validator_regexp = None

        if model is not None:
            completer = ParameterCompleter()
            completer.setModel(model)
            completer.setCompletionMode(completer.InlineCompletion)
            self.setCompleter(completer)
        if validator_regexp is not None:
            self.setValidator(QtGui.QRegExpValidator(validator_regexp))

    def getValue(self):
        """Return the value of the widget."""
        return self.text()

    def setValue(self, value):
        """Set the value of the widget."""
        self.setText(str(value))

    def clearValue(self):
        """Clear the value of the widget."""
        self.clear()
