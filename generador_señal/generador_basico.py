import math, wave, array
import matplotlib.pyplot as plt
tipe=str(input("Tipo de señal(Rectangular|Seno|Coseno|Triangular): "))
freq=int(input("Frecuencia: "))
try:
    
    sampleRate=int(input("Numero de muestras por segundo: "))
except:
    sampleRate = 44100
try:
    volume=int(input("Volumen de 0 a 100 (por defecto 50%):"))
except:
    volume=50
duration=int(input("Durasion: "))
#Constantes
data = array.array('h')
numChan=1
dataSize = 2
numSamplesPerCyc = int(sampleRate / freq)
numSamples = sampleRate * duration
cont_a=0
y=0
t=list()
for i in range(numSamples):
    sample = 32767 * float(volume) / 100
    if tipe== 's'or tipe=='S':
        sample *= math.sin(2*math.pi*(i%numSamplesPerCyc)/ numSamplesPerCyc)
        data.append(int(sample))
    if tipe== 'c'or tipe=='C':
        sample *= math.cos(2*math.pi*(i%numSamplesPerCyc)/ numSamplesPerCyc)
        data.append(int(sample))
    if tipe== 'R' or tipe== 'r':
        if cont_a<=numSamplesPerCyc/2:
            sample = 32767 * float(volume) / 100
            data.append(int(sample))
            cont_a+=1
        elif cont_a<=numSamplesPerCyc:
            sample = -32767 * float(volume) / 100
            data.append(int(sample))
            cont_a+=1
        else:
            cont_a=0
    if tipe== 'T' or tipe== 't':
        if cont_a<numSamplesPerCyc/4 or (numSamplesPerCyc*3)/4 < cont_a<=numSamplesPerCyc:
            sample = 32767 * float(volume) / 100
            y=sample*cont_a/(numSamplesPerCyc/4)
            print(int(y))
            data.append(int(y))
            cont_a+=1
            
        elif cont_a<=(numSamplesPerCyc*3)/4:
            sample = -32767 * float(volume) / 100
            y=(sample/(numSamplesPerCyc*3/4))*cont_a
            data.append(int(y))
            cont_a+=1
        else:
            cont_a=0
    t.append(float(float(1/44100)*i))
f = wave.open('SineWave_' + str(freq) +'_'+tipe+ '_Hz.wav', 'w')
f.setparams((numChan, dataSize, sampleRate, numSamples, "NONE", "Uncompressed"))
f.writeframes(data.tostring())
f.close()
plt.subplot(111)
plt.plot(t,data)
plt.show()
