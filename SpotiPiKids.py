#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The main file, setup GPIO, set spotify device, start qr reader
"""

if __name__ == "__main__":
    import sys
    import gpio_btns
    import qr_reader
    from spotify_if import set_default_device
    set_default_device()
    gpio_btns.init_gpio_buttons()
    show_window = False
    if "show_window" in sys.argv[1:]:
        show_window = True
    qr_reader.qr_detect_loop(2, show_window)
    