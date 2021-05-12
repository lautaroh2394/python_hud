from flask import Flask
import json
import sys
sys.path.insert(0, '..')
from HUD import HUD

HUD.thread_start()
app = Flask(__name__)

@app.route("/update_text/<type>/<texto>")
def update_text(texto, type="json"):
    if type == "json":
        try:
            json_para_actualizar = json.loads(texto)
            HUD.update_text(json_para_actualizar)
            return 'ok. texto actualizado con json'
        except:
            return f'Hubo un error. Revisá que en la url estés usando comillas dobles (") en vez de simples (\'): {sys.exc_info()[0]}'
        
    if type == "text":
        HUD.update_text(texto)
        return 'ok. texto actualizado'
        
    return 'type no válido'

if __name__ == "__main__":    
    #app.run(host="0.0.0.0")
    app.run(host="0.0.0.0")