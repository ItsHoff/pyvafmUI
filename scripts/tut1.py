'Block #0'
import sys
sys.path.append('/home/keisano1/Project/pyvafm-master/src')

from vafmbase import ChannelType
from vafmcircuits import Machine
from customs_pll import *
import vafmcircuits

machine = Machine(name='machine', dt = 0.01, pushed=True)


'Block #1'
machine.AddCircuit(type='waver', name='wave', amp=1, freq=2, pushed = True)
machine.AddCircuit(type='opAdd', name = 'opAdd2', factors = 2, pushed = True)
output = machine.AddCircuit(type='output', name='output', file = 'tut1.dat', dump = 1, pushed = True)



'Block #2'
machine.Connect("wave.sin", "opAdd2.in2")
machine.Connect("wave.sin", "opAdd2.in1")


'Block #3'

output.Register('global.time', 'wave.sin', 'opAdd2.out')



'Block #4'
machine.Wait(5)


