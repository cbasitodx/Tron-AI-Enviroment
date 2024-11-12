from random import randint

from .consts import PLAYER_1, PLAYER_2, N_STELLA, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT, MOVE_UP


class Player:
  def __init__(self, number: int, size: int):
    self.__number: int = number
    self.__position: list[tuple[int, int]] = [self.__generate_initial_position(size)] + [None] * N_STELLA
    self.__previous_move: int = 0  # 0 means no previous move

  @property
  def number(self) -> int:
    return self.__number

  @property
  def position(self) -> list[tuple[int, int]]:
    return self.__position

  @property
  def previous_move(self) -> int:
    return self.__previous_move

  def __generate_initial_position(self, size: int) -> tuple[int, int]:
    """
    Generate the random initial position for the player

    The board looks like this:

        +---+---+---+---+---+---+
     0  | # | # | # |...| # | # |
        +---+---+---+---+---+---+
     1  | # |   | 1 | 1 | 1 | # |
        +---+---+---+---+---+---+
     2  | # | 2 |   | 1 | 1 | # |
        +---+---+---+---+---+---+
    ... |...| 2 | 2 |   | 1 |...|
        +---+---+---+---+---+---+
    n-2 | # | 2 | 2 | 2 |   | # |
        +---+---+---+---+---+---+
    n-1 | # | # | # |...| # | # |
        +---+---+---+---+---+---+
          0   1   2  ... n-1 n-2

    :param size: The size of the board
    :type size: int
    :return: The initial position of the player
    :rtype: tuple[int, int]
    """
    if self.__number == PLAYER_1:
      x = randint(2, size - 3)
      y = randint(1, x - 1)

    elif self.__number == PLAYER_2:
      y = randint(2, size - 3)
      x = randint(1, y - 1)

    else:
      raise InvalidPlayerNumberError(f"Invalid player number: {self.__number}")

    return x, y

  def player_suicided(self, new_move: int) -> bool:
    """
    Check if the player suicided

    :return: True if the player suicided, False otherwise
    :rtype: bool
    """
    # Use int() to avoid errors
    match self.__previous_move:
      case 1:  # Move left
        return new_move == MOVE_RIGHT
      case 2:  # Move up
        return new_move == MOVE_DOWN
      case 3:  # Move right
        return new_move == MOVE_LEFT
      case 4:  # Move down
        return new_move == MOVE_UP
      case _:
        return False


class InvalidPlayerNumberError(Exception):
  pass
