import tkinter as tk

def submit():
    """
    This is called when submit button is pressed
    """
    print("Submission button pressed.")
    entry = text_entry.get()

    if entry.lower() == "bird":
        print(f"The contents of entry box are: {entry}")
        entry_label.configure(text = f"Your submission: {entry}")

        # spawn bird
        global sd_image
        sd_image = tk.PhotoImage(file="bird.png")

        image_label = tk.Label(window, image=sd_image)
        image_label.place(relx=.5, rely=.5, anchor='center')

        window.geometry()


    elif entry:
        print(f"The contents of entry box are: {entry}")
        entry_label.configure(text = f"Your submission: {entry}")

    else:
        print("Submission entry is empty.")
        entry_label.configure(text="Submission entry is empty.",font="consolas")

# setup window
window = tk.Tk()
window.title("Test Title")
#window.geometry('200x150')
window.geometry()

# Create label widget and put it in the window
entry_label = tk.Label(window, text="Enter text")
entry_label.configure(font="consolas")

# methods to put a widget in a window
entry_label.grid(column=2,row=1)
# entry_label.grid()
# entry_label.place()

# create a text entry
text_entry = tk.Entry(window, width=30)
text_entry.configure(border=10)
text_entry.grid(column=2)

# create a button
button = tk.Button(window,text = 'Submit', command=submit)
button.configure(borderwidth=10, font="consolas", bg="Red",fg="Yellow")
button.grid(column=2)

print('Tkinter GUI initialized successfully.')
window.mainloop()

