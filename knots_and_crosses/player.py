import pandas


class Player:
    def __init__(self, player, player_data):
        self.name = player.title()
        if self.name in player_data["player"].to_list():
            self.score = player_data[player_data["player"] == self.name].wins.to_list()[0]
        else:
            self.score = 0
            list_row = [player, 0, 0]
            player_data.loc[len(player_data)] = list_row
            print(player_data)
            player_data.to_csv("player_data.csv", index=False)
