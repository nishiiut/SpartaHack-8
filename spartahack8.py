from tkinter import *
import tkinter as tk
from tkinter import ttk
import random
from PIL import ImageTk, Image 


LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
	
	# __init__ function for class tkinterApp
	def __init__(self, *args, **kwargs):
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {}

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (StartPage, CatagoryOptions, Type_Name, Write_Name, FoodGame1, FoodGame2, FoodGame3, FoodGame4, FoodGame5, FoodGame6, FoodGame7, FoodGame8, FoodGame9, FoodGame10, ShapeGame, AnimalGame, NumberGame, Correct1, Incorrect1, Correct2, Incorrect2, Correct3, Incorrect3, Correct4, Incorrect4, Correct5, Incorrect5, Correct6, Incorrect6, Correct7, Incorrect7, Correct8, Incorrect8, Correct9, Incorrect9, Correct10, Incorrect10):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, CatagoryOptions, page2 respectively with
			# for loop
			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

#---------------------------------------------------------------------------------#

# first window frame startpage

class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)

		image1 = Image.open(r"image3.jpg")
		background_image = ImageTk.PhotoImage(image1)

		label1 = tk.Label(self, image=background_image)
		label1.image = background_image
		label1.place(x=0, y=0, relwidth=1, relheight=1)
        
		title = tk.Label(self, text="Kindergarten Ready!", font=(
            'Comic Sans MS', 25, 'bold'), pady=5, bd=12, bg="#F0F8FF", fg="Black")
		title.place(relx=0.509, rely=0.45, anchor=tk.CENTER)

		start_button = tk.Button(self, text="start", bg="#F0F8FF",
            font=('Comic Sans MS', 18, 'bold'), activebackground = "#AFDCEB", command = lambda : controller.show_frame(CatagoryOptions))
		start_button.place(relx=0.43, rely=0.78, anchor=tk.CENTER)

		exit_button = tk.Button(self, text="exit", bg="#F0F8FF",
            font=('Comic Sans MS', 18, 'bold'), activebackground = "#AFDCEB")
		exit_button.place(relx=0.63, rely=0.78, anchor=tk.CENTER)

#---------------------------------------------------------------------------------#

# second window frame CatagoryOptions
class CatagoryOptions(tk.Frame):
	def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            image2 = Image.open(r"image5.jpg")
            background_image = ImageTk.PhotoImage(image2)
            
            label2 = tk.Label(self, image=background_image)
            label2.image = background_image
            label2.place(x=0, y=0, relwidth=1, relheight=1)
            
            label = tk.Label(self, text ="Choose A Category", font=('Comic Sans MS', 30, 'bold', 'underline'))
            label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
            label.config(background='white')

		    # button to show frame 2 with text
		    # layout1
            button1 = tk.Button(self, text ="Shapes", font=('Comic Sans MS', 18, 'bold'), 
                            command = lambda : controller.show_frame(ShapeGame))
            button1.place(relx=0.35, rely=0.32, anchor=tk.CENTER)

		    # button to show frame 3 with text
		    # layout2
            button2 = tk.Button(self, text ="Animals", font=('Comic Sans MS', 18, 'bold'), 
                            command = lambda : controller.show_frame(AnimalGame))
            button2.place(relx=0.35, rely=0.58, anchor=tk.CENTER)
        
		    # button to show frame 3 with text
		    # layout3
            button3 = tk.Button(self, text ="Food", font=('Comic Sans MS', 18, 'bold'), 
                            command = lambda : controller.show_frame(FoodGame1))
            button3.place(relx=0.65, rely=0.32, anchor=tk.CENTER)
        
		    # button to show frame 3 with text
		    # layout4
            button4 = tk.Button(self, text ="Count to 10", font=('Comic Sans MS', 18, 'bold'), 
                            command = lambda : controller.show_frame(NumberGame))
            button4.place(relx=0.65, rely=0.58, anchor=tk.CENTER)

            # button to show frame 3 with text
		    # layout4
            button4 = tk.Button(self, text ="Writing Your Name", font=('Comic Sans MS', 18, 'bold'), 
                            command = lambda : controller.show_frame(Type_Name))
            button4.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
        
		    # button to show frame 3 with text
		    # layout5
            button5 = tk.Button(self, text ="Start Page", font=('Comic Sans MS', 10, 'bold'),
							command = lambda : controller.show_frame(StartPage))
            button5.place(relx=0.5, rely=0.68, anchor=tk.CENTER)
        
#---------------------------------------------------------------------------------#

