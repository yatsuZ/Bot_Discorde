from All_structure.list_trier import Node

class Queue :
    """
    Structure de la Queue on peut avoir
    accée qu'au premier element ajouter
    """
    def __init__(self, data):
        self.first_push = Node(data)
        size = 0
    
    def push(self, data):
        """
        Ajouter un element a la queue.
        """
        N = Node(data)
        current = self.first_push
        while current.next:
            current = current.next
        self.size = self.size + 1
        current.next = N

    def pop(self):
        """
        Avoir accée au premier element
        +
        Le retirer de la queue
        """
        if (self.first_push == None):
            return (None)
        N = self.first_push
        self.first_push = N.next
        N.next = None
        self.size = self.size - 1
        return (N)

    def size(self):
        """
        Retourne la taille de la Pile
        """
        return self.size

    def peek(self):
        """
        Avoir accée au premier element
        """
        return (self.first_push)
    
    def print_del(self):
        if (self.first_push == None):
            print("NULL")
            return ()
        print(N.pop().data)

#### Test
# N = Queue(10)
# N.push(1)
# N.push(-2)
# N.push(4)
# N.push(43)
# N.push(2)
# N.print_del()
# N.print_del()
# N.print_del()
# N.print_del()
# N.print_del()
# N.print_del()
# N.print_del()
# N.print_del()
# N.print_del()
