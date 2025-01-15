from machine import Pin, PWM
import utime

servo = PWM(Pin(0))  # Define el pin GPIO0 como salida PWM
servo.freq(50)  # Configura la frecuencia PWM a 50Hz (estándar para servos)

def set_angle(angle):
    # Mapea el ángulo (0-180) al ciclo de trabajo del PWM (1000-9000)
    duty = int(1000 + (angle/180)*8000)
    servo.duty_u16(duty)

while True:
    set_angle(0)    # Gira el servo a 0 grados
    utime.sleep(1)  # Espera 1 segundo
    set_angle(90)   # Gira el servo a 90 grados
    utime.sleep(1)  # Espera 1 segundo
    set_angle(180)  # Gira el servo a 180 grados
    utime.sleep(1)  # Espera 1 segundo