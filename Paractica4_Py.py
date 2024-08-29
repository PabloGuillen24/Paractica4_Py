from ast import Delete
from multiprocessing import Value
from os import write
import tkinter as tk
from tkinter import messagebox

def limpar_campos():
    tbNombre.delete(0,tk.END)
    tbApellidos.delete(0,tk.END)
    tbEdad.delete(0,tk.END)
    tbEstatura.delete(0,tk.END)
    tbTelefono.delete(0,tk.END)
    var_genero.set(0)
    
def borrar_fun():
    limpar_campos()

    
def guardar_valores():
    nombres = tbNombre.get()
    apellidos = tbApellidos.get()
    edad = tbEdad.get()
    telefono = tbTelefono.get()
    estatura = tbEstatura.get()
    genero = ""
    if var_genero.get()==1:
        genero = "Hombre"
    elif var_genero.get()==2:
        genero = "Mujer"
    
    datos = "Nombre(s): " + nombres + "\n" + "Apellidos: " + apellidos + "\n" + "Edad: " + edad + "\n" + "Telefono: " + telefono + "\n" + "Estatura: " + estatura + "cm" + "\n" + "Genero: " + genero
    with open ("302024Datos.txt", "a") as archivo:
        archivo.write(datos+"\n\n")
    messagebox.showinfo("Informacion", "Datos guardados con exito: \n\n" + datos)
    tbNombre.Delete(0,tk.END)
    tbApellidos.Delete(0,tk.END)
    tbEdad.Delete(0,tk.END)
    tbEstatura.Delete(0,tk.END)
    tbTelefono.Delete(0,tk.END)
    var_genero.set(0)
        


ventana = tk.Tk()
ventana.geometry("520x500")
ventana.title("Formulario en Python")

var_genero =tk.IntVar()

lblNombre = tk.Label(ventana, text="Nombres: ")
lblNombre.pack()
tbNombre = tk.Entry()
tbNombre.pack()
lblApellidos = tk.Label(ventana, text="Apellidos: ")
lblApellidos.pack()
tbApellidos = tk.Entry()
tbApellidos.pack()
lblEdad = tk.Label(ventana, text="Edad: ")
lblEdad.pack()
tbEdad = tk.Entry()
tbEdad.pack()
lblTelefono = tk.Label(ventana, text="Telefono: ")
lblTelefono.pack()
tbTelefono = tk.Entry()
tbTelefono.pack()
lblEstatura = tk.Label(ventana, text="Estatura: ")
lblEstatura.pack()
tbEstatura = tk.Entry()
tbEstatura.pack()
lblGenero = tk.Label(ventana, text="Genero")
lblGenero.pack() 
rbHombre =tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
rbHombre.pack()
rbMujer =tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
rbMujer.pack()

btnBorrar = tk.Button(ventana, text="Limpiar campos", command=borrar_fun)
btnBorrar.pack()
btnGuardar = tk.Button(ventana, text="Guardar", command=guardar_valores)
btnGuardar.pack()

ventana.mainloop()