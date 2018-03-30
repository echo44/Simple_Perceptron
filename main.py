# -*- coding: utf-8 -*-
import neuron as nrn

v = 0.5

# создали нейрон
neuron = nrn.Neuron()

# создали 2 синапса [значение, вес]
y = [-1, 0.22]
x = [-1, 0.34]

# упакуем их в список для передачи на нейрон
synapses = []
synapses.append(x)
synapses.append(y)

# обучение
while(True):
    neuron.activation(synapses)
    if (neuron.axon <= 0.001):
        print("DONE")
        print(neuron.axon)
        break
    else:
        #print("BAD")
        #print(neuron.axon)
        delta = 0 - neuron.axon
        for s in synapses:
            s[1] += (v * delta) * s[0]

while(True):
    neuron.activation(synapses)
    if (neuron.axon >= 0.999):
        print("DONE")
        print(neuron.axon)
        break
    else:
        #print("BAD")
        #print(neuron.axon)
        delta = 1 - neuron.axon
        for s in synapses:
            s[1] += (v * delta) * s[0]


while(True):
    a = input("ENTER X")
    b = input("ENTER Y")
    synapses[0][0] = a
    synapses[1][0] = b
    neuron.activation(synapses)
    print(neuron.axon)
    if(neuron.axon >= 0.99):
        print("THIS IS 2-nd CLASS")
    if (neuron.axon <= 0.001):
        print("THIS IS 1-st CLASS")