"""
This example should be used with a 90 degree (range of rotation) servo
on channel 0 of the Pi Servo Hat.

The extended code (commented out), at the end of the example could be
used to test the full range of the servo motion. However, users should
be wary as they can damage their servo by giving it a position outside
the standard range of motion.
"""

from pi_servo_hat import PiServoHat
import time

# Initialize Constructor
test = PiServoHat()

# Restart Servo Hat (in case Hat is frozen/locked)
test.restart()

# Test Run
#########################################
# Moves servo position to 0 degrees (1ms), Channel 0
test.move_servo_position(0, 0)

# Pause 1 sec
time.sleep (1)

# Moves servo position to 90 degrees (2ms), Channel 0
test.move_servo_position(0, 90)

# Sweep
#########################################
while True:
    for i in range(0, 90):
        print(i)
        test.move_servo_position(0, i)
        time.sleep(.001)
    for i in range(90, 0, -1):
        print(i)
        test.move_servo_position(0, i)
        time.sleep(.001)

#########################################
# Code below may damage servo, use with caution
# Test sweep for full range of servo (outside 0 to 180 degrees).
# while True:
#     for i in range(-23, 100):
#         print(i)
#         test.move_servo_position(0, i)
#         time.sleep(.001)
#     for i in range(100, -23, -1):
#         print(i)
#         test.move_servo_position(0, i)
#         time.sleep(.001)
