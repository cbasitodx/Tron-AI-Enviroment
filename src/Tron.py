import asyncio

from src.consts import *
from src.player import Player
from src.input import get_input


class Tron:
  def __init__(self, size: int):
    # Dimensions of the board
    self.__size: int = size

    # Players
    self.__player_1: Player = Player(PLAYER_1, size)
    self.__player_2: Player = Player(PLAYER_2, size)

    # Game board. 0 means empty, 1 means player 1, 2 means player 2
    self.__board: list[list[int]] = [[0] * size for _ in range(size)]
    self.__walls: set[tuple[int, int]] = set()
    self.__init_walls()

    # Add the initial positions of the players to the board
    self.__board[self.__player_1.position[0][0]][self.__player_1.position[0][1]] = PLAYER_1
    self.__board[self.__player_2.position[0][0]][self.__player_2.position[0][1]] = PLAYER_2

    # Flag for breaking the game loop
    self.__game_over: bool = False

    # Winner of the game
    self.__winner: Player | None = None

  def __init_walls(self) -> None:
    n = self.__size - 1
    for i in range(self.__size):
      self.__walls.add((0, i))
      self.__walls.add((self.__size - 1, i))
      self.__walls.add((i, 0))
      self.__walls.add((i, self.__size - 1))

      self.__board[0][i] = WALL
      self.__board[n][i] = WALL
      self.__board[i][0] = WALL
      self.__board[i][n] = WALL

  def __is_valid_move(self, move: int) -> bool:
    if not isinstance(move, int):
      return False

    if 1 <= move <= 4:
      return True

    return False

  async def __get_moves(self) -> tuple[tuple[int, int], tuple[int, int]]:
    move_1, move_2 = await asyncio.gather(get_input(self.__player_1.number), get_input(self.__player_2.number))
    if not self.__is_valid_move(move_1) or self.__player_1.player_suicided(move_1):
      move_1 = self.__player_1.previous_move

    if not self.__is_valid_move(move_2) or self.__player_2.player_suicided(move_2):
      move_2 = self.__player_2.previous_move

    return move_1, move_2

  def __get_new_position(self, player: Player, move: int) -> tuple[int, int]:
    match move:
      case 1:  # Move left
        new_pos = (player.position[0][0], player.position[0][1] - 1)
      case 2:  # Move up
        new_pos = (player.position[0][0] - 1, player.position[0][1])
      case 3:  # Move right
        new_pos = (player.position[0][0], player.position[0][1] + 1)
      case 4:  # Move down
        new_pos = (player.position[0][0] + 1, player.position[0][1])

    return new_pos

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

    if player_1.position[0] in player_2.position or player_1.position[0] in self.__walls:
      return player_2

    if player_2.position[0] in player_1.position or player_2.position[0] in self.__walls:
      return player_1

    if player_1.position[0] in self.__walls and player_2.position[0] in self.__walls:
      return BOTH_WALLS

    return None

  def __move_player(self, player: Player, move: int) -> None:
    new_pos = self.__get_new_position(player, move)
    player.move(new_pos, move)

  def __handle_collisions(self) -> str | None:
    collision = self.__get_collision(self.__player_1, self.__player_2)

    end_message = None

    if collision is not None:
      if collision == PLAYERS_COLLIDED:
        self.__winner = None
        end_message = "Both players collided into each other"
      elif collision == BOTH_WALLS:
        self.__winner = None
        end_message = "Both players collided into a wall"
      else:
        self.__winner = collision
        end_message = f"Player {collision.number} wins!"

      self.__game_over = True

    return end_message

  def __update_board(self, last_pos_1: tuple[int, int] | None, last_pos_2: tuple[int, int] | None) -> None:
    for pos_1, pos_2 in zip(self.__player_1.position, self.__player_2.position):
      if pos_1 is None or pos_2 is None:
        break
      self.__board[pos_1[0]][pos_1[1]] = PLAYER_1
      self.__board[pos_2[0]][pos_2[1]] = PLAYER_2

      if last_pos_1 is None or last_pos_2 is None:
        break
      self.__board[last_pos_1[0]][last_pos_1[1]] = 0
      self.__board[last_pos_2[0]][last_pos_2[1]] = 0

  async def play(self) -> None:
    self.print_board()
    end_message = ""
    while not self.__game_over:
      # Get and validate moves
      move_1, move_2 = await self.__get_moves()

      # Move the players
      self.__move_player(self.__player_1, move_1)
      self.__move_player(self.__player_2, move_2)

      # Check for collisions
      end_message = self.__handle_collisions()
      if self.__game_over:
        break

      # Get the last position of the players to remove them from the matrix
      last_pos_1 = self.__player_1.position[-1]
      last_pos_2 = self.__player_2.position[-1]

      # Update the matrix
      self.__update_board(last_pos_1, last_pos_2)

      # Print the matrix
      self.print_board()

    print(end_message)

  def print_board(self) -> None:
    for row in self.__board:
      print(" ".join(str(cell) for cell in row))


if __name__ == "__main__":
  tron = Tron(7)
  asyncio.run(tron.play())
