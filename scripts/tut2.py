'Block #0'
import sys
sys.path.append('/home/keisano1/Project/pyvafm-master/src')

from vafmbase import ChannelType
from vafmcircuits import Machine
from customs_pll import *
import vafmcircuits

machine = Machine(name='machine', dt = 0.01, pushed=True)


'Block #1'
scann = machine.AddCircuit(type='Scanner', name='scann', pushed = True)


inter = machine.AddCircuit(type = 'i3Dlin', name = 'inter', components = 3, pushed = True)
inter.Configure(steps = [0.705, 0.705, 0.1], npoints = [8, 8, 201], pbc = [True, True, False])
inter.ReadData('/home/keisano1/Project/UIPyVAFM/scripts/NaClforces.dat')

image = machine.AddCircuit(type='output', name='image', file = 'tut2.dat', dump = 0, pushed = True)



'Block #2'
machine.Connect("scann.record", "image.record")
machine.Connect("scann.x", "inter.x")
machine.Connect("scann.y", "inter.y")
machine.Connect("scann.z", "inter.z")


'Block #3'
scann.Recorder = image
scann.BlankLines = True
scann.Resolution = [64, 64]
scann.ImageArea(11.68, 11.68)
image.Register('scann.x', 'scann.y', 'inter.F3')




'Block #4'
scann.Place(x=0, y=0, z=4)
scann.ScanArea()


