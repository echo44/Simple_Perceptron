# -*- coding: utf-8 -*-
import math


class Neuron():

    def __init__(self):
        self.__axon = 0  # выходное значение

    @property
    def axon(self):
        return self.__axon

    @axon.setter
    def set_axon(self, value):
        self.__axon = value

    def sum(self, synapses):
        """Суммирует произведения весов и значений синопсов"""
        a = 0
        for s in synapses:
            a += float(s[0]) * float(s[1])
        return a

    def activation(self, synapses):
        """Функция активации"""
        a = self.sum(synapses)
        self.__axon = 1 / (1 + math.exp(-a))
        
    def learn_me(self, coor, class_id, synapses, v):
        """Обучение нейрона"""
        synapses[0][0] = coor[0]
        synapses[1][0] = coor[1]
        if (class_id == 1):
            while(True):
                self.activation(synapses)
                if (self.__axon <= 0.001):
                    print("DONE")
                    print(self.__axon)
                    break
                else:
                    delta = 0 - self.__axon
                    for s in synapses:
                        s[1] += (v * delta) * s[0]

        if (class_id == 2):
            while(True):
                self.activation(synapses)
                if (self.__axon >= 0.999):
                    print("DONE")
                    print(self.__axon)
                    break
                else:
                    delta = 1 - self.__axon
                    for s in synapses:
                        s[1] += (v * delta) * s[0]
