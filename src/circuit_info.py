'''
Created on Jun 12, 2014

@author: keisano1
'''

GENERAL = 0
MATHEMATICS = 1
SIGNAL_GENERATION = 2
SIGNAL_PROCESSING = 3
SIGNAL_CONTROL = 4
FLIPFLOPS = 5

groups = ["Mathematics", "Signal Generation", "Signal Processing", 
          "Signal Control", "Output", "Flip-Flops", "Custom", "Cantilever",
          "Interpolation", "Scanner", "Van Der Walls", "Recently Used"]


class CircuitInfo(object):
    '''
    classdocs
    '''


    def __init__(self, name, io_type, inputs = [], outputs = [], param_window_style={}, script_format = None):
        '''
        Constructor
        '''
        self.circuit_name = name
        self.io_type = io_type
        self.params = []
        self.default_values = []
        self.param_window_style = param_window_style
        self.script_format = script_format
        self.inputs = inputs
        self.outputs = outputs