from tkinter import ttk
from tkinter import *
import sys, os
import webbrowser
from tkinter import messagebox
import subprocess

if hasattr(sys, '_MEIPASS'): 
    os.chdir(sys._MEIPASS) 
new = 1
url = "https://bit.ly/3uPYaoQ"
def ok ():
        messagebox.showinfo(message="Este Programa fue desarrollado para toda la comunidad\n que tiene un Ipod Touch 5 y necesita pasarle musica", title="Informacion")
def openweb():
    webbrowser.open(url,new=new)
def cm():
    #subprocess.run("ideviceactivation activate -s chipcrack.chipcrack.com/chipcrack.php -d", shell=True)
    subprocess.run("ideviceactivation activate -s localhost/chipcrack/chipcrack.php -d", shell=True)
    messagebox.showinfo(message=">>>>>>Dispositivo Activado<<<<< \nrecuerda tener cerrado itunes \nsi aun no esta activado \nvulve a intentar, tenemos mucha demanda en el servidor ", title="Informacion")
class Product:
    
    def __init__(self,windows):
        self.wind = window
        self.wind.title('Server Icloud A5')
        self.wind.eval('tk::PlaceWindow . center')
        self.wind.resizable(0,0)     
        self.wind.iconbitmap("logo.ico")
        self.wind.geometry("320x100")
        #self.wind.config(bg="#cdffbe")
        btn = ttk.Button(self.wind, text='Activar',command=cm).place(x=120,y=10)
        Label(self.wind,text="Luego de Activar el Dispositivo").place(x=75,y=40)  
        Label(self.wind,text="Sincroniza tu Musica con itunes").place(x=72,y=60)
       
if __name__ == '__main__':
    window = Tk()
    
    img = PhotoImage(file='a.png')
    fondo = Label(window, image=img)
    fondo.place(x=1, y=10)
    aplication = Product(window)
    menubar = Menu(window)
    window.config(menu=menubar)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Suscribete",command=openweb)
    helpmenu.add_separator()
    helpmenu.add_command(label="Acerca de...",command=ok)
    helpmenu.add_separator()
    helpmenu.add_command(label="Creado Por Angelo Lopez Torrico")
    helpmenu.add_separator()
    helpmenu.add_command(label="Salir", command=window.quit)
    menubar.add_cascade(label="Ayuda", menu=helpmenu)

    window.mainloop()