from list_trier import Node

class Stack :
    """
    Structure de Pile on peut avoir
    accée qu'au dernier element ajouter
    """
    def __init__(self, data):
        self.last_push = Node(data)
        size = 0
    
    def push(self, data):
        """
        Ajouter un element a la pile.
        """
        N = Node(data)
        N.next = self.last_push
        size+=1
        self.last_push = N

    def pop(self):
        """
        Avoir accée au dernier element
        +
        Le retirer de la pile
        """
        N = self.last_push
        self.last_push = N.next
        N.next = None
        size-=1
        return (N)

    def size(self):
        """
        Retourne la taille de la Pile
        """
        return self.size

    def peek(self):
        """
        Avoir accée au dernier element
        """
        return (self.last_push)
