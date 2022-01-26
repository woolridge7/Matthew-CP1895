"""
Lightbulb
----------
attribute:
wattage: int
is_led: bool
brand_name: str
is_on: bool
brightness: int
----------
methods:
turn_on()
turn_off()
to_string() -> prints wattage, brand etc (general info)
set_brightness(level) : 0 - 10
"""

class Lightbulb:
    def __init__(self, wattage, is_led, brand_name, is_on, brightness):
        '''
        assert isinstance(int, wattage), 'wattage must be an int'
        assert isinstance(bool, is_led), 'is_led must be a bool'
        assert isinstance(str, brand_name), 'brand_name must be str'
        assert isinstance(bool, is_on), 'is_on must be bool'
        assert isinstance(int, brightness), 'brightness must be int'
        '''
        self.wattage = wattage
        self.is_led = is_led
        self.brand_name = brand_name
        self.is_on = is_on
        self.brightness = brightness

    def print_info(self):
        print("Wattage:                         " + str(self.wattage) + 'W')
        print("Is it Led:                       " + str(self.is_led))
        print("What is the brand name:          " + str(self.brand_name))
        print("Is the lightbulb on:             " + str(self.is_on))
        print("What is the level of brightness: " + str(self.brightness))

lightbulb_object = Lightbulb(100, True, 'GE', True, 8)
lightbulb_object.print_info()