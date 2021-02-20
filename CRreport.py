from tkinter import *
from tkinter import filedialog


root= Tk()
root.title("CRrepot")

frame= LabelFrame(root, text = "Reporte")
frame.grid(row=1, column=0)

def save_file():
	open_file= filedialog.asksaveasfile(mode="w")
	if open_file is None: 
		return


def open_file():
	file= filedialog.askopenfile(mode="r")
	if file is not None:
		content = file.read()
		print(content)

b1= Button(root, text= "Save", command= save_file)
b1.grid(row=0, column=1)

b2= Button(root, text= "Open", command= open_file)
b2.grid(row=0, column=2)



# #lista de clasificaciones. boton para anadir y para quitar.
# tags_billing=["cancelaciones", "reembolsos" ]
# tags_cuenta=["Fraude", "Otros"]

# #CAncelacion
# botonadd = Button(root, text = "+", width = 5, height = 2 )
# botonsub = Button(root, text = "-", width = 5, height = 2 )
# cancel= Label(root, text=" Cancelaciones")

# cancel.grid(row=0, column=1)
# botonadd.grid(row=0, column=3)
# botonsub.grid(row=0, column=0)

#Reembolso

global qty_reem
qty_reem = 0

def add():
	global qty_reem
	qty_reem += 1
	qty2.config(text= qty_reem)

def sub():
	global qty_reem
	qty_reem -= 1
	qty2.config(text= qty_reem)


qty2= Label(frame, text= add)
qty2.grid(row=2, column=2)


botonsub = Button(frame, text = "-", command= sub, width = 5, height = 2 )
botonsub.grid(row=2, column=0)

reem= Label(frame, text=" Reembolso").grid(row=2, column=1)

botonadd = Button(frame, text = "+", command= add, width = 5, height = 2 )
botonadd.grid(row=2, column=3)






root.mainloop()