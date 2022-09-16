#Se utiliza FIFO (First in First Out)
import os

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Cola:

    def __init__(self):
        self.head = None
        self.last = None

    #AGREGAR UNA PERSONA A LA COLA
    def encolar(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last.next.prev = self.last
            self.last = self.last.next

    #QUITAR UNA PERSONA DE LA COLA (PRIMERA QUE SALE)
    def desencolar(self):
        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp


    #MOSTRAR LA PRIMERA PERSONA EN LA COLA
    def primeroencola(self):
        return self.head.data

