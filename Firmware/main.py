import board
import digitalio
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.extensions.rgb import RGB
from kmk.extensions.oled import Oled, OledData
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

keyboard.col_pins = (
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4,
    board.GP5, board.GP6, board.GP7, board.GP8, board.GP9,
    board.GP10, board.GP11, board.GP12, board.GP13, board.GP14,
)
keyboard.row_pins = (
    board.GP15, board.GP16, board.GP17, board.GP18, board.GP19,
    board.GP20,
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.GP21, board.GP22, board.GP23),)  # adjust pins
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD),)  
]
keyboard.modules.append(encoder_handler)

rgb = RGB(
    pixel_pin=board.GP24,   # DIN pin for SK6812 LEDs
    num_pixels=90,          # adjust to number of LEDs in schematic
    hue_default=180,
    sat_default=255,
    val_default=100,
)
keyboard.extensions.append(rgb)

oled = Oled(
    i2c=busio.I2C(board.GP25, board.GP26),  # SDA, SCL pins
    width=128,
    height=64,
    flip=False,
)
keyboard.extensions.append(oled)
def draw(oled_data: OledData):
    oled_data.text("Hi :3", 0, 0)


keyboard.keymap = [
    [
        KC.ESC, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSPC, KC.NO, KC.NO, KC.NO,
        KC.TAB, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.ENT, KC.NO, KC.NO, KC.NO,
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.NO, KC.NO, KC.NO,
        KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.RALT, KC.RGUI, KC.RCTL, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
    ]
]

if __name__ == '__main__':
    keyboard.go()
