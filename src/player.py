class Player:
  def __init__(self, number: int, initial_position: tuple[int, int]):
    self.__number: int = number
    self.__position: tuple[int, int] = initial_position
    self.__previous_move: int = 0

  @property
  def number(self) -> int:
    return self.__number

  @property
  def position(self) -> tuple[int, int]:
    return self.__position

  @property
  def previous_move(self) -> int:
    return self.__previous_move
