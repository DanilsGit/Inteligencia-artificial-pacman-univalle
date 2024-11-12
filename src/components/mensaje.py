import tkinter as tk

def mostrar_mensaje(mensaje):
    # Crear una nueva ventana principal (Toplevel)
    ventana = tk.Tk()
    ventana.title("¡El juego ha terminado!")

    # para el Tamaño de la ventana
    ancho_ventana = 400
    alto_ventana = 150
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}")
    ventana.resizable(False, False)

    #centrar la pantalla
    pantalla_ancho = ventana.winfo_screenwidth()  # Ancho de la pantalla
    pantalla_alto = ventana.winfo_screenheight()  # Alto de la pantalla
    posicion_x = (pantalla_ancho - ancho_ventana) // 2  # X centrado
    posicion_y = (pantalla_alto - alto_ventana) // 2  # Y centrado
    ventana.geometry(f"+{posicion_x}+{posicion_y}")  # Establecer la posición


    # Cambiar el color de fondo de la ventana
    ventana.config(bg="#F4F4F9")

    # Etiqueta con el mensaje
    etiqueta = tk.Label(ventana, text=mensaje, font=("Poppins", 16), fg="#333333", bg="#F4F4F9" ,padx=20, pady=20)
    etiqueta.pack(pady=10)

    # Botón de cerrar
    boton_cerrar = tk.Button(ventana, text="Cerrar", font=("Baton", 12), fg="white", bg="#007BFF", command=ventana.destroy)
    boton_cerrar.pack(pady=10, ipadx=10, ipady=5)

    # Establecer apariencia del botón
    boton_cerrar.config(borderwidth=0, relief="flat", highlightthickness=0)
    boton_cerrar.config(activebackground="#0056b3")


    # Iniciar el bucle de eventos de tkinter
    ventana.mainloop()














    # messagebox.showinfo("Mensaje", mensaje)

    # # # Crear una nueva ventana principal
    # # ventana = tk.Tk()
    # # # Iniciar el bucle de eventos de tkinter
    # # ventana.mainloop()


