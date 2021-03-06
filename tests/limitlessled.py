#!/usr/bin/env python

import time

from optparse import OptionParser

import wifileds

if __name__=="__main__":
    parser = OptionParser()
    parser.add_option('-a', '--address', default='192.168.1.100', help='wifi block ip address')
    parser.add_option('-p', '--port', type='int', default=50000, help='wifi block port address')
    (options, args) = parser.parse_args()

    print 'Create a connection to the wifi bridge...'
    led_connection = wifileds.limitlessled.connect(options.address, options.port)

    print 'Turn on all color lights...'
    led_connection.rgb.all_on()

    print 'Fade lights all the way up...'
    led_connection.rgb.effect('fade_up')

    print 'Ensure they cannot get brighter...'
    time.sleep(1)
    led_connection.rgb.effect('fade_up')

    print 'Change to lilac...'
    led_connection.rgb.set_color('lilac')
    time.sleep(1)

    print 'Change to yellow...'
    led_connection.rgb.set_color('yellow')
    time.sleep(1)

    print 'Fade lights all the way down...'
    led_connection.rgb.effect('fade_down')

    print 'Ensure they cannot get dimmer...'
    time.sleep(1)
    led_connection.rgb.effect('fade_down')

    print 'Return to full brightness...'
    led_connection.rgb.effect('fade_up')

    print 'Colorful strobe effect. Can be customized to select only certain colors...'
    led_connection.rgb.effect('colorful_strobe')

    print 'Wave pattern with the fading of the lights...'
    led_connection.rgb.effect('fade_up')
    led_connection.rgb.effect('fade_down')
    led_connection.rgb.effect('fade_up')
    led_connection.rgb.effect('fade_down')

    print 'Police flashers effects. Colors can be customized or fully random...'
    led_connection.rgb.effect('police_flashers')

    print 'Pulsating yellow factory flashers. Colors can be customized or fully random...'
    led_connection.rgb.effect('pulsating_swells', effect_options={'duration': 15})

    print 'Rainbow fade. Speed of change and difference of change can be customized...'
    led_connection.rgb.effect('rainbow_fade', effect_options={'delta': 5})

    print 'Strobe effect based on the previously set color...'
    led_connection.rgb.effect('strobe', effect_options={'duration': 5})

    print 'Flash the lights a final time...'
    led_connection.rgb.all_off()
    time.sleep(1)
    led_connection.rgb.all_on()

    print '=' * 20
    print 'Now focusing on the white bulbs...\n'

    print 'Turn on all color lights...'
    led_connection.white.all_on()

    print 'Wave pattern with the fading of the lights...'
    led_connection.white.effect('fade_up')
    led_connection.white.effect('fade_down')
    led_connection.white.effect('fade_up')
    led_connection.white.effect('fade_down')
    time.sleep(1)

    print 'Turn off all lights...'
    led_connection.white.all_off()
    time.sleep(1)

    print 'Turn on one zone at a time...'
    for i in range(1, 5):
        led_connection.white.zone_on(i)
        time.sleep(1)
    time.sleep(1)

    print 'Make all lights nightlights...'
    led_connection.white.nightlight_all()
    time.sleep(2)

    print 'Get all lights to full brightness...'
    led_connection.white.full_all()
    time.sleep(2)

    print 'Max cool...'
    led_connection.white.max_cool()
    time.sleep(2)

    print 'Max warm...'
    led_connection.white.max_warm()
    time.sleep(2)

    print 'Strobe effect...'
    led_connection.white.effect('strobe')

    print 'Now focusing on the rgbw bulbs...\n'

    print 'Turn on all rgbw lights...'
    led_connection.rgbw.all_on()
    led_connection.rgbw.white()

    print 'Turn off one zone at a time...'
    for i in range(1, 5):
        led_connection.rgbw.zone_off(i)
        time.sleep(1)
    time.sleep(1)

    print 'Turn on one zone at a time...'
    for i in range(1, 5):
        led_connection.rgbw.zone_on(i)
        time.sleep(1)
    time.sleep(1)

    print 'Set brightness for different zones'
    for i in range(1, 5):
        led_connection.rgbw.set_brightness(i*5, i)
        time.sleep(1)
    time.sleep(1)

    print 'Fade lights all the way up...'
    led_connection.rgbw.effect('fade_up')

    print 'Change to lilac...'
    led_connection.rgbw.set_color('lilac')
    time.sleep(1)

    print 'Change to yellow...'
    led_connection.rgbw.set_color('yellow')
    time.sleep(1)

    colors = ['baby_blue', 'mint', 'orange', 'lavendar']
    print 'Set color for different zones'
    for i in range(1, 5):
        led_connection.rgbw.set_color(colors[i-1], i)
        time.sleep(1)
    time.sleep(1)

    print 'Set white one zone at a time'
    for i in range(1, 5):
        led_connection.rgbw.white(i)
        time.sleep(1)
    time.sleep(1)

    print 'Fade lights all the way down...'
    led_connection.rgbw.effect('fade_down')

    print 'Return to full brightness...'
    led_connection.rgbw.effect('fade_up')

    print 'Colorful strobe effect. Can be customized to select only certain colors...'
    led_connection.rgbw.effect('colorful_strobe')

    print 'Wave pattern with the fading of the lights...'
    led_connection.rgbw.effect('fade_up')
    led_connection.rgbw.effect('fade_down')
    led_connection.rgbw.effect('fade_up')
    led_connection.rgbw.effect('fade_down')

    print 'Police flashers effects. Colors can be customized or fully random...'
    led_connection.rgbw.effect('police_flashers')

    print 'Pulsating yellow factory flashers. Colors can be customized or fully random...'
    led_connection.rgbw.effect('pulsating_swells', effect_options={'duration': 15})

    print 'Rainbow fade. Speed of change and difference of change can be customized...'
    led_connection.rgbw.effect('rainbow_fade', effect_options={'delta': 5})

    print 'Strobe effect based on the previously set color...'
    led_connection.rgbw.effect('strobe', effect_options={'duration': 5})

    print 'Turn off all lights...'
    led_connection.rgbw.all_off()
    time.sleep(1)

    print 'Done.'
