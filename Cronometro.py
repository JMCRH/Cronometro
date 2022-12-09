from tkinter import *
from tkinter import Canvas, Button, Frame, Label,Tk


#Creacion de la ventana y ajuste de tamaño
ventana  = Tk()
ventana.config(bg = 'black')
ventana.geometry('500x250')
ventana.title('Cronómetro - Teoría de Autómatas')
ventana.minsize(width = 500, height = 250)

#Configuración de columnas y filas
ventana.columnconfigure(0,weight = 2)
ventana.rowconfigure(0,weight = 2)
ventana.columnconfigure(1,weight = 2)
ventana.rowconfigure(0,weight = 2)
ventana.columnconfigure(2,weight = 2)
ventana.rowconfigure(0,weight = 2)
ventana.columnconfigure(1,weight = 2)
ventana.rowconfigure(1,weight = 1)
ventana.columnconfigure(1,weight = 2)
ventana.rowconfigure(1,weight = 1)

#Creación de frames o cuadros para colocar la información
frame1 = Frame(ventana)
frame1.grid(column = 0, row = 0, sticky = 'snew')
frame2 = Frame(ventana)
frame2.grid(column = 1, row = 0, sticky = 'snew')
frame3 = Frame(ventana)
frame3.grid(column = 2, row = 0, sticky = 'snew')
frame4 = Frame(ventana, bg = 'gray10')
frame4.grid(row = 1, columnspan = 3, sticky = 'snew')
frame5 = Frame(ventana, bg = 'black')
frame5.grid(row = 2, columnspan = 3, sticky = 'snew')


#Configuración de los frames para ser dinámicos
frame1.columnconfigure(0, weight = 1)
frame1.rowconfigure(0, weight = 1)
frame2.columnconfigure(0, weight = 1)
frame2.rowconfigure(0, weight = 1)
frame3.columnconfigure(0, weight = 1)
frame3.rowconfigure(0, weight = 1)
frame4.columnconfigure(0, weight = 1)
frame4.rowconfigure(0, weight = 1)
frame5.columnconfigure(0, weight = 1)
frame5.rowconfigure(0, weight = 1)

#Creación de canvas para cargar formas y texto
canvas1 = Canvas(frame1, bg = 'gray40', width = 200, height = 200, relief = 'ridge')
canvas1.grid(column = 0, row = 0, sticky = 'snew')
canvas2 = Canvas(frame2, bg = 'gray30', width = 200, height = 200, relief = 'ridge')
canvas2.grid(column = 0, row = 0, sticky = 'snew')
canvas3 = Canvas(frame3, bg = 'gray20', width = 200, height = 200, relief = 'ridge')
canvas3.grid(column = 0, row = 0, sticky = 'snew')

#Formato del texto en los canvas
texto1 = canvas1.create_text(1,1, text = 0, font = ('Arial', 12, 'bold'), fill = 'white')
texto2 = canvas2.create_text(1,1, text = 0, font = ('Arial', 12, 'bold'), fill = 'white')
texto3 = canvas3.create_text(1,1, text = 0, font = ('Arial', 12, 'bold'), fill = 'white')

#Textos indicadores del tiempo mostrado
texto_minutos = canvas1.create_text(1,1, text = 'Minutos', font = ('Arial', 12, 'bold'), fill = 'white')
texto_segundos = canvas2.create_text(1,1, text = 'Segundos', font = ('Arial', 12, 'bold'), fill = 'white')
texto_milisegundos = canvas3.create_text(1,1, text = 'Milisegundos', font = ('Arial', 10, 'bold'), fill = 'white')
#circulos para cada intervalo de tiempo
circulo1 = canvas1.create_oval(10,10,100,100, outline = 'red2', width = 10)
circulo2 = canvas2.create_oval(10,10,100,100, outline = 'medium spring green', width = 10)
circulo3 = canvas3.create_oval(10,10,100,100, outline = 'magenta2', width = 10)

mi = 0
se = 0
ml = 0
contar = 0
click_stop = 0
click_inicio = 0


#Método del botón de inicio que controla el inicio/pausa del cronómetro
def iniciar_pausar():
	global mi, se, ml, click_stop, click_inicio, contar
	ml = ml + 1
	if ml == 999:
		ml = 0
		se = se + 1
		if se == 59:
			se = 0
			mi = mi + 1
	
	contar = inicio.after(1,iniciar_pausar)		

	click_inicio = inicio.grid_forget()
	if click_inicio is None:
		stop.grid(column = 0, row = 0, padx = 10, pady = 10, sticky = 'snew')
		stop.config(bg = 'orange', text = 'DETENER')

