



ID_CARDS = {
    '420':('First Time Caller', 2.00),
    '69':('Long Time Listener', 5.00),
    '80085':('Helpuncle Jack', 10.00),
    '1': ('Offthe Roof', 15.00)
}

class Player:
    def __init__(self) -> None:
        self.initialize_name_wallet()

        self.bets = {}

    def initialize_name_wallet(self) -> None:
        
        print(f'{'Enter the desired betting ID to get started':^100}')
        id_input = input()
        while id_input not in ID_CARDS:
            print(f'{'MMMMmmmmm can you please type the ID CORRECTLY???? Thank you.':^100}\n')
        self.name, self.wallet = ID_CARDS[id_input]

    def list_bets(self) -> None:
        print(f'{' ' + self.name + ' Bets ':_^30}')
        for key, value in self.bets.items():
            print(f'Bet {key}')
            value.print_bet()
        print(f'{'':_^30}')
        
