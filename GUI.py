from tkinter import*
from main import action
from commandList import CommandsList
from PIL import ImageTk, Image

root = Tk()  #CLASS
root.title("AI Assistant")
root.geometry("800x650")
root.resizable(False, False)
root.config(bg="grey")
#6F8FAF


#frame
frame = LabelFrame(root, padx=100, pady=7, borderwidth=5, relief="raised")
frame.config(bg="sky blue")
frame.grid(row=100, column=1, padx=200, pady=10)

#text lable

text_label = Label(frame, text="AI Assistant", font=("comic Sans ms", 15, "bold"))
text_label.grid(padx=20, pady=10)


# Add a text button1

mic_img=Image.open("Mic.png")
mic_img=mic_img.resize((500,500))
mic_img=ImageTk.PhotoImage(mic_img)

button1 = Button(root, image=mic_img, bg="#356696",  borderwidth=3, relief=SOLID, command=action)
button1.place(x=350, y=200)

myMenu = Menu(root)
m1 = Menu(myMenu, tearoff=0)  # tearoff=0 means the submenu can't be teared of from the window
m1.add_command(label='Commands List', command=CommandsList)
m1.add_command(label='Cut')
m1.add_command(label='Copy')
m1.add_command(label='Paste')
m1.add_command(label='Select All')
myMenu.add_cascade(label="Help", menu=m1)

root.config(menu=myMenu)
root.mainloop()