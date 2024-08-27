import pygame, sys, time

from objects.clock import Clock
from objects.player import Player
from gui import *

class BettingState:
    def __init__(self, screen, gsm):
        self.screen = screen
        self.gsm = gsm
        self.mouse_pos = pygame.mouse.get_pos()
        
        # Timers and Clocks
        self.pygameclock = pygame.time.Clock()
        self.clock = Clock()
        
        self.test = pygame.transform.scale_by(pygame.image.load('assets/startState/test.png'), 4)
    
    def render_bg(self) -> None:
        self.screen.blit(self.test, (0, 0))
        StaticText(self.screen, 135, 75, '', 40, 'white', self.clock.format_time())
    
    def render_gui(self) -> None:
        pass
        
    
    """ Start state run loop """            
    def run(self):
        while True:
            self.screen.fill((95, 205, 228))
            self.mouse_pos = pygame.mouse.get_pos()
            

            self.clock.update()
            self.render_bg()
            self.render_gui()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(self.mouse_pos)

            self.pygameclock.tick(60)
            pygame.display.flip()