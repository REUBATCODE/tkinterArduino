from tkinter import Tk, Label, Button, PhotoImage, Frame
from datetime import datetime
import tkinter as tk
import serial

def derecha():
    print("Derecha")
    estado_motor.config(text="Current StateL: Turning right")
    boton_paro.config(state="normal")
    boton_derecha.config(state="disabled")
    boton_izquierda.config(state="normal")
    try:
        arduino.write(b's')
        arduino.write(b'd')
    except:
        print('No se pudo abrir el puerto serial')

def izquierda():
    print("Izquierda")
    estado_motor.config(text="Current State: Turning left")
    boton_paro.config(state="normal")
    boton_derecha.config(state="normal")
    boton_izquierda.config(state="disabled")
    try:
        arduino.write(b's')
        arduino.write(b'i')
    except:
        print('Could not open serial port.')

def paro():
    print("Stop")
    estado_motor.config(text="Current State: Stopped")
    boton_paro.config(state="disabled")
    boton_derecha.config(state="normal")
    boton_izquierda.config(state="normal")
    try:
        arduino.write(b's')
    except:
        print('Could not open serial port.')

def update_time():
    current_time = datetime.now().strftime('%d/%m %H:%M:%S')
    timer.config(text=current_time)
    ventana.after(1000, update_time)

#Arduino connection
try:
    arduino = serial.Serial('/dev/cu.usbserial-1130', 9600)
except:
    print('Could not connect to Arduino.')

ventana = Tk()
ventana.title('Motor Control System - GUI')
ventana['bg'] = 'white'
ventana.geometry("800x600") #Window dimensions

frame_superior = Frame(ventana, bg='white')
frame_superior.pack(fill='x')

nombre_proyecto = Label(frame_superior, text="Motor Control System", bg='white', fg='black', font=("Arial Bold", 24))
nombre_proyecto.pack(pady=10)

etiqueta = Label(frame_superior, text="Developed by Ruben Vega", bg="white", fg='black', font=("Arial", 28))
etiqueta.pack()

frame_inferior = Frame(ventana, bg='white')
frame_inferior.pack(fill='both', expand=True)

estado_motor = Label(frame_inferior, text="Current State: Stopped", bg="white", fg='black', font=("Arial", 36))
estado_motor.pack(pady=20)

timer = Label(ventana, text="", font=("Arial Bold", 20), bg="white", fg='black')
timer.pack(side='bottom', pady=10)

update_time()

#Images
fondo = PhotoImage(file="./img/fondo.png")
img_derecha = PhotoImage(file="./img/derecha.png")
img_izq = PhotoImage(file="./img/izquierda.png")
img_paro = PhotoImage(file="./img/paro.png")

#Buttons
boton_derecha = Button(ventana, image=img_derecha, command=derecha)
boton_derecha.pack(side='right', padx=10, pady=50)

boton_izquierda = Button(ventana, image=img_izq, command=izquierda)
boton_izquierda.pack(side='left', padx=10, pady=50)

boton_paro = Button(ventana, image=img_paro, state="disabled", command=paro)
boton_paro.pack(side='bottom', pady=20)

ventana.mainloop()

#End of the program
try:
    arduino.close()
except:
    print('No se pudo cerrar la conexión con Arduino')
