class Cache:
    def __init__(self, cache_length=20):        
        self.cache_length = cache_length
        self.cache = dict()
        self.key_list = list()
        
    def __iter__(self):
        return iter(self.cache)
    
    def __getitem__(self, key):
        return self.cache[key]
    
    def push(self, key, value):
        if key in self.cache:
            return
        
        if len(self.cache) > self.cache_length:
            top_key = self.key_list[0]
            del self.cache[top_key]
            del self.key_list[0]
            
        self.cache[key] = value
        self.key_list.append(key)