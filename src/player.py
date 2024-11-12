from random import randint

from .consts import PLAYER_1, PLAYER_2, N_STELLA


class Player:
  def __init__(self, number: int, size: int):
    self.__number: int = number
    self.__position: list[tuple[int, int]] = [self.__generate_initial_position(size)] + [None] * N_STELLA
    self.__previous_move: int = 0  # 0 means no previous move

  @property
  def number(self) -> int:
    return self.__number

  @property
  def position(self) -> tuple[int, int]:
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
     1  | # |   | 2 | 2 | 2 | # |
        +---+---+---+---+---+---+
     2  | # | 1 |   | 2 | 2 | # |
        +---+---+---+---+---+---+
    ... |...| 1 | 1 |   | 2 |...|
        +---+---+---+---+---+---+
    n-2 | # | 1 | 1 | 1 |   | # |
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


class InvalidPlayerNumberError(Exception):
  pass
