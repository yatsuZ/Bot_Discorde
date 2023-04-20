class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

##################

class list_chained_sorted:
    def __init__(self, data):
        self.first_node = Node(data)

    def add_data(self, data):
        N = Node(data)
        if data < self.first_node.data:
            N.next = self.first_node
            self.first_node = N
            return
        
        current_node = self.first_node
        while current_node.next and current_node.next.data < data :
            current_node = current_node.next
        
        N.next = current_node.next
        current_node.next = N
    
    def print(self):
        current = self.first_node
        while (current):
            print(current.data)
            current = current.next

###############################

class list_chained:
    def __init__(self, data=None):
        if data != None:
            N = Node(data)
            self.first_node = N
            self.end = self.first_node.next
            self.size = 1
        else:
            self.first_node, self.end = None, None
            self.size = 0

    def add_data(self, data):
        N = Node(data)
        if self.first_node == None:
            self.first_node = N
            self.first_node.next = self.end
        else:
            self.last_node = N
            self.last_node = self.last_node.next
        self.size = self.size + 1
    
    def get_by_index(self, i):
        if (i >= self.size):
            print("Erreur Out of range")
            return None
        current = self.first_node
        while (i != 0):
            current = current.next
        return current.data