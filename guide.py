import tkinter as tk
from tkinter import ttk
import random


LARGEFONT =("Verdana", 35)

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

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
		for F in (StartPage, Page1, Page2, FoodGame, FoodGame2):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, page1, page2 respectively with
			# for loop
			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

# first window frame startpage

class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		# label of frame Layout 2
		label = ttk.Label(self, text ="Startpage", font = LARGEFONT)
		
		# putting the grid in its place by using
		# grid
		label.grid(row = 0, column = 2, padx = 10, pady = 10)

		button1 = ttk.Button(self, text ="Start Game",
		command = lambda : controller.show_frame(Page1))
	
		# putting the button in its place by
		# using grid
		button1.grid(row = 1, column = 2, padx = 10, pady = 10)



# second window frame page1
class Page1(tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Let's Learn!", font = LARGEFONT)
		label.grid(row = 0, column = 2, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="StartPage",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place
		# by using grid
		button1.grid(row = 2, column = 2, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button2 = ttk.Button(self, text ="Choose Category",
							command = lambda : controller.show_frame(Page2))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 1, column = 2, padx = 10, pady = 10)
        
# third window frame page2
class Page2(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Choose Category", font = LARGEFONT)
		label.grid(row = 0, column = 2, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout1
		button1 = ttk.Button(self, text ="Shapes",
							command = lambda : controller.show_frame(StartPage))
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		# button to show frame 3 with text
		# layout2
		button2 = ttk.Button(self, text ="Animals",
							command = lambda : controller.show_frame(StartPage))
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)
        
		# button to show frame 3 with text
		# layout3
		button3 = ttk.Button(self, text ="Food",
							command = lambda : controller.show_frame(FoodGame1))
		button3.grid(row = 1, column = 3, padx = 10, pady = 10)
        
		# button to show frame 3 with text
		# layout4
		button4 = ttk.Button(self, text ="Numbers",
							command = lambda : controller.show_frame(StartPage))
		button4.grid(row = 2, column = 3, padx = 10, pady = 10)
        
		# button to show frame 3 with text
		# layout5
		button5 = ttk.Button(self, text ="Startpage",
							command = lambda : controller.show_frame(StartPage))
		button5.grid(row = 3, column = 2, padx = 10, pady = 10)
        
#---------------------------------------------------------------------------------#


# Food Game
class FoodGame(i)(tk.Frame):
    def __init__(self, parent, controller):   
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Food", font = LARGEFONT)
        label.grid(row = 0, column = 2, padx = 10, pady = 10)
        
        # words
        foodWords = ["apple", "banana", "bread", "cheese", "milk", 
             "juice", "water", "cookie", "egg", "candy"]
        foodq1 = ()
        foodq1 = random.sample(foodWords, k=4)
        
#         def randomize():
#             foodWords = ["apple", "banana", "bread", "cheese", "milk", 
#              "juice", "water", "cookie", "egg", "candy"] 
#             foodq1 = ()
#             foodq1 = random.sample(foodWords, k=4)
#             label.config(text=random_number)

        answer = ()
        answer=random.sample(foodq1, k=1)
        label = ttk.Label(self, text =answer, font = LARGEFONT)
        label.grid(row = 1, column = 2, padx = 10, pady = 10)
        
#         def correct():
#             if text=answer:           

        # buttons
        option1 = ttk.Button(self, text =foodq1[0],
#                          command = lambda : combine_funcs(controller.show_frame(FoodGame), randomize))
                         command = lambda : controller.show_frame(FoodGame2))
        option1.grid(row = 2, column = 1, padx = 10, pady = 10)

        option2 = ttk.Button(self, text =foodq1[1],
#                          command = lambda : combine_funcs(controller.show_frame(FoodGame), randomize))
                         command = lambda : controller.show_frame(FoodGame2))
        option2.grid(row = 3, column = 1, padx = 10, pady = 10)

        option3 = ttk.Button(self, text =foodq1[2],
#                          command = lambda : combine_funcs(controller.show_frame(FoodGame), randomize))
                         command = lambda : controller.show_frame(FoodGame2))
        option3.grid(row = 2, column = 3, padx = 10, pady = 10)

        option4 = ttk.Button(self, text =foodq1[3],
#                          command = lambda : combine_funcs(controller.show_frame(FoodGame), randomize))
                         command = lambda : controller.show_frame(FoodGame2))
        option4.grid(row = 3, column = 3, padx = 10, pady = 10)

        option5 = ttk.Button(self, text ="Startpage",
                         command = lambda : controller.show_frame(StartPage))
        option5.grid(row = 4, column = 2, padx = 10, pady = 10)
        
# class FoodGame2(tk.Frame):
#     def __init__(self, parent, controller):   
#         tk.Frame.__init__(self, parent)
#         label = ttk.Label(self, text ="Food", font = LARGEFONT)
#         label.grid(row = 0, column = 2, padx = 10, pady = 10)
        
#         # words
#         foodWords = ["apple", "banana", "bread", "cheese", "milk", 
#              "juice", "water", "cookie", "egg", "candy"]
#         foodq1 = ()
#         foodq1 = random.sample(foodWords, k=4)
        
#         answer = ()
#         answer=random.sample(foodq1, k=1)
#         label = ttk.Label(self, text =answer, font = LARGEFONT)
#         label.grid(row = 1, column = 2, padx = 10, pady = 10)
        

#         # buttons
#         option1 = ttk.Button(self, text =foodq1[0],
# #                          command = lambda : combine_funcs(controller.show_frame(FoodGame), randomize))
#                          command = lambda : controller.show_frame(FoodGame))
#         option1.grid(row = 2, column = 1, padx = 10, pady = 10)

#         option2 = ttk.Button(self, text =foodq1[1],
# #                          command = lambda : combine_funcs(controller.show_frame(FoodGame), randomize))
#                          command = lambda : controller.show_frame(FoodGame))
#         option2.grid(row = 3, column = 1, padx = 10, pady = 10)

#         option3 = ttk.Button(self, text =foodq1[2],
# #                          command = lambda : combine_funcs(controller.show_frame(FoodGame), randomize))
#                          command = lambda : controller.show_frame(FoodGame))
#         option3.grid(row = 2, column = 3, padx = 10, pady = 10)

#         option4 = ttk.Button(self, text =foodq1[3],
# #                          command = lambda : combine_funcs(controller.show_frame(FoodGame), randomize))
#                          command = lambda : controller.show_frame(FoodGame))
#         option4.grid(row = 3, column = 3, padx = 10, pady = 10)

#         option5 = ttk.Button(self, text ="Startpage",
#                          command = lambda : controller.show_frame(StartPage))
#         option5.grid(row = 4, column = 2, padx = 10, pady = 10)
              
# Driver Code
app = tkinterApp()
app.mainloop()

# for x in range(1, 10):
#     frame = FoodGame(app, controller)
#     frame.pack()
