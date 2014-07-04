'''
Created on Jun 12, 2014

@author, keisano1
'''
from circuit_info import CircuitInfo
from collections import OrderedDict

machine_param_window_style = OrderedDict([
                            ("PyVAFM src", "DirDialog"),
                            ("dt", "LineEdit"),
                            ("Wait", "LineEdit"),
                            ("Pushed", "CheckBox")
                            ])

circuits = OrderedDict([
# MATHEMATICS
("opAdd", CircuitInfo("opAdd", "Mathematics",
                     ["in1", "in2"],
                     ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "LineEdit"),
                                         ("Factors", "LineEdit"),
                                         ("In1", "LineEdit"),
                                         ("In2", "LineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     script_format = "formats/opAdd.format"
                     )
 ),
("opSub", CircuitInfo("opSub", "Mathematics",
                     ["in1", "in2"],
                     ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "LineEdit"),
                                         ("In1", "LineEdit"),
                                         ("In2", "LineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     script_format = "formats/opSub.format"
                     )
 ),
("opMul", CircuitInfo("opMul", "Mathematics",
                     ["in1", "in2"],
                     ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "LineEdit"),
                                         ("In1", "LineEdit"),
                                         ("In2", "LineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     script_format = "formats/opMul.format"
                     )
 ),
("opDiv", CircuitInfo("opDiv", "Mathematics",
                     ["in1", "in2"],
                     ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "LineEdit"),
                                         ("In1", "LineEdit"),
                                         ("In2", "LineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     script_format = "formats/opDiv.format"
                     )
 ),
("opLinC", CircuitInfo("opLinC", "Mathematics",
                      ["ina1", "ina2", "inb1", "inb2"],
                      ["out"],
                      param_window_style = OrderedDict([
                                          ("Name", "LineEdit"),
                                          ("Factors", "LineEdit"),
                                          ("Ina1", "LineEdit"),
                                          ("Ina2", "LineEdit"),
                                          ("Inb1", "LineEdit"),
                                          ("Inb2", "LineEdit"),
                                          ("Pushed", "CheckBox")
                                          ]),
                      script_format = "formats/opLinC.format"
                      )
 ),
("opPow", CircuitInfo("opPow", "Mathematics",
                     ["signal"],
                     ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "LineEdit"),
                                         ("Power", "LineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     script_format = "formats/opPow.format"
                     )
 ),
("opAbs", CircuitInfo("opAbs", "Mathematics",
                     ["signal"],
                     ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "LineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     script_format = "formats/opAbs.format"
                     )
 ),

("Greater or Equal", CircuitInfo("GreaterOrEqual", "Mathematics",
                                ["in1", "in2"],
                                ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "LineEdit"),
                                         ("In1", "LineEdit"),
                                         ("In2", "LineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     script_format = "formats/GreaterOrEqual.format"
                     )
 ),
("Less or Equal", CircuitInfo("LessOrEqual", "Mathematics",
                             ["in1", "in2"],
                             ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "LineEdit"),
                                         ("In1", "LineEdit"),
                                         ("In2", "LineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     script_format = "formats/LessOrEqual.format"
                     )),
("Equal", CircuitInfo("Equal", "Mathematics",
                     ["in1", "in2"],
                     ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "LineEdit"),
                                         ("In1", "LineEdit"),
                                         ("In2", "LineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     script_format = "formats/Equal.format"
                     )
 ),

("Not", CircuitInfo("NOT", "Mathematics",
                   ["signal"],
                   ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "LineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     script_format = "formats/NOT.format"
                     )
 ),
("And", CircuitInfo("AND", "Mathematics",
                   ["in1", "in2"],
                   ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "LineEdit"),
                                         ("Factors", "LineEdit"),
                                         ("In1", "LineEdit"),
                                         ("In2", "LineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     script_format = "formats/AND.format"
                     )
 ),
("Or", CircuitInfo("OR", "Mathematics",
                  ["in1", "in2"],
                  ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "LineEdit"),
                                         ("Factors", "LineEdit"),
                                         ("In1", "LineEdit"),
                                         ("In2", "LineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     script_format = "formats/OR.format"
                     )
 ),
("XOr", CircuitInfo("XOR", "Mathematics",
                   ["in1", "in2"],
                   ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "LineEdit"),
                                         ("Factors", "LineEdit"),
                                         ("In1", "LineEdit"),
                                         ("In2", "LineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     script_format = "formats/XOR.format"
                     )
 ),
("NOr", CircuitInfo("NOR", "Mathematics",
                   ["in1", "in2"],
                   ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "LineEdit"),
                                         ("Factors", "LineEdit"),
                                         ("In1", "LineEdit"),
                                         ("In2", "LineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                     script_format = "formats/NOR.format"
                     )
 ),

# SIGNAL GENERATION
("Waver", CircuitInfo("waver", "Signal Generation",
                     ["freq", "amp", "offset"],
                     ["sin", "cos", "saw"],
                     param_window_style = OrderedDict([
                                         ("Name", "LineEdit"),
                                         ("Amp", "LineEdit"),
                                         ("Freq", "LineEdit"),
                                         ("Offset", "LineEdit"),
                                         ("Pushed", "CheckBox")
                                         ]),
                      script_format = "formats/waver.format"
                      )
 ),
("Square", CircuitInfo("square", "Signal Generation",
                      ["freq", "amp", "offset", "duty"],
                      ["out"],
                     param_window_style = OrderedDict([
                                         ("Name", "LineEdit"),
                                         ("Amp", "LineEdit"),
                                         ("Freq", "LineEdit"),
                                         ("Duty", "LineEdit"),
                                         ("Offset", "LineEdit"),
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
                                        ("Name", "LineEdit"),
                                        ("Gain", "LineEdit"),
                                        ("Q", "LineEdit"),
                                        ("FCut", "LineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/SKLP.format"
                    )
 ),
("SKHP", CircuitInfo("SKHP", "Signal Processing",
                    ["signal"],
                    ["out"],
                    param_window_style = OrderedDict([
                                        ("Name", "LineEdit"),
                                        ("Gain", "LineEdit"),
                                        ("Q", "LineEdit"),
                                        ("FCut", "LineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/SKHP.format"
                    )
 ),
("SKBP", CircuitInfo("SKBP", "Signal Processing",
                    ["signal"],
                    ["out"],
                    param_window_style = OrderedDict([
                                        ("Name", "LineEdit"),
                                        ("Gain", "LineEdit"),
                                        ("FC", "LineEdit"),
                                        ("Band", "LineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/SKBP.format"
                    )
 ),
("RCLP", CircuitInfo("RCLP", "Signal Processing",
                    ["signal"],
                    ["out"],
                    param_window_style = OrderedDict([
                                        ("Name", "LineEdit"),
                                        ("FCut", "LineEdit"),
                                        ("Order", "LineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/RCLP.format"
                    )
 ),
("RCHP", CircuitInfo("RCHP", "Signal Processing",
                    ["signal"],
                    ["out"],
                    param_window_style = OrderedDict([
                                        ("Name", "LineEdit"),
                                        ("FCut", "LineEdit"),
                                        ("Order", "LineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/RCHP.format"
                    )
 ),

("Avg", CircuitInfo("avg", "Signal Processing",
                    ["signal"],
                    ["out"],
                    param_window_style = OrderedDict([
                                        ("Name", "LineEdit"),
                                        ("Time", "LineEdit"),
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
                                        ("Name", "LineEdit"),
                                        ("Gain", "LineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/gain.format"
                    )
 ),
("Min Max", CircuitInfo("minmax", "Signal Processing",
                    ["signal"],
                    ["max", "min", "amp", "offset"],
                    param_window_style = OrderedDict([
                                        ("Name", "LineEdit"),
                                        ("CheckTime", "LineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/minmax.format"
                    )
 ),
("Limiter", CircuitInfo("limiter", "Signal Processing",
                    ["signal", "min", "max"],
                    ["out"],
                    param_window_style = OrderedDict([
                                        ("Name", "LineEdit"),
                                        ("Min", "LineEdit"),
                                        ("Max", "LineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/limiter.format"
                    )
 ),
("Derivative", CircuitInfo("derivative", "Signal Processing",
                    ["signal"],
                    ["out"],
                    param_window_style = OrderedDict([
                                        ("Name", "LineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/derivate.format"
                    )
 ),
("Integral", CircuitInfo("integral", "Signal Processing",
                    ["signal"],
                    ["out"],
                    param_window_style = OrderedDict([
                                        ("Name", "LineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/integral.format"
                    )
 ),
("Delay", CircuitInfo("delay", "Signal Processing",
                    ["signal"],
                    ["out"],
                    param_window_style = OrderedDict([
                                        ("Name", "LineEdit"),
                                        ("DelayTime", "LineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/delay.format"
                    )
 ),
("Peaker", CircuitInfo("peaker", "Signal Processing",
                    ["signal"],
                    ["tick", "peak", "delay"],
                    param_window_style = OrderedDict([
                                        ("Name", "LineEdit"),
                                        ("Up", "LineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/peaker.format"
                    )
 ),
("Phasor", CircuitInfo("phasor", "Signal Processing",
                      ["in1", "in2"],
                      ["tick", "delay"],
                    param_window_style = OrderedDict([
                                        ("Name", "LineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/phasor.format"
                    )
 ),
("Flip", CircuitInfo("flip", "Signal Processing",
                    ["signal"],
                    ["out"],
                    param_window_style = OrderedDict([
                                        ("Name", "LineEdit"),
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
                                        ("Name", "LineEdit"),
                                        ("Kp", "LineEdit"),
                                        ("Ki", "LineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/PI.format"
                    )
 ),
("PID", CircuitInfo("PID", "Signal Control",
                    ["signal", "set", "Kd", "Ki", "Kp"],
                    ["out"],
                    param_window_style = OrderedDict([
                                        ("Name", "LineEdit"),
                                        ("Kp", "LineEdit"),
                                        ("Ki", "LineEdit"),
                                        ("Kd", "LineEdit"),
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
                                        ("Name", "LineEdit"),
                                        ("File", "LineEdit"),
                                        ("Dump", "LineEdit"),
                                        ("Register", "LineEdit"),
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
                                        ("Name", "LineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/SRFlipFlop.format"
                    )
 ),
("JK Flip Flop", CircuitInfo("JKFlipFlop", "Flip-Flops",
                            ["J", "K", "clock"],
                            ["Q", "Qbar"],
                    param_window_style = OrderedDict([
                                        ("Name", "LineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/JKFlipFlop.format"
                    )
 ),
("D Flip Flop", CircuitInfo("DFlipFlop", "Flip-Flops",
                           ["D", "clock"],
                           ["Q", "Qbar"],
                    param_window_style = OrderedDict([
                                        ("Name", "LineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/DFlipFlop.format"
                    )
 ),
("DR Flip Flop", CircuitInfo("DRFlipFlop", "Flip-Flops",
                            ["D", "R", "clock"],
                            ["Q", "Qbar"],
                    param_window_style = OrderedDict([
                                        ("Name", "LineEdit"),
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
                                        ("Name", "LineEdit"),
                                        ("Filters", "LineEdit"),
                                        ("Kp", "LineEdit"),
                                        ("Ki", "LineEdit"),
                                        ("Gain", "LineEdit"),
                                        ("f0", "LineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/aPLL.format"
                    )
 ),
("aPFD", CircuitInfo("aPFD", "Custom",
                    ["ref", "vco", "f0", "KI", "KP"],
                    ["sin", "cos", "df", "dbg"],
                    param_window_style = OrderedDict([
                                        ("Name", "LineEdit"),
                                        ("Gain", "LineEdit"),
                                        ("Fcut", "LineEdit"),
                                        ("f0", "LineEdit"),
                                        ("Ki", "LineEdit"),
                                        ("Kp", "LineEdint"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/aPFD.format"
                    )
 ),
("aAMPD", CircuitInfo("aAMPD", "Custom",
                    ["signal"],
                    ["amp", "norm"],
                    param_window_style = OrderedDict([
                                        ("Name", "LineEdit"),
                                        ("Fcut", "LineEdit"),
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
                                        ("Name", "LineEdit"),
                                        ("StartingZ", "LineEdit"),
                                        ("Q", "LineEdit"),
                                        ("k", "LineEdit"),
                                        ("f0", "LineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/simple_canti.format"
                    )
 ),
("Advanced Cantilever", CircuitInfo("AdCanti", "Cantilever",
                                   ["To Do"],
                                   ["To Do"],
                    param_window_style = OrderedDict([
                                        ("Name", "LineEdit"),
                                        ("NumberOfModesV", "LineEdit"),
                                        ("NumberOfModesL", "LineEdit"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/advanced_canti.format"
                    )
 ),

# INTERPOLATION
("3d Linear Interpolation", CircuitInfo("i3Dlin", "Interpolation",
                                       ["x", "y", "z"],
                                       ["F1", "F2", "F3"],
                    param_window_style = OrderedDict([
                                        ("Name", "LineEdit"),
                                        ("Components","LineEdit"),
                                        ("Steps", "LineEdit"),
                                        ("Npoints", "LineEdit"),
                                        ("PBC", "LineEdit"),
                                        ("Force Multiplier", "LineEdit"),
                                        ("Pushed", "CheckBox"),
                                        ("Filename", "FileDialog")
                                        ]),
                    script_format = "formats/i3Dlin.format"
                    )
 ),
("1d Linear Interpolation", CircuitInfo("i1Dlin", "Interpolation",
                                       ["x"],
                                       ["F1", "F2", "F3"],
                    param_window_style = OrderedDict([
                                        ("Name", "LineEdit"),
                                        ("Components", "LineEdit"),
                                        ("Step", "LineEdit"),
                                        ("Filename", "FileDialog"),
                                        ("PBC", "CheckBox"),
                                        ("Pushed", "CheckBox")
                                        ]),
                    script_format = "formats/i1Dlin.format"
                    )
 ),

# SCANNER
("Scanner", CircuitInfo("Scanner", "Scanner",
                       [],
                       ["x", "y", "z", "record"],
                    param_window_style = OrderedDict([
                                        ("Name", "LineEdit"),
                                        ("Place", "LineEdit"),
                                        ("Recorder", "LineEdit"),
                                        ("Resolution", "LineEdit"),
                                        ("ImageArea", "LineEdit"),
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
                                        ("Name", "LineEdit"),
                                        ("Gamma", "LineEdit"),
                                        ("Hamaker", "LineEdit"),
                                        ("Radius", "LineEdit"),
                                        ("Offset", "LineEdit"),
                                        ("Pushed", "CheckBox"),
                                        ]),
                    script_format = "formats/VDW.format"
                    )
 ),
])
