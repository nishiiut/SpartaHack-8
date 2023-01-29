from tkinter import *

app = Tk()
app.geometry("400x400")

canvas = Canvas(app, bg='white')
# canvas.pack()
canvas.pack(anchor='nw', fill='both', expand=1)

# image = Image.open("image.jpg")
# image = image.resize((400,400), Image.ANTIALIAS)
# image = ImageTk.PhotoImage(image)
# canvas.create_image(0,0, image=image, anchor='nw')

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
Button(app, text="Delete Shape", command=on_click).pack()


app.mainloop()