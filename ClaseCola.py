import os
#Se utiliza FIFO (First in First Out)

class Node:
    
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Cola:

    def __init__(self):
        self.head = None
        self.last = None

    #AGREGAR UNA PERSONA A LA COLA
    def encolar(self, data):
        node = Node(data)
        if self.last == None:
            self.head = node
            self.last = self.head
        else:
            self.last.next = node
            self.last.next.prev = self.last
            self.last = self.last.next


    #QUITAR UNA PERSONA DE LA COLA (PRIMERA QUE SALE)
    def desencolar(self):
        if self.head == None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp


    #MOSTRAR LA PRIMERA PERSONA EN LA COLA
    def primeroencola(self):
        return self.head.data

    #VERIFICAR SI LA COLA ESTÁ VACÍA
    def ColaVacia(self):

        if self.head==None:
            return True
        else:
            return False


    #IMPRIMIR LA COLA DE LAS PERSONAS
    def imprimirCola(self):
        print("----------------------------")
        print("Las Ordenes en la cola son:")
        print("----------------------------")
        temp=self.head
        while temp != None:
            print(temp.data,end="   le sigue       ")
            temp=temp.next


