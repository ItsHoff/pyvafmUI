'''
Created on Jun 12, 2014

@author, keisano1
'''
from circuit_info import CircuitInfo, groups
from collections import OrderedDict

machine_param_window_style = OrderedDict([("PyVAFM src", "DirDialog"),
                                          ("dt", "LineEdit"),
                                          ("Wait", "LineEdit"), 
                                          ("Pushed", "CheckBox")
                                          ])

circuits = OrderedDict([
("opAdd",CircuitInfo("opAdd", "Mathematics", 
                     ["in1", "in2"], 
                     ["out"], 
                     param_window_style = OrderedDict([("Name", "LineEdit"), 
                                                      ("Factors", "LineEdit"),
                                                      ("In1", "LineEdit"), 
                                                      ("In2", "LineEdit"), 
                                                      ("Pushed", "CheckBox")
                                                      ]),
                     script_format = "formats/opAdd.frm"
                                        )),
("opSub",CircuitInfo("opSub", "Mathematics", 
                     ["in1", "in2"], 
                     ["out"], 
                     param_window_style = OrderedDict([("Name", "LineEdit"),
                                                       ("In1", "LineEdit"), 
                                                       ("In2", "LineEdit"), 
                                                       ("Pushed", "CheckBox") 
                                                       ]), 
                     script_format = "formats/opSub.frm"
                                        )),
("opMul",CircuitInfo("opMul", "Mathematics", 
                     ["in1", "in2"], 
                     ["out"], 
                     param_window_style = OrderedDict([("Name", "LineEdit"),
                                                       ("In1", "LineEdit"), 
                                                       ("In2", "LineEdit"), 
                                                       ("Pushed", "CheckBox") 
                                                       ]), 
                     script_format = "formats/opMul.frm"
                                        )),
("opDiv",CircuitInfo("opDiv", "Mathematics", 
                     ["in1", "in2"], 
                     ["out"],
                     param_window_style = OrderedDict([("Name", "LineEdit"),
                                                       ("In1", "LineEdit"), 
                                                       ("In2", "LineEdit"), 
                                                       ("Pushed", "CheckBox") 
                                                       ]),
                     script_format = "formats/opDiv.frm"
                                        )),
("opLinC",CircuitInfo("opLinC", "Mathematics", 
                      ["ina1", "ina2", "inb1", "inb2"], 
                      ["out"], 
                      param_window_style = OrderedDict([("Name", "LineEdit"),
                                                       ("Factors", "LineEdit"),
                                                       ("Ina1", "LineEdit"), 
                                                       ("Ina2", "LineEdit"),
                                                       ("Inb1", "LineEdit"), 
                                                       ("Inb2", "LineEdit"),  
                                                       ("Pushed", "CheckBox") 
                                                       ]),
                      script_format = "formats/opLinC.frm"
                                        )),
("opPow",CircuitInfo("opPow", "Mathematics", 
                     ["signal"], 
                     ["out"],
                     param_window_style = OrderedDict([("Name", "LineEdit"),
                                                       ("Power", "LineEdit"),
                                                       ("Pushed", "CheckBox") 
                                                       ])
                                        )),
("opAbs",CircuitInfo("opAbs", "Mathematics", 
                     ["signal"], 
                     ["out"],
                     param_window_style = OrderedDict([("Name", "LineEdit"),
                                                       ("Pushed", "CheckBox") 
                                                       ])
                                        )),

("Greater or Equal",CircuitInfo("GreaterOrEqual", "Mathematics", 
                                ["in1", "in2"], 
                                ["out"],
                     param_window_style = OrderedDict([("Name", "LineEdit"),
                                                       ("In1", "LineEdit"), 
                                                       ("In2", "LineEdit"), 
                                                       ("Pushed", "CheckBox") 
                                                       ])
                                        )),
("Less or Equal",CircuitInfo("LessOrEqual", "Mathematics", 
                             ["in1", "in2"], 
                             ["out"],
                     param_window_style = OrderedDict([("Name", "LineEdit"),
                                                       ("In1", "LineEdit"), 
                                                       ("In2", "LineEdit"), 
                                                       ("Pushed", "CheckBox") 
                                                       ])
                                        )),
("Equal",CircuitInfo("Equal", "Mathematics", 
                     ["in1", "in2"], 
                     ["out"],
                     param_window_style = OrderedDict([("Name", "LineEdit"),
                                                       ("In1", "LineEdit"), 
                                                       ("In2", "LineEdit"), 
                                                       ("Pushed", "CheckBox") 
                                                       ])
                                        )),

("Not",CircuitInfo("NOT", "Mathematics", 
                   ["signal"], 
                   ["out"],
                     param_window_style = OrderedDict([("Name", "LineEdit"),
                                                       ("Pushed", "CheckBox") 
                                                       ])
                                        )), 
("And",CircuitInfo("AND", "Mathematics", 
                   ["in1", "in2"], 
                   ["out"],
                     param_window_style = OrderedDict([("Name", "LineEdit"),
                                                       ("Factors", "LineEdit"),
                                                       ("In1", "LineEdit"), 
                                                       ("In2", "LineEdit"), 
                                                       ("Pushed", "CheckBox") 
                                                       ])
                                        )), 
("Or",CircuitInfo("OR", "Mathematics",
                  ["in1", "in2"], 
                  ["out"],
                     param_window_style = OrderedDict([("Name", "LineEdit"),
                                                       ("Factors", "LineEdit"),
                                                       ("In1", "LineEdit"), 
                                                       ("In2", "LineEdit"), 
                                                       ("Pushed", "CheckBox") 
                                                       ])
                                        )), 
("XOr",CircuitInfo("XOR", "Mathematics", 
                   ["in1", "in2"], 
                   ["out"],
                     param_window_style = OrderedDict([("Name", "LineEdit"),
                                                       ("Factors", "LineEdit"),
                                                       ("In1", "LineEdit"), 
                                                       ("In2", "LineEdit"), 
                                                       ("Pushed", "CheckBox") 
                                                       ])
                                        )), 
("NOr",CircuitInfo("NOR", "Mathematics",
                   ["in1", "in2"], 
                   ["out"],
                     param_window_style = OrderedDict([("Name", "LineEdit"),
                                                       ("Factors", "LineEdit"),
                                                       ("In1", "LineEdit"), 
                                                       ("In2", "LineEdit"), 
                                                       ("Pushed", "CheckBox") 
                                                       ])
                                        )), 


("Waver",CircuitInfo("waver", "Signal Generation", 
                     ["freq", "amp", "offset"], 
                     ["sin", "cos", "saw"],
                     param_window_style = OrderedDict([("Name", "LineEdit"),
                                                       ("Amp", "LineEdit"),
                                                       ("Freq", "LineEdit"),
                                                       ("Offset", "LineEdit"),
                                                       ("Pushed", "CheckBox") 
                                                       ]),
                      script_format = "formats/waver.frm"
                                        )), 
("Square",CircuitInfo("square", "Signal Generation", 
                      ["freq", "amp", "offset", "duty"], 
                      ["out"],
                     param_window_style = OrderedDict([("Name", "LineEdit"),
                                                       ("Amp", "LineEdit"),
                                                       ("Freq", "LineEdit"),
                                                       ("Duty", "LineEdit"), 
                                                       ("Offset", "LineEdit"),
                                                       ("Pushed", "CheckBox") 
                                                       ])
                                        )), 


("SKLP",CircuitInfo("SKLP", "Signal Processing",
                    ["signal"], 
                    ["out"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"),
                                                      ("Gain", "LineEdit"),
                                                      ("Q", "LineEdit"), 
                                                      ("FCut", "LineEdit"), 
                                                      ("Pushed", "CheckBox")
                                                      ])
                                        )),
("SKHP",CircuitInfo("SKHP", "Signal Processing",
                    ["signal"], 
                    ["out"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"),
                                                      ("Gain", "LineEdit"),
                                                      ("Q", "LineEdit"), 
                                                      ("FCut", "LineEdit"), 
                                                      ("Pushed", "CheckBox")
                                                      ])
                                        )),
