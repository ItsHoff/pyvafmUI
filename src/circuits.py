'''
Created on Jun 12, 2014

@author, keisano1
'''
from circuit_info import CircuitInfo
from collections import OrderedDict

machine_param_window_style = OrderedDict([
                            ("PyVAFM src", "DirDialog"),
                            ("dt", "FloatLineEdit"),
                            ("Pushed", "CheckBox")
                            ])

run_time_functions = {"Machine": ["Wait"],
                      "Scanner": ["Place", "Move", "MoveTo", "MoveRecord", "ScanArea"],
                      "output": ["Dump", "Stop", "Start"]
                      }

global_channels = ["time"]

circuits = OrderedDict([
# MATHEMATICS
("opAdd", CircuitInfo("opAdd", "Mathematics",
                     ["in#Factors"],
                     ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "NameLineEdit"),
                                         ("Factors", "IntLineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     default_values = {"Factors": 2},
                     script_format = "formats/opAdd.format"
                     )
 ),
("opSub", CircuitInfo("opSub", "Mathematics",
                     ["in1", "in2"],
                     ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "NameLineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     script_format = "formats/opSub.format"
                     )
 ),
("opMul", CircuitInfo("opMul", "Mathematics",
                     ["in#Factors"],
                     ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "NameLineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     default_values = {"Factors": 2},
                     script_format = "formats/opMul.format"
                     )
 ),
("opDiv", CircuitInfo("opDiv", "Mathematics",
                     ["in1", "in2"],
                     ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "NameLineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     script_format = "formats/opDiv.format"
                     )
 ),
("opLinC", CircuitInfo("opLinC", "Mathematics",
                      ["ina#Factors", "inb#Factors"],
                      ["out"],
                      param_window_style = OrderedDict([
                                          ("Name", "NameLineEdit"),
                                          ("Factors", "IntLineEdit"),
                                          ("Pushed", "CheckBox")
                                          ]),
                      default_values = {"Factors": 2},
                      script_format = "formats/opLinC.format"
                      )
 ),
("opPow", CircuitInfo("opPow", "Mathematics",
                     ["signal"],
                     ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "NameLineEdit"),
                                         ("Power", "FloatLineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     script_format = "formats/opPow.format"
                     )
 ),
("opAbs", CircuitInfo("opAbs", "Mathematics",
                     ["signal"],
                     ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "NameLineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     script_format = "formats/opAbs.format"
                     )
 ),

("Greater or Equal", CircuitInfo("GreaterOrEqual", "Mathematics",
                                ["in1", "in2"],
                                ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "NameLineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     script_format = "formats/GreaterOrEqual.format"
                     )
 ),
("Less or Equal", CircuitInfo("LessOrEqual", "Mathematics",
                             ["in1", "in2"],
                             ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "NameLineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     script_format = "formats/LessOrEqual.format"
                     )),
("Equal", CircuitInfo("Equal", "Mathematics",
                     ["in1", "in2"],
                     ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "NameLineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     script_format = "formats/Equal.format"
                     )
 ),

("Not", CircuitInfo("NOT", "Mathematics",
                   ["signal"],
                   ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "NameLineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     script_format = "formats/NOT.format"
                     )
 ),
("And", CircuitInfo("AND", "Mathematics",
                   ["in#Factors"],
                   ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "NameLineEdit"),
                                         ("Factors", "IntLineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     default_values = {"Factors": 2},
                     script_format = "formats/AND.format"
                     )
 ),
("Or", CircuitInfo("OR", "Mathematics",
                  ["in#Factors"],
                  ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "NameLineEdit"),
                                         ("Factors", "IntLineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     default_values = {"Factors": 2},
                     script_format = "formats/OR.format"
                     )
 ),
("XOr", CircuitInfo("XOR", "Mathematics",
                   ["in#Factors"],
                   ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "NameLineEdit"),
                                         ("Factors", "IntLineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     default_values = {"Factors": 2},
                     script_format = "formats/XOR.format"
                     )
 ),
("NOr", CircuitInfo("NOR", "Mathematics",
                   ["in#Factors"],
                   ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "NameLineEdit"),
                                         ("Factors", "IntLineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     default_values = {"Factors": 2},
                     script_format = "formats/NOR.format"
                     )
 ),

# SIGNAL GENERATION
("Waver", CircuitInfo("waver", "Signal Generation",
                     ["freq", "amp", "offset"],
                     ["sin", "cos", "saw"],
                     param_window_style = OrderedDict([
                                         ("Name", "NameLineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                      script_format = "formats/waver.format"
                      )
 ),
("Square", CircuitInfo("square", "Signal Generation",
                      ["freq", "amp", "offset", "duty"],
                      ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "NameLineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     script_format = "formats/square.format"
                     )
 ),

# SIGNAL PROCESSING
("SKLP", CircuitInfo("SKLP", "Signal Processing",
                    ["signal"],
                    ["out"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("Gain", "IntLineEdit"),
                                        ("Q", "FloatLineEdit"),
                                        ("FCut", "IntLineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/SKLP.format"
                    )
 ),
("SKHP", CircuitInfo("SKHP", "Signal Processing",
                    ["signal"],
                    ["out"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("Gain", "IntLineEdit"),
                                        ("Q", "FloatLineEdit"),
                                        ("FCut", "IntLineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/SKHP.format"
                    )
 ),
("SKBP", CircuitInfo("SKBP", "Signal Processing",
                    ["signal"],
                    ["out"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("Gain", "IntLineEdit"),
                                        ("FC", "IntLineEdit"),
                                        ("Band", "IntLineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/SKBP.format"
                    )
 ),
("RCLP", CircuitInfo("RCLP", "Signal Processing",
                    ["signal"],
                    ["out"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("FCut", "IntLineEdit"),
                                        ("Order", "IntLineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/RCLP.format"
                    )
 ),
("RCHP", CircuitInfo("RCHP", "Signal Processing",
                    ["signal"],
                    ["out"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("FCut", "IntLineEdit"),
                                        ("Order", "IntLineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/RCHP.format"
                    )
 ),

("Avg", CircuitInfo("avg", "Signal Processing",
                    ["signal"],
                    ["out"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("Time", "FloatLineEdit"),
                                        ("Moving", "CheckBox"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/avg.format"
                    )
 ),

("Gain", CircuitInfo("gain", "Signal Processing",
                    ["signal"],
                    ["out"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("Gain", "FloatLineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/gain.format"
                    )
 ),
("Min Max", CircuitInfo("minmax", "Signal Processing",
                    ["signal"],
                    ["max", "min", "amp", "offset"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("CheckTime", "FloatLineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/minmax.format"
                    )
 ),
("Limiter", CircuitInfo("limiter", "Signal Processing",
                    ["signal", "min", "max"],
                    ["out"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/limiter.format"
                    )
 ),
("Derivative", CircuitInfo("derivative", "Signal Processing",
                    ["signal"],
                    ["out"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/derivative.format"
                    )
 ),
("Integral", CircuitInfo("integral", "Signal Processing",
                    ["signal"],
                    ["out"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/integral.format"
                    )
 ),
("Delay", CircuitInfo("delay", "Signal Processing",
                    ["signal"],
                    ["out"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("DelayTime", "IntLineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/delay.format"
                    )
 ),
("Peaker", CircuitInfo("peaker", "Signal Processing",
                    ["signal"],
                    ["tick", "peak", "delay"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("Up", "BitLineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/peaker.format"
                    )
 ),
("Phasor", CircuitInfo("phasor", "Signal Processing",
                      ["in1", "in2"],
                      ["tick", "delay"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/phasor.format"
                    )
 ),
("Flip", CircuitInfo("flip", "Signal Processing",
                    ["signal"],
                    ["out"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/flip.format"
                    )
 ),

# SIGNAL CONTROL
("PI", CircuitInfo("PI", "Signal Control",
                    ["signal", "set", "Ki", "Kp"],
                    ["out"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/PI.format"
                    )
 ),
("PID", CircuitInfo("PID", "Signal Control",
                    ["signal", "set", "Kd", "Ki", "Kp"],
                    ["out"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/PID.format"
                    )
 ),

# OUTPUT
("Output", CircuitInfo("output", "Output",
                      ["record"],
                      [],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("File", "FileLineEdit"),
                                        ("Dump", "IntLineEdit"),
                                        ("Register", "RegisterDialog"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/output.format"
                    )
 ),

# FLIP-FLOPS
("SR Flip Flop", CircuitInfo("SRFlipFlop", "Flip-Flops",
                            ["S", "R", "clock"],
                            ["Q", "Qbar"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/SRFlipFlop.format"
                    )
 ),
("JK Flip Flop", CircuitInfo("JKFlipFlop", "Flip-Flops",
                            ["J", "K", "clock"],
                            ["Q", "Qbar"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/JKFlipFlop.format"
                    )
 ),
("D Flip Flop", CircuitInfo("DFlipFlop", "Flip-Flops",
                           ["D", "clock"],
                           ["Q", "Qbar"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/DFlipFlop.format"
                    )
 ),
("DR Flip Flop", CircuitInfo("DRFlipFlop", "Flip-Flops",
                            ["D", "R", "clock"],
                            ["Q", "Qbar"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/DRFlipFlop.format"
                    )
 ),

# CUSTOM
("aPLL", CircuitInfo("aPLL", "Custom",
                    ["signal1", "signal2", "f0"],
                    ["sin", "cos", "df", "dbg"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("Filters", "TripleIntLineEdit"),
                                        ("Kp", "FloatLineEdit"),
                                        ("Ki", "FloatLineEdit"),
                                        ("Gain", "FloatLineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/aPLL.format"
                    )
 ),
("dPFD", CircuitInfo("dPFD", "Custom",
                    ["ref", "vco", "f0", "KI", "KP"],
                    ["sin", "cos", "df", "dbg"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("Gain", "FloatLineEdit"),
                                        ("Fcut", "IntLineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/dPFD.format"
                    )
 ),
("aAMPD", CircuitInfo("aAMPD", "Custom",
                    ["signal"],
                    ["amp", "norm"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("Fcut", "IntLineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/aAMPD.format"
                    )
 ),

# CANTILEVER
("Simple Cantilever", CircuitInfo("SiCanti", "Cantilever",
                                 ["holderz", "fz", "exciter"],
                                 ["ztip", "zabs", "vz"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("StartingZ", "FloatLineEdit"),
                                        ("Q", "FloatLineEdit"),
                                        ("k", "FloatLineEdit"),
                                        ("f0", "FloatLineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/simple_canti.format"
                    )
 ),
("Advanced Cantilever", CircuitInfo("AdCanti", "Cantilever",
                                   ["exciterz", "excitery", "Holderx",
                                    "Holdery", "Holderz", "ForceV", "ForceL"],
                                   ["zPos", "yPos", "xABS", "yABS", "zABS",
                                    "vV#NumberOfModesV", "vL#NumberOfModesL",
                                    "yL#NumberOfModesL", "zV#NumberOfModesV"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("NumberOfModesV", "IntLineEdit"),
                                        ("NumberOfModesL", "IntLineEdit"),
                                        ("StartingPos", "TripleFloatLineEdit"),
                                        ("Modes", "ModeSetup"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    default_values = {"NumberOfModesV": 1, "NumberOfModesL": 1},
                    script_format = "formats/advanced_canti.format"
                    )
 ),

# INTERPOLATION
("3d Linear Interpolation", CircuitInfo("i3Dlin", "Interpolation",
                                       ["x", "y", "z"],
                                       ["F#Components"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("Components","IntLineEdit"),
                                        ("Steps", "TripleFloatLineEdit"),
                                        ("Npoints", "TripleIntLineEdit"),
                                        ("PBC", "TripleBoolLineEdit"),
                                        ("Force Multiplier", "FloatLineEdit"),
                                        ("Data", "FileDialog"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    default_values = {"Components": 3},
                    script_format = "formats/i3Dlin.format"
                    )
 ),
("1d Linear Interpolation", CircuitInfo("i1Dlin", "Interpolation",
                                       ["x"],
                                       ["F#Components"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("Components", "IntLineEdit"),
                                        ("Step", "FloatLineEdit"),
                                        ("Data", "LineEdit"),
                                        ("PBC", "CheckBox"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    default_values = {"Components": 1},
                    script_format = "formats/i1Dlin.format"
                    )
 ),

# SCANNER
("Scanner", CircuitInfo("Scanner", "Scanner",
                       [],
                       ["x", "y", "z", "record"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("Recorder", "NameLineEdit"),
                                        ("Resolution", "DoubleIntLineEdit"),
                                        ("ImageArea", "DoubleFloatLineEdit"),
                                        ("BlankLines", "CheckBox"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/scanner.format"
                    )
 ),

# VAN DER WALLS
("Van Der Walls Force", CircuitInfo("VDW", "Van Der Walls",
                                   ["ztip"],
                                   ["fz"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("Gamma", "FloatLineEdit"),
                                        ("Hamaker", "FloatLineEdit"),
                                        ("Radius", "FloatLineEdit"),
                                        ("Offset", "FloatLineEdit"),
                                        ("Pushed", "CheckBox"),
                                        ]),
                    script_format = "formats/VDW.format"
                    )
 ),
("VDWtorn", CircuitInfo("VDWtorn", "Van Der Walls",
                                   ["ztip"],
                                   ["fz"],
                    param_window_style = OrderedDict([
                                        ("Name", "NameLineEdit"),
                                        ("A1", "FloatLineEdit"),
                                        ("A2", "FloatLineEdit"),
                                        ("A3", "FloatLineEdit"),
                                        ("A4", "FloatLineEdit"),
                                        ("A5", "FloatLineEdit"),
                                        ("A6", "FloatLineEdit"),
                                        ("Tip Offset", "FloatLineEdit"),
                                        ("Pushed", "CheckBox"),
                                        ]),
                    script_format = "formats/VDWtorn.format"
                    )
 )
])
