import pygame, sys

class IntroState:
    def __init__(self, screen, gsm):
        self.screen = screen
        self.gsm = gsm
        self.mouse_pos = pygame.mouse.get_pos()
        
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick() / 1000    
    
    """ Start state run loop """            
    def run(self):
        while True:
            self.screen.fill((95, 205, 228))
            self.mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.dt = self.clock.tick(60) / 1000
            pygame.display.flip()