from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import app.convertorlogic
from convertorlogic import convert_images_to_pdf
import subprocess


def images_to_pdf():
    output_filename = ask_output_name.get()
    if images and output_filename:
        output_file = app.convert_images_to_pdf(images)
        if output_file:
            Label(win, text=f"Saved as {output_file}").pack()
            subprocess.Popen([output_file], shell=True)


# UI Module (pdf_ui.py)
win = Tk()
win.geometry('400x550')
win.title("IMG.PDF")
win.attributes('-alpha', 0.90)

images = []  # List to store selected image file paths
image_index = 0  # Index to keep track of the currently displayed

# setting background
#label_back = Label(win, image=background)
#label_back.place(x=0, y=0)


def select_files():
    global images
    images = filedialog.askopenfilenames(initialdir="", title="Select Images", filetypes=(
        ("Image files", "*.jpg *.jpeg *.png *.gif *.bmp *.tiff"), ("All files", "*.*")))
    selected_files_label.config(text="\n".join(images))
    display_image(0)


def display_image(index):
    global image_index
    if 0 <= index < len(images):
        image_index = index
        image_path = images[index]
        img = Image.open(image_path)
        img.thumbnail((400, 400))
        img = ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img
        image_index_label.config(text=f"Image {index + 1}/{len(images)}")


def next_image():
    if images:
        new_index = (image_index + 1) % len(images)
        display_image(new_index)


def previous_image():
    if images:
        new_index = (image_index - 1) % len(images)
        display_image(new_index)


def images_to_pdf():
    output_filename = ask_output_name.get()
    if images and output_filename:
        output_file = convert_images_to_pdf(images, output_filename)
        if output_file:
            Label(win, text=f"Saved as {output_file}").pack()


Label(win, text="Image to PDF Converter", font="Caveat 25 bold").pack(pady=10)




button_select_inactive = Image.open('C:\\Users\\thebo\\PycharmProjects\\imagestopdf\\design\\buttons\\select_images_inactive.png')
button_select_inactive_nohover = ImageTk.PhotoImage(button_select_inactive)

button_select_active = Image.open('C:\\Users\\thebo\\PycharmProjects\\imagestopdf\\design\\buttons\\select_images_active.png')
button_select_active_hover = ImageTk.PhotoImage(button_select_active)

button_select_click = Image.open('C:\\Users\\thebo\\PycharmProjects\\imagestopdf\\design\\buttons\\select_images_click.png')
button_select_onclick = ImageTk.PhotoImage(button_select_click)
button_submit = Button(win, text="Select Images",image=button_select_inactive_nohover, command=select_files, bd=0, relief="sunken")
button_submit.config()
button_submit.pack(ipadx=10)

def on_hover(event):
    button_submit.config(image= button_select_active_hover)
def on_leave(event):
    button_submit.config(image= button_select_inactive_nohover)
def on_click(event):
    # Change the image or perform any action you want on button click
    button_submit.config(image=button_select_onclick)

style = ttk.Style()
style.configure("TButton", relief="sunken")
button_submit.bind("<Enter>", on_hover)
button_submit.bind("<Leave>", on_leave)
button_submit.bind("<Button-1>", on_click)


frame = Frame(win)
frame.pack()





ttk.Button(frame, text="Convert and Save as PDF", command=images_to_pdf).pack(side=LEFT, pady=20, ipadx=10)

ask_output_name = ttk.Entry(win, textvariable=StringVar(value="output.pdf"))
ask_output_name.pack()

selected_files_label = Label(win, text="", wraplength=600)
selected_files_label.pack()

image_label = Label(win)
image_label.pack()
image_index_label = Label(win, text="Image 0/0")
image_index_label.pack()

ttk.Button(frame, text="Previous", command=previous_image).pack(side=LEFT, padx=10)
ttk.Button(frame, text="Next", command=next_image).pack(side=LEFT, padx=10)




win.mainloop()
