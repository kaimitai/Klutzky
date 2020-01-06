from os.path import join


class Defines:
    WINDOW_W = 864
    WINDOW_H = 864
    TILE_W = 32
    TILE_H = 32

    RESOURCES_PATH = ".\\resources"
    FONT_PATH = join(RESOURCES_PATH, "fonts")
    GFX_PATH = join(RESOURCES_PATH, "gfx")
    GFX_BLOCK_PATH = join(GFX_PATH, "blocks")
    GFX_BG_PATH = join(GFX_PATH, "bgs")

    KLUTZKY_VERSION = "(alpha version)"
    WINDOW_TITLE = "Klutzky " + KLUTZKY_VERSION
