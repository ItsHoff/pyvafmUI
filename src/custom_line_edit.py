"""Module containing the custom line edit and all the regular expressions
it uses.
"""

from PyQt4 import QtGui, QtCore

from parameter_completer import ParameterCompleter
from parameter_completion_model import ParameterCompletionModel


DOUBLER = "((%s),\s?)(%s)"
TRIPLER = "((%s),\s?){2}(%s)"
BOOL_REGEXP = "T?r?u?e?|F?a?l?s?e?"
TRIPLE_BOOL_REGEXP = TRIPLER % (BOOL_REGEXP, BOOL_REGEXP)
FLOAT_REGEXP = "[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?"
DOUBLE_FLOAT_REGEXP = DOUBLER % (FLOAT_REGEXP, FLOAT_REGEXP)
TRIPLE_FLOAT_REGEXP = TRIPLER % (FLOAT_REGEXP, FLOAT_REGEXP)
DIM_REGEXP = "[x-z]?=[0-9.]*"
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

    def __init__(self, subtype=None):
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

    def event(self, event):
        """Reimplement the default behaviour of tab."""
        if event.type() == event.KeyPress and event.key() == QtCore.Qt.Key_Tab:
            return self.tabMove()
        else:
            return super(CustomLineEdit, self).event(event)

    def tabMove(self):
        """Select the next parameter value when tab is pressed. Return True
        if operation was succesfull. If last parameter is allready selected
        or operation failed return False to signal default tab movement.
        """
        text = self.text()
        # If there is no list present we don't need any special movement.
        if ',' not in text:
            return False
        # If we have selected multiple items tab will select the first
        # partially selected one.
        if "," in self.selectedText() or "=" in self.selectedText():
            pos = self.selectionStart()
        else:
            pos = self.selectionEnd()
        # We're at the end.
        if pos == len(text):
            return False
        # We're at the end of a item so move to the next one.
        if text[pos] == ',':
            pos += 1
        eq_pos = text.find('=', pos) + 1
        # If there's no equality signs select the text surrounded by the
        # closest delimiter (comma, eol, bol). If we've gone past the last
        # equality sign return False to jump to next widget.
        if eq_pos == 0:
            comma_pos = text.find(',', pos)
            left_comma = text.rfind(',', 0, comma_pos) + 1
            if comma_pos == -1:
                left_eq = text.rfind('=', 0, pos)
                if left_comma < left_eq:
                    return False
                else:
                    self.setSelection(left_comma, len(text)-left_comma)
            else:
                self.setSelection(left_comma, comma_pos-left_comma)
        # If equality sign was found select text from the sign untill the
        # next delimiter (comma or eol).
        else:
            comma_pos = text.find(',', eq_pos)
            if comma_pos == -1:
                self.setSelection(eq_pos, len(text)-eq_pos)
            else:
                self.setSelection(eq_pos, comma_pos-eq_pos)
        return True

    def selectionEnd(self):
        """Return the end index of selection or if nothing is selected
        return cursor pos."""
        if self.hasSelectedText():
            return self.selectionStart() + len(self.selectedText())
        else:
            return self.cursorPosition()

    def highlightCompletion(self, new_text):
        """Insert the new part after the cursor position and highlight it
        until the next comma or end of line.
        """
        cursor_pos = self.cursorPosition()
        old_text = self.text()
        self.setText(old_text[:cursor_pos] + new_text[cursor_pos:])
        text = self.text()
        comma_pos = text.find(',', cursor_pos)
        if comma_pos == -1:
            self.setSelection(len(text), cursor_pos-len(text))
        else:
            self.setSelection(comma_pos, cursor_pos-comma_pos)

    def focusInEvent(self, event):
        """Replace the protected internal completion highlighting with our
        own one.
        """
        super(CustomLineEdit, self).focusInEvent(event)
        if self.completer() is not None:
            # Qt should've automatically connected highlighted() to
            # an internal slot, but check just to be sure
            recievers = self.completer().getRecievers("highlighted(QString)")
            if recievers > 0:
                self.completer().highlighted["QString"].disconnect()
            self.connect(self.completer(), QtCore.SIGNAL("highlighted(QString)"),
                         self.highlightCompletion)
