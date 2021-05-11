from tkinter import *
import threading
import time

class HUD():
    execution_thread = None
    raiz = None
    label_texto = None
    text_widget = None

    @staticmethod
    def create_widgets(opts={}):
        #Opts es un dict con una key por cada elemento del hud, cada key es un booleano. Tiene que estar específicamente en True para mostrar dicho elemento

        HUD.raiz = Tk()
        HUD.raiz.title("Python HUD para Nico")
        HUD.raiz.geometry("300x300")
        HUD.raiz.protocol("WM_DELETE_WINDOW", HUD.close_callback)
        #HUD.raiz.protocol("WM_DELETE_WINDOW", HUD.raiz.quit)
        
        frame = Frame()
        frame.pack(side="top")
        frame.config(width=300, height=300, bg="red")

        if "label" in opts and opts["label"]:
            label = Label(frame, text="prueba")
            label.pack()

            HUD.label_texto = StringVar()
            label['textvariable'] = HUD.label_texto
            HUD.label_texto.set("No hay datos")
        
        if "text" in opts and opts["text"]:
            HUD.text_widget = Text(frame, width = 40, height = 300)
            HUD.text_widget.pack()
            HUD.text_widget['state'] = 'normal'
            HUD.text_widget.delete(0.0, HUD.text_widget.index('end'))
            HUD.text_widget.insert('0.0',"No hay datos")
            HUD.text_widget['state'] = 'disabled'

    @staticmethod
    def thread_start(opts = {"text": True}):
        HUD.execution_thread = threading.Thread(target=HUD.start,args=[opts])
        HUD.execution_thread.start()    

    @staticmethod
    def start(opts):
        HUD.create_widgets(opts)
        HUD.raiz.mainloop()

    @staticmethod
    def close():
        #Llamar desde afuera del contexto del hilo
        HUD.raiz.quit()
        HUD.execution_thread.join()

    @staticmethod
    def update_label(texto):
        if HUD.exists(HUD.label_texto):
            if type(texto) is str:
                HUD.label_texto.set(texto)
                return
            if type(texto) is dict:
                t = "\n".join([f"{key}: {texto[key]}" for key in texto.keys()])
                HUD.label_texto.set(t)
    
    @staticmethod
    def update_text(texto):
        if HUD.exists(HUD.text_widget):
            #Borro lo anterior
            HUD.text_widget['state'] = 'normal'
            HUD.text_widget.delete(0.0, HUD.text_widget.index('end'))
            
            if type(texto) is str:
                HUD.text_widget.insert("0.0", texto)
                return
            if type(texto) is dict:
                #TODO: Aceptar dicts con arrays y subdicts
                indice = 0
                keys = [key for key in texto.keys() if "_color" not in key]
                for key in keys:
                    color_key = f"{key}_color"
                    linea = f"{key}: {texto[key]}\n"
                    prox_indice = indice + linea.count("\n")
                    HUD.text_widget.insert('end',linea)
                    if color_key in texto:
                        HUD.text_widget.tag_add(color_key, f"{indice+1}.0", f"{prox_indice + 1}.0")
                        HUD.text_widget.tag_configure(color_key, background=texto[color_key], font='TkFixedFont', relief='raised')
                    indice = prox_indice

            HUD.text_widget['state'] = 'disabled'

    @staticmethod
    def exists(elem):
        return elem is not None and HUD.execution_thread.is_alive()

    @staticmethod
    def close_callback():
        print("close callback")
        HUD.raiz.quit()

if __name__ == "__main__":
    HUD.thread_start()
    #Prueba
    for i in range(3):
        time.sleep(1)
        t = time.localtime()
        HUD.update_label(f"{t.tm_year}/{t.tm_mon}/{t.tm_mday} \n {t.tm_hour}:{t.tm_min}:{t.tm_sec}")

    HUD.close()
    print("Fin")
