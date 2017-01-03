from tkinter import *
root = Tk()
def drawcircle(canv,x,y,rad):
    canv.create_oval(x-rad,y-rad,x+rad,y+rad,width=0,fill='blue')
canvas = Canvas(width=600, height=200, bg='white')
canvas.pack(expand=YES, fill=BOTH)
text = canvas.create_text(50,10, text="tk test")
#i'd like to recalculate these coordinates every frame
circ1=drawcircle(canvas,100,100,20)
circ2=drawcircle(canvas,500,100,20)
root.mainloop()