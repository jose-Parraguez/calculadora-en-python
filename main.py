from tkinter import *


ventana = Tk()
ventana.title("calculadora")
#tamaño de la ventana
ventana.resizable(0,0)

#el i es para que en la calculadora no se anote al reves
i = 0
#------------------------------------------------------------------------------
#entrada

e_texto = Entry(ventana, font= ("Calibri 20"))
e_texto.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady = 5)
#columnspan sirve para ver cuantas columnas quierer usar el boton


#------------------------------------------------------------------------------



#botones
#numeros del 1 al 10
#el width es el ancho del boton y el heigth el largo

boton1 = Button(ventana, text = "1", width = 5, height = 2, command = lambda: click_boton(1))
boton2 = Button(ventana, text = "2", width = 5, height = 2, command = lambda: click_boton(2))
boton3 = Button(ventana, text = "3", width = 5, height = 2, command = lambda: click_boton(3))
boton4 = Button(ventana, text = "4", width = 5, height = 2, command = lambda: click_boton(4))
boton5 = Button(ventana, text = "5", width = 5, height = 2, command = lambda: click_boton(5))
boton6 = Button(ventana, text = "6", width = 5, height = 2, command = lambda: click_boton(6))
boton7 = Button(ventana, text = "7", width = 5, height = 2, command = lambda: click_boton(7))
boton8 = Button(ventana, text = "8", width = 5, height = 2, command = lambda: click_boton(8))
boton9 = Button(ventana, text = "9", width = 5, height = 2, command = lambda: click_boton(9))
boton0 = Button(ventana, text = "0", width = 5, height = 2, command = lambda: click_boton(0))



boton_borrar = Button(ventana, text = "Borrar", width = 5, height = 2, command = lambda: borrar())
boton_sumar = Button(ventana, text = "+", width = 5, height = 2, command = lambda: click_boton("+"))
boton_restar = Button(ventana, text = "-", width = 5, height = 2, command = lambda: click_boton("-"))
boton_multiplicar = Button(ventana, text = "x", width = 5, height = 2, command = lambda: click_boton("*"))
boton_dividir = Button(ventana, text = "/", width = 5, height = 2, command = lambda: click_boton("/"))
boton_parentesis1= Button(ventana, text = "(", width = 5, height = 2, command = lambda: click_boton("("))
boton_parentesis2 = Button(ventana, text = ")", width = 5, height = 2, command = lambda: click_boton(")"))
boton_punto = Button(ventana, text = ",", width = 5, height = 2, command = lambda: click_boton(","))
boton_igual = Button(ventana, text = "=", width = 5, height = 2, command = lambda: hacer_operacion())
boton_elevado = Button(ventana, text = "^", width = 5, height = 2, command = lambda: click_boton("**"))
boton_undo = Button(ventana, text = "<--", width = 5, height = 2, command = lambda: undo())

#--------------------------------------------------------------------
boton_formulas = Button(ventana, text = "Formulas", width = 25, height = 2, command = lambda: abrir_formulas ())
#--------------------------------------------------------------------


#botones en pantalla
#row es la fila hacia el lado
#colum es la posicion hacia abajo
boton_borrar.grid(row = 5, column = 1, padx = 5, pady = 5)
boton_sumar.grid(row = 1, column = 3, padx = 5, pady = 5)
boton_restar.grid(row = 1, column = 4, padx = 5, pady = 5)
boton_multiplicar.grid(row = 2, column = 4, padx = 5, pady = 5)
boton_dividir.grid(row = 3, column = 4, padx = 5, pady = 5)
boton_parentesis1.grid(row = 1, column = 1, padx = 5, pady = 5)
boton_parentesis2.grid(row = 1, column = 2,  padx = 5, pady = 5)
boton_punto.grid (row = 4, column = 4,  padx = 5, pady = 5)
boton_igual.grid (row = 5, column = 4, padx = 5, pady = 5)
boton_elevado.grid(row = 5, column = 3, padx = 5, pady = 5)
boton_undo.grid(row = 6, column = 4, padx = 5, pady = 5)
#--------------------------------------------------------------------
boton_formulas.grid(row = 6, column = 1, columnspan = 3, padx = 5, pady = 5)
#--------------------------------------------------------------------

#botones numericos
boton1.grid(row = 4, column = 1, padx = 5, pady = 5)
boton2.grid(row = 4, column = 2, padx = 5, pady = 5)
boton3.grid(row = 4, column = 3, padx = 5, pady = 5)
boton4.grid(row = 3, column = 1, padx = 5, pady = 5)
boton5.grid(row = 3, column = 2, padx = 5, pady = 5)
boton6.grid(row = 3, column = 3, padx = 5, pady = 5)
boton7.grid(row = 2, column = 1, padx = 5, pady = 5)
boton8.grid(row = 2, column = 2, padx = 5, pady = 5)
boton9.grid(row = 2, column = 3, padx = 5, pady = 5)
boton0.grid(row = 5, column = 2, padx = 5, pady = 5)
#--------------------------------------------------------------------

#funciones para agrrgar en pantalla los numeros

def click_boton (valor):
    global i
    e_texto.insert(i, valor)
    i += 1



#--------------------------------------------------------------------
#funcion para borrar
def borrar ():
    e_texto.delete(0, END)
    i=0

#--------------------------------------------------------------------


#funcion operacion obtiene el texto de la pantalla y con eval, resuelve la
#ecuacion despues borra lo de la pantalla  para poner el resultado
def hacer_operacion():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0,END)
    e_texto.insert(0,resultado)
    i = 0
#--------------------------------------------------------------------

#funcion para borrar solo un numero
#obtengo los string de la pantalla y los convierto en uno nuevo , le descuento solo 1 para que solo borre 1
#y finalmente los ingreso denuevo a la pantalla    
def undo():
    e_texto_etado =e_texto.get()
    if len (e_texto_etado):
        e_texto_new_state = e_texto_etado[:-1]
        borrar()
        e_texto.insert(0,e_texto_new_state )
    else:
        borrar()

#--------------------------------------------------------------------
#funcion para abrir las formulas
##def abrir_formulas ():
##    ventana_de_formulas = Tk()
##    ventana_de_formulas.title("Fomulas")
##    ventana_de_formulas.geometry("450x500")
##    texto = Entry(ventana_de_formulas, font= ("Calibri 20"))
##    texto.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady = 5)
##    texto.place(height =400)
##    archivo= open("formulas.txt")
##    archivo .read ()
##    ventana_de_formulas.mainloop()
#--------------------------------------------------------------------



#ciclo para que se pueda abrir la ventana
    ventana.mainloop()