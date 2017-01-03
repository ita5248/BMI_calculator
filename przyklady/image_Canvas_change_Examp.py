from tkinter import *

def stuff(event):
    global picture3
    picture3 = PhotoImage(file='image1.png')
    c.itemconfigure(picture2, image = picture3)

main = Tk()
c = Canvas(main, width=300, height=300)
c.pack()

picture = PhotoImage(file='image2.png')
picture2 = c.create_image(150,150,image=picture)

c.bind("<Button-1>", stuff)

main.mainloop()