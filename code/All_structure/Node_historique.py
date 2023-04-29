class NodeH:
    """
    Les noeuds contenant les donnée
    """
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def get_data(self):
        return self.data

class PileH:
    def __init__(self):
        self.size = 0
        self.last_Node = None

    def push(self, data):
        new_node = NodeH(data)
        
        self.size =+ 1
        
        if (self.last_Node == None):
            self.last_Node = new_node
            return
        
        self.last_Node.previous = new_node
        new_node.next = self.last_Node
        self.last_Node = new_node
    
    def del_last_node(self):
        if (self.last_Node == None):
            return
        self.last_Node = self.last_Node.next
        self.size = self.size - 1

    def get_size(self): return self.size
    def get_lastNode(self): return self.last_Node