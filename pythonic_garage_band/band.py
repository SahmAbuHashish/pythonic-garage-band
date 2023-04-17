from abc import abstractclassmethod

class Musician:
    
    def __init__(self, name):
        self.name = name

    @abstractclassmethod
    def __str__(self):
        pass

    @abstractclassmethod
    def __repr__(self):
        pass

    @abstractclassmethod
    def get_instrument(self):
        pass

    @abstractclassmethod
    def play_solo(self):
        pass
    

class Band:
 
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)
    
    def __str__(self):
        return f" band {self.name}"

    def __repr__(self):
       return f"{self.name}"
    

    def play_solos(self):
        solos_member = []
        for member in self.members:
            solos_member.append(member.play_solo())
        return solos_member

    
    
    @classmethod
    def to_list(cls):
        return cls.instances


class Guitarist (Musician):
      
      def __init__ (self,name):
            self.name=name
            
      def __str__(self):
            return (f'My name is {self.name} and I play guitar')
      
      def __repr__(self):
            return (f'Guitarist instance. Name = {self.name}')
      
      def get_instrument(self):
          return 'guitar'
      
      def play_solo (self):
          return 'face melting guitar solo'



class Drummer(Musician):
       
       def __init__(self, name):
        self.name = name

       def __str__(self):
            return (f'My name is {self.name} and I play drums')
       
       def __repr__(self):
            return (f'Drummer instance. Name = {self.name}')
       
       def get_instrument(self):
          return 'drums'
       
       def play_solo (self):
          return 'rattle boom crash'

 
class Bassist(Musician):
       
       def __init__(self, name):
        self.name = name
        
       def __str__(self):
            return (f'My name is {self.name} and I play bass')
       
       def __repr__(self):
            return (f'Bassist instance. Name = {self.name}')
       
       def get_instrument(self):
          return 'bass'
       
       def play_solo (self):
          return 'bom bom buh bom'