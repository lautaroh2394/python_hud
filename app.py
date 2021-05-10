#Ejemplo
import threading
import time
from HUD import HUD
from Container import Container
t = threading.Thread(target=HUD.start)
t.start()

while 1:
    #Actualizo la hora cada 0.1 seg    
    t = time.localtime()
    Container.value = f"{t.tm_year}/{t.tm_mon}/{t.tm_mday} - {t.tm_hour}:{t.tm_min}:{t.tm_sec}"
    time.sleep(1)