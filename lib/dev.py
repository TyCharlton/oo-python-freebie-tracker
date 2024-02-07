from freebie import Freebie

class Dev:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value

    def freebies(self):
        from freebie import Freebie
        return [freebie for freebie in Freebie.all if freebie.dev == self]
    
    def company(self):
        return (set([freebie.company for  freebie in self.freebies()]))
    
    def received_one(self, item_name):
        received = False
        for freebie in self.freebies():
            if freebie.item_name == item_name:
                return received
            
        return received
    
    def give_away(self, dev, freebie):
        if freebie.dev == self:
            freebie.dev = dev


    def __repr__(self):
        return self.name
        pass
