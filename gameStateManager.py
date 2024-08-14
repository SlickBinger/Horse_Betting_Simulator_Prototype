"""
    GameStateManager
    
    Description: 
        Manages the game state via the initial 'Game' run loop.
        Setting the game state only activates when the respective state run loop returns reverting to the initial 'Game' run loop.
        
        It also maintains Player and Horses information inorder to maintain information acrross states as well as reinitialize states.
"""
class GameStateManager:
    def __init__(self, current_state: str) -> None:
        self.set_state(current_state)
        
    def set_state(self, state: str) -> None:
        self.state = state
    def get_state(self) -> str:
        return self.state
    
    def set_player(self, player: 'Player') -> None:
        self.player = player
    def get_player(self) -> 'Player':
        return self.player
    
    def set_horses(self, horses: list) -> None:
        self.horses = horses
    def get_horses(self) -> list:
        return self.horses
    