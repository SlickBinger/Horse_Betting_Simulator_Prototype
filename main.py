"""
    Main
    
    main
"""
import pygame, sys
import gameStateManager 

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1600, 900))
        self.gsm = gameStateManager('intro')
        
        # Game State Initializations
        self.introState = IntroState(self.screen, self.gsm)
        self.bettingState = BettingState(self.screen, self.gsm)
        self.racingState = RacingState(self.screen, self.gsm)
        self.resolvingState = ResolvingState(self.screen, self.gsm)
        
        self.states = {
            'intro': self.introState,
            'betting': self.bettingState,
            'racing': self.racingState,
            'resolving': self.resolvingState
        }
        
    def run(self):
        pygame.display.set_caption('Glimpy Piddles: Race Day')
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.states[self.gsm.get_state()].run()
            
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()