# config.py

# Grid and Room Settings
GRID_ROWS = 3
GRID_COLS = 3
ROOM_WIDTH = 200
ROOM_HEIGHT = 200
WALL_THICK = 4
DOOR_SIZE = 40

# Player Settings
PLAYER_RADIUS = 10
PLAYER_SPEED = 100

# Screen Size
WIDTH = ROOM_WIDTH * GRID_COLS
HEIGHT = ROOM_HEIGHT * GRID_ROWS

# Colors (R, G, B)
BG_COLOR = (204, 0, 102)
WALL_COLOR = (255, 204, 255)
PLAYER_COLOR = (100, 200, 255)
BOX_COLOR = (225,153,100)

# Frames Per Second
FPS = 60

# --- Player appearance ---
PLAYER_IMAGE_PATH = "./Squirrel.png"  # transparent PNG, e.g. 48x48
PLAYER_IMAGE_SIZE = (75, 75)             # w, h in pixels
PLAYER_RADIUS = 24                       # half of width; used by your collision