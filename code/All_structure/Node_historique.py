import discord

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

    def check_unique(self, data):
        index = self.last_Node
        while index :
            if index.data == data :
                return False
            index = index.next
        return True

    def push_No_double(self, data):
        if (self.check_unique(data)):
            self.push(data)
            return True
        return False

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
    def pop(self):
        if (self.last_Node == None):
            return
        last_node = self.get_lastNode()
        self.del_last_node()
        return last_node
    def get_message(self, Param_U = None, Param_C = None, Param_R = None):
        """
        Retourne le dernier noeud en ayant les parametre valide.
        """

        resu = self.get_lastNode()
        if (Param_U == None and Param_C == None and Param_R == None):
            return resu
        while (resu != None):
            message : discord.Message = resu.get_data()
            channel_message : discord.TextChannel = message.channel
            auteur_message : discord.User = message.author
            member = message.guild.get_member(auteur_message.id)
            if (Param_C is None or channel_message in Param_C) and \
               (Param_U is None or auteur_message in Param_U) and \
               (Param_R is None or any(role in member.roles for role in Param_R)):
                return resu
            resu = resu.next
        return (None)
    
    def del_this_node(self, node: NodeH):
        current_node = self.get_lastNode()

        while current_node is not None:
            if current_node == node:
                if current_node.previous is not None:
                    current_node.previous.next = current_node.next

                if current_node.next is not None:
                    current_node.next.previous = current_node.previous

                current_node.next = None
                current_node.previous = None

                print("Noeud supprimé.")
                return

            current_node = current_node.next

        print("Noeud non trouvé dans la pile.")
