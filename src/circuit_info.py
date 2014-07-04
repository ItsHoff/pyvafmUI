'''
Created on Jun 12, 2014

@author: keisano1
'''

groups = ["Mathematics", "Signal Generation", "Signal Processing",
          "Signal Control", "Output", "Flip-Flops", "Custom", "Cantilever",
          "Interpolation", "Scanner", "Van Der Walls", "Recently Used"]


class CircuitInfo(object):
    """Container for all the general circuit parameters."""

    def __init__(self, name, io_type, inputs=[], outputs=[],
                 param_window_style={}, script_format=None):
        """Save all the parameters."""
        self.circuit_name = name
        self.io_type = io_type
        self.params = []
        self.default_values = []
        self.param_window_style = param_window_style
        self.script_format = script_format
        self.inputs = inputs
        self.outputs = outputs
