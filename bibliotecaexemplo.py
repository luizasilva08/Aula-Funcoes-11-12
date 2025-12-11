'''traz um número aleatorio, usuario entra com um numero de numeros vendidos'''

n = []
sit = 's'
import random
import time
from datetime import datetime

print("Sistema iniciando...")
time.sleep(3)

ns = int(input('Insira quantos números foram vendidos: '))

while(sit=='s'):
    numero = random.randint(1,ns)
    agora = datetime.now()

    n.append(numero)

    print("Número gerado: ",numero)
    print("Horário: ", agora)
    sit = input("Você quer continuar? (s/n): ")
    
print(n)
time.sleep(2)
print('Sistema finalizado.')