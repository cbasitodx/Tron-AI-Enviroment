import asyncio

from base.consts import *
from base.player import Player
from base.input import get_input
from base.move import Move
from base.board import Board


class Tron:
    def __init__(self, size: int):
        self.__player_1: Player = Player(PLAYER_1, size)
        self.__player_2: Player = Player(PLAYER_2, size)

        self.__size = size
        self.__board = Board(size, self.__player_1, self.__player_2)

        # Flag for breaking the game loop
        self.__game_over: bool = False

        # Winner of the game
        self.__winner: Player | None = None

    @property
    def player_1(self) -> Player:
        return self.__player_1

    @property
    def player_2(self) -> Player:
        return self.__player_2

    @property
    def size(self) -> int:
        return self.__size

    @property
    def board(self) -> Board:
        return self.__board

    @property
    def game_over(self) -> bool:
        return self.__game_over

    @property
    def winner(self) -> Player | None:
        return self.__winner

    async def get_moves(self) -> tuple[tuple[int, int], tuple[int, int]]:
        move_1, move_2 = await asyncio.gather(get_input(self.player_1.number), get_input(self.player_2.number))
        if not Move.is_valid_move(move_1) or self.player_1.player_suicided(move_1):
            move_1 = self.player_1.previous_move

        if not Move.is_valid_move(move_2) or self.player_2.player_suicided(move_2):
            move_2 = self.player_2.previous_move

        return move_1, move_2

    def __get_collision(self, player_1: Player, player_2: Player) -> int | None:
        """
        Check if a collision happened

        :return: The type of collision that happened or None if no collision happened
        :rtype: Player | PLAYERS_COLLIDED | BOTH_WALLS | None
        """
        # Check if the players collided into each other diagonally or head-on
        if player_1.position[0] == player_2.position[0] or \
                (player_1.position[1] == player_2.position[0] and player_1.position[0] == player_2.position[1]):
            return PLAYERS_COLLIDED

        if player_1.position[0] in self.board.walls and player_2.position[0] in self.board.walls:
            return BOTH_WALLS

        if player_1.position[0] in player_2.position or player_1.position[0] in self.board.walls:
            return player_2

        if player_2.position[0] in player_1.position or player_2.position[0] in self.board.walls:
            return player_1

        return None

    def handle_collisions(self) -> str | None:
        collision = self.__get_collision(self.player_1, self.player_2)

        end_message = None

        if collision is not None:
            if collision == PLAYERS_COLLIDED:
                self.__winner = None
                end_message = "Players collided into each other"
            elif collision == BOTH_WALLS:
                self.__winner = None
                end_message = "Both players collided into a wall"
            else:
                self.__winner = collision
                end_message = f"Player {collision.number} wins!"

            self.__game_over = True

        return end_message
