from typing import List

class Tron:

    def __init__(self, 
                 height : int, 
                 width : int):

        # Dimensions of the board
        self.__height : int = height
        self.__width  : int = width

        # Game board
        self.__board : List[List[int]] = [[0]*width]*height 

        # Players current position (they are indices in self.board)
        self.__p1_pos : tuple = (0,0)
        self.__p2_pos : tuple = (width - 1, height - 1)

        # Players turns 
        self.__is_p1_turn : bool = False
        self.__is_p2_turn : bool = False

        # Flag for breaking the game loop
        self.__game_over : bool = False

        # Winner of the game
        self.__winner : int = 0 # When set to 0, this variables indicates that no one has won the game yet
    
    def __is_valid_move(self, new_position : tuple) -> bool:
        if  (
                (new_position[0] < 0 or new_position[0] >= self.__width) or
                (new_position[1] < 0 or new_position[1] >= self.__height)
            ):

            # If an illegal move is attempted, then end the game
            self.__game_over = True
            return False
        
        else:
            return True
    
    def __collision_happened(self, new_position : tuple) -> bool:
        # TODO: TIENE QUE REVISAR SI OCURRIO UNA COLISION Y TIENE JUGADOR MURIO (VIENDO EL TURNO)
        pass

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
        pass
