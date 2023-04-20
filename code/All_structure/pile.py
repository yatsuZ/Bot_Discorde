from All_structure.list_trier import Node

class Pile :
    """
    Structure de Pile on peut avoir
    accée qu'au dernier element ajouter
    """
    def __init__(self, data=None):
        if data:
            self.last_push = Node(data)
            self.size = 1
        else:
            self.last_push = None
            self.size = 0
    
    def push(self, data):
        """
        Ajouter un element a la pile.
        """
        N = Node(data)
        if self.last_push != None:
            N.next = self.last_push
        self.last_push = N
        self.size = self.size + 1

    def pop(self, X:int = None) -> Node:
        """
        Avoir accée au X dernier element.
        +
        Les retirer de la pile.
        return un noeud ou une liste de noeud.
        """
        if (X == None or X == 0 ):
            N = self.last_push
            if N == None:
                return N
            self.last_push = N.next
            N.next = None
            self.size = self.size - 1
            return (N)
        else :
            tour = 1
            tete = self.last_push
            current = self.last_push
            while X and current.next:
                tour = tour + 1
                current = current.next
                X = X - 1
            self.last_push = current.next
            current.next = None
            self.size = self.size - tour
            return (tete)

    def get_size(self) -> int:
        """
        Retourne la taille de la Pile.
        """
        return self.size

    def peek(self):
        """
        Avoir accée a la data du dernier element.
        sans le retirer de la pile.
        """
        if (self.last_push):
            return (self.last_push.data)
        return None
    
    def print_peek(self):
        print(self.peek())
    def print_last_POP(self, X:int=None):
        resulta = self.pop(X)
        if resulta:
            print(resulta.data)
        else:
            print(None)

# S = Pile(5)
# # S.push(10)
# # S.print_peek()
# # S.push(32)
# # S.print_peek()
# # print(S.pop().data)
# # S.print_peek()
# # print(S.pop().data)
# # S.print_peek()
# S.push(12)
# S.push(-12)
# S.push(6)
# S.push(-6)
# S.push(3)
# S.push(-3)
# S.push(0)
# print("Taille de la pile = " + str(S.get_size()))
# S.print_last_POP(6)
# print("Taille de la pile = " + str(S.get_size()))
