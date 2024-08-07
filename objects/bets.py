from objects.horse import Horse

"""
Bet:
    odds - return odds[0] of each odds[1] placed
    horse - target of bet
    amount - amount of cash placed on bet 
    returns - amount won if bet resolves
"""
class Bet:
    def __init__(self, odds: tuple, horse: Horse) -> None:
        self.bet_horse = horse
        self.bet_odds = odds

    # Bet is placed if:
    #   - bet amount is greater than the minimum required bet
    #   - bet amount is less then or equal to the players wallet
    def set_bet_amount(self, amount: float, wallet: float) -> bool:
        if amount < self.bet_odds[1] or amount > wallet: 
            return False
        
        self.bet_amount = amount
        self.bet_returns = round((self.bet_odds[0] / self.bet_odds[1]) * amount, 2)

        return True
    
"""
Position Bet:
    Bet for a horse to finish at specific position
"""
class Position(Bet):
    def __init__(self, horse: Horse) -> None:
        super().__init__((10, 1), horse)
        self.type = 'Position'

    # Position is unique to this bet type requiring extra criteria
    def set_position(self, pos: int) -> None:
        self.position = pos - 1

    def resolve(self, results: list) -> float:
        for pos, horse in enumerate(results):
            if pos == self.position and horse == self.horse:
                return self.bet_returns
        return 0.00
    
    def print_bet(self) -> None:
        print(f'{' ' + self.type + ' ':-^30}\n')
        print(f'    Horse:      {self.bet_horse.name}')
        print(f'    Position:   {self.position}')
        print(f'    Odds:       {self.bet_odds[0]} : {self.bet_odds[1]}')
        print(f'    Amount:     {self.bet_amount}.00$')
        print(f'    Returns:    {self.bet_returns}')
        print(f'{'':_^30}')
    
"""
Top Three:
    Bet for a horse to finish in the top 3
"""
class TopThree(Bet):
    def __init__(self, horse: Horse) -> None:
        super().__init__((7, 2), horse)
        self.type = 'Top 3'

    def resolve(self, results: list) -> float:
        for pos, horse in enumerate(results):
            if pos <= 2 and horse == self.horse:
                return self.bet_returns
        return 0.00
    
    def print_bet(self) -> None:
        print(f'{' ' + self.type + ' ':-^30}\n')
        print(f'    Horse:      {self.bet_horse.name}')
        print(f'    Odds:       {self.bet_odds[0]} : {self.bet_odds[1]}')
        print(f'    Amount:     {self.bet_amount}.00$')
        print(f'    Returns:    {self.bet_returns}')
        print(f'{'':_^30}')
    
"""
Top Half:
    Bet for a horse to finish in the top half of horses
"""
class TopHalf(Bet):
    def __init__(self, horse: Horse) -> None:
        super().__init__((5, 3), horse)
        self.type = 'Top Half'

    def resolve(self, results: list) -> float:
        for pos, horse in enumerate(results):
            if pos <= 4 and horse == self.horse:
                return self.bet_returns
        return 0.00
    
    def print_bet(self) -> None:
        print(f'{' ' + self.type + ' ':-^30}\n')
        print(f'    Horse:      {self.bet_horse.name}')
        print(f'    Odds:       {self.bet_odds[0]} : {self.bet_odds[1]}')
        print(f'    Amount:     {self.bet_amount}.00$')
        print(f'    Returns:    {self.bet_returns}')
        print(f'{'':_^30}')
    
"""
Top Half:
    Bet for a horse to finish in the top half of horses
"""
class BottomHalf(Bet):
    def __init__(self, horse: Horse) -> None:
        super().__init__((5, 3), horse)
        self.type = 'Bottom Half'

    def resolve(self, results: list) -> float:
        for pos, horse in enumerate(results):
            if pos > 4:
                return self.bet_returns
        return 0.00
    
    def print_bet(self) -> None:
        print(f'{' ' + self.type + ' ':-^30}\n')
        print(f'    Horse:      {self.bet_horse.name}')
        print(f'    Odds:       {self.bet_odds[0]} : {self.bet_odds[1]}')
        print(f'    Amount:     {self.bet_amount}.00$')
        print(f'    Returns:    {self.bet_returns}')
        print(f'{'':_^30}')
    
"""
Does Not Finish:
    Bet that a horse will not complete the race due to health, or stamina, or does not meet minimum time
"""
class Dnf(Bet):
    def __init__(self, horse: Horse) -> None:
        super().__init__((6, 2), horse)
        self.type = 'DNF'

    def resolve(self, results: list):
        for horse in results:
            if horse == self.horse and not horse.race_completion_status:
                return self.bet_returns
        return 0.00
    
    def print_bet(self) -> None:
        print(f'{' ' + self.type + ' ':-^30}\n')
        print(f'    Horse:      {self.bet_horse.name}')
        print(f'    Odds:       {self.bet_odds[0]} : {self.bet_odds[1]}')
        print(f'    Amount:     {self.bet_amount}.00$')
        print(f'    Returns:    {self.bet_returns}')
        print(f'{'':_^30}')
    
    




