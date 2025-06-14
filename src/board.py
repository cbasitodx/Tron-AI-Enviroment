from src.player import Player
from src.consts import PLAYER_1, PLAYER_2, WALL


class Board:
    def __init__(self, size: int, player_1: Player, player_2: Player):
        self.__size: int = size

        # Save the players' info
        self.__player_1: Player = player_1
        self.__player_2: Player = player_2

        # Initialize the board
        self.__board: list[list[int]] = [[0] * size for _ in range(size)]
        self.__walls: set[tuple[int, int]] = set()
        self.__init_walls()

        # Add the initial positions of the players to the board
        self.__board[self.__player_1.position[0][0]][self.__player_1.position[0][1]] = PLAYER_1
        self.__board[self.__player_2.position[0][0]][self.__player_2.position[0][1]] = PLAYER_2

    def __init_walls(self) -> None:
        n = self.__size - 1
        for i in range(self.__size):
            self.__walls.add((0, i))
            self.__walls.add((n, i))
            self.__walls.add((i, 0))
            self.__walls.add((i, n))

            self.__board[0][i] = WALL
            self.__board[n][i] = WALL
            self.__board[i][0] = WALL
            self.__board[i][n] = WALL

    def update_board(self, last_pos_1: tuple[int, int], last_pos_2: tuple[int, int]) -> None:
        for pos_1, pos_2 in zip(self.__player_1.position, self.__player_2.position):
            if pos_1 is None or pos_2 is None:
                break
            self.__board[pos_1[0]][pos_1[1]] = PLAYER_1
            self.__board[pos_2[0]][pos_2[1]] = PLAYER_2

            if last_pos_1 is None or last_pos_2 is None:
                break
            self.__board[last_pos_1[0]][last_pos_1[1]] = 0
            self.__board[last_pos_2[0]][last_pos_2[1]] = 0

    @property
    def walls(self) -> set[tuple[int, int]]:
        return self.__walls

    def __str__(self) -> str:
        res = ""
        for row in self.__board:
            res += " ".join(str(cell) for cell in row) + "\n"

        return res
