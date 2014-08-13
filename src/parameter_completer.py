"""Module containing the ParameterCompleter."""

from PyQt4 import QtGui


class ParameterCompleter(QtGui.QCompleter):
    """Completer to match ',' separated string with a tree model of strings."""

    def __init__(self):
        super(ParameterCompleter, self).__init__()

    def splitPath(self, path):
        """Split the path to list of its components."""
        split = path.split(',')
        # Strip the individual items of white space and
        # values given after '=' sign.
        for item in split:
            item_index = split.index(item)
            item = item.strip()
            eq_index = item.find('=')
            if eq_index != -1:
                item = item[:eq_index+1]
            split[item_index] = item
        return split

    def pathFromIndex(self, index):
        """Return the text that is inserted when the item given by index
        is selected."""
        prefix = self.completionPrefix()
        prefix_split = prefix.split(",")
        # If the last item allready contains the index data
        # nothing should be inserted.
        if prefix_split[-1].find(index.data()) != -1:
            return None
        # Strip the last item of partial index data so
        # the text won't be dublicated.
        prefix_split[-1] = prefix_split[-1].strip(index.data())
        prefix = ",".join(prefix_split)
        return prefix + index.data()
