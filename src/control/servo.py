from machine import Pin, PWM

'''Clase Servo requiere que al menos se defina un pin con capacidad PWM, pensada para controlar servos SG90 y MG90s
Parametros: pin (GPIO), frecuencia del PWM, duty cycle min y max'''
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
        duty = int(self.minfreq + (angle / 180) * (self.maxfreq-self.minfreq))
        self.pwm_obj.duty_u16(duty)
