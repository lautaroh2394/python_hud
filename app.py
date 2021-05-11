#Ejemplo de como usar HUD en otro script
import time
from HUD import HUD
HUD.thread_start()

def run_app():
    while HUD.execution_thread.is_alive():
        #Actualizo la hora cada 0.1 seg    
        t = time.localtime()
        #time_formated = f"{t.tm_year}/{t.tm_mon}/{t.tm_mday} - {t.tm_hour}:{t.tm_min}:{t.tm_sec}"
        time_formated = {
            "año": t.tm_year,
            "mes": t.tm_mon,
            "dia": t.tm_mday,
            "hora": t.tm_hour,
            "min": t.tm_min,
            "sec": t.tm_sec
        }
        print(time_formated)
        HUD.update_label(time_formated)

        #Actualizo el texto:
        #Para darle color a una linea debo agregar la key f"{key_origina}_color"
        time_formated = {
            "año": t.tm_year,
            "mes": t.tm_mon,
            "dia": t.tm_mday,
            "hora": t.tm_hour,
            "min": t.tm_min,
            "sec": t.tm_sec,
            "año_color": "green",
            "mes_color": "blue",
            "dia_color": "yellow",
            "hora_color": "red"
        }
        HUD.update_text(time_formated)
        time.sleep(1)

if __name__ == "__main__":
    run_app()