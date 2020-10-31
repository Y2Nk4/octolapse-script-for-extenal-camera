try:
    import RPi.GPIO as GPIO
    import time

    focus_pin = 27
    trigger_pin = 17

    # For Sony A73, it takes at least 1.2s
    # to activate from sleep mode

    # activate_wait_sec = 1.2

    # If the camera is charging,
    # the camera won't sleep and
    # there is no need to activate
    
    activate_wait_sec = 0

    # Focus
    activate_wait_p2_sec = 0.2
    focus_wait_sec = 0.5
    trigger_wait_sec = 0.25

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(focus_pin, GPIO.OUT)
    GPIO.setup(trigger_pin, GPIO.OUT)

    GPIO.output(focus_pin, GPIO.HIGH)

    # To activate the camera by focusing
    GPIO.output(focus_pin, GPIO.LOW)
    time.sleep(activate_wait_sec)
    GPIO.output(focus_pin, GPIO.HIGH)
    time.sleep(activate_wait_p2_sec)

    # To focus
    GPIO.output(focus_pin, GPIO.LOW)
    time.sleep(focus_wait_sec)

    # trigger the shutter
    GPIO.output(trigger_pin, GPIO.LOW)

    time.sleep(trigger_wait_sec)

    # reset all pins
    GPIO.output(trigger_pin, GPIO.HIGH)
    GPIO.output(focus_pin, GPIO.HIGH)
    GPIO.cleanup()

except RuntimeError as e:
    print(e)
    print(
        "Error importing RPi.GPIO!  This is probably because you need superuser privileges.  "
        "You can achieve this by using 'sudo' to run your script")