'Block #0'
import sys
sys.path.append('/home/keisano1/Project/pyvafm-master/src')

from vafmbase import ChannelType
from vafmcircuits import Machine
from customs_pll import *
import vafmcircuits

machine = Machine(name='machine', dt = 5e-8, pushed=True)


'Block #1'
scan = machine.AddCircuit(type='Scanner', name='scan', pushed = True)

canti = machine.AddCircuit(type='Cantilever', name='canti', Q = 42497, k=112.32, f0 = 23065, pushed = True)
machine.AddCircuit(type='Machine', name = 'amp', assembly = aAMPD, fcut=500, pushed = True)
machine.AddCircuit(type='limiter', name='agclim', min = 0, max = 10, pushed = True)
machine.AddCircuit(type='opMul', name='pllinv', in2 = -1, pushed = True)
machine.AddCircuit(type='opMul', name='exc', pushed = True)
machine.AddCircuit(type='PI', name='agc',set = 0.387, Kp = 0.1, Ki = 2.1, pushed = True)
machine.AddCircuit(type='Machine', name = 'pll', assembly = dPFD, fcut=500, gain = 1000, f0 = 23065, KI = 3, KP = 0.5, pushed = True)
machine.AddCircuit(type='VDWtorn', name='Dimer', A1=-0.0166279, A2=0.22753, A3=-1819.29, A4=27055.6, A5=-106878, A6=31.8093, tipoffset=0, pushed=True)
output3 = machine.AddCircuit(type='output', name='output3', file = 'tut4.dat', dump = 0, pushed = True)



'Block #2'
machine.Connect("scan.z", "canti.holderz")
machine.Connect("canti.zabs", "Dimer.ztip")
machine.Connect("Dimer.fz", "canti.fz")
machine.Connect("canti.ztip", "amp.signal")
machine.Connect("amp.amp", "agc.signal")
machine.Connect("amp.norm", "pll.ref")
machine.Connect("pll.cos", "pll.vco")
machine.Connect("agc.out", "agclim.signal")
machine.Connect("agclim.out", "exc.in1")
machine.Connect("pll.sin", "pllinv.in1")
machine.Connect("pllinv.out", "exc.in2")
machine.Connect("exc.out", "canti.exciter")
machine.Connect("scan.record", "output3.record")


'Block #3'
scan.BlankLines = True
output3.Register('scan.z', 'pll.df')




'Block #4'
output3.Stop()
scan.Place(x=0, y=0, z=15)
scan.Move(x=0, y=0, z=-1)
machine.Wait(1)
output3.Start()
scan.MoveRecord(x=0, y=0, z=-9.5,v=1,points=200)