("SKBP",CircuitInfo("SKBP", "Signal Processing",
                    ["signal"], 
                    ["out"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"),
                                                      ("Gain", "LineEdit"), 
                                                      ("FC", "LineEdit"), 
                                                      ("Pushed", "CheckBox")
                                                      ])
                                        )),
("RCLP",CircuitInfo("RCLP", "Signal Processing",
                    ["signal"], 
                    ["out"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"),
                                                      ("FCut", "LineEdit"), 
                                                      ("Order", "LineEdit"),
                                                      ("Pushed", "CheckBox")
                                                      ])
                                        )),
("RCHP",CircuitInfo("RCHP", "Signal Processing",
                    ["signal"], 
                    ["out"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"),
                                                      ("FCut", "LineEdit"), 
                                                      ("Order", "LineEdit"), 
                                                      ("Pushed", "CheckBox")
                                                      ])
                                        )),

("Avg",CircuitInfo("avg", "Signal Processing",
                    ["signal"], 
                    ["out"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"),
                                                      ("Time", "LineEdit"),
                                                      ("Moving", "CheckBox"), 
                                                      ("Pushed", "CheckBox")
                                                      ])
                                        )),

("Gain",CircuitInfo("gain", "Signal Processing",
                    ["signal"], 
                    ["out"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"),
                                                      ("Gain", "LineEdit"), 
                                                      ("Pushed", "CheckBox")
                                                      ])
                                        )),
