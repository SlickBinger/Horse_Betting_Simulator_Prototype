from objects.horse import Horse
from objects.bets import Position, TopThree, TopHalf, BottomHalf, Dnf

class BBProfile:
    def __init__(self, username: str, password: str, balance: float):
        # BetBot Profile
        self.username = username
        self.password = password
        self.balance = balance
        
        # [wins/losses, total cash wins/losses]
        self.wins = [0, 0.00]       
        self.losses = [0, 0.00]
    
    def __str__(self) -> str:
        return f'User: {self.username} Password: {self.password} Balance: {self.balance:.2f}\n{"Wins | Total Earnings:":<30}{self.wins[0]} | {self.wins[1]:.2f}\n{"Losses | Total Earnings Lost:":<30}{self.losses[0]} | {self.losses[1]:.2f}'
    
    def get_balance(self) -> float:
        return self.balance
    
    def charge(self, charge_amount: float) -> bool:
        self.balance -= charge_amount
    
    def update_win(self, win_amount: float) -> None:
        self.balance += win_amount
        self.wins[0] += 1
        self.wins[1] += win_amount
        
    def update_loss(self, loss_amount: float) -> None:
        self.balance -= win_amount
        self.losses[0] += 1
        self.losses[1] += loss_amount
        
         

class BetBot:
    def __init__(self, username: str, password: str, balance: float):
        self.user = BBProfile(username, password, balance)
        
        
    def login(self, username: str, password: str) -> str:
        if username != self.user.username:
            return f'Incorrect Username'
        elif password != self.user.password:
            return f'Incorrect Password'
        return ''
    """
        schedule:
            {
                'race 1': {
                    'time': 11:00
                    '
                }
            }
    """
    def add_race_schedule(self, schedule: dict) -> None:
        pass