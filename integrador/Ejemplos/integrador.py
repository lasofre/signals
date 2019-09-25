# -*- coding: utf-8 -*-
import array
import math
import matplotlib.pyplot as plt
from wave import open as waveOpen
import struct
s = waveOpen('in.wav','rb')
(nc,sw,fr,nf,comptype, compname) = s.getparams( )
print(nc,sw,fr,nf,comptype, compname)
#data = s.readframes(nf)
tm=float(1/fr)
integral=0
data = array.array('h',s.readframes(nf))
s.close()
muestr=array.array('h')
sample=0
g=1000
for i in range(0,nf):
    integral+=float(data[i]*tm)*g
    muestr.append(int(integral))
minimo=muestr[0]
maximo=muestr[0]
for i in range(0,nf):
    if maximo<muestr[i]:
        maximo=muestr[i]
    if minimo>muestr[i]:
        minimo=muestr[i]
print(maximo-minimo)
for i in range(0,nf):
    if (maximo-minimo)>0 and maximo>0 and minimo>0:
        muestr[i]=(muestr[i]-int((maximo-minimo)/2))
    elif minimo<0 and maximo<0 and (minimo-maximo)<0:
        muestr[i]=(muestr[i]-int((minimo-maximo)/2))
    else:
        muestr[i]=int(float(muestr[i])-(maximo+minimo)/nf*i)
f = waveOpen('out.wav', 'w')
f.setparams((nc, sw, fr, nf, "NONE", "Uncompressed"))
f.writeframes(muestr.tostring())
f.close()
plt.subplot(211)
plt.plot(data)
plt.subplot(212)
plt.plot(muestr)
plt.show()

