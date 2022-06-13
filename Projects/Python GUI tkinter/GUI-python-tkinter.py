from tkinter import *
from tkinter import * # for GUI
from PIL import ImageTk, Image
from tkinter import messagebox

def handle_login():
    email = email_input.get()
    pwd = password_input.get()

    if email == 'phapha' and pwd == 'phauna':
        messagebox.showinfo('YIT','Welcome phaha')
    else:
        messagebox.showerror('Error', 'Not a phapha')

root = Tk()

# GUI title
root.title('Login Form') 

# GUI icon
root.iconbitmap(r'C:\Personal Project Work\Beginner-Python-Projects\Projects\Python GUI tkinter\src\Data.ico')

# minimum GUI size (restrict size not less than)
# root.minsize(400,400)

# max GUI size (restrict size not more than)
# root.maxsize(600,600)

# setting up a particular size setting
root.geometry('350x500')

# GUI backgroud colour
root.configure(background='#0096DC')

# open the image
img = Image.open(r'C:\Personal Project Work\Beginner-Python-Projects\Projects\Python GUI tkinter\src\flipkart-logo.png')
# resize the image
resized_img = img.resize((70,70))
# fit the resized image to make it final img
final_img = ImageTk.PhotoImage(resized_img)

img_label = Label(root, image=final_img)
img_label.pack(pady=(10,10))

# display 'Flipkart' text (with colouwr of text(foreground) as white, background same as blue)
text_label = Label(root, text='Flipkart',foreground='white',background='#0096DC')
text_label.config(font=('Verdana',25))
text_label.pack()


# email label
email_label = Label(root, text='Enter Email',foreground='white',background='#0096DC')
email_label.pack(pady=(20,5))
text_label.config(font=('Verdana',11))

# email input
email_input = Entry(root, width=50)
email_input.pack(ipady=6,pady=(1,15))

# password label
password_label = Label(root, text='Enter Password',foreground='white',background='#0096DC')
password_label.pack(pady=(20,5))
password_label.config(font=('Verdana',11))

# password input
password_input = Entry(root, width=50)
password_input.pack(ipady=6,pady=(1,15))

# login button
login_btn = Button(root, text='Login Here', bg='white', fg='black', width=10, height=2, command=handle_login)
login_btn.config(font=('verdana',14))
login_btn.pack(pady=(10,20))


root.mainloop()
