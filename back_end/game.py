from back_end.player import Player


class Game:
    def __init__(self, game_name="joker", players=None):
        self.game_name = game_name
        if players is None:
            players = [Player("Dima"), Player("Julia")]
        self.players = players

        # games = ["joker", "SeeSaltPaper", "1000", "king"]
        # rules = ""  # game_name.txt

    def game_over(self, player):
        print(f"Игрок {player.name} выиграл. Счёт {player.points}")

    def check_game_over(self):
        for player in self.players:
            if self.game_name == "joker" and player.points >= 501 or \
                    self.game_name == "1000" and player.points >= 1000 or \
                    self.game_name == "SeeSaltPaper" and \
                    (len(self.players) == 2 and player.points >= 30 or
                     len(self.players) == 3 and player.points >= 35 or
                     len(self.players) == 4 and player.points >= 40):
                self.game_over(player)
                return True
        return False

    def process(self):
        while True:
            self.show_current_results()
            if self.take_score(): break

    def take_score(self):
        for player in range(len(self.players)):
            while True:
                try:
                    n, score = [int(val) for val in input("Номер, счёт: ").split()]
                    break
                except:
                    print("Упс, что-то не то. Введите 2 числа через пробел: номер игрока _ кол-во очков")
            self.players[n - 1].add_points(score)
        return self.check_game_over()

    def show_current_results(self):
        current_results = ""
        for i, player in enumerate(self.players, 1):
            current_results += str(i) + " " + player.name + ": " + str(player.points) + "\t"
        print("\n" + current_results)

    # def add_player(self, player): self.players.append(player)

# class JokerGame(Game):
