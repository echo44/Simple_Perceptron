# -*- coding: utf-8 -*-
import neuron as nrn
import numpy as np
import matplotlib.pyplot as plt
import pylab


def learn_me(coor, class_id):
    synapses[0][0] = coor[0]
    synapses[1][0] = coor[1]
    if (class_id == 1):
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

    if (class_id == 2):
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


def draw_plot():
    for dot in dots:
        if (dot[2] == 1):
            plt.scatter(dot[0], dot[1], color="green")
        if (dot[2] == 2):
            plt.scatter(dot[0], dot[1], color="red")
    x = np.arange(-10, 10, 1)
    plt.plot(x, (-1 * synapses[0][1] * x) / synapses[1][1])
    plt.grid(False)
    labels = ["Classes sep. line", "Green 1-st class", "Red 2-nd class"]
    pylab.legend(labels)
    plt.show()

# константы
v = 0.5  # коэфициент обучения
dots = []  # хранит координаты точек и их класс

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
learn_me([-1, -1], 2)
dots.append([-1, -1, 2])

learn_me([-2, -1], 2)
dots.append([-2, -1, 2])

learn_me([-2, -2], 2)
dots.append([-2, -2, 2])

learn_me([1, 1], 1)
dots.append([1, 1, 1])

learn_me([2, 2], 1)
dots.append([2, 2, 1])

learn_me([1, 0], 1)
dots.append([1, 0, 1])


for i in range(2):
    a = int(input("ENTER X "))
    b = int(input("ENTER Y "))
    synapses[0][0] = a
    synapses[1][0] = b
    neuron.activation(synapses)
    print(neuron.axon)
    if(neuron.axon >= 0.99):
        print("THIS IS 2-nd CLASS")
        dots.append([a, b, 2])
    if (neuron.axon <= 0.001 or neuron.axon == 0.5):
        print("THIS IS 1-st CLASS")
        dots.append([a, b, 1])

draw_plot()
