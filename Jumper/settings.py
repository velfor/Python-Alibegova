
SC_WIDTH = 600
SC_HEIGHT = 800
FPS = 60
FONT_NAME = 'arial'

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.1
PLAYER_JUMP_SPEED = -15
GRAVITY = 0.5

PLATFORM_LIST = [(0, SC_HEIGHT - 40, SC_WIDTH, 40),
                 (SC_WIDTH/4, SC_HEIGHT*3/4, SC_WIDTH/2, 40),
                 (SC_WIDTH*3/4, SC_HEIGHT/2, SC_WIDTH/5, 20),
                 (SC_WIDTH/4, SC_HEIGHT/4, SC_WIDTH/5, 20)
                ]
PLATFORMS_QTY = 7
