import badger2040
from badger2040 import WIDTH

import uasyncio as asyncio
import aioble
import bluetooth

TEXT_SIZE = 1

display = badger2040.Badger2040()
display.led(128)
display.set_update_speed(badger2040.UPDATE_NORMAL)
display.set_thickness(2)

display.set_font("serif")
display.text("Hello World", 5, 1, WIDTH, TEXT_SIZE)


# Scan for 5 seconds, in active mode, with very low interval/window (to
# maximise detection rate).
# def scan():
#     async with aioble.scan(5000, interval_us=30000, window_us=30000, active=True) as scanner:
#         async for result in scanner:
#             print 

while True:
    display.keepalive()
    display.halt()
