class Player:
  def __init__(self, number: int, initial_position: tuple[int, int]):
    self.__number: int = number
    self.__position: tuple[int, int] = initial_position
    self.__dash: list[tuple[int, int]] = [initial_position]

  @property
  def number(self) -> int:
    return self.__number

  @property
  def position(self) -> tuple[int, int]:
    return self.__position

  @property
  def dash(self) -> list[tuple[int, int]]:
    return self.__dash
