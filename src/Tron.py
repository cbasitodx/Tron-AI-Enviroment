import asyncio

from src.consts import *
from src.player import Player
from src.input import get_input
from src.move import Move
from src.board import Board


class Tron:
    def __init__(self, size: int):
        self.__player_1: Player = Player(PLAYER_1, size)
        self.__player_2: Player = Player(PLAYER_2, size)

        self.__board = Board(size, self.__player_1, self.__player_2)

        # Flag for breaking the game loop
        self.__game_over: bool = False

        # Winner of the game
        self.__winner: Player | None = None

    async def __get_moves(self) -> tuple[tuple[int, int], tuple[int, int]]:
        move_1, move_2 = await asyncio.gather(get_input(self.__player_1.number), get_input(self.__player_2.number))
        if not Move.is_valid_move(move_1) or self.__player_1.player_suicided(move_1):
            move_1 = self.__player_1.previous_move

        if not Move.is_valid_move(move_2) or self.__player_2.player_suicided(move_2):
            move_2 = self.__player_2.previous_move

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

        if player_1.position[0] in self.__board.walls and player_2.position[0] in self.__board.walls:
            return BOTH_WALLS

        if player_1.position[0] in player_2.position or player_1.position[0] in self.__board.walls:
            return player_2

        if player_2.position[0] in player_1.position or player_2.position[0] in self.__board.walls:
            return player_1

        return None

    def __handle_collisions(self) -> str | None:
        collision = self.__get_collision(self.__player_1, self.__player_2)

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

    async def play(self) -> None:
        print(self.__board)
        end_message = ""
        while not self.__game_over:
            # Get and validate moves
            move_1, move_2 = await self.__get_moves()

            # Get the last position of the players to remove them from the matrix
            last_pos_1 = self.__player_1.position[-1]
            last_pos_2 = self.__player_2.position[-1]

            # Move the players
            Move.move_player(self.__player_1, move_1)
            Move.move_player(self.__player_2, move_2)

            # Check for collisions
            end_message = self.__handle_collisions()
            if self.__game_over:
                break

            # Update the matrix
            self.__board.update_board(last_pos_1, last_pos_2)

            # Print the matrix
            print(self.__board)

        print(end_message)


if __name__ == "__main__":
    tron = Tron(7)
    asyncio.run(tron.play())
