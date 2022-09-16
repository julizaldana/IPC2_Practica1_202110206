#Se utiliza FIFO (First in First Out)

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



