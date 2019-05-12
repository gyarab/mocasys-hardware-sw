import busio
from digitalio import DigitalInOut
from adafruit_pn532.i2c import PN532_I2C

i2c = busio.I2C(board.SCL, board.SDA)

reset_pin = DigitalInOut(board.D6)
req_pin = DigitalInOut(board.D12)
pn532 = PN532_I2C(i2c, debug=False, reset=reset_pin, req=req_pin)

ic, ver, rev, support = pn532.get_firmware_version()

pn532.SAM_configuration()

print('Waiting for card')
while True:
    # card check
    uid = pn532.read_passive_target(timeout=0.5)
    if uid is None:
        continue
    card_auth(uid)
