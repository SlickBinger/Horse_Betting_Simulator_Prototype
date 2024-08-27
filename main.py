
import pygame, sys, ctypes

from gameStateManager import GameStateManager
from states.start import StartState
from states.intro import IntroState
from states.betting import BettingState
from states.racing import RacingState
from states.resolving import ResolvingState 

user32 = ctypes.windll.user32
WIDTH, HEIGHT = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.gameStateManager = GameStateManager('start')
        self.gameStateManager.set_resolution_var(1080)
        # Game State Initializations
        self.startState = StartState(self.screen, self.gameStateManager)
        self.introState = IntroState(self.screen, self.gameStateManager)
        self.bettingState = BettingState(self.screen, self.gameStateManager)
        self.racingState = RacingState(self.screen, self.gameStateManager)
        self.resolvingState = ResolvingState(self.screen, self.gameStateManager)
        
        self.states = {
            'start': self.startState,
            'intro': self.introState,
            'betting': self.bettingState,
            'racing': self.racingState,
            'resolving': self.resolvingState
        }
        
    def run(self) -> None:
        pygame.display.set_caption('Glimpy Piddles: Race Day')
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.states[self.gameStateManager.get_state()].run()
            
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()