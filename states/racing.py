import pygame, sys, time

from objects.clock import RaceClock
from objects.player import Player
from objects.horse import Horse
from gui import *



class RacingState:
    def __init__(self, screen, gsm):
        self.screen = screen
        self.gsm = gsm
        self.mouse_pos = pygame.mouse.get_pos()
        
        self.pyClock = pygame.Clock()
        self.dt = 0
        
        # [img, scroll var]
        self.backgrounds = {
            'foreground': pygame.transform.scale_by(pygame.image.load('assets/startState/Foreground.png').convert_alpha(), 4),
            'horizon': pygame.transform.scale_by(pygame.image.load('assets/startState/Horizon.png').convert_alpha(), 4),
            'scroll f': 0,
            'scroll h': 0
        }
        
        self.title = {
            'img': pygame.transform.scale_by(pygame.image.load('assets/startState/title.png').convert_alpha(), 4)
        }
        
        self.start_btn = pygame.transform.scale_by(pygame.image.load('assets/startState/test.png').convert_alpha(), 4)
        
        self.clock = RaceClock()
        self.start = False
        self.node = pygame.transform.scale_by(pygame.image.load('assets/startState/node.png').convert_alpha(), 2)
        self.finished_horses = []
        self.map = [
            (200, 450), 
            (440, 600), (440, 450), (440, 300), 
            (680, 600), (680, 450), (680, 300), 
            (920, 600), (920, 450), (920, 300), 
            (1160, 600), (1160, 450), (1160, 300),
            (1400, 450)
        ]
        
    def render_bg(self) -> None:
        for i in range(0, 2):
            self.screen.blit(self.backgrounds['horizon'], (i * 1600 + self.backgrounds['scroll h'], 388))
        for i in range(0, 2):  
            self.screen.blit(self.backgrounds['foreground'], (i * 1600 + self.backgrounds['scroll f'], 388))
        
        self.backgrounds['scroll h'] -= 60 * self.dt
        self.backgrounds['scroll f'] -= 120 * self.dt
        
        if self.backgrounds['scroll h'] < -1600:
            self.backgrounds['scroll h'] = 0
        if self.backgrounds['scroll f'] < -1600:
            self.backgrounds['scroll f'] = 0

            
    def insertion_sort(self):
        arr = self.horses
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key.pos_x > arr[j].pos_x:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
    
    def render_gui(self) -> None:
        for node in self.map:
            self.screen.blit(self.node, node)
        if self.start:
            self.clock.update()
            StaticText(self.screen, 1300, 100, '', 'Pixeltype', 60, 'white', self.clock.format_time())
            for i, horse in enumerate(self.horses):
                if horse.update(self.dt, self.clock.get_time()):
                    self.finished_horses.append((self.horses.pop(i), self.clock.format_time()))
                self.screen.blit(horse.sprite, (horse.pos_x, horse.pos_y))
                stam = f'{horse.stamina}'
                #table horse
                self.screen.blit(horse.sprite, (50, i * 70), (0, 0, 64, 64))
                text = f'{str(i)+".":<10}{horse.name:<10}{f"{horse.stamina:.2f}":<10}{f"{horse.health:.2f}":<10}'
                StaticText(self.screen, 70, i*70+20, '', 'Pixeltype', 60, 'white', text)
                    
                
                
            self.horses = self.insertion_sort()
            if len(self.horses) == 0:
                print(f'{"Final Results":-^30}')
                for i,tupe in enumerate(self.finished_horses):
                    name = tupe[0].name
                    time = tupe[1]
                    print(f'{str(i):<15}{name:<30}{time}')
                self.start = False
            

        
        
    
    """ Start state run loop """            
    def run(self):
        self.horses = []
        for i in range(10):
            self.horses.append(Horse(i))
        for horse in self.horses:
            horse.initialize_race_horse()
            print(horse)
            
        while True:
            self.screen.fill((95, 205, 228))
            self.mouse_pos = pygame.mouse.get_pos()
            

            self.render_bg()
            self.render_gui()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.start = True
                    self.clock.start()

            self.dt = self.pyClock.tick() / 1000

            pygame.display.flip()
            