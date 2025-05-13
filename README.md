# Leaky Integrate & Fire (LIF) Neuron Simulation

A simulated neuron model that integrates incoming current (input), gradually loses voltage due to leakiness, and generates a spike when the membrane potential crosses a threshold.

## Works

- Neuron receives an  input current
- Membrane potential increases gradually.
- If the threshold is crossed, it fires and resets
- All spike times are plotted.
- The neuron updates using the differential equation :

### Equation

```
dV = (-V + I) * (dt / tau)
```
### Notations

- `V` : Membrane potential (voltage)
- `I` : Input current
- `tau` : Membrane time constant (leakiness)
- `dt` : Time step (simulation resolution)
- `dV` : Change in membrane potential during one time step
