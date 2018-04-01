# -*- coding: utf-8 -*-
import neuron as nrn
import numpy as np
import matplotlib.pyplot as plt
import pylab


def draw_plot():
    """Рисует точки на координатной плоскости"""
    for dot in dots:
        if (dot[2] == 1):
            plt.scatter(dot[0], dot[1], color="green")
        if (dot[2] == 2):
            plt.scatter(dot[0], dot[1], color="red")
    x = np.arange(-10, 10, 1)
    plt.plot(x, (-1 * synapses[0][1] * x) / synapses[1][1])  # рисуем линию разделения 2-х классов
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
neuron.learn_me([-1, -1], 2, synapses, v)
dots.append([-1, -1, 2])

neuron.learn_me([-2, -1], 2, synapses, v)
dots.append([-2, -1, 2])

neuron.learn_me([-2, -2], 2, synapses, v)
dots.append([-2, -2, 2])

neuron.learn_me([1, 1], 1, synapses, v)
dots.append([1, 1, 1])

neuron.learn_me([2, 2], 1, synapses, v)
dots.append([2, 2, 1])

neuron.learn_me([1, 0], 1, synapses, v)
dots.append([1, 0, 1])


for i in range(2):  # вводим 2 точки
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
