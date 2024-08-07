from objects.player import Player
from objects.horse import Horse
import objects.bets as bets
import sys


class Main:
    def __init__(self) -> None:
        self.render_intro()
        self.options = {
            'options': 'self.list_options()',
            'player': 'self.display_player()',
            'bets': 'self.display_betting_schema()',
            'betting': 'self.start_betting_state()',
            'racers': 'self.display_racers(self.racers)',
            'add': 'self.add_bet()',
            'start': 'self.start_race(self.racers)'
        }
        self.horses = [Horse(i + 1) for i in range(100)]
        self.player = Player()

        # Betting
        self.betting_status = False

        self.run()


    def render_intro(self) -> None:
        # Title Display
        print(f'\n\n{'*' * 102}')
        print(f'*{'----------------------------':^100}*')
        print(f'*{'| Glimpy Piddles: Race Day |':^100}*')
        print(f'*{'----------------------------':^100}*')
        print(f'*{'  ____/>':^100}*')
        print(f'*{'/|| ||':^100}*\n*{'':^100}*')
        print(f'{'*' * 102}\n\n')
        print('Welcome to the show! Hit enter to get started')
        start = input()
        while start != '':
            start = input()

        # Intro Text
        print('(John Krazinsky)')
        print(f'{'Howdy Partner!':^100}\n{'Finally decided to come back for your wallet hey?':^100}\n{'YOU CAM TO PLAY???':^100}')
        print(f'{'Finally decided to come back for your wallet hey?':^100}')
        print(f'{' Well I guess just pick one of these IDs cause I know your balance was uhm.... dry...':^20}')

        # ID card display
        print('--------------------------------    --------------------------------')
        print('|       BETTING ID CARD        |    |       BETTING ID CARD        |')
        print('|  ID: 420                     |    |  ID: 69                      |')
        print('|  Name:                       |    |  Name:                       |')
        print('|      First Time Caller       |    |      Long Time Listener      |')
        print('|  Wallet Balance:             |    |  Wallet Balance:             |')
        print('|      2.00$                   |    |      5.00$                   |')
        print('--------------------------------    --------------------------------\n')
        print('--------------------------------    --------------------------------')
        print('|       BETTING ID CARD        |    |       BETTING ID CARD        |')
        print('|  ID: 80085                   |    |  ID: 1                       |')
        print('|  Name:                       |    |  Name:                       |')
        print('|      Helpuncle Jack          |    |      Offthe Roof             |')
        print('|  Wallet Balance:             |    |  Wallet Balance:             |')
        print('|      10.00$                  |    |      15.00$                  |')
        print('--------------------------------    --------------------------------\n')


    def list_options(self) -> None:
        print(f'\n{' Commands ':-^76}')
        print(f'   {'options:':15}Lists all currently available command')
        print(f'   {'player:':15}Lists player name, balance, current bets')
        print(f'   {'bets:':15}Lists all possible bet types and their respective odds')

        if self.betting_status:
            print(f'   {'racers:':15}Displays all racing horses and respective stats')
            print(f'   {'add:':15}Allows you to place a bet')
            print(f'   {'start:':15}Begins the race')
        else:
            print(f'   {'betting:':15}Initialize a race to being betting')
        print(f'{'':-^76}\n')

    def list_horses(self) -> None:
        print(f'{'RACING HORSES':^87}\n')
        print(f'{'':-^87}')
        print(f'|{'Race ID':^10}|{'Horse':^30}|{'Health':^10}|{'Stamina':^10}|{'Speed':^10}|{'Dexterity':^10}|')
        for i,horse in enumerate(self.horses):
            horse.print_horse(i + 1)
        print(f'{'':-^87}\n')
        

    def display_player(self) -> None:
        print(f'{' ' + self.player.name + ' ':^30}')
        print(f'    Wallet:     {self.player.wallet}')
        self.player.list_bets()
        print(f'{'':^30}')

    def start_betting_state(self) -> None:
        self.betting_status = True
        print('Lets start betting!\n')

    def add_bet(self):
        print(f'\n{' Add Bet ':-^20}')
        bet_types = 'Positional:     10 to 1 odds\nTop Three:    7 to 2 odds\nTop half:    5 to 3 odds\nBottom Half:    5 to 3 odds\nDNF      6 to 2 odds'
        print(bet_types)




    def run(self) -> None:
        run_bool = True
        self.list_options()
        while run_bool:
            player_input = input()
            if player_input == 'kill':
                print('Goodbye!')
                sys.exit()
            elif player_input not in self.options:
                print('Error: Invalid Option...')
                print('Type `options` to view valid commands or `help` for more info.')
            else:
                exec(self.options[player_input])
            




if __name__ == '__main__':
    main = Main()