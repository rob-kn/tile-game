import pygame as pg

GRID_SQUARE_SIZE = 64
CAMERA_HEIGHT = 11
CAMERA_WIDTH = 13
CENTER_X = int(CAMERA_WIDTH / 2 + 1)
CENTER_Y = int(CAMERA_HEIGHT / 2 + 1)
SCREEN_HEIGHT = CAMERA_HEIGHT * GRID_SQUARE_SIZE
SCREEN_WIDTH = CAMERA_WIDTH * GRID_SQUARE_SIZE
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
COMPLETE_GRID = [line.strip() for line in open('maps/level_0_map.txt').readlines()]
GRID_WIDTH = len(COMPLETE_GRID[0])
GRID_HEIGHT = len(COMPLETE_GRID)

SCORE = 0
done = False
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

pg.init()
screen = pg.display.set_mode(SCREEN_SIZE)
clock = pg.time.Clock()
FONT = pg.font.Font('amatic/Amatic-Bold.ttf', 32)

# Graphics
wall_img = pg.image.load("graphics/crawl-tiles Oct-5-2010/dc-dngn/wall/brick_dark0.png")
wall_img = pg.transform.scale(wall_img, (GRID_SQUARE_SIZE, GRID_SQUARE_SIZE))
player_img = pg.image.load("graphics/crawl-tiles Oct-5-2010/player/transform/dragon_form.png")
player_img = pg.transform.scale(player_img, (GRID_SQUARE_SIZE, GRID_SQUARE_SIZE))
floor_img = pg.image.load("graphics/crawl-tiles Oct-5-2010/dc-dngn/floor/tomb0.png")
floor_img = pg.transform.scale(floor_img, (GRID_SQUARE_SIZE, GRID_SQUARE_SIZE))
strawb_img = pg.image.load("graphics/crawl-tiles Oct-5-2010/item/food/strawberry.png")
strawb_img = pg.transform.scale(strawb_img, (GRID_SQUARE_SIZE, GRID_SQUARE_SIZE))

