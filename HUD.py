from tkinter import *
import threading
from Container import Container
import time

class HUD():
    instance = None
    execution_thread = None
    raiz = None
    label_texto = None

    @staticmethod
    def create_widgets():
        HUD.raiz = Tk()
        HUD.raiz.geometry("300x300")
        
        frame = Frame()
        frame.pack(side="top")
        frame.config(width=300, height=300, bg="red")

        label = Label(frame, text="prueba")
        label.pack()

        HUD.label_texto = StringVar()
        print(HUD.label_texto)
        label['textvariable'] = HUD.label_texto
        HUD.label_texto.set("No hay datos")

    @staticmethod
    def task():
        print("task")
        HUD.raiz.after(100, HUD.task)  #Actualiza label en 0.1 seg
        if Container.value is not None:
            print("task - Container.value : " + Container.value)
            HUD.update_label(Container.value)

    @staticmethod
    def start():
        HUD.create_widgets()
        #HUD.execution_thread = threading.Thread(target=HUD.raiz.mainloop)
        #HUD.execution_thread.start()    

        HUD.raiz.after(200, HUD.task)
        HUD.raiz.mainloop()

    @staticmethod
    def stop():
        HUD.execution_thread.stop()

    @staticmethod
    def update_label(texto):
        if HUD.label_texto is not None:
            HUD.label_texto.set(texto)



if __name__ == "__main__":
    t = threading.Thread(target=HUD.start)
    t.start()

    for i in range(10000):
        time.sleep(1)
        Container.value = str(i)
        print("main - Container.value: " + Container.value)
