#1
%Name% = machine.AddCircuit(type = 'i3Dlin', name = '%Name%', $components = %Components%$, $pushed = %Pushed%$)

£%Name%.Configure($steps = [%Steps%]$, $npoints = [%Npoints%]$, $pbc = [%PBC%]$, $ForceMultiplier = %ForceMultiplier%$)£
£%Name%.ReadData($'%Filename%'$)£
