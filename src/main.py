import asyncio

from Tron import Tron

from Frontend import Frontend

from base.move import Move


async def play_game(tron: Tron, frontend: Frontend):
    while not tron.game_over:
        move_1, move_2 = await tron.get_moves()

        # Get the last position of the players to remove them from the matrix
        last_pos_1 = tron.player_1.position[-1]
        last_pos_2 = tron.player_2.position[-1]

        # Move the players
        Move.move_player(tron.player_1, move_1)
        Move.move_player(tron.player_2, move_2)

        # Check for collisions
        end_message = tron.handle_collisions()

        if end_message:
            print(end_message)

        # Update the matrix
        tron.board.update_board(last_pos_1, last_pos_2)

        frontend.draw_game_board()


async def main():
    tron = Tron(16)
    frontend = Frontend(tron, 30)

    frontend.draw_game_board()
    await play_game(tron, frontend)


if __name__ == "__main__":
    asyncio.run(main())
