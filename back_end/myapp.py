from back_end.player import Player
from back_end.game import Game


class myApp:
    def __init__(self):
        self.game_number = 0
        self.players = []
        print("В какую игру играете: 1 Джокер, 2 МореСольБумага, 3 1000, 4 Кинг")
        while True:
            try:
                self.game_number = int(input("Введите номер игры: "))
                if self.game_number in (1, 2, 3, 4):
                    break
            except:
                print("Только число, соответствующее номеру игры :)")
        while True:
            try:
                player_number = int(input("Сколько игроков играет: "))
                if player_number in (1, 2, 3, 4, 5, 6, 7, 8):
                    break
            except:
                print("Только число, соответствующее количеству игроков :)")
            finally:
                self.players = [Player(input(f"Имя игрока №{number+1}: ")) for number in range(player_number)]
        self.start()

    def start(self):
        games = {1: "joker", 2: "SeeSaltPaper", 3: "1000", 4: "king"}
        game = Game(game_name=games[self.game_number], players=self.players)
        game.process()
