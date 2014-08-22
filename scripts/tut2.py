'Block 0'
'Imports and machine setup'
import sys
sys.path.append('/home/keisano1/Project/pyvafm-master/src')

from vafmbase import ChannelType
from vafmcircuits import Machine
from customs_pll import *
import vafmcircuits

machine = Machine(name='machine', dt = 5.0e-8, pushed=True)


'Block 1'
'Initialisation of circuits and basic setup'
scan = machine.AddCircuit(type='Scanner', name='scan', pushed = True)

# Setup 3D linear interpolation
inter = machine.AddCircuit(type = 'i3Dlin', name = 'inter', components = 3, pushed = True)
inter.Configure(steps = [0.705, 0.705, 0.1], npoints = [8, 8, 201], pbc = [True, True, False])
inter.ReadData('/home/keisano1/Project/UIPyVAFM/scripts/NaClforces.dat')


# Setup output
imager = machine.AddCircuit(type='output', name='imager', file = 'tut2.dat', dump = 0, pushed = True)



'Block 2'
'Connections'
machine.Connect("scan.x", "inter.x")
machine.Connect("scan.y", "inter.y")
machine.Connect("scan.z", "inter.z")
machine.Connect("scan.record", "imager.record")


'Block 3'
'Additional setup'

# Setup scanner
scan.Recorder = imager
scan.BlankLines = True
scan.Resolution = [64, 64]
scan.ImageArea(11.68, 11.68)

# Select registered channels
imager.Register('scan.x', 'scan.y', 'inter.F3')



'Block 4'
'Runtime operations'
scan.Place(x=0, y=0, z=4)
scan.ScanArea()


