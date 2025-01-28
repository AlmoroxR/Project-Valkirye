import machine
import time
import MPU6050
import math
from machine import Pin, PWM

i2c = machine.I2C(0, sda=machine.Pin(4), scl=machine.Pin(5))
mpu = MPU6050.MPU6050(i2c)

# Configura el pin GPIO0 como salida PWM
servoz = PWM(Pin(12, mode=Pin.OUT))
servoz.freq(50)  # Configura la frecuencia a 50Hz (estándar para servos)

servoy = PWM(Pin(15, mode=Pin.OUT))
servoy.freq(50)  # Configura la frecuencia a 50Hz (estándar para servos)


# wake up the MPU6050 from sleep
mpu.wake()

roll = 0
pitch = 0
yaw = 0


yaw = 0  # Inicializa el ángulo de yaw
tiempo_anterior = time.ticks_ms()  # Tiempo de la medición anterior


# Función para mapear el ángulo al rango del servo
def map_angle(angulo):
  return int(angulo * 65535 / 180)  # 65535 es el rango máximo del PWM


while True:
  # Lee los datos del giroscopio
  gyro_data = mpu.read_gyro_data()
  accel_data = mpu.read_accel_data()

  ax = accel_data[0]
  ay = accel_data[1]
  az = accel_data[2]
  
  roll = math.atan(ax / math.sqrt(ay**2 + az**2 + 0.0001)) * (180.0 / math.pi)
  pitch = math.atan(ay / math.sqrt(ax**2 + az**2 + 0.0001)) * (180.0 / math.pi)


  # Calcula el tiempo transcurrido
  tiempo_actual = time.ticks_ms()
  dt = (tiempo_actual - tiempo_anterior) / 1000  # Convierte a segundos

  # Integra la velocidad angular en el eje z (yaw)
  yaw += gyro_data[2] * dt + 0.0125
  # Actualiza el tiempo anterior
  tiempo_anterior = tiempo_actual
  
  angulo_servoz = map_angle(yaw) 
  servoz.duty_u16(angulo_servoz) 
  
  angulo_servoy = map_angle(pitch)
  servoy.duty_u16(angulo_servoy)
  
  print("angulos:", yaw, roll, pitch)
  time.sleep_ms(10)  # Espera un corto tiempo