("Min Max",CircuitInfo("minmax", "Signal Processing",
                    ["signal"], 
                    ["max", "min", "amp", "offset"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"),
                                                      ("CheckTime", "LineEdit"), 
                                                      ("Pushed", "CheckBox")
                                                      ])
                                        )),
("Limiter",CircuitInfo("limiter", "Signal Processing",
                    ["signal", "min", "max"], 
                    ["out"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"),
                                                      ("Min", "LineEdit"),
                                                      ("Max", "LineEdit"), 
                                                      ("Pushed", "CheckBox")
                                                      ]), 
                       script_format = "formats/limiter.frm"
                                        )),
("Derivative",CircuitInfo("derivative", "Signal Processing",
                    ["signal"], 
                    ["out"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"), 
                                                      ("Pushed", "CheckBox")
                                                      ])
                                        )),
("Integral",CircuitInfo("integral", "Signal Processing",
                    ["signal"], 
                    ["out"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"), 
                                                      ("Pushed", "CheckBox")
                                                      ])
                                        )),
("Delay",CircuitInfo("delay", "Signal Processing",
                    ["signal"], 
                    ["out"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"),
                                                      ("DelayTime", "LineEdit"), 
                                                      ("Pushed", "CheckBox")
                                                      ])
                                        )),
("Peaker",CircuitInfo("peaker", "Signal Processing",
                    ["signal"], 
                    ["tick", "peak", "delay"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"),
                                                      ("Up", "LineEdit"), 
                                                      ("Pushed", "CheckBox")
                                                      ])
                                        )),
("Phasor",CircuitInfo("phasor", "Signal Processing", 
                      ["in1", "in2"], 
                      ["tick", "delay"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"), 
                                                      ("Pushed", "CheckBox")
                                                      ])
                                        )),
("Flip",CircuitInfo("flip", "Signal Processing",
                    ["signal"], 
                    ["out"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"), 
                                                      ("Pushed", "CheckBox")
                                                      ])
                                        )),


("PI",CircuitInfo("PI", "Signal Control",
                    ["signal", "set", "Ki", "Kp"], 
                    ["out"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"),
                                                      ("Kp", "LineEdit"), 
                                                      ("Ki", "LineEdit"), 
                                                      ("Pushed", "CheckBox")
                                                      ]), 
                  script_format = "formats/PI.frm"
                                        )),
("PID",CircuitInfo("PID", "Signal Control",
                    ["signal", "set", "Kd", "Ki", "Kp"], 
                    ["out"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"), 
                                                      ("Kp", "LineEdit"), 
                                                      ("Ki", "LineEdit"),
                                                      ("Kd", "LineEdit"),
                                                      ("Pushed", "CheckBox")
                                                      ])
                                        )),


("Output",CircuitInfo("output", "Output", 
                      ["record"], 
                      [], 
                    param_window_style = OrderedDict([("Name", "LineEdit"),
                                                      ("File", "LineEdit"),
                                                      ("Dump", "LineEdit"),
                                                      ("Register", "LineEdit"), 
                                                      ("Pushed", "CheckBox")
                                                      ]),
                      script_format = "formats/output.frm"
                                        )),


("SR Flip Flop",CircuitInfo("SRFlipFlop", "Flip-Flops", 
                            ["S", "R", "clock"], 
                            ["Q", "Qbar"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"), 
                                                      ("Pushed", "CheckBox")
                                                      ])
                                        )), 
