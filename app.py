#Ejemplo de como usar HUD en otro script
import threading
import time
from HUD import HUD
HUD.thread_start()

while 1:
    #Actualizo la hora cada 0.1 seg    
    t = time.localtime()
    HUD.update_label(f"{t.tm_year}/{t.tm_mon}/{t.tm_mday} - {t.tm_hour}:{t.tm_min}:{t.tm_sec}")
    time.sleep(1)