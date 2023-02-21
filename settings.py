# game setup
WIDTH = 1280
HEIGHT = 720
FPS = 60
TILE_SIZE = 64

# user interface
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 200
ITEM_BOX_SIZE = 100
UI_FONT = 'assets/font/joystix.ttf'
UI_FONT_SIZE = 20

# general colors
WATER_COLOR = '#71DDEE'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# weapons
weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15, 'image': 'assets/images/weapons/sword/full.png'},
    'lance': {'cooldown': 400, 'damage': 30, 'image': 'assets/images/weapons/lance/full.png'},
    'axe': {'cooldown': 300, 'damage': 20, 'image': 'assets/images/weapons/axe/full.png'},
    'rapier': {'cooldown': 50, 'damage': 8, 'image': 'assets/images/weapons/rapier/full.png'},
    'sai': {'cooldown': 80, 'damage': 10, 'image': 'assets/images/weapons/sai/full.png'}
}
