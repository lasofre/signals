# -*- coding: utf-8 -*-
import math
import matplotlib.pyplot as plt
import wave
obj = wave.open('in.wav','r')
tm=1/obj.getframerate()
N=obj.getnframes()
muestr=list()
integral=0
trama=0
signal=list()
signal=obj.rewind()
for i in range(0,N):
    integral+=float(signal[i]*tm)
    muestr.append(integral)
plt.subplot(211)
plt.plot(tiemp,signal)
plt.subplot(212)
plt.plot(tiemp,muestr)
plt.show()
