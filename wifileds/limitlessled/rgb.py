import sys

class RGB:
    def effect(self, effect_name, args=[], effect_options={}):
        effect = sys.modules['wifileds.limitlessled.effects.%s' % effect_name]
        try:
            effect.run(self, *args, **effect_options)
        except AttributeError as e:
            logging.error('Effect "%s" failed due to missing lighting attribute: %s' % (effect_name, e))
            pass

    def __init__(self, parent):
        self.parent = parent
        self.long_pause = parent.long_pause
        self.short_pause = parent.short_pause

        self.color_map = {
            'violet': 0x00,
            'royal_blue': 0x10,
            'baby_blue': 0x20,
            'aqua': 0x30,
            'mint': 0x40,
            'seafoam_green': 0x50,
            'green': 0x60,
            'lime_green': 0x70,
            'yellow': 0x80,
            'yellow_orange': 0x90,
            'orange': 0xA0,
            'red': 0xB0,
            'pink': 0xC0,
            'fusia': 0xD0,
            'lilac': 0xE0,
            'lavendar': 0xF0
        }

    def all_on(self):
        self.parent.send_command(0x22)

    def all_off(self):
        self.parent.send_command(0x21)

    def brightness_up(self):
        self.parent.send_command(0x23)

    def brightness_down(self):
        self.parent.send_command(0x24)

    def mode_up(self):
        self.parent.send_command(0x27)

    def mode_down(self):
        self.parent.send_command(0x28)

    def speed_up(self):
        self.parent.send_command(0x25)

    def speed_down(self):
        self.parent.send_command(0x26)

    def set_color(self, color_name):
        try:
            self.set_color_hex(self.color_map[color_name])
        except KeyError as e:
            raise KeyError('Color not found: %s' % e)

    def set_color_hex(self, color_value):
        self.parent.send_command(0x20, color_value)

    def max_brightness(self):
        for i in range(0, 9):
            self.brightness_up()
            self.parent.short_pause()

    def min_brightness(self):
        for i in range(0, 9):
            self.brightness_down()
            self.parent.short_pause()

    def white(self):
        for i in range(0, 20):
            self.mode_down()

    def party_mode(self, number):
        self.white()
        for i in range(0, number):
            self.mode_up()