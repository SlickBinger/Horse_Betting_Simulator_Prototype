from horse import Horse
from clock import RaceClock
import random, copy


class Race:
    def __init__(self, map: Map, horses: Dict[Horse]):
        self.map = map
        self.racers = set_racers(horses)
        self.race_clock = RaceClock()
        
    @staticmethod
    def set_racers(horses: Dict[Horse]) -> Dict[Horse]:
        id_list = []
        racers = {}
        for i in range(10):
            id = random.randint(100)
            while id in id_list:
                id = random.randint()
            id_list.append(id)
            racers[id] = copy.deepcopy(horses[id])
        return racers
    
    def start_race(self) -> None:
        self.race_clock.start()

class Map:
    def __init__(self, seed='0000'):
        self.seed = seed

        self.leg_dist = 240
        