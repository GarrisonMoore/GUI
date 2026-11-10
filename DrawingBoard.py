import tkinter as tk
from token import LEFTSHIFT

"""
Basically copied this to learn how to build the basic drawing board
https://www.w3resource.com/python-exercises/tkinter/python-tkinter-canvas-and-graphics-exercise-2.php
"""

drawing = False
last_X, last_y = None, None
bg_color = "white"
brush_color = "black"
brush_width = 2

def start_drawling(event):
    """
    Method to mark the starting point of the initial pointer coordinates (mouse click)
    """
    global drawing
    drawing = True
    global last_X, last_y
    last_X, last_y = event.x, event.y

def stop_drawling(event):
    """
    Method to mark the ending of the drawing coordinates (mouse release)
    """
    global drawing
    drawing = False

def draw(event):
    """
    Method to execute drawing a line (Draws a line between the two mouse points)
    """
    global last_X, last_y

    if drawing:
        x, y = event.x, event.y
        canvas.create_line((last_X, last_y, x, y), fill = brush_color, width = brush_width)
        last_X, last_y = x, y

def change_color(new_color):
    """
    Changes brush color
    """
    global brush_color
    brush_color = new_color

def change_bg_color(new_color):
    """
    Changes canvas background color
    """
    global bg_color
    bg_color = new_color
    canvas.configure(bg=bg_color)

def change_brush_size(new_size):
    """
    Change brush size
    """
    global brush_width
    brush_width = new_size

def clear_canvas():
    """
    clear canvas
    """
    canvas.delete("all")

# === Initiate the window ===

window = tk.Tk()
window.title("DrawlingBoard")

# create a toolbar to store all our buttons
toolbar = tk.Frame(window)
toolbar.pack(side=tk.TOP, fill=tk.X, pady=5, padx=5)

# create the reset button and put it in the toolbar
reset_button = tk.Button(toolbar, text="Clear Canvas", command=clear_canvas)
reset_button.pack(side=tk.TOP, pady=5)

# create a frame to store brush colors in, put this in the toolbar
brush_color_frame = tk.Frame(toolbar)
brush_color_frame.pack(side=tk.LEFT, pady=5, padx=5)

# list of colors
colors = ["red","blue","green","cyan","yellow","orange","pink"]

# Creating a list of brush color buttons
color_buttons_label = tk.Label(brush_color_frame, text="Brush Colors: ")
color_buttons_label.pack(side=tk.LEFT)
color_buttons = []
for color in colors:
    color_buttons.append(tk.Button(brush_color_frame, text=color.capitalize(), bg=color, command=lambda c=color: change_color(c)))
    color_buttons[-1].pack(side=tk.LEFT)

# create a frame for background color buttons, put this in the toolbar
bg_color_buttons_frame = tk.Frame(toolbar)
bg_color_buttons_frame.pack(side=tk.RIGHT, pady=5,padx=5)

# create a list of background color buttons
bg_color_buttons_label = tk.Label(bg_color_buttons_frame, text="Background Colors: ")
bg_color_buttons_label.pack(side=tk.LEFT)
bg_color_buttons = []
for color in colors:
    bg_color_buttons.append(tk.Button(bg_color_buttons_frame, text=color.capitalize(), bg=color, command=lambda c=color: change_bg_color(c)))
    bg_color_buttons[-1].pack(side=tk.LEFT)

# create a frame to store brush size buttons in
size_frame = tk.Frame(toolbar)
size_frame.pack(side=tk.LEFT, padx=5)

# create a label for the brush size buttons
size_label = tk.Label(size_frame, text="Brush size:")
size_label.pack(side=tk.LEFT)

brush_sizes = [1,2,3,4,5,6,7,8,9,10]

# store the current selected size
selected_size = tk.IntVar(window)
selected_size.set(brush_sizes[1])

# store the brush sizes in a dropdown menu
brush_size_options = tk.OptionMenu(size_frame, selected_size, *brush_sizes, command=change_brush_size)
brush_size_options.pack(side=tk.TOP, pady=5)

# Initiate drawing canvas
canvas = tk.Canvas(window, height=1000, width=1000, bg=bg_color)
canvas.pack()

canvas.bind("<Button-1>", start_drawling)
canvas.bind("<ButtonRelease-1>", stop_drawling)
canvas.bind("<B1-Motion>", draw)

window.mainloop()
