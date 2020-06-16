import random
from tkinter import*

room=Tk()
room.title("Habit Generator")  
room.geometry('300x300')

#Lists of things--------------------------------------
goals=['violin', 'painting', 'Learning Video', 'Japanese', 'programming','sewing', 'Music','Read','Excercise']

violin_habits=["scales",'etudes', 'bow excercises', 'finger excercises', 'vibrato', 'repertoir']
painting_habits=['study poses', 'object study', 'watercolor practice', 'composition study', 'challenge', 'plant study']
videos_habits=['gardening','biology', 'language cartoon','sewing','music theory', 'japanese']
japanese_habits=['course','misa or miku','intention anime watching','practice kanji']
programming_habits=['one page of book','code wars','my program']
sewing_habits=['watch video','plan project']
music_habits=['vocal excercises','sing scales','music theory','interval training', 'rythm training']
read_habits=['LOTR', 'wealth book']
excercise_habits=['cloe ting','25 sentadillas','push ups']

goal= random.choice(goals)
# List--------------------------------------------------------

hello_label= Label(room, text="hope")
hello_label.pack()

# Cuadrito de Insert donde aparece el habito a completar
habit_box= Entry(room)
habit_box.pack()

# Functions
def choose():
	habit_box.delete(0, END)
	def seleccion(goal_select,habit_select):
		if clicked.get()== goal_select:
			a= random.choice(habit_select)
			habit_box.insert(0, a)

	seleccion('violin', violin_habits)
	seleccion('', '')

	 # if clicked.get()=='violin':
	 # 	a= random.choice(violin_habits)
	 # 	habit_box.insert(0, a)


	# 	habit=Label(room, text= a).pack()
	# elif clicked.get()=="painting":
	# 	a=random.choice(painting_habits)
	# 	habit=Label(room, text= a).pack()



clicked= StringVar()
clicked.set("choose")
drop= OptionMenu(room, clicked, 'violin', 'painting', 'Learning Video', 'Japanese', 'programming','sewing', 'Music','Read','Excercise')
drop.pack()

def aleatorio():

#Defining the random goal.
	goal= random.choice(goals)

	# Deciding random habit
	if goal=='violin':
	    a=(random.choice(violin_habits))
	elif goal=='painting':
	    a=(random.choice(painting_habits))
	elif goal=='Learning Video':
	    a=(random.choice(videos_habits))
	elif goal=='Japanese':
	    a=(random.choice(japanese_habits))
	elif goal=='programming':
	    a=(random.choice(programming_habits))
	elif goal=='sewing':
	    a=(random.choice(sewing_habits))
	elif goal=='Music':
	    a=(random.choice(music_habits))
	elif goal=='Read':
	    a=(random.choice(read_habits))
	elif goal=='Excercise':
	    a=(random.choice(excercise_habits))

	aleatorio_habit= Label(room, text= a).pack()


# Buttons to choose if you want to get a random goal or choose it yourself.

chooseButton= Button(room, text="you choose", command=choose)
chooseButton.pack()

aleatorioButton= Button(room, text="Random", command=aleatorio)
aleatorioButton.pack()


room.mainloop()