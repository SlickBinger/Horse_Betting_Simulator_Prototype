import pygame, sys, time, random

from objects.clock import RaceClock
from objects.player import Player
from objects.horse import Horse
from gui import *



class StartState:
    def __init__(self, screen: pygame.Surface, gameStateManager):
        self.screen = screen
        self.gameStateManager = gameStateManager
        self.res_scaler, self.screen_w, self.screen_h = gameStateManager.get_resolution_var()
        self.mouse_pos = pygame.mouse.get_pos()
        
        self.pyClock = pygame.Clock()
        self.dt = 0
        self.clock = RaceClock()
        
        self.start = False
        self.train_x = 498
        
        # [img, scroll var]
        self.backgrounds = {
            'train': pygame.transform.scale_by(pygame.image.load('assets/startState/train.png').convert_alpha(), self.res_scaler),
            'rail': pygame.transform.scale_by(pygame.image.load('assets/startState/traintrack.png').convert_alpha(), self.res_scaler),
            'rail light': pygame.transform.scale_by(pygame.image.load('assets/startState/rail_light.png').convert_alpha(), self.res_scaler),
            'sky': pygame.transform.scale_by(pygame.image.load('assets/startState/sky_bg.png').convert_alpha(), self.res_scaler),
            'buildF': pygame.transform.scale_by(pygame.image.load('assets/startState/first_buildings.png').convert_alpha(), self.res_scaler),
            'scroll train': 0,
            'scroll sky': 0,
            'scroll buildF': 0
        }
        
        self.title = {
            'img': pygame.transform.scale_by(pygame.image.load('assets/startState/title.png').convert_alpha(), 4)
        }
        
        self.img_to_render = []
        
    def render_bg(self) -> None:
        self.format_render(self.backgrounds['sky'], (0, 0))
        for i in range(0, 2):
            self.format_render(self.backgrounds['sky'], (i * self.screen_w + self.backgrounds['scroll sky'], 0))
            
        for i in range(0, 2):
            self.format_render(self.backgrounds['buildF'], (i * self.screen_w + self.backgrounds['scroll buildF'], 0))
            
        for i in range(0, 2):
            self.format_render(self.backgrounds['rail light'], (i * self.backgrounds['rail'].get_width() + self.backgrounds['scroll train'] + 1032, 606))
        

        self.format_render(self.backgrounds['train'], (self.train_x, 714))
        
        for i in range(0, 2):
            self.format_render(self.backgrounds['rail'], (i * self.backgrounds['rail'].get_width() + self.backgrounds['scroll train'], 606))
        
        self.backgrounds['scroll buildF'] -= 500 * self.dt
        self.backgrounds['scroll train'] -= 1000 * self.dt
        self.backgrounds['scroll sky'] -= 30 * self.dt
        
        if self.start:
            self.train_x += 400 * self.dt
            StaticText(self.screen, self.train_x, 600, '', 'Pixeltype', 60, 'white', "You're kinda gay....")
        
        if self.backgrounds['scroll train'] < -self.backgrounds['rail'].get_width():
            self.backgrounds['scroll train'] = 0
        
        if self.backgrounds['scroll buildF'] < -self.screen_w:
            self.backgrounds['scroll buildF'] = 0
        
        if self.backgrounds['scroll sky'] < -self.screen_w:
            self.backgrounds['scroll sky'] = 0
            
    def render_gui(self) -> None:
        pass
    
    def format_render(self, img: pygame.Surface, pos: (int, int), frame=0) -> None:
        self.img_to_render.append((img, pos, (frame * img.get_width(), 0, img.get_width(), img.get_height())))
        print(self.img_to_render)
        
    def render_screen(self):
        for img in self.img_to_render:
            self.screen.blit(img[0],img[1], img[2])
        self.img_to_render = []
        if self.start:
        
            StaticText(self.screen, self.train_x, 600, '', 'Pixeltype', 60, 'white', "Break A Leg")
        
        
        
    
    """ Start state run loop """            
    def run(self):
        self.clock.start()
            
        while True:
            self.screen.fill((95, 205, 228))
            self.mouse_pos = pygame.mouse.get_pos()
            self.clock.update()

            self.render_bg()
            self.render_gui()
            self.render_screen()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.start = True

            self.dt = self.pyClock.tick() / 1000

            pygame.display.flip()
            