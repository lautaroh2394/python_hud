# Simple HUD 
Sencillo HUD que muestra un único componente al cual se le puede actualizar el texto. 
\
Hecho con Python y Tkinter. En desarrollo
\
\
Para ver un ejemplo sencillo ejecutar en consola: `py app.py`
\
Se mostrará una ventana donde se actualizará a cada segundo el texto con la hora.
\
\
![](https://raw.githubusercontent.com/lautaroh2394/python_hud/master/assets/hud.png)

## HUD con Flask
Para poder ejecutar remotamente tareas pero de igual manera visualizar localmente el HUD desarrollé un simple servidor Flask. El programa que ejecute tareas remotamente puede tirar peticiones a este servidor para actualizar su estado e impactar en el HUD. La aplicación Flask se ejecuta en el puerto 5000 y escucha peticiones de la red local
\
\
Para este servidor existe el endpoint `/update_text` (GET)
\
Para actualizar el HUD vía este enpoint se debe hacer un GET con el siguiente formato:
\
`[ip:puerto]/update_text/<type>/<texto>`
\
ip: Si se está ejecutando el server en la misma pc, puede usarse localhost, 127.0.0.1, etc. Si el servidor está en otra máquina dentro de la misma red usar la ip privada de esa máquina
\
puerto: 5000
\
type: json, text
\
\
Ejemplo:
\
`127.0.0.1:5000/update_text/text/hola`
\
`127.0.0.1:5000/update_text/json/{"mensaje":"esto es un ejemplo","mensaje_color":"yellow","mensaje2":"segundo ejemplo"}`
\
\
Para levantar servidor:
```
#Solo la primera vez. Creamos virtual env e instalamos los requerimientos
cd .../py hud/
python -m venv venv
./venv/Scripts/activate
pip install -r ./requirements.txt

#La propia ejecución del server:
cd .../py hud/server
flask run --host=0.0.0.0 #O sino también: py app.py
```
\
Se puede ejecutar el script /server/cliente_test.py para ver un ejemplo de como se llamaría programáticamente a esta aplicación Flask

```
cd .../py hud/server
py cliente_test.py
```