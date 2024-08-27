import random, pygame
from objects.clock import Timer
import time

class Horse:
    def __init__(self, id: int):
        self.id = id
        self.name = 'Pig ' + str(id)
        
        self.wins = 0
        self.losses = 0
        
        # ------ Assets ------
        self.sprite = pygame.transform.scale_by(pygame.image.load('assets/racingState/test_horse.png').convert_alpha(), 2)    
        
        # ------ Stats ------
        self.health:    int =   random.randint(75, 125)
        self.stamina:   int =   random.randint(50, 100)
        self.speed:     float = round(random.uniform(0.50, 1.00), 2)
        self.dexterity: float = round(random.uniform(0.00, 1.00), 2)
        self.luck:      float = round(random.uniform(0.00, 1.00), 3)
        
        # ------ Traits ------
        self.alcoholic: bool =  random.choice((True, False))
        self.partier:   bool =  random.choice((True, False))
        self.criminal:  bool =  random.choice((True, False))
        self.exhausted: bool =  False
        self.injured:   bool =  False
        
        # ******************************************* RACE VARIABLES *******************************************
        # ------ race state var ------- 
        self.dead = False
        self.state = 2
        self.race_completion = False
        self.race_state_table = {
            0: self.running,        # 0 -> 0, 1
            1: self.execute_node,   # 1 -> 2, 3
            2: self.set_new_node,   # 2 -> 0, 4
            3: self.waiting         # 3 -> 3, 2
        }
        # ------- waiting state var
        self.wait_till: (int, int, int)
        self.time: (int, int, int)
        
        # ------- node execution and setting var -------
        self.race_leg = 0
        self.target: (int, int, int) # (x, y, node effect)
        self.node_effect_table = {
            1: self.alcoholic_node,
            2: self.partier_node,
            3: self.criminal_node,
            4: self.hospital_node,
            5: self.diner_node,
            6: lambda: self.dexterity_node(0),  # rain
            7: lambda: self.dexterity_node(1),  # cactus patch
            8: lambda: self.dexterity_node(2),  # traffic
            9: lambda: self.dexterity_node(3),  # minefield
        }

        # ------- running state var -------
        self.slope: float
        self.pos_x: int
        self.pos_y: int

    # Rendering Functions
    def render_static_horse(self, screen: pygame.Surface, pos: (int, int)):
        screen.blit(self.static_sprite, pos)
        
    def render_static_animated_horse(self, screen: pygame.Surface, pos: (int, int), dt):
        pass
    
        
    # Racing Initializations
    def path_luck_roll(self, best_option=0) -> int:
        roll = random.random()
        if self.luck >= roll:
            return best_option
        elif best_option < 1:
            return self.path_luck_roll(1)
        else:
            return 2   
        
    def add_node_events(self, path, map):
        for i, node in enumerate(path):
            if node[1] == 300:
                x = 2
            if node[1] == 450:
                x = 1
            else:
                x = 0
            path[i].append(map[i][x])
        return path
        
    def pick_path(self, map) -> list:
        path = [[200, 450], [440, None], [680, None], [920, None], [1160, None], [1400, 450]]
        
        top =       [300, 450, 600]
        middle =    [450, 300, 600]
        bottom =    [600, 450, 300]
        
        for i in range(1, 5):
            if path[i - 1][0] == top[0]:
                path[i][1] = top[self.path_luck_roll()]
            elif path[i -1][0] == middle[0]:
                path[i][1] = middle[self.path_luck_roll()]
            else:
                path[i][1] = bottom[self.path_luck_roll()]
                
        return self.add_node_events(path, map)
                
    def initialize_race_horse(self, map=[
        [None, 'start', None],
        [0, 0, 1],
        [1, 2, 9],
        [9, 9, 2],
        [9, 9, 9],
        [None, 10, None]]):
        self.pos_x = 200
        self.pos_y = 450
        self.step = 1
        
        self.path = self.pick_path(map)

    # Node Effects          
    def alcoholic_node(self) -> int:
        if self.alcoholic:
            self.dexterity *= 0.5
            self.stamina *= 0.75
            self.wait_till = (self.time[0], self.time[1] + 2, self.time[2])
            return 3, False
        return 2, False
    
    def partier_node(self) -> int:
        if self.partier:
            self.speed *= 1.5
            self.stamina *= 0.5
            print(f'{self.name} Stopped at the club')
            self.wait_till = (self.time[0], self.time[1] + 2, self.time[2])
            return 3, False
        return 2, False
    
    def criminal_node(self) -> int:
        if self.criminal:
            self.wait_till = (self.time[0], self.time[1] + 4, self.time[2])
            return 3, False
        return 2, False
    
    def hospital_node(self) -> int:
        if self.injured:
            self.wait_till = (self.time[0], self.time[1] + 1, self.time[2])
            return 3, False
        return 2, False
    
    def diner_node(self) -> int:
        if self.exhausted:
            self.wait_till = (self.time[0], self.time[1] + 1, self.time[2])
            return 3, False
        return 2, False
    
    def dexterity_node(self, event_type: int) -> int:
        roll = random.random()
        if self.dexterity < roll:
            damage = event_type / 100
            self.health *= damage
            print(f'{self.name} Blown up!')
        if self.health <= 0:
            self.dead = True
        return 2, False
                
        
    def execute_node(self):
        if self.target[2] == 0:
            return 2, False
        elif self.target[2] == 10:
            return 4, True
        return self.node_effect_table[self.target[2]]()
    
    def waiting(self):
        if self.time >= self.wait_till:
            return 2, False
        return 3, False
            
            
    # Sets the next target node
    def set_new_node(self) -> (int, bool):
        self.race_leg += 1
        self.target = self.path[self.race_leg]
        # Set New Slope
        if self.target[1] > self.pos_y or self.target[1] < self.pos_y:
            self.slope = (self.target[1] - self.pos_y) / (self.target[0] - self.pos_x)
        else:
            self.slope = 0
        return 0, False
    
    def reached_node_check(self) -> int:
        if self.pos_x >= self.target[0]:
            self.pos_x, self.pos_y = self.target[0], self.target[1]
            return 1
        return 0
    
    def running(self) -> (int, bool):
        if self.slope == 0 or self.step == 1:
            # pos_x, pos_y movement
            self.pos_x += (60 * self.speed) * self.dt
            self.step = 0
        else:
            self.pos_y += (60 * self.slope * self.speed) * self.dt
            self.step = 1
        # stamina decrease
        if not self.exhausted:
            self.stamina -= 1 * self.dt
            if self.stamina <= 0:
                self.exhausted = True
        else:
            self.health -= 1 * self.dt
            if self.health <= 0:
                self.dead = True
                self.sprite = pygame.transform.scale_by(pygame.image.load('assets/racingState/grave.png').convert_alpha(), 2)
            
        return self.reached_node_check(), False

    def update(self, dt: float, time: (int, int, int)) -> bool:
        # If state is 4 horse has completed the race
        if self.dead:
            return False
        if self.race_completion: 
            return True
        self.dt = dt
        self.time = time
        self.state, self.race_completion = self.race_state_table[self.state]()
        return self.race_completion

    def __str__(self) -> str:
        id_name_wl = f'ID: {self.id:<5}Name: {self.name}\n{"":-^50}\nWins: {self.wins:<5}Losses: {self.losses}\n'
        stats = f'{"Health:":<15}{self.health}\n{"Stamina:":<15}{self.stamina}\n{"Speed:":<15}{self.speed}\n{"Dexterity:":<15}{self.dexterity}\n{"Luck:":<15}{self.luck}\n{"Alcoholic:":<15}{self.alcoholic}\n{"":-^50}\n'
        return id_name_wl + stats
    