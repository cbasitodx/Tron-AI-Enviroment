from src.player import Player


class Move:
    @staticmethod
    def move_player(player: Player, move: int) -> None:
        new_pos = Move.__get_new_position(player, move)
        player.move(new_pos, move)

    @staticmethod
    def __get_new_position(player: Player, move: int) -> tuple[int, int]:
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

    @staticmethod
    def is_valid_move(move: int) -> bool:
        if not isinstance(move, int):
            return False

        return 1 <= move <= 4
