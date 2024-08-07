import random

class Horse:
    def __init__(self, id: int) -> None:
        self.id = id
        self.name = 'Pig ' + str(id)

        # Horse Stats 
        self.initialize_stats()

        # Horse Traits - These can impact how they interact with the race course or alter their stats
        self.initialize_traits()

        # Race Attributes
        self.race_completion_status = False
    
    def initialize_stats(self) -> None:
        self.health =       random.randint(75, 125)
        self.stamina =      random.randint(75, 125)
        self.speed =        round(random.uniform(0.10, 1.00), 2)
        self.dexterity =    round(random.uniform(0.00, 1.00), 2)
        self.luck =         round(random.uniform(0.00, 1.00), 3)

    def initialize_traits(self) -> None:
        self.traits = {
            'Alcoholic': random.randint(0, 1),
            'Partier': random.randint(0, 1),
            'Criminal': random.randint(0, 1),
            'Plagued': False,
            'Injured': False
        }

    def finish_race(self) -> None:
        self.race_completion_status = True

    def print_horse(self, race_id: int):
        print(f'{'':-^87}')
        print(f'|{race_id:^10}| {self.name:29}|{self.health:^10}|{self.stamina:^10}|{self.speed:^10}|{self.dexterity:^10}|')