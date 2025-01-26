import machine
import time
import MPU6050
from machine import Pin, PWM

i2c = machine.I2C(0, sda=machine.Pin(4), scl=machine.Pin(5))
mpu = MPU6050.MPU6050(i2c)

# Configura el pin GPIO0 como salida PWM
servo = PWM(Pin(12, mode=Pin.OUT))
servo.freq(50)  # Configura la frecuencia a 50Hz (estándar para servos)

yaw = 0  # Inicializa el ángulo de yaw
tiempo_anterior = time.ticks_ms()  # Tiempo de la medición anterior


# Función para mapear el ángulo al rango del servo
def map_angle(angulo):
  return int(angulo * 65535 / 180)  # 65535 es el rango máximo del PWM


while True:
  # Lee los datos del giroscopio
  gyro_data = mpu.read_gyro_data()

  # Calcula el tiempo transcurrido
  tiempo_actual = time.ticks_ms()
  dt = (tiempo_actual - tiempo_anterior) / 1000  # Convierte a segundos

  # Integra la velocidad angular en el eje z (yaw)
  yaw += gyro_data[0] * dt -0.025

  # Actualiza el tiempo anterior
  tiempo_anterior = tiempo_actual
  
  angulo_servo = map_angle(yaw) 
  servo.duty_u16(angulo_servo) 



  print("Ángulo de yaw:", yaw)
  time.sleep_ms(10)  # Espera un corto tiempo



