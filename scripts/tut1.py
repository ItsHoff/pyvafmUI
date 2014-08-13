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
machine.AddCircuit(type='opAdd', name = 'Add', factors = 2, pushed = True)
output3 = machine.AddCircuit(type='output', name='output3', file = 'tut1.dat', dump = 1, pushed = True)



'Block #2'
machine.Connect("wave.sin", "Add.in1")
machine.Connect("wave.sin", "Add.in2")


'Block #3'

output3.Register('global.time', 'wave.sin', 'Add.out')



'Block #4'
machine.Wait(5)


