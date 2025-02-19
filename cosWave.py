import matplotlib.pyplot as plot
import numpy as np

time = np.arange(0, 20.1, 0.1)
amplitude = np.cos(time)

plot.plot(time, amplitude)
plot.ylabel("Amplitude = sin(time)")
plot.title("Cos Wave")
plot.xlabel("Time")
plot.grid(True, which='both')
plot.axhline(y=0, color="k")
plot.show()