class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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