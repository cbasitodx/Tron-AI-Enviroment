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
    if self.__number == PLAYER_1:
      x = randint(1, size - 1)
      y = randint(0, x - 2)

    elif self.__number == PLAYER_2:
      y = randint(1, size - 1)
      x = randint(1, y - 2)

    else:
      raise InvalidPlayerNumberError(f"Invalid player number: {self.__number}")

    return x, y


class InvalidPlayerNumberError(Exception):
  pass
