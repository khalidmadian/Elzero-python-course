class Games:
    def __init__(self, games):
        self.games = games

    def show_games(self):
        if type(self.games) == str:
            print(f'I Have One Game "{self.games}"')

        elif type(self.games) == list:
            print('I Have Many Games:')
            for i in self.games:
                print(f'-- {i}')

        elif type(self.games) == int:
            print(f'I Have {self.games} Game.')


my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)

my_game.show_games()
# Ouput
# I Have One Game Called "Shadow Of Mordor"

my_games_names.show_games()
# Ouput
# I Have Many Games:
# -- Ys II
# -- Ys Oath In Felghana
# -- YS Origin

my_games_count.show_games()
# Output
# I Have 80 Game.
