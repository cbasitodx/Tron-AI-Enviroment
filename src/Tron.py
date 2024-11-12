from typing import List
import asyncio

from .consts import *
from .player import Player
from .input import get_input
from .board import update_board


class Tron:
  def __init__(self, size: int):
    # Dimensions of the board
    self.__size: int = size

    # Players
    self.__player_1: Player = Player(PLAYER_1, size)
    self.__player_2: Player = Player(PLAYER_2, size)

    # Game board. 0 means empty, 1 means player 1, 2 means player 2
    self.__board: List[List[int]] = [[0] * size] * size
    self.__walls: list[tuple[int, int]] = []
    self.__init_walls()

    # Flag for breaking the game loop
    self.__game_over: bool = False

    # Winner of the game
    self.__winner: Player | None = None

  def __init_walls(self) -> None:
    for i in range(self.__size):
      self.__walls.append((0, i))
      self.__walls.append((self.__size - 1, i))
      self.__walls.append((i, 0))
      self.__walls.append((i, self.__size - 1))

      self.__board[0][i] = WALL
      self.__board[self.__size - 1][i] = WALL
      self.__board[i][0] = WALL
      self.__board[i][self.__size - 1] = WALL

  def __is_valid_move(self, move: int) -> bool:
    if not isinstance(move, int):
      return False

    if 1 <= move <= 4:
      return True

    return False

  def __get_collision(self, player_1: Player, player_2: Player) -> Player | int | None:
    """
    Check if a collision happened

    :return: The type of collision that happened or None if no collision happened
    :rtype: Player | PLAYERS_COLLIDED | BOTH_WALLS | None
    """
    if player_1.position[0] == player_2.position[0]:
      return PLAYERS_COLLIDED

    if player_1.position[0] in player_2.position or player_1.position[0] in self.__walls:
      return player_2

    if player_2.position[0] in player_1.position or player_2.position[0] in self.__walls:
      return player_1

    if player_1.position[0] in self.__walls and player_2.position[0] in self.__walls:
      return BOTH_WALLS

    return None

  async def play(self) -> None:
    while not self.__game_over:
      # Get the moves from the players
      move_1, move_2 = await asyncio.gather(get_input(self.__player_1.id), get_input(self.__player_2.id))
      if not self.__is_valid_move(move_1) or self.__player_1.player_suicided(move_1):
        move_1 = self.__player_1.previous_move

      if not self.__is_valid_move(move_2) or self.__player_2.player_suicided(move_2):
        move_2 = self.__player_2.previous_move

      # Check if a collision happened
      collision = self.__get_collision(self.__player_1, self.__player_2)

      if collision is not None:
        if isinstance(collision, int):
          self.__game_over = True
          self.__winner = None
          continue

        self.__game_over = True
        self.__winner = collision
        continue

      # Update players's positions
      self.__player_1.move(move_1)
      self.__player_2.move(move_2)

      # Update the board
      update_board()

    if self.__winner is None:
      print("It's a tie!")
      print("Restarting the game...")
    else:
      print(f"Player {self.__winner.id} won!")