("JK Flip Flop",CircuitInfo("JKFlipFlop", "Flip-Flops", 
                            ["J", "K", "clock"], 
                            ["Q", "Qbar"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"), 
                                                      ("Pushed", "CheckBox")
                                                      ])
                                        )),
("D Flip Flop",CircuitInfo("DFlipFlop", "Flip-Flops", 
                           ["D", "clock"], 
                           ["Q", "Qbar"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"), 
                                                      ("Pushed", "CheckBox")
                                                      ])
                                        )),
("DR Flip Flop",CircuitInfo("DRFlipFlop", "Flip-Flops", 
                            ["D", "R", "clock"], 
                            ["Q", "Qbar"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"), 
                                                      ("Pushed", "CheckBox")
                                                      ])
                                        )),


("aPLL",CircuitInfo("aPLL", "Custom", 
                    ["signal1", "signal2", "f0"], 
                    ["sin", "cos", "df", "dbg"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"),
                                                      ("Filters", "LineEdit"), 
                                                      ("Kp", "LineEdit"), 
                                                      ("Ki", "LineEdit"),
                                                      ("Gain", "LineEdit"), 
                                                      ("f0", "LineEdit"),
                                                      ("Pushed", "CheckBox")
                                                      ]),
                    script_format = "formats/aPLL.frm"
                                        )),
("aPFD",CircuitInfo("aPFD", "Custom", 
                    ["ref", "vco", "f0", "KI", "KP"], 
                    ["sin", "cos", "df", "dbg"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"),
                                                      ("Gain", "LineEdit"),
                                                      ("Fcut", "LineEdit"), 
                                                      ("Pushed", "CheckBox")
                                                      ])
                                        )),
("aAMPD",CircuitInfo("aAMPD", "Custom", 
                    ["signal"], 
                    ["amp", "norm"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"),
                                                      ("Fcut", "LineEdit"), 
                                                      ("Pushed", "CheckBox")
                                                      ]), 
                     script_format = "formats/aAMPD.frm"
                                        )),


("Simple Cantilever",CircuitInfo("SiCanti", "Cantilever", 
                                 ["holderz", "fz", "exciter"], 
                                 ["ztip", "zabs", "vz"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"),
                                                      ("StartingZ", "LineEdit"),
                                                      ("Q", "LineEdit"),
                                                      ("k", "LineEdit"), 
                                                      ("f0", "LineEdit"), 
                                                      ("Pushed", "CheckBox")
                                                      ]), 
                                 script_format = "formats/simple_canti.frm"
                                        )),
("Advanced Cantilever",CircuitInfo("AdCanti", "Cantilever", 
                                   ["To Do"], 
                                   ["To Do"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"),
                                                      ("NumberOfModesV", "LineEdit"), 
                                                      ("NumberOfModesL", "LineEdit"), 
                                                      ("Pushed", "CheckBox")
                                                      ])
                                        )),


("3d Linear Interpolation",CircuitInfo("i3Dlin", "Interpolation", 
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
                                       script_format = "formats/3Dlin.frm"
                                                                         
                                       )
),
("1d Linear Interpolation",CircuitInfo("i1Dlin", "Interpolation", 
                                       ["x"], 
                                       ["Fn"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"),
                                                      ("Components", "LineEdit"),
                                                      ("Step", "LineEdit"),
                                                      ("PBC", "CheckBox"), 
                                                      ("Pushed", "CheckBox")
                                                      ])
                                        )),


("Scanner",CircuitInfo("Scanner", "Scanner", 
                       [], 
                       ["x", "y", "z", "record"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"),
                                                      ("Place", "LineEdit"),
                                                      ("Recorder", "LineEdit"),
                                                      ("Resolution", "LineEdit"),
                                                      ("ImageArea", "LineEdit"),
                                                      ("BlankLines", "CheckBox"), 
                                                      ("Pushed", "CheckBox")
                                                      ]),
                       script_format = "formats/scanner.frm"
                                        )),


("Van Der Walls Force",CircuitInfo("VDW", "Van Der Walls", 
                                   ["ztip"], 
                                   ["fz"], 
                    param_window_style = OrderedDict([("Name", "LineEdit"),
                                                      ("Gamma", "LineEdit"),
                                                      ("Hamaker", "LineEdit"),
                                                      ("Radius", "LineEdit"),
                                                      ("Offset", "LineEdit"), 
                                                      ("Pushed", "CheckBox")
                                                      ])
                                        )),
])
