import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeyMatrixScanner
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.peg_oled_display import Oled, OledDisplayMode, OledReactionType, OledData

keyboard = KMKKeyboard()

keyboard.scanner = KeyMatrixScanner(
    row_pins=(board.A0, board.A1, board.A2),
    col_pins=(board.A5, board.A7, board.A8),
    columns_to_anodes=True,
)

layers = Layers()
keyboard.modules.append(layers)

encoder = EncoderHandler()
encoder.pins = ((board.A3, board.TX, board.A10, False),)
keyboard.modules.append(encoder)

oled = Oled(
    OledData(
        corner_one={0: OledReactionType.STATIC, 1: ['BASE']},
        corner_two={0: OledReactionType.LAYER, 1: ['BASE', 'FN']},
        corner_three={0: OledReactionType.STATIC, 1: ['ENC:ARW']},
        corner_four={0: OledReactionType.LAYER, 1: ['ENC:ARW', 'ENC:VOL']},
    ),
    toDisplay=OledDisplayMode.TXT,
    flip=False,
)
keyboard.extensions.append(oled)

MO1 = KC.MO(1)

keyboard.keymap = [
    [
        KC.N1,  KC.N2,  KC.N3,
        KC.N4,  KC.N5,  KC.N6,
        KC.N7,  KC.N8,  MO1,
    ],
    [
        KC.F1,   KC.F2,   KC.F3,
        KC.MUTE, KC.VOLD, KC.VOLU,
        KC.TRNS, KC.TRNS, KC.TRNS,
    ],
]

encoder.map = [
    ((KC.LEFT, KC.RIGHT),),
    ((KC.VOLD, KC.VOLU),),
]

if __name__ == '__main__':
    keyboard.go()
