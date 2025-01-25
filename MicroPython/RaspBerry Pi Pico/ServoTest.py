from machine import Pin, PWM
import time

# Configura el pin GPIO0 como salida PWM
servo = PWM(Pin(12, mode=Pin.OUT))
servo.freq(50)  # Configura la frecuencia a 50Hz (estándar para servos)

while True:
    servo.duty_ns(600000)  # 2ms
    print("90")
    time.sleep_ms(500)
    servo.duty_ns(1500000)  # 1.5ms
    print("180")
    time.sleep_ms(500)
    servo.duty_ns(2400000)  # 1ms
    print("90")
    time.sleep_ms(500)
    servo.duty_ns(1500000)  # 1.5ms
    print("270")
    time.sleep_ms(500)