# Type Name
class Type_Name(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Enter Your Name!")
        label.pack(pady=10, padx=10)
        
        self.entry = tk.Entry(self)
        self.entry.pack(pady=10, padx=10)

        button = tk.Button(self, text="Submit", command = lambda : controller.show_frame(Write_Name))
        button.pack(pady=10)

    def submit_name(self):
        name = self.entry.get()



#---------------------------------------------------------------------------------#

# Write Name
class Write_Name(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        call_typeclass = Type_Name(parent, controller)
        get_typename = call_typeclass.submit_name()
        label = tk.Label(self, text=f"{get_typename}")
        label.pack(pady=10, padx=10)

        canvas = Canvas(self, bg='white')
        canvas.pack(anchor='nw', fill='both', expand=1)

        def get_x_and_y(event):
            global lasx, lasy
            lasx, lasy = event.x, event.y

        def draw_smth(event):
            global lasx, lasy
            canvas.create_line((lasx, lasy, event.x, event.y), 
                            fill='black', 
                            width=2)
            lasx, lasy = event.x, event.y

        canvas.bind("<Button-1>", get_x_and_y)
        canvas.bind("<B1-Motion>", draw_smth)   

        # Define a function to delete the shape
        def on_click():
            canvas.delete('all')

        # Create a button to delete the button
        delete_button = tk.Button(self, text="Delete", font=('Comic Sans MS', 10, 'bold'), command=on_click)
        delete_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

        # Create a button to go back to Typing Name
        tryagain_button = tk.Button(self, text ="Type Again", font=('Comic Sans MS', 10, 'bold'),
							command = lambda : controller.show_frame(Type_Name))
        tryagain_button.place(relx=0.2, rely=0.9, anchor=tk.CENTER)

        # Create a button to go back to Category
        category_button = tk.Button(self, text ="Category", font=('Comic Sans MS', 10, 'bold'),
							command = lambda : controller.show_frame(CatagoryOptions))
        category_button.place(relx=0.8, rely=0.9, anchor=tk.CENTER)


#--------------------------------_------------------------------------------------#

# Animal Game
class AnimalGame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.animalWords = ["cat", "dog", "cow", "horse", "pig", "mouse", "girrafe", "zebra", "chicken", "sheep"]
        self.question_number = 1
        self.answer = None
        self.create_question()
        
    def create_question(self):
        animalq = random.sample(self.animalWords, k=4)
        self.answer = random.sample(animalq, k=1)
        label = ttk.Label(self, text="Animal", font=LARGEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)
        option1 = ttk.Button(self, text=animalq[0], command=lambda: self.check_answer(animalq[0]))
        option1.grid(row=2, column=1, padx=10, pady=10)
        option2 = ttk.Button(self, text=animalq[1], command=lambda: self.check_answer(animalq[1]))
        option2.grid(row=3, column=1, padx=10, pady=10)
        option3 = ttk.Button(self, text=animalq[2], command=lambda: self.check_answer(animalq[2]))
        option3.grid(row=2, column=3, padx=10, pady=10)
        option4 = ttk.Button(self, text=animalq[3], command=lambda: self.check_answer(animalq[3]))
        option4.grid(row=3, column=3, padx=10, pady=10)
        next_button = ttk.Button(self, text="Next Question", command=lambda: self.next_question())
        next_button.grid(row=4, column=2, padx=10, pady=10)
        label = ttk.Label(self, text=self.answer[0], font=LARGEFONT)
        label.grid(row=1, column=2, padx=10, pady=10)

    def check_answer(self, answer):
        if answer == self.answer[0]:
            self.controller.show_frame(Correct)
        else:
            self.controller.show_frame(Incorrect)
            
    def next_question(self):
        self.animalWords = random.sample(self.animalWords, k=4)
        self.answer = random.sample(self.animalWords, k=1)
        self.question_number += 1
        self.create_question()
  
#---------------------------------------------------------------------------------#

# Number Game
class NumberGame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.numberWords = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
        self.question_number = 1
        self.answer = None
        self.create_question()

        
    def create_question(self):
        numberq = random.sample(self.numberWords, k=4)
        self.answer = random.sample(numberq, k=1)
        label = ttk.Label(self, text="Number", font=LARGEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)
        option1 = ttk.Button(self, text=numberq[0], command=lambda: self.check_answer(numberq[0]))
        option1.grid(row=2, column=1, padx=10, pady=10)
        option2 = ttk.Button(self, text=numberq[1], command=lambda: self.check_answer(numberq[1]))
        option2.grid(row=3, column=1, padx=10, pady=10)
        option3 = ttk.Button(self, text=numberq[2], command=lambda: self.check_answer(numberq[2]))
        option3.grid(row=2, column=3, padx=10, pady=10)
        option4 = ttk.Button(self, text=numberq[3], command=lambda: self.check_answer(numberq[3]))
        option4.grid(row=3, column=3, padx=10, pady=10)
        category_button = ttk.Button(self, text="Category", command=lambda: self.controller.show_frame(CatagoryOptions))
        category_button.grid(row=4, column=2, padx=10, pady=10)
        label = ttk.Label(self, text=self.answer[0], font=LARGEFONT)
        label.grid(row=1, column=2, padx=10, pady=10)

    def check_answer(self, answer):
        if answer == self.answer[0]:
            self.controller.show_frame(Correct)
        else:
            self.controller.show_frame(Incorrect)
            
    def next_question(self):
        self.numberWords = random.sample(self.numberWords, k=4)
        self.answer = random.sample(self.numberWords, k=1)
        self.question_number += 1
        self.create_question()

#---------------------------------------------------------------------------------#

# Shapes Game
class ShapeGame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.shapeWords = ["circle", "square", "triangle", "rectangle", "octagon", "hexagon", "heart", "star", "diamond", "oval"]
        self.question_number = 1
        self.answer = None
        self.create_question()
        self.controller.foodgame = self

        
    def create_question(self):
        shapeq = random.sample(self.shapeWords, k=4)
        self.answer = random.sample(shapeq, k=1)
        label = ttk.Label(self, text="Shape", font=LARGEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)
        option1 = ttk.Button(self, text=shapeq[0], command=lambda: self.check_answer(shapeq[0]))
        option1.grid(row=2, column=1, padx=10, pady=10)
        option2 = ttk.Button(self, text=shapeq[1], command=lambda: self.check_answer(shapeq[1]))
        option2.grid(row=3, column=1, padx=10, pady=10)
        option3 = ttk.Button(self, text=shapeq[2], command=lambda: self.check_answer(shapeq[2]))
        option3.grid(row=2, column=3, padx=10, pady=10)
        option4 = ttk.Button(self, text=shapeq[3], command=lambda: self.check_answer(shapeq[3]))
        option4.grid(row=3, column=3, padx=10, pady=10)
        next_button = ttk.Button(self, text="Next Question", command=lambda: self.next_question())
        next_button.grid(row=4, column=2, padx=10, pady=10)
        label = ttk.Label(self, text=self.answer[0], font=LARGEFONT)
        label.grid(row=1, column=2, padx=10, pady=10)

    def check_answer(self, answer):
        if answer == self.answer[0]:
            self.controller.show_frame(Correct)
        else:
            self.controller.show_frame(Incorrect)
            
    def next_question(self):
        self.shapeWords = random.sample(self.shapeWords, k=4)
        self.answer = random.sample(self.shapeWords, k=1)
        self.question_number += 1
        self.create_question()

#---------------------------------------------------------------------------------#

# Food Game
class FoodGame1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.foodWords = ["apple", "banana", "bread", "cheese", "milk", "juice", "water", "cookie", "egg", "candy"]
        self.question_number = 1
        self.answer = None
        self.create_question()

        
    def create_question(self):
        foodq = random.sample(self.foodWords, k=4)
        self.answer = random.sample(foodq, k=1)
        label = ttk.Label(self, text="Food", font=LARGEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)
        option1 = ttk.Button(self, text=foodq[0], command=lambda: self.check_answer(foodq[0]))
        option1.grid(row=2, column=1, padx=10, pady=10)
        option2 = ttk.Button(self, text=foodq[1], command=lambda: self.check_answer(foodq[1]))
        option2.grid(row=3, column=1, padx=10, pady=10)
        option3 = ttk.Button(self, text=foodq[2], command=lambda: self.check_answer(foodq[2]))
        option3.grid(row=2, column=3, padx=10, pady=10)
        option4 = ttk.Button(self, text=foodq[3], command=lambda: self.check_answer(foodq[3]))
        option4.grid(row=3, column=3, padx=10, pady=10)
        category_button = ttk.Button(self, text="Category", command=lambda: self.controller.show_frame(CatagoryOptions))
        category_button.grid(row=4, column=2, padx=10, pady=10)
        label = ttk.Label(self, text=self.answer[0], font=LARGEFONT)
        label.grid(row=1, column=2, padx=10, pady=10)

    def check_answer(self, answer):
        if answer == self.answer[0]:
            self.controller.show_frame(Correct1)
        else:
            self.controller.show_frame(Incorrect1)
        
    def next_question(self):
        self.foodWords = random.sample(self.foodWords, k=4)
        self.answer = random.sample(self.foodWords, k=1)
        self.question_number += 1
        self.create_question()



# Correct_Page
class Correct1(tk.Frame):
    def __init__(self, parent, controller):   
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Correct!")
        label.pack()
        button = ttk.Button(self, text="Next Question",
                           command=lambda: controller.show_frame(FoodGame2))
        button.pack()

        exit_button = ttk.Button(self, text="exit", 
                                command=lambda: controller.show_frame(CatagoryOptions))
        exit_button.pack()

    def on_show(self):
        self.controller.foodgame.next_question()


# Incorrect Page
class Incorrect1(tk.Frame):
    def __init__(self, parent, controller):   
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Incorrect!")
        label.pack()
        button = ttk.Button(self, text="Next Question",
                           command=lambda: controller.show_frame(FoodGame2))
        button.pack()

        exit_button = ttk.Button(self, text="exit", command=lambda: controller.show_frame(CatagoryOptions))
        exit_button.pack()

    def on_show(self):
        self.controller.foodgame.next_question()




class FoodGame2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.foodWords = ["apple", "banana", "bread", "cheese", "milk", "juice", "water", "cookie", "egg", "candy"]
        self.question_number = 1
        self.answer = None
        self.create_question()

        
    def create_question(self):
        foodq = random.sample(self.foodWords, k=4)
        self.answer = random.sample(foodq, k=1)
        label = ttk.Label(self, text="Food", font=LARGEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)
        option1 = ttk.Button(self, text=foodq[0], command=lambda: self.check_answer(foodq[0]))
        option1.grid(row=2, column=1, padx=10, pady=10)
        option2 = ttk.Button(self, text=foodq[1], command=lambda: self.check_answer(foodq[1]))
        option2.grid(row=3, column=1, padx=10, pady=10)
        option3 = ttk.Button(self, text=foodq[2], command=lambda: self.check_answer(foodq[2]))
        option3.grid(row=2, column=3, padx=10, pady=10)
        option4 = ttk.Button(self, text=foodq[3], command=lambda: self.check_answer(foodq[3]))
        option4.grid(row=3, column=3, padx=10, pady=10)
        category_button = ttk.Button(self, text="Category", command=lambda: self.controller.show_frame(CatagoryOptions))
        category_button.grid(row=4, column=2, padx=10, pady=10)
        label = ttk.Label(self, text=self.answer[0], font=LARGEFONT)
        label.grid(row=1, column=2, padx=10, pady=10)

    def check_answer(self, answer):
        if answer == self.answer[0]:
            self.controller.show_frame(Correct2)
        else:
            self.controller.show_frame(Incorrect2)
        
    def next_question(self):
        self.foodWords = random.sample(self.foodWords, k=4)
        self.answer = random.sample(self.foodWords, k=1)
        self.question_number += 1
        self.create_question()



# Correct_Page
class Correct2(tk.Frame):
    def __init__(self, parent, controller):   
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Correct!")
        label.pack()
        button = ttk.Button(self, text="Next Question",
                           command=lambda: controller.show_frame(FoodGame3))
        button.pack()

        exit_button = ttk.Button(self, text="exit", 
                                command=lambda: controller.show_frame(CatagoryOptions))
        exit_button.pack()

    def on_show(self):
        self.controller.foodgame.next_question()


# Incorrect Page
class Incorrect2(tk.Frame):
    def __init__(self, parent, controller):   
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Incorrect!")
        label.pack()
        button = ttk.Button(self, text="Next Question",
                           command=lambda: controller.show_frame(FoodGame3))
        button.pack()

        exit_button = ttk.Button(self, text="exit", command=lambda: controller.show_frame(CatagoryOptions))
        exit_button.pack()

    def on_show(self):
        self.controller.foodgame.next_question()


#---------------------------------------------------------------------------------------------------------------#

class FoodGame3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.foodWords = ["apple", "banana", "bread", "cheese", "milk", "juice", "water", "cookie", "egg", "candy"]
        self.question_number = 1
        self.answer = None
        self.create_question()

        
    def create_question(self):
        foodq = random.sample(self.foodWords, k=4)
        self.answer = random.sample(foodq, k=1)
        label = ttk.Label(self, text="Food", font=LARGEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)
        option1 = ttk.Button(self, text=foodq[0], command=lambda: self.check_answer(foodq[0]))
        option1.grid(row=2, column=1, padx=10, pady=10)
        option2 = ttk.Button(self, text=foodq[1], command=lambda: self.check_answer(foodq[1]))
        option2.grid(row=3, column=1, padx=10, pady=10)
        option3 = ttk.Button(self, text=foodq[2], command=lambda: self.check_answer(foodq[2]))
        option3.grid(row=2, column=3, padx=10, pady=10)
        option4 = ttk.Button(self, text=foodq[3], command=lambda: self.check_answer(foodq[3]))
        option4.grid(row=3, column=3, padx=10, pady=10)
        category_button = ttk.Button(self, text="Category", command=lambda: self.controller.show_frame(CatagoryOptions))
        category_button.grid(row=4, column=2, padx=10, pady=10)
        label = ttk.Label(self, text=self.answer[0], font=LARGEFONT)
        label.grid(row=1, column=2, padx=10, pady=10)

    def check_answer(self, answer):
        if answer == self.answer[0]:
            self.controller.show_frame(Correct3)
        else:
            self.controller.show_frame(Incorrect3)
        
    def next_question(self):
        self.foodWords = random.sample(self.foodWords, k=4)
        self.answer = random.sample(self.foodWords, k=1)
        self.question_number += 1
        self.create_question()



# Correct_Page
class Correct3(tk.Frame):
    def __init__(self, parent, controller):   
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Correct!")
        label.pack()
        button = ttk.Button(self, text="Next Question",
                           command=lambda: controller.show_frame(FoodGame4))
        button.pack()

        exit_button = ttk.Button(self, text="exit", 
                                command=lambda: controller.show_frame(CatagoryOptions))
        exit_button.pack()

    def on_show(self):
        self.controller.foodgame.next_question()


# Incorrect Page
class Incorrect3(tk.Frame):
    def __init__(self, parent, controller):   
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Incorrect!")
        label.pack()
        button = ttk.Button(self, text="Next Question",
                           command=lambda: controller.show_frame(FoodGame4))
        button.pack()

        exit_button = ttk.Button(self, text="exit", command=lambda: controller.show_frame(CatagoryOptions))
        exit_button.pack()

    def on_show(self):
        self.controller.foodgame.next_question()


#---------------------------------------------------------------------------------------------------------------#

class FoodGame4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.foodWords = ["apple", "banana", "bread", "cheese", "milk", "juice", "water", "cookie", "egg", "candy"]
        self.question_number = 1
        self.answer = None
        self.create_question()

        
    def create_question(self):
        foodq = random.sample(self.foodWords, k=4)
        self.answer = random.sample(foodq, k=1)
        label = ttk.Label(self, text="Food", font=LARGEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)
        option1 = ttk.Button(self, text=foodq[0], command=lambda: self.check_answer(foodq[0]))
        option1.grid(row=2, column=1, padx=10, pady=10)
        option2 = ttk.Button(self, text=foodq[1], command=lambda: self.check_answer(foodq[1]))
        option2.grid(row=3, column=1, padx=10, pady=10)
        option3 = ttk.Button(self, text=foodq[2], command=lambda: self.check_answer(foodq[2]))
        option3.grid(row=2, column=3, padx=10, pady=10)
        option4 = ttk.Button(self, text=foodq[3], command=lambda: self.check_answer(foodq[3]))
        option4.grid(row=3, column=3, padx=10, pady=10)
        category_button = ttk.Button(self, text="Category", command=lambda: self.controller.show_frame(CatagoryOptions))
        category_button.grid(row=4, column=2, padx=10, pady=10)
        label = ttk.Label(self, text=self.answer[0], font=LARGEFONT)
        label.grid(row=1, column=2, padx=10, pady=10)

    def check_answer(self, answer):
        if answer == self.answer[0]:
            self.controller.show_frame(Correct4)
        else:
            self.controller.show_frame(Incorrect4)
        
    def next_question(self):
        self.foodWords = random.sample(self.foodWords, k=4)
        self.answer = random.sample(self.foodWords, k=1)
        self.question_number += 1
        self.create_question()



# Correct_Page
class Correct4(tk.Frame):
    def __init__(self, parent, controller):   
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Correct!")
        label.pack()
        button = ttk.Button(self, text="Next Question",
                           command=lambda: controller.show_frame(FoodGame5))
        button.pack()

        exit_button = ttk.Button(self, text="exit", 
                                command=lambda: controller.show_frame(CatagoryOptions))
        exit_button.pack()

    def on_show(self):
        self.controller.foodgame.next_question()


# Incorrect Page
class Incorrect4(tk.Frame):
    def __init__(self, parent, controller):   
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Incorrect!")
        label.pack()
        button = ttk.Button(self, text="Next Question",
                           command=lambda: controller.show_frame(FoodGame5))
        button.pack()

        exit_button = ttk.Button(self, text="exit", command=lambda: controller.show_frame(CatagoryOptions))
        exit_button.pack()

    def on_show(self):
        self.controller.foodgame.next_question()


#---------------------------------------------------------------------------------------------------------------#

class FoodGame5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.foodWords = ["apple", "banana", "bread", "cheese", "milk", "juice", "water", "cookie", "egg", "candy"]
        self.question_number = 1
        self.answer = None
        self.create_question()

        
    def create_question(self):
        foodq = random.sample(self.foodWords, k=4)
        self.answer = random.sample(foodq, k=1)
        label = ttk.Label(self, text="Food", font=LARGEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)
        option1 = ttk.Button(self, text=foodq[0], command=lambda: self.check_answer(foodq[0]))
        option1.grid(row=2, column=1, padx=10, pady=10)
        option2 = ttk.Button(self, text=foodq[1], command=lambda: self.check_answer(foodq[1]))
        option2.grid(row=3, column=1, padx=10, pady=10)
        option3 = ttk.Button(self, text=foodq[2], command=lambda: self.check_answer(foodq[2]))
        option3.grid(row=2, column=3, padx=10, pady=10)
        option4 = ttk.Button(self, text=foodq[3], command=lambda: self.check_answer(foodq[3]))
        option4.grid(row=3, column=3, padx=10, pady=10)
        category_button = ttk.Button(self, text="Category", command=lambda: self.controller.show_frame(CatagoryOptions))
        category_button.grid(row=4, column=2, padx=10, pady=10)
        label = ttk.Label(self, text=self.answer[0], font=LARGEFONT)
        label.grid(row=1, column=2, padx=10, pady=10)

    def check_answer(self, answer):
        if answer == self.answer[0]:
            self.controller.show_frame(Correct5)
        else:
            self.controller.show_frame(Incorrect5)
        
    def next_question(self):
        self.foodWords = random.sample(self.foodWords, k=4)
        self.answer = random.sample(self.foodWords, k=1)
        self.question_number += 1
        self.create_question()



# Correct_Page
class Correct5(tk.Frame):
    def __init__(self, parent, controller):   
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Correct!")
        label.pack()
        button = ttk.Button(self, text="Next Question",
                           command=lambda: controller.show_frame(FoodGame6))
        button.pack()

        exit_button = ttk.Button(self, text="exit", 
                                command=lambda: controller.show_frame(CatagoryOptions))
        exit_button.pack()

    def on_show(self):
        self.controller.foodgame.next_question()


# Incorrect Page
class Incorrect5(tk.Frame):
    def __init__(self, parent, controller):   
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Incorrect!")
        label.pack()
        button = ttk.Button(self, text="Next Question",
                           command=lambda: controller.show_frame(FoodGame6))
        button.pack()

        exit_button = ttk.Button(self, text="exit", command=lambda: controller.show_frame(CatagoryOptions))
        exit_button.pack()

    def on_show(self):
        self.controller.foodgame.next_question()


#---------------------------------------------------------------------------------------------------------------#

class FoodGame6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.foodWords = ["apple", "banana", "bread", "cheese", "milk", "juice", "water", "cookie", "egg", "candy"]
        self.question_number = 1
        self.answer = None
        self.create_question()

        
    def create_question(self):
        foodq = random.sample(self.foodWords, k=4)
        self.answer = random.sample(foodq, k=1)
        label = ttk.Label(self, text="Food", font=LARGEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)
        option1 = ttk.Button(self, text=foodq[0], command=lambda: self.check_answer(foodq[0]))
        option1.grid(row=2, column=1, padx=10, pady=10)
        option2 = ttk.Button(self, text=foodq[1], command=lambda: self.check_answer(foodq[1]))
        option2.grid(row=3, column=1, padx=10, pady=10)
        option3 = ttk.Button(self, text=foodq[2], command=lambda: self.check_answer(foodq[2]))
        option3.grid(row=2, column=3, padx=10, pady=10)
        option4 = ttk.Button(self, text=foodq[3], command=lambda: self.check_answer(foodq[3]))
        option4.grid(row=3, column=3, padx=10, pady=10)
        category_button = ttk.Button(self, text="Category", command=lambda: self.controller.show_frame(CatagoryOptions))
        category_button.grid(row=4, column=2, padx=10, pady=10)
        label = ttk.Label(self, text=self.answer[0], font=LARGEFONT)
        label.grid(row=1, column=2, padx=10, pady=10)

    def check_answer(self, answer):
        if answer == self.answer[0]:
            self.controller.show_frame(Correct6)
        else:
            self.controller.show_frame(Incorrect6)
        
    def next_question(self):
        self.foodWords = random.sample(self.foodWords, k=4)
        self.answer = random.sample(self.foodWords, k=1)
        self.question_number += 1
        self.create_question()



# Correct_Page
class Correct6(tk.Frame):
    def __init__(self, parent, controller):   
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Correct!")
        label.pack()
        button = ttk.Button(self, text="Next Question",
                           command=lambda: controller.show_frame(FoodGame7))
        button.pack()

        exit_button = ttk.Button(self, text="exit", 
                                command=lambda: controller.show_frame(CatagoryOptions))
        exit_button.pack()

    def on_show(self):
        self.controller.foodgame.next_question()


# Incorrect Page
class Incorrect6(tk.Frame):
    def __init__(self, parent, controller):   
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Incorrect!")
        label.pack()
        button = ttk.Button(self, text="Next Question",
                           command=lambda: controller.show_frame(FoodGame7))
        button.pack()

        exit_button = ttk.Button(self, text="exit", command=lambda: controller.show_frame(CatagoryOptions))
        exit_button.pack()

    def on_show(self):
        self.controller.foodgame.next_question()


#---------------------------------------------------------------------------------------------------------------#

class FoodGame7(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.foodWords = ["apple", "banana", "bread", "cheese", "milk", "juice", "water", "cookie", "egg", "candy"]
        self.question_number = 1
        self.answer = None
        self.create_question()

        
    def create_question(self):
        foodq = random.sample(self.foodWords, k=4)
        self.answer = random.sample(foodq, k=1)
        label = ttk.Label(self, text="Food", font=LARGEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)
        option1 = ttk.Button(self, text=foodq[0], command=lambda: self.check_answer(foodq[0]))
        option1.grid(row=2, column=1, padx=10, pady=10)
        option2 = ttk.Button(self, text=foodq[1], command=lambda: self.check_answer(foodq[1]))
        option2.grid(row=3, column=1, padx=10, pady=10)
        option3 = ttk.Button(self, text=foodq[2], command=lambda: self.check_answer(foodq[2]))
        option3.grid(row=2, column=3, padx=10, pady=10)
        option4 = ttk.Button(self, text=foodq[3], command=lambda: self.check_answer(foodq[3]))
        option4.grid(row=3, column=3, padx=10, pady=10)
        category_button = ttk.Button(self, text="Category", command=lambda: self.controller.show_frame(CatagoryOptions))
        category_button.grid(row=4, column=2, padx=10, pady=10)
        label = ttk.Label(self, text=self.answer[0], font=LARGEFONT)
        label.grid(row=1, column=2, padx=10, pady=10)

    def check_answer(self, answer):
        if answer == self.answer[0]:
            self.controller.show_frame(Correct7)
        else:
            self.controller.show_frame(Incorrect7)
        
    def next_question(self):
        self.foodWords = random.sample(self.foodWords, k=4)
        self.answer = random.sample(self.foodWords, k=1)
        self.question_number += 1
        self.create_question()



# Correct_Page
class Correct7(tk.Frame):
    def __init__(self, parent, controller):   
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Correct!")
        label.pack()
        button = ttk.Button(self, text="Next Question",
                           command=lambda: controller.show_frame(FoodGame8))
        button.pack()

        exit_button = ttk.Button(self, text="exit", 
                                command=lambda: controller.show_frame(CatagoryOptions))
        exit_button.pack()

    def on_show(self):
        self.controller.foodgame.next_question()


# Incorrect Page
class Incorrect7(tk.Frame):
    def __init__(self, parent, controller):   
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Incorrect!")
        label.pack()
        button = ttk.Button(self, text="Next Question",
                           command=lambda: controller.show_frame(FoodGame8))
        button.pack()

        exit_button = ttk.Button(self, text="exit", command=lambda: controller.show_frame(CatagoryOptions))
        exit_button.pack()

    def on_show(self):
        self.controller.foodgame.next_question()


#---------------------------------------------------------------------------------------------------------------#

class FoodGame8(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.foodWords = ["apple", "banana", "bread", "cheese", "milk", "juice", "water", "cookie", "egg", "candy"]
        self.question_number = 1
        self.answer = None
        self.create_question()

        
    def create_question(self):
        foodq = random.sample(self.foodWords, k=4)
        self.answer = random.sample(foodq, k=1)
        label = ttk.Label(self, text="Food", font=LARGEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)
        option1 = ttk.Button(self, text=foodq[0], command=lambda: self.check_answer(foodq[0]))
        option1.grid(row=2, column=1, padx=10, pady=10)
        option2 = ttk.Button(self, text=foodq[1], command=lambda: self.check_answer(foodq[1]))
        option2.grid(row=3, column=1, padx=10, pady=10)
        option3 = ttk.Button(self, text=foodq[2], command=lambda: self.check_answer(foodq[2]))
        option3.grid(row=2, column=3, padx=10, pady=10)
        option4 = ttk.Button(self, text=foodq[3], command=lambda: self.check_answer(foodq[3]))
        option4.grid(row=3, column=3, padx=10, pady=10)
        category_button = ttk.Button(self, text="Category", command=lambda: self.controller.show_frame(CatagoryOptions))
        category_button.grid(row=4, column=2, padx=10, pady=10)
        label = ttk.Label(self, text=self.answer[0], font=LARGEFONT)
        label.grid(row=1, column=2, padx=10, pady=10)

    def check_answer(self, answer):
        if answer == self.answer[0]:
            self.controller.show_frame(Correct8)
        else:
            self.controller.show_frame(Incorrect8)
        
    def next_question(self):
        self.foodWords = random.sample(self.foodWords, k=4)
        self.answer = random.sample(self.foodWords, k=1)
        self.question_number += 1
        self.create_question()



# Correct_Page
class Correct8(tk.Frame):
    def __init__(self, parent, controller):   
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Correct!")
        label.pack()
        button = ttk.Button(self, text="Next Question",
                           command=lambda: controller.show_frame(FoodGame9))
        button.pack()

        exit_button = ttk.Button(self, text="exit", 
                                command=lambda: controller.show_frame(CatagoryOptions))
        exit_button.pack()

    def on_show(self):
        self.controller.foodgame.next_question()


# Incorrect Page
class Incorrect8(tk.Frame):
    def __init__(self, parent, controller):   
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Incorrect!")
        label.pack()
        button = ttk.Button(self, text="Next Question",
                           command=lambda: controller.show_frame(FoodGame9))
        button.pack()

        exit_button = ttk.Button(self, text="exit", command=lambda: controller.show_frame(CatagoryOptions))
        exit_button.pack()

    def on_show(self):
        self.controller.foodgame.next_question()


#---------------------------------------------------------------------------------------------------------------#

class FoodGame9(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.foodWords = ["apple", "banana", "bread", "cheese", "milk", "juice", "water", "cookie", "egg", "candy"]
        self.question_number = 1
        self.answer = None
        self.create_question()

        
    def create_question(self):
        foodq = random.sample(self.foodWords, k=4)
        self.answer = random.sample(foodq, k=1)
        label = ttk.Label(self, text="Food", font=LARGEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)
        option1 = ttk.Button(self, text=foodq[0], command=lambda: self.check_answer(foodq[0]))
        option1.grid(row=2, column=1, padx=10, pady=10)
        option2 = ttk.Button(self, text=foodq[1], command=lambda: self.check_answer(foodq[1]))
        option2.grid(row=3, column=1, padx=10, pady=10)
        option3 = ttk.Button(self, text=foodq[2], command=lambda: self.check_answer(foodq[2]))
        option3.grid(row=2, column=3, padx=10, pady=10)
        option4 = ttk.Button(self, text=foodq[3], command=lambda: self.check_answer(foodq[3]))
        option4.grid(row=3, column=3, padx=10, pady=10)
        category_button = ttk.Button(self, text="Category", command=lambda: self.controller.show_frame(CatagoryOptions))
        category_button.grid(row=4, column=2, padx=10, pady=10)
        label = ttk.Label(self, text=self.answer[0], font=LARGEFONT)
        label.grid(row=1, column=2, padx=10, pady=10)

    def check_answer(self, answer):
        if answer == self.answer[0]:
            self.controller.show_frame(Correct9)
        else:
            self.controller.show_frame(Incorrect9)
        
    def next_question(self):
        self.foodWords = random.sample(self.foodWords, k=4)
        self.answer = random.sample(self.foodWords, k=1)
        self.question_number += 1
        self.create_question()



# Correct_Page
class Correct9(tk.Frame):
    def __init__(self, parent, controller):   
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Correct!")
        label.pack()
        button = ttk.Button(self, text="Next Question",
                           command=lambda: controller.show_frame(FoodGame10))
        button.pack()

        exit_button = ttk.Button(self, text="exit", 
                                command=lambda: controller.show_frame(CatagoryOptions))
        exit_button.pack()

    def on_show(self):
        self.controller.foodgame.next_question()


# Incorrect Page
class Incorrect9(tk.Frame):
    def __init__(self, parent, controller):   
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Incorrect!")
        label.pack()
        button = ttk.Button(self, text="Next Question",
                           command=lambda: controller.show_frame(FoodGame10))
        button.pack()

        exit_button = ttk.Button(self, text="exit", command=lambda: controller.show_frame(CatagoryOptions))
        exit_button.pack()

    def on_show(self):
        self.controller.foodgame.next_question()


#---------------------------------------------------------------------------------------------------------------#

class FoodGame10(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.foodWords = ["apple", "banana", "bread", "cheese", "milk", "juice", "water", "cookie", "egg", "candy"]
        self.question_number = 1
        self.answer = None
        self.create_question()

        
    def create_question(self):
        foodq = random.sample(self.foodWords, k=4)
        self.answer = random.sample(foodq, k=1)
        label = ttk.Label(self, text="Food", font=LARGEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)
        option1 = ttk.Button(self, text=foodq[0], command=lambda: self.check_answer(foodq[0]))
        option1.grid(row=2, column=1, padx=10, pady=10)
        option2 = ttk.Button(self, text=foodq[1], command=lambda: self.check_answer(foodq[1]))
        option2.grid(row=3, column=1, padx=10, pady=10)
        option3 = ttk.Button(self, text=foodq[2], command=lambda: self.check_answer(foodq[2]))
        option3.grid(row=2, column=3, padx=10, pady=10)
        option4 = ttk.Button(self, text=foodq[3], command=lambda: self.check_answer(foodq[3]))
        option4.grid(row=3, column=3, padx=10, pady=10)
        category_button = ttk.Button(self, text="Category", command=lambda: self.controller.show_frame(CatagoryOptions))
        category_button.grid(row=4, column=2, padx=10, pady=10)
        label = ttk.Label(self, text=self.answer[0], font=LARGEFONT)
        label.grid(row=1, column=2, padx=10, pady=10)

    def check_answer(self, answer):
        if answer == self.answer[0]:
            self.controller.show_frame(Correct10)
        else:
            self.controller.show_frame(Incorrect10)
        
    def next_question(self):
        self.foodWords = random.sample(self.foodWords, k=4)
        self.answer = random.sample(self.foodWords, k=1)
        self.question_number += 1
        self.create_question()



# Correct_Page
class Correct10(tk.Frame):
    def __init__(self, parent, controller):   
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Correct!")
        label.pack()

        exit_button = ttk.Button(self, text="exit", 
                                command=lambda: controller.show_frame(CatagoryOptions))
        exit_button.pack()

    def on_show(self):
        self.controller.foodgame.next_question()


# Incorrect Page
class Incorrect10(tk.Frame):
    def __init__(self, parent, controller):   
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Incorrect!")
        label.pack()

        exit_button = ttk.Button(self, text="exit", command=lambda: controller.show_frame(CatagoryOptions))
        exit_button.pack()

    def on_show(self):
        self.controller.foodgame.next_question()


#---------------------------------------------------------------------------------------------------------------#

        
        
# Driver Code
app = tkinterApp()
app.mainloop()