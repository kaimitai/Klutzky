import pygame
from pygame import DOUBLEBUF, HWSURFACE
from common import gfxmanager
from common import defines
from common.defines import Defines
import block

mouse_down = False
selected_block_index = -1


def main():
    global mouse_down, selected_block_index
    screen = pygame.display.set_mode((Defines.WINDOW_W, Defines.WINDOW_H), DOUBLEBUF | HWSURFACE)
    pygame.init()
    pygame.display.set_caption(Defines.WINDOW_TITLE)
    gfxmanager.load_graphics()
    pygame.display.set_icon(gfxmanager.block_gfx[1])

    blox = [block.Block([[0, 0, 0, 1], [1, 1, 1, 1]], 10, 10),
            block.Block([[1, 1, 0, 0], [0, 1, 1, 1]], 15, 15),
            block.Block([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 22, 3)]

    while True:
        mx, my = pygame.mouse.get_pos()
        gx, gy = gfxmanager.mouse_to_grid_coords(mx, my)

        for e in pygame.event.get():
            if (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE) or e.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True
            elif e.type == pygame.MOUSEBUTTONUP:
                mouse_down = False
                if selected_block_index != -1:
                    blox[selected_block_index].x = gx
                    blox[selected_block_index].y = gy
                    selected_block_index = -1

        gfxmanager.draw_background(screen)
        gfxmanager.step_background()

        for b in blox:
            gfxmanager.draw_block(screen, b)

        gfxmanager.draw_text(screen, "ABDEFGHIJKLMNOPQRSTUVWXYZ 024689", 0)

        if mouse_down:
            for i in range(len(blox)):
                if blox[i].contains_cell(gx, gy):
                    selected_block_index = i

        pygame.display.update()


if __name__ == "__main__": main()
