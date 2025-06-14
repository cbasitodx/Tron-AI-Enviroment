import pygame

from frontend.consts import *

from base.consts import PLAYER_1, PLAYER_2, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT, MOVE_UP
from base.player import Player
from Tron import Tron


class Frontend:
    def __init__(self, game: Tron, cell_size: int, caption: str = "Tron Game"):
        pygame.init()
        self.game = game

        self.cell_size = cell_size

        self.base_size = self.game.size * self.cell_size
        self.width = self.base_size
        self.height = self.base_size + 50

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(caption)
        self.font = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()

    def __draw_cell(self, x: int, y: int, color: tuple[int, int, int]) -> None:
        pygame.draw.rect(
            self.screen,
            color,
            (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
        )

    def draw_grid(self) -> None:
        for i in range(self.game.size):
            for j in range(self.game.size):
                if i % 3 == 0 or j % 3 == 0:
                    self.__draw_cell(i, j, COLOR_GREY)
                else:
                    self.__draw_cell(i, j, COLOR_PURPLE)

    def __draw_player_head(self, player: Player) -> None:
        head_pos = player.position[0]
        if head_pos is None:
            raise ValueError("Player head position is None")

        if player.number == PLAYER_1:
            color = COLOR_P1_HEAD

        elif player.number == PLAYER_2:
            color = COLOR_P2_HEAD

        else:
            raise ValueError("Invalid player number")

        self.__draw_cell(head_pos[1], head_pos[0], color)

    def __draw_player_trail(self, player: Player) -> None:
        for pos in player.position[1:]:
            if pos is None:
                break
            if player.number == PLAYER_1:
                color = COLOR_P1_TRAIL
            elif player.number == PLAYER_2:
                color = COLOR_P2_TRAIL
            else:
                raise ValueError("Invalid player number")
            self.__draw_cell(pos[1], pos[0], color)

    def __draw_walls(self) -> None:
        for wall in self.game.board.walls:
            self.__draw_cell(wall[1], wall[0], COLOR_WALL)

    def draw_game_board(self) -> None:
        self.screen.fill(COLOR_BLACK)
        self.draw_grid()
        self.__draw_player_head(self.game.player_1)
        self.__draw_player_head(self.game.player_2)
        self.__draw_player_trail(self.game.player_1)
        self.__draw_player_trail(self.game.player_2)
        pygame.display.flip()

    def display_winner(self, winner: int) -> None:
        self.screen.fill(COLOR_BLACK)
        if winner is None:
            text = "It's a draw!"
        elif winner == PLAYER_1:
            text = "Player 1 wins!"
        elif winner == PLAYER_2:
            text = "Player 2 wins!"
        else:
            raise ValueError("Invalid winner number")

        text_surface = self.font.render(text, True, COLOR_WHITE)
        text_rect = text_surface.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(text_surface, text_rect)
        pygame.display.flip()
        pygame.time.delay(2000)
