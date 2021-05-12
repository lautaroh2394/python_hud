import requests as r
import json
import time

config_file = "config.json"
ip = None
puerto = None

with open(config_file) as f:
     config = f.read()
     config_loaded = json.loads(config)
     ip = config_loaded["ip"]
     puerto = config_loaded["puerto"]

while 1:
     t = time.localtime()
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
     
     url = f"{ip}:{puerto}/update_text/json/{json.dumps(time_formated)}"
     print(url)
     r.get(f"http://{ip}:{puerto}/update_text/json/{json.dumps(time_formated)}")
     time.sleep(1)