import json
from pieces import Pieces


class Board:
    moves = {
        "R": "straight",
        "B": "cross",
        "N": "jump",
        "Q": "both",
        "K": "allStep",
        "P": "step",
    }

    def __init__(self):
        with open(r"src\board.json", "r", encoding="utf-8") as f:
            self.board = json.load(f)["Board"]

    def positionf(self, str):
        return self.board[8 - int(str[1])][ord(str[0]) - 97]

    def position(self, pos1, pos2):
        return self.board[pos1][pos2]

    def move(self, dis_vec, start, field, p):
        print(p[1:])
        print(self.moves[p])
        return getattr(Pieces, self.moves[p])(dis_vec, start, field)
