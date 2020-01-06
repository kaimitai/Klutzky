import pygame
import shutil
from os.path import join
from os import walk

from common.defines import Defines


def draw_block(surface, block):
    for i in range(block.w()):
        for j in range(block.h()):
            if block.layout[j][i] == 1:
                surface.blit(block_gfx[0], (Defines.TILE_W * (block.x + i), Defines.TILE_H * (block.y + j)))


class Background:
    steps_per_frame = 10
    current_step = 0
    bg_pos = [0, 0]
    bg_index = 0


block_gfx = []
bg_gfx = []
font_gfx = []
gfx_font = None


def step_background():
    Background.current_step += 1
    if Background.current_step >= Background.steps_per_frame:
        Background.current_step = 0
    else:
        return

    Background.bg_pos[0] += 1
    if Background.bg_pos[0] >= bg_gfx[Background.bg_index].get_size()[0]:
        Background.bg_pos[0] = 0
    Background.bg_pos[1] += 1
    if Background.bg_pos[1] >= bg_gfx[Background.bg_index].get_size()[1]:
        Background.bg_pos[1] = 0


def draw_background(surface):
    w, h = bg_gfx[Background.bg_index].get_size()
    for i in range(-1 - Background.bg_pos[0], Defines.WINDOW_W, w):
        for j in range(-1 - Background.bg_pos[1], Defines.WINDOW_H, h):
            surface.blit(bg_gfx[Background.bg_index], (i, j))


def load_graphics():
    global gfx_font
    load_gfx(Defines.GFX_BLOCK_PATH, block_gfx, Defines.TILE_W, Defines.TILE_H)
    load_gfx(Defines.GFX_BG_PATH, bg_gfx, None, None)
    gfx_font = pygame.font.Font(join(Defines.FONT_PATH, "ToetheLineless.ttf"), 40)


def load_gfx(file_path, result, scale_w, scale_h):
    for _, _, file_list in walk(file_path):
        for file_name in file_list:
            tmp_surface = pygame.image.load(join(file_path, file_name)).convert_alpha()
            if scale_w is not None:
                tmp_surface = pygame.transform.scale(tmp_surface, (scale_w, scale_h))
            result.append(tmp_surface)


def draw_text(surface, text, color):
    text_surface = gfx_font.render(text, False, (0, 0, 0))
    surface.blit(text_surface, (0, 0))


def mouse_to_grid_coords(mx, my):
    return mx // Defines.TILE_W, my // Defines.TILE_H
