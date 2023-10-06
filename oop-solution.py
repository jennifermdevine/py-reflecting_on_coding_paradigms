#First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.

class Pod_racer:
  def __init__(self, max_speed, condition, price, owner):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price
    self.owner = owner

   # Define a repair() method that will update the condition of the podracer to "repaired".

    def repair(self):
        self.condition = "repaired"

    #Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.

class Anakins_Pod(Pod_racer):
    def __init__(self, max_speed, condition, price, owner = 'Anakin'):
        super().__init__(max_speed, condition, price, owner)

def boost(self):
    self.max_speed *= 2

    #Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".

class Sebulbas_Pod(Pod_racer):
    def __init__(self, max_speed, condition, price, owner = 'Sebulba'):
        super().__init__(max_speed, condition, price, owner)

def flame_jet(self,other):
    other.condition = "trashed"

anakins_pod = Anakins_Pod(25, 'perfect', 1000)
sebulbas_pod = Sebulbas_Pod(50, 'perfect', 1000000)

print(anakins_pod.condition)
print(sebulbas_pod.condition)