import machine
import time
import MPU6050

i2c = machine.I2C(0, sda=machine.Pin(4), scl=machine.Pin(5))
mpu = MPU6050.MPU6050(i2c)

yaw = 0  # Inicializa el ángulo de yaw
tiempo_anterior = time.ticks_ms()  # Tiempo de la medición anterior

while True:
  # Lee los datos del giroscopio
  gyro_data = mpu.read_gyro_data()

  # Calcula el tiempo transcurrido
  tiempo_actual = time.ticks_ms()
  dt = (tiempo_actual - tiempo_anterior) / 1000  # Convierte a segundos

  # Integra la velocidad angular en el eje z (yaw)
  yaw += gyro_data[0] * dt 

  # Actualiza el tiempo anterior
  tiempo_anterior = tiempo_actual

  print("Ángulo de yaw:", yaw)
  time.sleep_ms(10)  # Espera un corto tiempo