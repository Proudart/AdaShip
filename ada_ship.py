
class Board:
    def __init__(self, size=10):
        self.size = size
        self.board = [[0 for x in range(size)] for y in range(size)]
        self.ships = []

    def add_ship(self, ship):
        self.ships.append(ship)

    def print_board(self):
        for row in self.board:
            print(row)

def main():
    board = Board()
    board.print_board()


if __name__ == '__main__':
    main()
