from tkinter import *
import threading
import time

class HUD():
    execution_thread = None
    raiz = None
    label_texto = None

    @staticmethod
    def create_widgets():
        HUD.raiz = Tk()
        HUD.raiz.geometry("300x300")
        HUD.raiz.protocol("WM_DELETE_WINDOW", HUD.close_callback)
        
        frame = Frame()
        frame.pack(side="top")
        frame.config(width=300, height=300, bg="red")

        label = Label(frame, text="prueba")
        label.pack()

        HUD.label_texto = StringVar()
        label['textvariable'] = HUD.label_texto
        HUD.label_texto.set("No hay datos")

    @staticmethod
    def thread_start():
        HUD.execution_thread = threading.Thread(target=HUD.start)
        HUD.execution_thread.start()    

    @staticmethod
    def start():
        HUD.create_widgets()
        HUD.raiz.mainloop()

    @staticmethod
    def close():
        #Llamar desde afuera del contexto del hilo
        HUD.raiz.quit()
        HUD.execution_thread.join()

    @staticmethod
    def update_label(texto):
        if HUD.label_texto is not None:
            HUD.label_texto.set(texto)
    
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
        HUD.update_label(f"{t.tm_year}/{t.tm_mon}/{t.tm_mday} - {t.tm_hour}:{t.tm_min}:{t.tm_sec}")

    HUD.close()
    print("Fin")
