from typing import List

from .consts import *
from .player import Player


class Tron:
  def __init__(self, size: int):
    # Dimensions of the board
    self.__size: int = size

    # Players
    self.__player_1: Player = Player(PLAYER_1, size)
    self.__player_2: Player = Player(PLAYER_2, size)

    # Players turns
    self.__is_p1_turn: bool = False
    self.__is_p2_turn: bool = False

    # Game board. 0 means empty, 1 means player 1, 2 means player 2
    self.__board: List[List[int]] = [[0] * size] * size
    self.__walls: list[tuple[int, int]] = []
    self.__init_walls()

    # Flag for breaking the game loop
    self.__game_over: bool = False

    # Winner of the game
    self.__winner: int = 0  # When set to 0, this variables indicates that no one has won the game yet

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

  def __collision_happened(self, player_1: Player, player_2: Player) -> int | None:
    """
    Check if a collision happened

    :return: The type of collision that happened or None if no collision happened
    :rtype: PLAYERS_COLLIDED | PLAYER_1_COLLIDED | PLAYER_2_COLLIDED | BOTH_WALLS | None
    """
    if player_1.position[0] == player_2.position[0]:
      return PLAYERS_COLLIDED

    if player_1.position[0] in player_2.position or player_1.position[0] in self.__walls:
      return PLAYER_1_COLLIDED

    if player_2.position[0] in player_1.position or player_2.position[0] in self.__walls:
      return PLAYER_2_COLLIDED

    if player_1.position[0] in self.__walls and player_2.position[0] in self.__walls:
      return BOTH_WALLS

    return None

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
