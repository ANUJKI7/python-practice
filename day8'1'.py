from abc import ABC,abstractmethod #abstraction

class animal(ABC):
  @abstractmethod
  def make_sound(self):
   pass

class lion(animal):
  def make_sound(self):
    print("roar!")

class cow(animal):
  def make_sound(self):
    print("moo!")

lion=lion()
lion.make_sound()

cow=cow()
cow.make_sound()