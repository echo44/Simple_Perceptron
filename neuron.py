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
