import numpy as np
import matplotlib.pyplot as plt

from scipy import signal
from matplotlib.widgets import Slider, RadioButtons

fig, ax = plt.subplots()

carrier = 220.0
modulator = 440.0
beta = 1.0

x1 = np.linspace(0.0, 0.03, num=2000)

# np.cos
# signal.square
# signal.sawtooth

carrierWave = np.cos
modulatorWave = np.cos

y1 = carrierWave(carrier * np.pi * x1)
y2 = modulatorWave(modulator * np.pi * x1)
y3 = carrierWave(carrier * np.pi * x1 + beta * y2)

plt.subplots_adjust(left = 0.1, bottom = 0.25)

plt.subplot(3, 1, 1)
carrierObj, = plt.plot(x1, y1, '-')
plt.axis([0, 0.03, -1.1, 1.1])
plt.title('Phase Modulation')
plt.ylabel('Carrier')

plt.subplot(3, 1, 2)
modulatorObj, = plt.plot(x1, y2, '-')
plt.axis([0, 0.03, -1.1, 1.1])
plt.ylabel('Modulator')

plt.subplot(3, 1, 3)
modulatedObj, = plt.plot(x1, y3, '-')
plt.axis([0, 0.03, -1.1, 1.1])
plt.xlabel('time (s)')
plt.ylabel('Modulated Carrier')

axbeta      = plt.axes([0.25, 0.05, 0.6, 0.03])
axcarrier   = plt.axes([0.25, 0.15, 0.6, 0.03])
axmodulator = plt.axes([0.25, 0.10, 0.6, 0.03])

sbeta = Slider(axbeta, "Modulation Index", 0.0, 10.0, valinit=beta, valstep=0.1)
scarrier = Slider(axcarrier, "Carrier Frequency", 0.0, 8000, valinit=carrier, valstep=5)
smodulator = Slider(axmodulator, "Modulator Frequency", 0.0, 8000, valinit=modulator, valstep=5)

def updateBeta(val):
	global beta
	beta = val
	updateModulated()
sbeta.on_changed(updateBeta)

def updateCarrierFrequency(val):
	global carrier
	carrier = val
	updateCarrier()
scarrier.on_changed(updateCarrierFrequency)

def updateModulatorFrequency(val):
	global modulator
	modulator = val
	updateModulator()
smodulator.on_changed(updateModulatorFrequency)

def updateCarrier():
	global carrier, carrierWave, x1, y1, carrierObj
	y1 = carrierWave(carrier * np.pi * x1)
	carrierObj.set_ydata(y1)
	updateModulated()

def updateModulator():
	global modulator, modulatorWave, x1, y2, modulatorObj
	y2 = modulatorWave(modulator * np.pi * x1)
	modulatorObj.set_ydata(y2)
	updateModulated()

def updateModulated():
	global carrier, carrierWave, x1, y2, y3, beta, modulatedObj
	y3 = carrierWave(carrier * np.pi * x1 + beta * y2)
	modulatedObj.set_ydata(y3)
	fig.canvas.draw_idle()
	
raxcarrier = plt.axes([0.9, 0.71, 0.09, 0.15])
rcarrier = RadioButtons(raxcarrier, ('Cosine', 'Sine', 'Square', 'Sawtooth'), active = 0)

def updateCarrierWave(label):
	global carrierWave
	if label == 'Cosine':
		carrierWave = np.cos
	elif label == 'Sine':
		carrierWave = np.sin
	elif label == 'Square':
		carrierWave = signal.square
	elif label == 'Sawtooth':
		carrierWave = signal.sawtooth
	updateCarrier()
rcarrier.on_clicked(updateCarrierWave)

raxmodulator = plt.axes([0.9, 0.5, 0.09, 0.15])
rmodulator = RadioButtons(raxmodulator, ('Cosine', 'Sine', 'Square', 'Sawtooth'), active = 0)

def updateModulatorWave(label):
	global modulatorWave
	if label == 'Cosine':
		modulatorWave = np.cos
	elif label == 'Sine':
		modulatorWave = np.sin
	elif label == 'Square':
		modulatorWave = signal.square
	elif label == 'Sawtooth':
		modulatorWave = signal.sawtooth
	updateModulator()
rmodulator.on_clicked(updateModulatorWave)

plt.show()