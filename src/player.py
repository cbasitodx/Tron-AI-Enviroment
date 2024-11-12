from random import randint

from .consts import PLAYER_1, PLAYER_2


class Player:
  def __init__(self, number: int, size: int):
    self.__number: int = number
    self.__position: list[tuple[int, int]] = [self.__generate_initial_position(size)] + [(0, 0)] * 5
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
    This function generates the initial position of the player.
    The posible positions are the following:

          0   1   2  ... n-2 n-1
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

    Where the # is a wall, 1 is player 1 and 2 is player 2.
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
