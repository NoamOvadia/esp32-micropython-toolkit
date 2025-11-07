# No Color
NONE = (0, 0, 0)

# Basic Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Extended Colors
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)
BROWN = (165, 42, 42)
GRAY = (128, 128, 128)
LIME = (0, 255, 0)
NAVY = (0, 0, 128)
TEAL = (0, 128, 128)
MAROON = (128, 0, 0)
OLIVE = (128, 128, 0)

# Light Shades
LIGHT_RED = (255, 128, 128)
LIGHT_GREEN = (144, 238, 144)
LIGHT_BLUE = (173, 216, 230)
LIGHT_YELLOW = (255, 255, 224)
LIGHT_PINK = (255, 182, 193)

# Dark Shades
DARK_RED = (139, 0, 0)
DARK_GREEN = (0, 100, 0)
DARK_BLUE = (0, 0, 139)
DARK_GRAY = (169, 169, 169)

# Warm Colors
CORAL = (255, 127, 80)
SALMON = (250, 128, 114)
GOLD = (255, 215, 0)
AMBER = (255, 191, 0)

# Cool Colors
TURQUOISE = (64, 224, 208)
AQUA = (0, 255, 255)
SKY_BLUE = (135, 206, 235)
LAVENDER = (230, 230, 250)

ALL_COLORS = [
    NONE,
    WHITE,
    RED,
    GREEN,
    BLUE,
    YELLOW,
    CYAN,
    MAGENTA,
    ORANGE,
    PURPLE,
    PINK,
    BROWN,
    GRAY,
    LIME,
    NAVY,
    TEAL,
    MAROON,
    OLIVE,
    LIGHT_RED,
    LIGHT_GREEN,
    LIGHT_BLUE,
    LIGHT_YELLOW,
    LIGHT_PINK,
    DARK_RED,
    DARK_GREEN,
    DARK_BLUE,
    DARK_GRAY,
    CORAL,
    SALMON,
    GOLD,
    AMBER,
    TURQUOISE,
    AQUA,
    SKY_BLUE,
    LAVENDER
]


def get_cool_colors() -> list:
    return [TURQUOISE, AQUA, SKY_BLUE, LAVENDER]

def get_warm_colors() -> list:
    return [CORAL, SALMON, GOLD, AMBER]

def get_dark_shades_colors() -> list:
    return [DARK_RED, DARK_GREEN, DARK_BLUE, DARK_GRAY]

def get_light_shades_colors() -> list:
    return [LIGHT_RED, LIGHT_GREEN, LIGHT_BLUE, LIGHT_YELLOW, LIGHT_PINK]

def get_extended_colors() -> list:
    return [ORANGE, PURPLE, PINK, BROWN, GRAY, LIME, NAVY, TEAL, MAROON, OLIVE]

def get_basic_colors() -> list:
    return [WHITE, RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA]





