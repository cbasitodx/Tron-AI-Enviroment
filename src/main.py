import asyncio

from GameState import GameState

from Frontend import Frontend

from base.input import get_input
from base.player import Player


async def get_moves(game: GameState) -> tuple[tuple[int, int], tuple[int, int]]:
    player_1 = game.player_1
    player_2 = game.player_2

    move_1, move_2 = await asyncio.gather(get_input(player_1.number), get_input(player_2.number))

    if not Player.is_valid_move(move_1) or player_1.player_suicided(move_1):
        move_1 = player_1.previous_move
    if not Player.is_valid_move(move_2) or player_2.player_suicided(move_2):
        move_2 = player_2.previous_move

    return move_1, move_2


async def play(game: GameState, frontend: Frontend):
    while not game.game_over:
        move_1, move_2 = await get_moves(game)
        game.tick(move_1, move_2)
        frontend.draw_game_board()


async def main():
    game = GameState(16)
    frontend = Frontend(game, 30)

    frontend.draw_game_board()
    await play(game, frontend)


if __name__ == "__main__":
    asyncio.run(main())
