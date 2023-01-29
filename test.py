import tkinter as tk
from tkinter import *
import random


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
		for F in (Home, ShapesGame, FoodsGame):

			frame = F(container, self)

			# initializing frame of that object from
			# Home, ShapesGame, FoodsGame respectively with
			# for loop
			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(Home)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

# Home Page

class Home(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		# label of frame Layout 2
		label = Label(self, text ="Home", font = LARGEFONT)
		
		# putting the grid in its place by using
		# grid
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		shapesButton = Button(self, text ="Shapes",
		command = lambda : controller.show_frame(ShapesGame))
	
		# putting the button in its place by
		# using grid
		shapesButton.grid(row = 1, column = 1, padx = 10, pady = 10)

		## button to show frame 2 with text layout2
		FoodsButton = Button(self, text ="Foods",
		command = lambda : controller.show_frame(FoodsGame))
	
		# putting the button in its place by
		# using grid
		FoodsButton.grid(row = 2, column = 1, padx = 10, pady = 10)

# Shapes Game

class ShapesGame(tk.Frame):
    def __init__(self, parent, controller):
        #frame
        tk.Frame.__init__(self, parent)
        label = Label(self, text = "shape", font = LARGEFONT)
        label.grid(row = 0, column = 2, padx = 10, pady = 10)
        
        # words
        shapeWords = ["circle", "square", "triangle", "rectangle", "octagon", 
                  "hexagon", "heart", "star", "diamond", "oval"]
        unusedWords = shapeWords
        shapeNum = 0;
        answers = []
        correctAnswer = ""
    
        # code stuff
        def game():
            if len(unusedWords) > 0:
                wrong = shapeWords
                numIncorrect = 8
            
                shapeNum = random.randint(0,len(unusedWords)-1)
                correctAnswer = unusedWords[shapeNum]
                answers.append(correctAnswer)
                unusedWords.pop()
            
                answers.append(wrong[random.randint(0,numIncorrect)])
                wrong.remove(answers[1])
                numIncorrect -=1
            
                answers.append(wrong[random.randint(0,numIncorrect)])
                wrong.remove(answers[2])
                numIncorrect -=1
            
                answers.append(wrong[random.randint(0,numIncorrect)])
                wrong.remove(answers[3])
                numIncorrect -=1
                
                random.shuffle(answers);
                
                option1.config(text=answers[0])
                option2.config(text=answers[1])
                option3.config(text=answers[2])
                option4.config(text=answers[3])
                
                answers.clear()
            else:
                shape = "you win!"
        
        def correct(text):
            if text == correctAnswer:
                game()
            else:
                shape = "try again"
        
        
         # buttons
        option1 = Button(self, text = "answer1",
                         command = lambda : correct(option1.cget('text')))
        option1.grid(row = 1, column = 1, padx = 10, pady = 10)
        
        option2 = Button(self, text = "answer2",
                         command = lambda : correct(option2.cget('text')))
        option2.grid(row = 1, column = 2, padx = 10, pady = 10)
        
        option3 = Button(self, text = "answer3",
                         command = lambda : correct(option3.cget('text')))
        option3.grid(row = 2, column = 1, padx = 10, pady = 10)
        
        option4 = Button(self, text = "answer4",
                         command = lambda : correct(option4.cget('text')))
        option4.grid(row = 2, column = 2, padx = 10, pady = 10)
        
        # starts
        game()



# Driver Code
app = tkinterApp()
app.mainloop()
