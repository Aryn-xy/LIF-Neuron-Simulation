import numpy as np
import matplotlib.pyplot as plt

T = 300   #ms
dt = 1  #time step (1 ms)
time = np.arange(0, T + dt, dt)  #time array

#neuron parameters
tau = 10           
V_rest = 0           
V_th = 1              
V_reset = 0     
I = 1.5             

V = np.zeros(len(time))

  # track spike times
spike_times = []

#looping over each time step
for t in range(1, len(time)):
    dV = (-V[t-1] + I) * (dt / tau)
    V[t] = V[t-1] + dV
    if V[t] >= V_th:
        V[t] = V_reset             #reset voltage
        spike_times.append(time[t])     # record spike time

plt.figure(figsize=(10, 4))
plt.plot(time, V, label='Membrane Potential (V)')
plt.axhline(V_th, color='red', linestyle='--', label='Threshold')
plt.xlabel('Time (ms)')
plt.ylabel('Membrane Potential (mV)')
plt.title('Leaky Integrate-and-Fire Neuron')
plt.legend()
plt.grid(True)
plt.show()
print("Spike times:", spike_times)
