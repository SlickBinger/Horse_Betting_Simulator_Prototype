import random

class Horse:
    def __init__(self, id: int):
        self.id = id
        self.name = 'Pig ' + str(id)

        # Horse Stats 
        self.initialize_stats()

        # Horse Traits - These can impact how they interact with the race course or alter their stats
        self.initialize_traits()

        # Race Attributes
        self.race_completion_status = False
    
    def initialize_stats(self):
        self.health =       random.randint(75, 125)
        self.stamina =      random.randint(75, 125)
        self.speed =        random.uniform(0.10, 1.00)
        self.dexterity =    random.uniform(0.00, 1.00)
        self.luck =         random.uniform(0.00, 1.00)

    def initialize_traits(self):
        self.traits = {
            'Alcoholic': random.randint(0, 1),
            'Partier': random.randint(0, 1),
            'Criminal': random.randint(0, 1),
            'Plagued': False,
            'Injured': False
        }

    def finish_race(self):
        self.race_completion_status = True
