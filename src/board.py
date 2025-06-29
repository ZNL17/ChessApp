import json


class Board:
    def __init__(self):
        with open(r"src\board.json", "r", encoding="utf-8") as f:
            self.board = json.load(f)["Board"]
        print(json.dumps(self.board, indent=2))
        f = "h1"
        print(Board.position(self, f))

    def position(self, str):
        return self.board[8 - int(str[1])][ord(str[0]) - 97]
        


x = Board()
