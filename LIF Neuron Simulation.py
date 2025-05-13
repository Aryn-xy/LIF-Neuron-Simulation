import numpy as np
import matplotlib.pyplot as plt

#Simulation parameterss
T = 300   # Total time to simulate (in ms)
dt = 1  # Time step (1 ms)
time = np.arange(0, T + dt, dt)  # Time array

#neuron parameters
tau = 10            # membrane time Constant (ms)
V_rest = 0           # resting potential (mV)
V_th = 1              # threshold potential (mV)
V_reset = 0          # reset potential after spike (mV)
I = 1.5              # Constant input current (arbitrary units)

#Initialize membrane potential array
V = np.zeros(len(time))

# track spike times
spike_times = []

#looping over each time step
for t in range(1, len(time)):
    # Calculate change in V using LIF formula
    dV = (-V[t-1] + I) * (dt / tau)
    V[t] = V[t-1] + dV

    #Check for spike
    if V[t] >= V_th:
        V[t] = V_reset             # Reset voltage
        spike_times.append(time[t])  # Record spike time

# ploting Membrane potential
plt.figure(figsize=(10, 4))
plt.plot(time, V, label='Membrane Potential (V)')
plt.axhline(V_th, color='red', linestyle='--', label='Threshold')
plt.xlabel('Time (ms)')
plt.ylabel('Membrane Potential (mV)')
plt.title('Leaky Integrate-and-Fire Neuron')
plt.legend()
plt.grid(True)
plt.show()

# Print spike times
print("Spike times:", spike_times)
