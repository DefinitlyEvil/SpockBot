"""
These constants are used in some plugins, but do not belong there.
Some of them can later be extracted from minecraft-data
"""

###########
# Physics #
###########

CLIENT_TICK_RATE = 0.05
PLAYER_HEIGHT = 1.80
PLAYER_WIDTH = 0.6

# These values are strictly for player and maybe mob physics, different types
# of entities have different drag coefficients and gravitational accelerations
# Someone who isn't nickelpro can go do all the other possible values if they
# want

PHY_GAV_ACC = 0.08
PHY_WLK_ACC = 0.10
PHY_FLY_ACC = 0.05
PHY_JMP_ACC = 0.02

PHY_JMP_ABS = 0.42

PHY_SOULSAND = 0.40
PHY_BASE_DRG = 0.98

PHY_DRG_MUL = 0.91
PHY_SPR_MUL = 1.30
PHY_JMP_MUL = 0.2

# Slipperiness value for normal materials
BASE_GND_SLIP = 0.6

############
# Interact #
############

INTERACT_ENTITY = 0
ATTACK_ENTITY = 1
INTERACT_ENTITY_AT = 2

ENTITY_ACTION_SNEAK = 0
ENTITY_ACTION_UNSNEAK = 1
ENTITY_ACTION_LEAVE_BED = 2
ENTITY_ACTION_START_SPRINT = 3
ENTITY_ACTION_STOP_SPRINT = 4
ENTITY_ACTION_JUMP_HORSE = 5
ENTITY_ACTION_OPEN_INVENTORY = 6

# the six faces of a block
FACE_Y_NEG = 0
FACE_Y_POS = 1
FACE_Z_NEG = 2
FACE_Z_POS = 3
FACE_X_NEG = 4
FACE_X_POS = 5

DIG_START = 0
DIG_CANCEL = 1
DIG_FINISH = 2
DIG_DROP_STACK = 3
DIG_DROP_ITEM = 4
DIG_DEACTIVATE_ITEM = 5

CHAT_POS_CHAT = 0
CHAT_POS_SYSTEM_MESSAGE = 1
CHAT_POS_ABOVE_HOTBAR = 2

BOOK_MAXPAGES = 50
BOOK_CHARS_PER_PAGE = 266

#############
# Inventory #
#############

# the button codes used in send_click
INV_BUTTON_LEFT = 0
INV_BUTTON_RIGHT = 1
INV_BUTTON_MIDDLE = 2

INV_OUTSIDE_WINDOW = -999
INV_SLOT_NR_CURSOR = -1
INV_WINID_CURSOR = -1  # the slot that follows the cursor
# player inventory window ID/type, not opened but updated by server
INV_WINID_PLAYER = 0
INV_ITEMID_EMPTY = -1

INV_SLOTS_PLAYER = 9  # crafting and armor
INV_SLOTS_INVENTORY = 9 * 3  # above hotbar
INV_SLOTS_HOTBAR = 9
# always accessible
INV_SLOTS_PERSISTENT = INV_SLOTS_INVENTORY + INV_SLOTS_HOTBAR

##############
# ClientInfo #
##############

GM_SURVIVAL = 0x00
GM_CREATIVE = 0x01
GM_ADVENTURE = 0x02
GM_SPECTATOR = 0x03

FLG_XPOS_REL = 0x01
FLG_YPOS_REL = 0x02
FLG_ZPOS_REL = 0x04
FLG_YROT_REL = 0x08
FLG_XROT_REL = 0x10

#########
# World #
#########

SMP_NETHER = -0x01
SMP_OVERWORLD = 0x00
SMP_END = 0x01

##########
# Blocks #
##########

# Gate
BLOCK_GATE_SOUTH = 0x00
BLOCK_GATE_WEST = 0x01
BLOCK_GATE_NORTH = 0x02
BLOCK_GATE_EAST = 0x03

BLOCK_GATE_CLOSE = 0x00
BLOCK_GATE_OPEN = 0x01

BLOCK_GATE_UNPOWERED = 0x00
BLOCK_GATE_POWERED = 0x01

# Door
BLOCK_DOOR_WEST = 0x00
BLOCK_DOOR_NORTH = 0x01
BLOCK_DOOR_EAST = 0x02
BLOCK_DOOR_SOUTH = 0x03

BLOCK_DOOR_CLOSE = 0x00
BLOCK_DOOR_OPEN = 0x01

BLOCK_DOOR_LOWER = 0x00
BLOCK_DOOR_UPPER = 0x01

BLOCK_DOOR_HINGE_LEFT = 0x00
BLOCK_DOOR_HINGE_RIGHT = 0x01


# Trapdoor
BLOCK_TRAPDOOR_WEST = 0x00
BLOCK_TRAPDOOR_NORTH = 0x01
BLOCK_TRAPDOOR_EAST = 0x02
BLOCK_TRAPDOOR_SOUTH = 0x03

BLOCK_TRAPDOOR_CLOSE = 0x00
BLOCK_TRAPDOOR_OPEN = 0x01

BLOCK_TRAPDOOR_LOWER = 0x00
BLOCK_TRAPDOOR_UPPER = 0x01

# Slab
BLOCK_SLAB_LOWER = 0x00
BLOCK_SLAB_UPPER = 0x01

############
# Protocol #
############

# Clientbound 0x38 Player List Item
PL_ADD_PLAYER = 0x00
PL_UPDATE_GAMEMODE = 0x01
PL_UPDATE_LATENCY = 0x02
PL_UPDATE_DISPLAY = 0x03
PL_REMOVE_PLAYER = 0x04

# Clientbound 0x3B Scoreboard Objective
SO_CREATE_BOARD = 0x00
SO_REMOVE_BOARD = 0x01
SO_UPDATE_BOARD = 0x02

# Clientbound 0x3C Update Score
US_UPDATE_SCORE = 0x00
US_REMOVE_SCORE = 0x01

# Clientbound 0x3E Teams
TE_CREATE_TEAM = 0x00
TE_REMOVE_TEAM = 0x01
TE_UPDATE_TEAM = 0x02
TE_ADDPLY_TEAM = 0x03
TE_REMPLY_TEAM = 0x04

# Clientbound 0x42 Combat Event
CE_ENTER_COMBAT = 0x00
CE_END_COMBAT = 0x01
CE_ENTITY_DEAD = 0x02

# Clientbound 0x44 World Border
WB_SET_SIZE = 0x00
WB_LERP_SIZE = 0x01
WB_SET_CENTER = 0x02
WB_INITIALIZE = 0x03
WB_SET_WARN_TIME = 0x04
WB_SET_WARN_BLOCKS = 0x05

# Clientbound 0x45 Title
TL_TITLE = 0x00
TL_SUBTITLE = 0x01
TL_TIMES = 0x02
TL_CLEAR = 0x03
TL_RESET = 0x04

# Serverbound 0x16 Client Status
CL_STATUS_RESPAWN = 0x00
CL_STATUS_STATS = 0x01
CL_STATUS_INV = 0x02

# Clientbound 0x2B Change Game State
GS_INVALID_BED = 0x00
GS_END_RAIN = 0x01
GS_START_RAIN = 0x02
GS_GAMEMODE = 0x03
GS_CREDITS = 0x04
GS_DEMO_MESSAGE = 0x05
GS_ARROW = 0x06
GS_FADE_VALUE = 0x07
GS_FADE_TIME = 0x08
