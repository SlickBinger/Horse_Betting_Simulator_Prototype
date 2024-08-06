class Bet:
    def __init__(self, odds: tuple, horse: Horse):
        self.bet_horse = horse
        self.bet_odds = odds

    def set_amount(self, amount):
        self.bet_amount = amount
        self.bet_returns = self.bet_odds * amount


"""
Position Bet:
    Bet for a horse to finish at specific position
"""
class Position(Bet):
    def __init__(self, horse):
        Bet.__init__((10, 1), horse)

    def set_position(self, pos):
        self.position = pos - 1

    def resolve(self, results: list):
        for pos, horse in enumerate(results):
            if pos == self.position and horse == self.horse:
                return self.bet_returns
        return 0.00
    
"""
Top Three:
    Bet for a horse to finish in the top 3
"""
class TopThree(Bet):
    def __init__(self, horse):
        Bet.__init__((7, 2), horse)

    def resolve(self, results):
        for pos, horse in enumerate(results):
            if pos <= 2 and horse == self.horse:
                return self.bet_returns
        return 0.00
    
"""
Top Half:
    Bet for a horse to finish in the top half of horses
"""
class TopHalf(Bet):
    def __init__(self, horse):
        Bet.__init__((5, 3), horse)

    def resolve(self, results):
        for pos, horse in enumerate(results):
            if pos <= 4 and horse == self.horse:
                return self.bet_returns
        return 0.00
    
"""
Top Half:
    Bet for a horse to finish in the top half of horses
"""
class BottomHalf(Bet):
    def __init__(self, horse):
        Bet.__init__((5, 3), horse)

    def resolve(self, results):
        for pos, horse in enumerate(results):
            if pos > 4:
                return self.bet_returns
        return 0.00
    
"""
Does Not Finish:
    Bet that a horse will not complete the race due to health, or stamina, or does not meet minimum time
"""
class Dnf(Bet):
    def __init__(self, horse):
        Bet.__init__((5, 3), horse)

    def resolve(self, results):
        for horse in results:
            if horse == self.horse and not horse.race_completion_status:
                return self.bet_returns
        return 0.00
    
    






