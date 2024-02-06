import argparse

class Params:
    score_type = {
        'td': {
            'value': 6,
            'name': 'Touchdown'
        },
        'fg': {
            'value': 3,
            'name': 'Field Goal'
        },
        'safety': {
            'value': 2,
            'name': 'Safety',
        },
        'pat': {
            'value': 1,
            'name': 'PAT'
        },
        '2pt': {
            'value': 2,
            'name': '2pt Conversion'
        }
    }
    teams = ['Chiefs', '49ers']
    participants = {
        'GF': {
            'name': 'Gian Favero',
            'profit': 0
        },
        'TB': {
            'name': 'Thomas Byrne',
            'profit': 0
        },
        'AI': {
            'name': 'Adrian Iannetta',
            'profit': 0
        },
        'RM': {
                'name': 'Robert McVinnie',
                'profit': 0
        },
        'BA': {
            'name': 'Brayden Amlin',
            'profit': 0
        },
        'MA': {
            'name': 'Matthew Ammoscato',
            'profit': 0
        },
        'AO': {
            'name': 'Andrew Ogley',
            'profit': 0
        },
        'SC': {
            'name': 'Steven Caro',
            'profit': 0
        },
        'NS': {
            'name': 'Noah Scholl',
            'profit': 0
        },
        'SH': {
            'name': 'Stevie Hill',
            'profit': 0
        },
    }
    pot = 200
    pay = 5

# Load grid from .csv file
def load_grid(file_path: str):
    grid = []
    with open('SB_Squares_2024.csv', 'r') as file:
        for line in file:
            row = line.strip().split(',')
            grid.append(row)
    return grid

grid = load_grid('SB_Squares_2024.csv')

class SquareBot:
    def __init__(self):
        self.pot = Params.pot
        self.team1 = Params.teams[0]
        self.team2 = Params.teams[1]
        self.score1 = 0
        self.score2 = 0
        self.participants = Params.participants

    def get_winner(self):
        row = self.score1 % 10
        col = self.score2 % 10
        winner = grid[row][col]
        return winner

    def score_update(self, team, score_type):
        if team == self.team1:
            self.score1 += score_type['value']
        elif team == self.team2:
            self.score2 += score_type['value']
        else:
            print("Invalid team name.")
            return

        self.pot -= Params.pay

        winner = self.get_winner()
        self.participants[winner]['profit'] += Params.pay

        self.tweet(score_type['name'], team.capitalize(), winner)

    def tweet(self, score_type: str, team: str, winner: str):
        team1 = Params.teams[0]
        team2 = Params.teams[1]
        tweet = f"\n {score_type} {team}! \n \n Score: {team1} {self.score1} - {team2} {self.score2} \n \n Winner: {self.participants[winner]['name']} -> +${Params.pay} (${self.participants[winner]['profit']}) \n \n Pot remaining: ${self.pot} \n \n #SuperBowlSquares"
        print(tweet)

def parse_arguments():
    parser = argparse.ArgumentParser(prog='SCORE_UPDATE', description="A Tweet bot for the Super Bowl Squares game.")
    parser.add_argument("score_type", type=str, choices=["td", "fg", "safety", "pat", "exit"],
                        help="The score update to perform or 'exit' to quit.")
    parser.add_argument("team", type=str, nargs='?', default=0, help="The first number.")
    return parser.parse_args()

def main():
    bot = SquareBot()

    while True:
        # Since input() and argparse don't work well together for interactive use,
        # we manually parse the arguments here for the continuous loop
        raw_input = input("Enter score type and team (or 'exit' to quit): ")
        if raw_input.lower() == 'exit':
            print("Bye-bye.")
            break

        args = raw_input.split()

        # Handling different types of inputs and errors
        try: 
            if args[0].lower() == 'exit':
                print("Bye-bye.")
                break
            elif args[0].lower() == 'set_score':
                bot.score1 = int(input(f"Enter score for {bot.team1}: "))
                bot.score2 = int(input(f"Enter score for {bot.team2}: "))
            elif args[0].lower() == 'restart':
                bot.score1 = 0
                bot.score2 = 0
                bot.pot = Params.pot
                for participant in bot.participants:
                    bot.participants[participant]['profit'] = 0
            elif args[0].lower() == 'game-over':
                print(f"\n Final score: {bot.team1} {bot.score1} - {bot.team2} {bot.score2}")
                bot.participants[bot.get_winner()]['profit'] += bot.pot
                print(f"\n Grand Prize Winner: {bot.participants[bot.get_winner()]['name']} -> +${bot.pot} (${bot.participants[bot.get_winner()]['profit']})")
                bot.pot = 0
                print("\n Final Winnings:")
                for participant in bot.participants:
                    print(f" {bot.participants[participant]['name']}: ${bot.participants[participant]['profit']}")
                print("\n #SuperBowlSquares")
            else:
                try:
                    score_type = Params.score_type[args[0].lower()]
                    team = args[1].lower()
                    team = team.capitalize()
                    if team not in Params.teams:
                        print(team)
                        print("Invalid team name. Please try again.")
                        continue

                    bot.score_update(team, score_type)
                except KeyError:
                    print("Invalid score update. Please try again.")
                    continue

        except (IndexError, ValueError):
            print("Invalid input. Please try again")
            continue

if __name__ == "__main__":
    main()
