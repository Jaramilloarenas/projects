from tkinter import ttk
from tkinter import messagebox
from client_mqtt import *
from tkinter import *
import logic
import threading 

class Window:

    _ICON : str = "ico.ico"
    _RESOLUTION : str = "1000x600+0+0"
    _TOPICS : list = ["verificacion", "prueba", "another"]

    def __init__(self, title : str = "Titulo por defecto") -> None:
        self.window = Tk()
        #self.topic_list = self.get_topics()
        self.datab = logic.DatabaseAdmin()
        self.define_components()
        self.load_components()
        self.set_tab_order()
        messagebox.showinfo("Prueba", "Esta es una aplicación de prueba que hace un monton de procesos inecesarios para mostrar un mensaje")
        self.window.mainloop()
    
    def load_components(self) -> None:
        self.window.iconbitmap(Window._ICON)
        self.window.geometry(Window._RESOLUTION)
        self.window.title("Mensajes HiveMQ")
        self.window.resizable(0, 0)
        #entry
        self.txt1.place(x = 20, y = 50)
        self.txt1.focus()
        self.btnAdd.bind("<Return>", self.addMessage)
        #labels
        self.lbl1.pack()
        self.lbl2.pack()
        self.lbl1.place(x = 20, y = 20)
        self.lbl2.place(x = 500, y = 55)
        #textarea
        self.txtSend.place(x = 20, y = 80)
        self.txtRecei.place(x = 500, y = 80)
        #buttons
        self.btnSend.place(x = 20, y = 500)
        self.btnShow.place(x = 500, y = 500)
        self.btnGet.place(x = 370, y = 500)
        self.btnAdd.place(x = 210, y = 47)
        #combobox
        #self.cmbTopic['values'] = topic_list ["verificacion", "prueba", "another"]
        self.cmbTopic['values'] = ["verificacion", "prueba", "another"]
        self.cmbTopic.place(x = 80, y = 503)

    def define_components(self) -> None:
        self.txt1 = Entry(width = 30, state = NORMAL)
        self.lbl1 = Label(self.window, text = "Mensajes para enviar")
        self.lbl2 = Label(self.window, text = "Mensajes recibidos")
        self.txtSend = Text(self.window, width = 50, height = 25, state = DISABLED)
        self.txtRecei = Text(self.window, width = 50, height = 25, state = NORMAL)
        self.btnSend = Button(text = "Enviar", command = self.send_messages)
        self.btnShow = Button(text = "Mostrar", command = self.show_messages)
        self.btnGet = Button(text = "Descargar", command = self.download)
        self.btnAdd = Button(text = "Agregar", command = self.addMessage)
        self.cmbTopic = ttk.Combobox(self.window, width = 17, state = "readonly")

    def set_tab_order(self) -> None:
        controls = [self.txt1, self.btnAdd, self.btnSend, self.cmbTopic, self.btnGet, self.btnShow]
        for _ in controls:
            _.lift()

    def send_messages(self) -> None:
        try:
            messages = (self.txtSend.get("1.0", END)).split("|")
            print(messages, " ", self.cmbTopic.get())           
            self.datab.send_data(self.cmbTopic.get(), messages)
        except Exception as ex:
            messagebox.showinfo("Error", ex)

    
    def show_messages(self):
        try:
            if(self.datab.estado):
                self.datab.stop_retrieve()
            self.datab.retrieve_messages()
        except Exception as ex:
            messagebox.showinfo("Error", ex)

    def download(self):
        try:
            self.datab.get_data()
        except Exception as ex:
            messagebox.showinfo("Error", ex)

    def addMessage(self, event):
        try:
            self.txtSend.configure(state = NORMAL)
            self.txtSend.insert(END, self.txt1.get() + "|")
            self.txt1.delete(0, "end")
            self.txt1.focus()
            self.txtSend.configure(state = DISABLED)
        except Exception as ex:
            messagebox.showinfo("Error", ex)

       
win = Window("Ventana")

