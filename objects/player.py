from objects.betbot import BetBot

class Player:
    def __init__(self, name: str, password: str, wallet: float, balance: float):
        self.name = name
        self.password = password
        self.wallet = wallet
        self.betbot = BetBot(name, password, balance)

    def __str__(self) -> str:
        return f'{"Name:":<10}{self.name}\n{"Balance:":<10}${self.balance:.2f}\n{"":-^50}\n'

        
