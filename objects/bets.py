from objects.horse import Horse

"""
Bet:
    odds - return odds[0] of each odds[1] placed
    horse - target of bet
    amount - amount of cash placed on bet 
    returns - amount won if bet resolves
"""
class Bet:
    def __init__(self, type: str, odds: tuple, horse: Horse) -> None:
        self.type = type
        self.bet_horse = horse
        self.bet_odds = odds
        self.bet_amount:    float = 0.00
        self.bet_returns:   float = 0.00

    def __str__(self) -> str:
        return f'{"":-^50}\n{"Bet Type:":<15}{self.type}\n{"Horse:":<15}{self.bet_horse.name}\n{"Odds:":<15}{self.bet_odds}\n{"Amount:":<15}{self.bet_amount}\n{"Returns":<15}{self.bet_returns}\n{"":-^50}\n'
    
    def set_bet_amount(self, amount: float) -> None:
        self.bet_amount = amount
        self.bet_returns = round((self.bet_odds[0] / self.bet_odds[1]) * amount, 2)
    
    
    
"""
Position Bet:
    Bet for a horse to finish at specific position
"""
class Position(Bet):
    def __init__(self, horse: Horse):
        super().__init__('Position', (10, 1), horse)

    # Position is unique to this bet type requiring extra criteria
    def set_position(self, pos: int) -> None:
        self.position = pos - 1

    def resolve(self, results: list) -> float:
        for pos, horse in enumerate(results):
            if pos == self.position and horse == self.horse:
                return self.bet_returns
        return 0.00
    
"""
Top Three:
    Bet for a horse to finish in the top 3
"""
class TopThree(Bet):
    def __init__(self, horse: Horse):
        super().__init__('Top 3', (7, 2), horse)

    def resolve(self, results: list) -> float:
        for pos, horse in enumerate(results):
            if pos <= 2 and horse == self.horse:
                return self.bet_returns
        return 0.00
    
"""
Top Half:
    Bet for a horse to finish in the top half of horses
"""
class TopHalf(Bet):
    def __init__(self, horse: Horse):
        super().__init__('Top Half', (5, 3), horse)

    def resolve(self, results: list) -> float:
        for pos, horse in enumerate(results):
            if pos <= 4 and horse == self.horse:
                return self.bet_returns
        return 0.00
    
"""
Top Half:
    Bet for a horse to finish in the top half of horses
"""
class BottomHalf(Bet):
    def __init__(self, horse: Horse):
        super().__init__('Bottom Half', (5, 3), horse)

    def resolve(self, results: list) -> float:
        for pos, horse in enumerate(results):
            if pos > 4:
                return self.bet_returns
        return 0.00
    
"""
Does Not Finish:
    Bet that a horse will not complete the race due to health, or stamina, or does not meet minimum time
"""
class Dnf(Bet):
    def __init__(self, horse: Horse):
        super().__init__('DNF', (6, 2), horse)
        
    def resolve(self, results: list):
        for horse in results:
            if horse == self.horse and not horse.race_completion_status:
                return self.bet_returns
        return 0.00
    
    


