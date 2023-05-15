class Dico: 
    def __init__(self):
        self.buckets = []
        self.size = 0

    def colision(self, index, tab=None) -> int:
        """
        Lorsqu'on assigne une clé, si la clé est déjà prise, on doit faire un décalage en cas de collision.
        """
        if tab is not None:
            buck = tab
        else:
            buck = self.buckets

        plus = 0
        moin = 0
        while True:
            if index + plus < len(buck) and buck[index + plus] is None:
                index = index + plus
                break
            if index - moin >= 0 and buck[index - moin] is None:
                index = index - moin
                break

            moin = moin + 1
            if plus < self.size:
                plus = plus + 1

        return index

    def realocate(self):
        """
        Si on ajoute un nouvelle element alors il fodra modifier le modulo qui et la taille de la liste
        donc re alouer lindex de tout les éléments.
        """
        new_buckets = [None] * (self.size + 1)
        for paire in self.buckets:
            key = paire[0]
            indice_key = hash(key) % (self.size + 1)
            if (new_buckets[indice_key] != None):
                indice_key = self.colision(indice_key, new_buckets)
            new_buckets[indice_key] =(paire[0], paire[1])
        self.size = self.size + 1
        self.buckets = new_buckets
 
    def append(self, key, data):
        """
        Ajoute une clée et une donnée
        """
        self.realocate()
        hashed_key = hash(key)
        indice_bucket = hashed_key % self.size
        if (self.buckets[indice_bucket] != None):
            if (self.buckets[indice_bucket][0] == key):
                print("Meme Clée problème key = ", key)
                return None
            indice_bucket = self.colision(indice_bucket)
        self.buckets[indice_bucket] = (key,data)

    def get_colision(self, indice_bucket, key : int):
        plus = 1
        moin = -1
        while (indice_bucket + plus < self.size or indice_bucket + moin >= 0):
            if (indice_bucket + plus < self.size and self.buckets[indice_bucket + plus][0] == key): return self.buckets[indice_bucket + plus]
            elif(indice_bucket + moin >= 0 and self.buckets[indice_bucket + moin][0] == key): return self.buckets[indice_bucket + moin]
            else:
                moin = moin - 1
                plus = plus + 1
        return None

    def get(self, key):
        if (self.size == 0): return None
        hashed_key = hash(key)
        indice_bucket = hashed_key % self.size
        if (self.buckets[indice_bucket] == None or self.size <= indice_bucket): return None
        if (self.buckets[indice_bucket][0] == key):
            return self.buckets[indice_bucket]
        
        return self.get_colision(indice_bucket, key)

    def del_key(self, key_param):
        if (self.size <= 0): return
        new_buckets = [None] * (self.size - 1)
        for paire in self.buckets:
            key = paire[0]
            if (key != key_param):
                indice_key = hash(key) % (self.size - 1)
                if (new_buckets[indice_key] != None):
                    indice_key = self.colision(indice_key, new_buckets)
                new_buckets[indice_key] =(paire[0], paire[1])
        self.size = self.size - 1
        self.buckets = new_buckets


# test pour voir si sa marche valide
# test = DiscordServerHashTable()
# print(test.buckets, test.size)
# test.append(10000, "Test")
# print(test.buckets, test.size)
# test.append(5, "test avec 5")
# print(test.buckets, test.size)
# test.append(840, "Sa donne quoi ?")
# print(test.buckets, test.size)
# number = 0
# while (test.get(number) == None or number == 5 or number == 840):
#     number = number + 1
#     print(number, test.get(number))