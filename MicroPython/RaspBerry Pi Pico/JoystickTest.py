from machine import Pin, ADC

potenciometro = ADC(Pin(26))

while True:
  valor = potenciometro.read_u16()
  print(valor)