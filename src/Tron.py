from typing import List

from re import findall

from .consts import *
from .player import Player


class Tron:
  def __init__(self, height: int, width: int):
    # Dimensions of the board
    self.__height: int = height
    self.__width: int = width

    # Game board. 0 means empty, 1 means player 1, 2 means player 2
    self.__board: List[List[int]] = [[0] * width] * height
    self.__board[0][0] = PLAYER_1
    self.__board[width - 1][height - 1] = PLAYER_2

    # Players current position (they are indices in self.board)
    self.__p1_pos: tuple = (0, 0)
    self.__p2_pos: tuple = (width - 1, height - 1)

    # Players turns
    self.__is_p1_turn: bool = False
    self.__is_p2_turn: bool = False

    # Flag for breaking the game loop
    self.__game_over: bool = False

    # Winner of the game
    self.__winner: int = 0  # When set to 0, this variables indicates that no one has won the game yet

  def __is_valid_move(self, move: int) -> bool:
    if not isinstance(move, int):
      return False

    if 1 <= move <= 4:
      return True

    return False

  def __collision_happened(self, player_a: Player, player_b: Player) -> bool:
    """
    Check if a collision happened
    """
    raise NotImplementedError

  def play(self) -> None:
    # TODO: AQUI VA A ESTAR EL GAME LOOP (while not self.__game_over). TIENE QUE:
    #   * ASIGNAR UN TURNO
    #   * ESPERAR POR ESE FICHERO (AQUI HACER FUNCIONES AUXILIARES)
    #   * UNA VEZ TENGA EL MOVIMIENTO EN EL FICHERO, LEERLO
    #   * COMPROBAR SI ES VALIDO
    #   * COMPROBAR SI HUBO COLISION
    #   * SI LAS DOS ANTERIORES NO OCURREN, HACER EL MOVIMIENTO (ACTUALIZAR EL BOARD)
    #   * QUITAR TURNO Y ASIGNAR TURNO CONTRARIO
    #   * REPETIR PROCESO CON EL OTRO JUGADOR
    #   * UNA VEZ HECHO, QUITARLE EL TURNO
    #   * ESCRIBIR EL NUEVO TABLERO EN EL FICHERO
    #   * REPETIR DESDE EL COMIENZO!
    raise NotImplementedError


def read_file(player: int) -> str:
  """
  Read the moves from the file of the player
  """
  if player == PLAYER_1:
    with open(MOVES_1, "r") as file:
      return file.read()

  elif player == PLAYER_2:
    with open(MOVES_2, "r") as file:
      return file.read()

  else:
    raise ValueError("Invalid player number")


def validate_move(move: str) -> bool:
  """
  Validate the move from the player.
  Valid moves are: 1, 2, 3; representing left, up, right respectively
  """
  return len(findall(r"[1-3]", move)) == 1
