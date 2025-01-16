# Programa para mover un servomotor 180° 
'''Se realiza la conexión del servomotor a la tarjeta, a una alimentación de 
5 voltios cable rojo, tierra cable negro y la señal del potenciometro PWM al pin 21'''

'''La primera linea Importa la señal del pin de la 
tarjeta ESP 32 y la señal del PWM 
que realiza el movimiento del servo, la segunda linea 
importa el tiempo en milisegundos que se mueve el servo'''

#Modulos
from machine import Pin, PWM
from utime import sleep, sleep_ms

'''Declaro el sensor, indicando que se encuentra en el
pin 18 de la tarjeta ESP32 y funciona a una frecuencia de 50Hz que equivalen
a 20ms de acuerdo con el fabricante'''

#Objeto
servo=PWM (Pin(15), freq=50)

'''Ciclo mientras afirmativo, realiza la operación de que mientras
el servo transcurre en el ciclo 1 genere un recorrido de acuerdo con la
resolución en un rango de 1800 a 8000'''
''' El servo realiza un recorrido en el ciclo de trabajo en un tiempo de 1 ms '''
while True:
     for i in range(1800, 8000):
        print(i)
        servo.duty_u16(i)
        sleep_ms(1)

'''Cierre de la programación'''