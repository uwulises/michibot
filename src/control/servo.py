from machine import Pin, PWM


class Servo:
    def __init__(self, pin: int, freq=50, min=2500, max=8000):
        gpio = Pin(pin, Pin.OUT)
        self.pwm_obj = PWM(gpio)
        self.pwm_obj.freq(freq)
        self.minfreq = min
        self.maxfreq = max

    def deinit(self):
        self.pwm_obj.deinit()

    def set_angle(self, angle: int):
        # map the angle (0-180) to a duty cycle
        duty = int(2500 + (angle / 180) * (self.maxfreq-self.minfreq))
        self.pwm_obj.duty_u16(duty)