def stop_boton():
	global  contar, clik_stop
	clik_stop = stop.grid_forget()
	if  clik_stop  is  None :
		inicio.grid(column=0, row=0, padx =10, pady=10, sticky='nsew')
		inicio.config(bg= 'aqua', text='CONTINUAR')		
		inicio.after_cancel(contar)

def reiniciar():
	global mi, se, ml, contar
	mi = 0
	se = 0
	ml = 0
	inicio.after_cancel(contar)
	stop.grid_forget()	
	inicio.grid(column=0, row=0, padx =10, pady=10, sticky='nsew')
	inicio.config(bg= 'green2', text='INICIAR')


def coordenadas():
	x = canvas1.winfo_width()
	y = canvas1.winfo_height()

	x1 = int(x - 0.1*x - 0.1*y + 25)
	y1 = int(x - 0.1*x - 0.1*y + 20)
	x2 = int(x - 0.4*x - 0.4*y - 15)
	y2 = int(x - 0.4*x - 0.4*y - 30)

	tamano = int(y1*0.2 + x1*0.1 + 10)
	tamano_texto = int(y1*0.02 + x1*0.02 + 3)

	#dibujar canvas con las coordenadas obtenidas
	canvas1.coords(circulo1, x1, y1, x2, y2)
	canvas2.coords(circulo2, x1, y1, x2, y2)
	canvas3.coords(circulo3, x1, y1, x2, y2)

	#coordenadas de los numeros
	z1 = int(x1*0.6 - 10)
	z2 = int(y1*0.6 - 10)

	#coordenadas del texto
	w1 = int(x1*0.49 + 8)
	w2 = int(y1*0.8 + 10)

	#ajuste de la posición de los textos donde se muestra el tiempo
	canvas1.coords(texto1, z1, z2)
	canvas2.coords(texto2, z1, z2)
	canvas3.coords(texto3, z1, z2)

	#ajuste del tamaño y contenido de los textos del tiempo
	canvas1.itemconfig(texto1, font = ('Arial', tamano, 'bold'), text = mi)
	canvas2.itemconfig(texto2, font = ('Arial', tamano, 'bold'), text = se)
	canvas3.itemconfig(texto3, font = ('Arial', tamano, 'bold'), text = ml)

	#ajuste de la posición de los textos que indican minutos, segundos y milisegundos
	canvas1.coords(texto_minutos, w1, w2)
	canvas2.coords(texto_segundos, w1, w2)
	canvas3.coords(texto_milisegundos, w1, w2)

	#ajuste del temaño de los textos
	canvas1.itemconfig(texto_minutos, font = ('Arial', tamano_texto, 'bold'))
	canvas2.itemconfig(texto_segundos, font = ('Arial', tamano_texto, 'bold'))
	canvas3.itemconfig(texto_milisegundos, font = ('Arial', tamano_texto, 'bold'))

	#actualizar los tamaños y posiciones cada 100ms
	canvas1.after(100, coordenadas)


#configuracion de los frames
frame4.columnconfigure(0,weight = 1)
frame4.rowconfigure(0, weight = 1)
frame4.columnconfigure(1, weight = 1)
frame4.rowconfigure(0, weight = 1)
frame4.columnconfigure(2, weight = 1)
frame4.rowconfigure(0, weight = 1)
frame4.columnconfigure(3, weight = 1)
frame4.rowconfigure(0, weight = 1)
frame4.columnconfigure(4, weight = 1)
frame4.rowconfigure(0, weight = 1)
frame4.columnconfigure(5, weight = 1)
frame4.rowconfigure(0, weight = 1)

#configuración del frame para los botones
frame5.columnconfigure(0, weight = 1)
frame5.rowconfigure(0, weight = 1)
frame5.columnconfigure(1, weight = 1)
frame5.rowconfigure(0, weight = 1)
frame5.columnconfigure(2, weight = 1)
frame5.rowconfigure(0, weight = 1)

#Creación de los botones
stop = Button(frame5, text = 'DETENER', relief = "raised", bd = 5, bg = 'orange', font = ('Arial', 12, 'bold'), width = 20, command = stop_boton)
stop.grid(column = 0, row = 0, padx = 10, pady = 10, sticky ='snew')

inicio = Button(frame5, text = 'INICIAR', relief = "raised", bd = 5, bg = 'green2', font = ('Arial', 12, 'bold'), width = 20, command = iniciar_pausar)
inicio.grid(column = 0, row = 0, padx = 10, pady = 10, sticky ='snew')

fin = Button(frame5, text = 'REINICIAR', relief = "raised", bd = 4, bg = 'red', font = ('Arial', 12, 'bold'), width = 20, command = reiniciar)
fin.grid(column = 2, row = 0, padx = 10, pady = 10, sticky = 'snew')


#Coordenadas de la ventana
coordenadas()
ventana.mainloop()