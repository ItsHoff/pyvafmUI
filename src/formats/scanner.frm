#1
%Name% = machine.AddCircuit(type='Scanner', name='%Name%', $pushed = %Pushed%$)

#3
£%Name%.Place($%Place%$)£
£%Name%.Recorder = $%Recorder%$£
£%Name%.BlankLines = $%BlankLines%$£
£%Name%.Resolution = $[%Resolution%]$£
£%Name%.ImageArea($%ImageArea%$)£

#4
%Name%.ScanArea()
