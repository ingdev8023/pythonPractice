class HashTable:
    def __init__(self):
        self.collection = {}
    
    def hash(self, key:str):        
        return sum(map(lambda x: ord(x), list(key)))
    
    def add(self, key, pair):
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            self.collection[hashed_key][key] = pair
        else:
            self.collection[hashed_key] = {key:pair}
        return self.collection

    def remove(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            del self.collection[hashed_key][key]
        else: 
            return None
         

    def lookup(self,key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            return self.collection[hashed_key][key]
        else:
            return None

