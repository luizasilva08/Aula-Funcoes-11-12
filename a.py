import random
import time
from datetime import datetime

print("Sistema iniciando...")
time.sleep(2)

numero=random.randint(1, 100)
agora=datetime.now()

print("Número gerado:", numero)
print("Horário:",agora)