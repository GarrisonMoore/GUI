import tkinter as tk


def submit():
    """
    This is called when submit button is pressed
    """
    print("Submission button pressed.")
    entry = text_entry.get()
    if entry:
        print(f"The contents of entry box are: {entry}")
        result_label.configure(text = f"Your submission: {entry}")
    else:
        print("Submission entry is empty.")
        result_label.configure(text="Submission entry is empty.")


# setup window
window = tk.Tk()
window.title("Test Title")
window.geometry('500x600')

# Create label widget and put it in the window
entry_label = tk.Label(window, text="Enter text")

# methods to put a widget in a window
entry_label.pack()
# entry_label.grid()
# entry_label.place()

# create a text entry
text_entry = tk.Entry(window, width=20)
text_entry.pack()

# create a button
button = tk.Button(window,text = 'Submit', command=submit)
button.pack()

result_label = tk.Label(window)
result_label.pack()

sd_image = tk.PhotoImage(file = "eagle.jpg")

image_label = tk.Label(window, image=sd_image)
image_label.place(relx=.5, rely=.5,anchor='center')

print('Tkinter GUI initialized successfully.')
window.mainloop()

