from abc import abstractclassmethod

## The Musician class is an abstract base class that defines the methods and properties for a musician
class Musician:
    
    def __init__(self, name):
        self.name = name

    @abstractclassmethod
    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"

    @abstractclassmethod
    def __repr__(self):
        return f"{self.name}"

    @abstractclassmethod
    def get_instrument(self):
        pass

    @abstractclassmethod
    def play_solo(self):
        pass
    

#The Band class represents a band, which is a group of musicians.
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
            return (f'My name is {self.name} and I play guitar')#returns a string representation of the musician, including their name and the instrument they play.
      
      def __repr__(self):
            return (f'Guitarist instance. Name = {self.name}')#returns a string representation of the musician for debugging purposes.
      
      def get_instrument(self):#returns the name of the instrument the musician plays.
          return 'guitar'
      
      def play_solo (self):#returns a string representation of the musician playing a solo.
          return 'face melting guitar solo'



class Drummer(Musician):
       
       def __init__(self, name):
        self.name = name

       def __str__(self):
            return (f'My name is {self.name} and I play drums')#returns a string representation of the musician, including their name and the instrument they play.
       
       def __repr__(self):
            return (f'Drummer instance. Name = {self.name}')#returns a string representation of the musician for debugging purposes.
       
       def get_instrument(self):#returns the name of the instrument the musician plays.
          return 'drums'
       
       def play_solo (self):#returns a string representation of the musician playing a solo.
          return 'rattle boom crash'

 
class Bassist(Musician):
       
       def __init__(self, name):
        self.name = name
        
       def __str__(self):
            return (f'My name is {self.name} and I play bass')#returns a string representation of the musician, including their name and the instrument they play.
       
       def __repr__(self):
            return (f'Bassist instance. Name = {self.name}')#returns a string representation of the musician for debugging purposes.
       
       def get_instrument(self):#returns the name of the instrument the musician plays.
          return 'bass'
       
       def play_solo (self):#returns a string representation of the musician playing a solo.
          return 'bom bom buh bom'
       

