from tkinter import *
from tkinter import ttk
import tkinter.messagebox



def doNothing():
    print("ppp")


def showInfo():
    tkinter.messagebox.showinfo("Informacje o programie", "Kalkulator BMI, wersja 1.01.")


def showChangelog():
    tkinter.messagebox.showinfo("Lista zmian", "Wersja 1.01. \n Zmiany: \n wersja 1.0 \n - dodane oznaczenia centyli \n - dodano linie oddzielające centyle")


def bmiCalc():

    try:
        h = float(height.get())
        w = float(weight.get())
        value = w / (h ** 2) * 10000
        bmi_value.set(round(value, 2))
        if various_age.current() == 0 or various_age.current() == 2:
            draw_indicator_0()
        if various_age.current() == 1 or various_age.current() == 3:
            draw_indicator_1()

    except ValueError:
        tkinter.messagebox.showinfo("Błąd", "Wprowadź liczbę.")
        pass


def draw_indicator_0(*args):
    global bmi_indicator
    bmi_value_num = float(bmi_value.get())
    person_age_years_num = int(person_age_years_number.get())
    person_age_months_num = int(person_age_months_number.get())
    person_age_months_and_years = person_age_years_num * 12 + person_age_months_num
    print(bmi_value_num)
    print(person_age_years_num * 12 + person_age_months_num)
    circle_center_x = 25 + person_age_months_and_years * 20
    print(circle_center_x)
    circle_center_y = 375 - ((bmi_value_num - 10) * 25)
    print(circle_center_y)
    imageCanvas.delete(bmi_indicator)
    if bmi_value_num < 24 and bmi_value_num > 10:
        bmi_indicator = imageCanvas.create_oval(circle_center_x - 5, circle_center_y - 5, circle_center_x + 5, circle_center_y + 5, fill="red")


def draw_indicator_1(*args):
    global bmi_indicator
    bmi_value_num = float(bmi_value.get())
    person_age_years_num = int(person_age_years_number.get())
    person_age_months_num = int(person_age_months_number.get())
    person_age_months_and_years = person_age_years_num * 12 + person_age_months_num
    print(bmi_value_num)
    print(person_age_years_num * 12 + person_age_months_num)
    circle_center_x = 25 + (person_age_months_and_years-24) * 80 / 6
    print(circle_center_x)
    circle_center_y = 375 - ((bmi_value_num - 10) * 25)
    print(circle_center_y)
    imageCanvas.delete(bmi_indicator)
    if bmi_value_num < 24 and bmi_value_num > 10:
        bmi_indicator = imageCanvas.create_oval(circle_center_x - 5, circle_center_y - 5, circle_center_x + 5, circle_center_y + 5, fill="red")


def imageChange(*args):
    imageCanvas.delete(ALL)
    if various_age.current() == 0:
        drawing_centyl_grid_0()
        imageCanvas.create_text(400, 10, text="siatka centylowa - bmi od wieku - dziewczynki 0-24 miesięce ")

    if various_age.current() == 1:
        drawing_centyl_grid_1()
        imageCanvas.create_text(400, 10, text="siatka centylowa - bmi od wieku - dziewczynki 2-5 lat ")
    if various_age.current() == 2:
        drawing_centyl_grid_2()
        imageCanvas.create_text(400, 10, text="siatka centylowa - bmi od wieku - chłopcy 0-24 miesięce ")
    if various_age.current() == 3:
       drawing_centyl_grid_3()
       imageCanvas.create_text(400, 10, text="siatka centylowa - bmi od wieku - chłopcy 2-5 lat ")
    drawing_coordinates()
    # print("zmieniam obraz")
    if various_age.current() == 0:
        imageCanvas.create_text(555, 160, text="97")
        imageCanvas.create_text(555, 190, text="85")
        imageCanvas.create_text(555, 215, text="50")
        imageCanvas.create_text(555, 260, text="15")
        imageCanvas.create_text(555, 285, text="3")

    if various_age.current() == 1:
        imageCanvas.create_text(555, 145, text="97")
        imageCanvas.create_text(555, 190, text="85")
        imageCanvas.create_text(555, 220, text="50")
        imageCanvas.create_text(555, 270, text="15")
        imageCanvas.create_text(555, 295, text="3")

    if various_age.current() == 2:
        imageCanvas.create_text(555, 155, text="97")
        imageCanvas.create_text(555, 185, text="85")
        imageCanvas.create_text(555, 215, text="50")
        imageCanvas.create_text(555, 255, text="15")
        imageCanvas.create_text(555, 275, text="3")

    if various_age.current() == 3:
        imageCanvas.create_text(555, 155, text="97")
        imageCanvas.create_text(555, 205, text="85")
        imageCanvas.create_text(555, 230, text="50")
        imageCanvas.create_text(555, 265, text="15")
        imageCanvas.create_text(555, 290, text="3")


def drawing_centyl_grid_0(*args):
    imageCanvas.create_polygon(25, 225, 30, 230, 45, 190, 65, 160, 85, 140, 105, 130, 125, 125, 145, 125, 165, 125, 185, 125, 205, 130, 225, 135, 245, 137, 265, 140, 305, 150, 405,165, 505, 170, 575, 170,
                               575, 25, 25, 25,
                               fill="#ffcccc") #red
    imageCanvas.create_line(25, 225, 30, 230, 45, 190, 65, 160, 85, 140, 105, 130, 125, 125, 145, 125, 165, 125, 185, 125, 205, 130, 225, 135, 245, 137, 265, 140, 305, 150, 405,165, 505, 170, 575, 170,
                            width=6, fill="red")
    imageCanvas.create_polygon(25, 260, 30, 265, 45, 225, 65, 185, 85, 175, 105, 165, 125, 160, 145, 157, 165, 160, 185, 165, 205, 170, 225, 170, 245, 172, 265, 175, 305, 185, 405, 195, 505, 200, 575, 200,
                               575, 170, 505, 170, 405, 165, 305, 150, 265, 140, 245, 137, 225, 135, 205, 130, 185, 125, 165, 125, 145, 125, 125, 125, 105, 130, 85, 140, 65, 160, 45, 190, 30, 230, 25, 225,
                               fill="#ffffb3")  # yellow
    imageCanvas.create_line(25, 260, 30, 265, 45, 225, 65, 185, 85, 175, 105, 165, 125, 160, 145, 157, 165, 160, 185, 165, 205, 170, 225, 170, 245, 172, 265, 175, 305, 185, 405, 195, 505, 200, 575, 200,
                            width=5, fill="yellow")
    imageCanvas.create_polygon(25, 325, 30, 330, 45, 290, 65, 267, 85, 255, 105, 250, 125, 242, 145, 238, 165, 237, 185, 238, 205, 242, 225, 245, 245, 248, 265, 250, 305, 260, 405, 265, 505, 268, 575, 270,
                               575, 200, 505, 200, 405, 195, 305, 185, 265, 175, 245, 172, 225, 170, 205, 170, 185, 165, 165, 160, 145, 157, 125, 160, 105, 165, 85, 175, 65, 185, 45, 225, 30, 265, 25, 260,
                               fill="#99ff99") #green
    imageCanvas.create_line(25, 297, 30, 297, 45, 257, 65, 226, 85, 215, 105, 207, 125, 201, 145, 197, 165, 198, 185, 201, 205, 206, 225, 207, 245, 210, 265, 212, 305, 222, 405, 230, 505, 234, 575, 235,
                            width=3, fill="green")
    imageCanvas.create_polygon(25, 340, 30, 350, 45, 325, 65, 295, 85, 285, 105, 275, 125, 270, 145, 265, 165, 267, 185, 269, 205, 272, 225, 272, 245, 275, 265, 278, 305, 282, 405, 285, 505, 290, 575, 293,
                               575, 270, 505, 268, 405, 265, 305, 260, 265, 250, 245, 248, 225, 245, 205, 242, 185, 238, 165, 237, 145, 238, 125, 242, 105, 250, 85, 255, 65, 267, 45, 290, 30, 330,25, 325,
                               fill="#ffffb3")  # yellow
    imageCanvas.create_line(25, 325, 30, 330, 45, 290, 65, 267, 85, 255, 105, 250, 125, 242, 145, 238, 165, 237, 185, 238, 205, 242, 225, 245, 245, 248, 265, 250, 305, 260, 405, 265, 505, 268, 575, 270,
                            width=3, fill="yellow")
    imageCanvas.create_polygon(25, 340, 30, 350, 45, 325, 65, 295, 85, 285, 105, 275, 125, 270, 145, 265, 165, 267, 185, 269, 205, 272, 225, 272, 245, 275, 265, 278, 305, 282, 405, 285, 505, 290, 575, 293,
                               575, 375, 25, 375,
                               fill="#ffcccc") #red
    imageCanvas.create_line(25, 340, 30, 350, 45, 325, 65, 295, 85, 285, 105, 275, 125, 270, 145, 265, 165, 267, 185, 269, 205, 272, 225, 272, 245, 275, 265, 278, 305, 282, 405, 285, 505, 290, 575, 293,
                            width=3, fill="red")  #red )


def drawing_centyl_grid_2(*args):
    imageCanvas.create_polygon(25, 225, 30, 230, 45, 200, 65, 145, 85, 135, 105, 120, 125, 117, 145, 115, 165, 117, 185, 120, 205, 125, 225, 130, 245, 132, 265, 135, 305, 140, 405, 160, 505, 165, 575, 165,
                               575, 25, 25, 25,
                               fill="#ffcccc") #red
    imageCanvas.create_line(25, 225, 30, 230, 45, 200, 65, 145, 85, 135, 105, 120, 125, 117, 145, 115, 165, 117, 185, 120, 205, 125, 225, 130, 245, 132, 265, 135, 305, 140, 405, 160, 505, 165, 575, 165,
                               width=6, fill="red")
    imageCanvas.create_polygon(25, 260, 30, 265, 45, 220, 65, 178, 85, 165, 105, 160, 125, 155, 145, 153, 165, 155, 185, 158, 205, 160, 225, 165, 245, 167, 265, 170, 305, 175, 405, 185, 505, 195, 575, 195,
                               575, 165, 505, 165, 405, 160, 305, 140, 265, 135, 245, 132, 225, 130, 205, 125, 185, 120, 165, 117, 145, 115, 125, 117, 105, 120, 85, 135, 65, 145, 45, 200, 30, 230, 25, 225,
                               fill="#ffffb3")  # yellow
    imageCanvas.create_line(25, 260, 30, 265, 45, 220, 65, 178, 85, 165, 105, 160, 125, 155, 145, 153, 165, 155, 185, 158, 205, 160, 225, 165, 245, 167, 265, 170, 305, 175, 405, 185, 505, 195, 575, 195,
                            width=6, fill="yellow")
    imageCanvas.create_polygon(25, 325, 30, 330, 45, 300, 65, 250, 85, 235, 105, 228, 125, 226, 145, 225, 165, 226, 185, 228, 205, 230, 225, 232, 245, 235, 265, 238, 305, 240, 405, 253, 505, 260, 575, 262,
                               575, 195, 505, 195, 405, 185, 305, 175, 265, 170, 245, 167, 225, 165, 205, 160, 185, 158, 165, 155, 145, 153, 125, 155, 105, 160, 85, 165, 65, 178, 45, 220, 30, 265, 25, 260,
                               fill="#99ff99") #green
    imageCanvas.create_line(25, 292, 30, 297, 45, 260, 65, 214, 85, 200, 105, 195, 125, 190, 145, 189, 165, 190, 185, 193, 205, 195, 225, 198, 245, 201, 265, 204, 305, 207, 405, 219, 505, 227, 575, 228,
                            width=3, fill="green")
    imageCanvas.create_polygon(25, 345, 30, 353, 45, 310, 65, 280, 85, 265, 105, 260, 125, 254, 145, 252, 165, 254, 185, 258, 205, 260, 225, 262, 245, 264, 265, 267, 305, 265, 405, 278, 505, 280, 575, 282,
                               575, 262, 505, 260, 405, 253, 305, 240, 265, 238, 245, 235, 225, 232, 205, 230, 185, 228, 165, 226, 145, 225, 125, 226, 105, 228, 85, 235, 65, 250, 45, 300, 30, 330, 25, 325,
                               fill="#ffffb3")  # yellow
    imageCanvas.create_line(25, 325, 30, 330, 45, 300, 65, 250, 85, 235, 105, 228, 125, 226, 145, 225, 165, 226, 185, 228, 205, 230, 225, 232, 245, 235, 265, 238, 305, 240, 405, 253, 505, 260, 575, 262,
                            width=3, fill="yellow")
    imageCanvas.create_polygon(25, 345, 30, 353, 45, 310, 65, 280, 85, 265, 105, 260, 125, 254, 145, 252, 165, 254, 185, 258, 205, 260, 225, 262, 245, 264, 265, 267, 305, 265, 405, 278, 505, 280, 575, 282,
                               575, 375, 25, 375,
                               fill="#ffcccc") #red
    imageCanvas.create_line(25, 345, 30, 353, 45, 310, 65, 280, 85, 265, 105, 260, 125, 254, 145, 252, 165, 254, 185, 258, 205, 260, 225, 262, 245, 264, 265, 267, 305, 265, 405, 278, 505, 280, 575, 282,
                            width=3, fill="red")


def drawing_centyl_grid_1(*args):
    imageCanvas.create_polygon(25, 162, 105, 165, 185, 170, 265, 165, 345, 165, 425, 163, 505, 162, 575, 160,
                               575, 25, 25, 25,
                               fill="#ffcccc") #red
    imageCanvas.create_line(25, 162, 105, 165, 185, 170, 265, 165, 345, 165, 425, 163, 505, 162, 575, 160,
                            width=6, fill="red")
    imageCanvas.create_polygon(25, 195, 105, 203, 185, 205, 265, 208, 345, 205, 425, 203, 505, 200, 575, 197,
                               575, 160, 505, 162, 425, 163, 345, 165, 265, 165, 185, 170, 105, 165,25, 162,
                               fill="#ffffb3")  # yellow
    imageCanvas.create_line(25, 195, 105, 203, 185, 205, 265, 208, 345, 205, 425, 203, 505, 200, 575, 197,
                            width=5, fill="yellow")
    imageCanvas.create_polygon(25, 265, 105, 270, 185, 272, 265, 275, 345, 277, 425, 279, 505, 282, 575, 284,
                               575, 197, 505, 200, 425, 203, 345, 205, 265, 208, 185, 205, 105, 203, 25, 195,
                               fill="#99ff99") #green
    imageCanvas.create_line(25, 230, 105, 235, 185, 238, 265, 241, 345, 241, 425, 242, 505, 241, 575, 241,
                            width=3, fill="green")
    imageCanvas.create_polygon(25, 285, 105, 290, 185, 292, 265, 296, 345, 300, 425, 304, 505, 308, 575, 310,
                               575, 284, 505, 282, 425, 279, 345, 277, 265, 275, 185, 272, 105, 270, 25, 265,
                                fill="#ffffb3")  # yellow
    imageCanvas.create_line(25, 265, 105, 270, 185, 272, 265, 275, 345, 277, 425, 279, 505, 282, 575, 284,
                            width=4, fill="yellow")
    imageCanvas.create_polygon(25, 285, 105, 290, 185, 292, 265, 296, 345, 300, 425, 304, 505, 308, 575, 310,
                               575, 375, 25, 375,
                                fill="#ffcccc") #red
    imageCanvas.create_line(25, 285, 105, 290, 185, 292, 265, 296, 345, 300, 425, 304, 505, 308, 575, 310,
                            width=3, fill="red")


def drawing_centyl_grid_3(*args):
    imageCanvas.create_polygon(25, 160, 105, 165, 185, 170, 265, 175, 345, 170, 425, 168, 505, 167, 575, 166,
                               575, 25, 25, 25,
                               fill="#ffcccc") #red
    imageCanvas.create_line(25, 160, 105, 165, 185, 170, 265, 175, 345, 170, 425, 168, 505, 167, 575, 166,
                               width=6, fill="red")
    imageCanvas.create_polygon(25, 190, 105, 196, 185, 200, 265, 205, 345, 208, 425, 210, 505, 212, 575, 213,
                               575, 166, 505, 167, 425, 168, 345, 170, 265, 175, 185, 170, 105, 165, 25, 160,
                               fill="#ffffb3")  # yellow
    imageCanvas.create_line(25, 190, 105, 196, 185, 200, 265, 205, 345, 208, 425, 210, 505, 212, 575, 213,
                               width=6, fill="yellow")
    imageCanvas.create_polygon(25, 260, 105, 263, 185, 265, 265, 270, 345, 272, 425, 275, 505, 277, 575, 279,
                               575, 213, 505, 212, 425, 210, 345, 208, 265, 205, 185, 200, 105, 196, 25, 190,
                               fill="#99ff99") #green
    imageCanvas.create_line(25, 225, 105, 229, 185, 233, 265, 235, 345, 240, 425, 242, 505, 245, 575, 246,
                            width=3, fill="green")
    imageCanvas.create_polygon(25, 276, 105, 280, 185, 287, 265, 292, 345, 295, 425, 297, 505, 300, 575, 305,
                               575, 279, 505, 277, 425, 275, 345, 272, 265, 270, 185, 265, 105, 263, 25, 260,
                                fill="#ffffb3")  # yellow
    imageCanvas.create_line(25, 260, 105, 263, 185, 265, 265, 270, 345, 272, 425, 275, 505, 277, 575, 279,
                               width=4, fill="yellow")
    imageCanvas.create_polygon(25, 276, 105, 280, 185, 287, 265, 292, 345, 295, 425, 297, 505, 300, 575, 305,
                               575, 375, 25, 375,
                                fill="#ffcccc") #red
    imageCanvas.create_line(25, 276, 105, 280, 185, 287, 265, 292, 345, 295, 425, 297, 505, 300, 575, 305,
                               width=3, fill="red")


def drawing_coordinates(*args):

    # ------// Drawing coordinate system //------- #
    if various_age.current() == 0 or various_age.current() == 2:
        k = 0
        delta_k = 1
        step = 20
    if various_age.current() == 1 or various_age.current() == 3:
        k = 2
        delta_k = 0.5
        step = 80

    for i in range(0, 551, step):
        imageCanvas.create_text(i+25, 385, text="%s" % (k))
        k += delta_k
        imageCanvas.create_line(i+25, 25, i+25, 375, fill="#9d9f9e")

    k=10
    for i in range(0, 351, 25):
        imageCanvas.create_text(15, 375-i, text="%s" % (k))
        k +=1
        imageCanvas.create_line(25, i+25, 575, i+25, fill="#9d9f9e")

    imageCanvas.create_rectangle(25, 25, 575, 375, outline="black")
    imageCanvas.create_text(15, 10, text="bmi")
    imageCanvas.create_text(560, 395, text="wiek")




root = Tk()
root.title("Kalkulator BMI - Body Mass Index")
root.iconbitmap('ikonka.ico')
# ------// Menu //------- #
top_menu_bar = Menu(root) #top menu bar will be display on root window
root.config(menu=top_menu_bar)

file_top_menu_bar = Menu(top_menu_bar)
top_menu_bar.add_cascade(label="Plik", menu=file_top_menu_bar)
file_top_menu_bar.add_separator()
file_top_menu_bar.add_command(label="Zakończ program", command = top_menu_bar.quit)

diff_top_mentu_bar = Menu(top_menu_bar)
top_menu_bar.add_cascade(label="Inne", menu = diff_top_mentu_bar)
diff_top_mentu_bar.add_separator()
diff_top_mentu_bar.add_command(label="Zmiany", command=showChangelog)
diff_top_mentu_bar.add_separator()
diff_top_mentu_bar.add_command(label="Informacje o programie", command=showInfo)

# ------// Wigets //------- #
wigets_frame = Frame(root)
person_weight = Label(wigets_frame, text="Waga:  ")
person_height = Label(wigets_frame, text="Wzrost:  ")
person_age = Label(wigets_frame, text="Wiek:  ")
person_weight_val = Label(wigets_frame, text="[kg]")
person_height_val = Label(wigets_frame, text="[cm]")
person_age_years = Label(wigets_frame, text="[lata]")
person_age_months = Label(wigets_frame, text="[miesiące]")
person_weight.grid(row=1, column=1, sticky=E)
person_height.grid(row=2, column=1, sticky=E)
person_age.grid(row=3, column=1, sticky=E)
person_weight_val.grid(row=1, column=3, sticky=W)
person_height_val.grid(row=2, column=3, sticky=W)
person_age_years.grid(row=3, column=3, sticky=W)
person_age_months.grid(row=4, column=3, sticky=W)

weight = StringVar()
age_years = StringVar()
age_months = StringVar()
height = StringVar()
bmi_value = StringVar()
# default values
weight.set(70)
age_years.set(0)
age_months.set(11)
height.set(182)
bmi_value.set(25.06)

bmi_label = Label(wigets_frame, textvariable=bmi_value, font=("bold", 26))
bmi_label.grid(row=1, column=4, rowspan=2, sticky=(W, E))

bmi_label2 = Label(wigets_frame, text="BMI", font=("bold", 16), fg="#423f3e", width=15)
bmi_label2.grid(row=3, column=4, sticky=(W, E))

person_weight_number = Entry(wigets_frame, width=15, textvariable = weight)
person_height_number = Entry(wigets_frame, width=15, textvariable = height)
person_age_years_number = Entry(wigets_frame, width=15, textvariable = age_years)
person_age_months_number = Entry(wigets_frame, width=15, textvariable = age_months)
person_weight_number.grid(row=1, column=2, sticky=W)
person_height_number.grid(row=2, column=2, sticky=W)
person_age_years_number.grid(row=3, column=2, sticky=W)
person_age_months_number.grid(row=4, column=2, sticky=W)

calculate_bmi = Button(wigets_frame, text="Oblicz BMI", font=("bold", 20), bg="green", fg="white", command=bmiCalc)
calculate_bmi.grid(row=1, column=5, rowspan=4, columnspan=3, sticky=W)

various_age_variable = StringVar()
various_age = ttk.Combobox(wigets_frame, textvariable=various_age_variable, state='readonly')
various_age['values'] = ('dziewczynki 0-24 ms', 'dziewczynki 2-5 lat', 'chłopcy 0-24 ms', 'chłopcy 2-5 lat')
various_age.bind('<<ComboboxSelected>>', imageChange)
various_age.current(0)
various_age.grid(row=5, column=1, columnspan=2, sticky=E)

wigets_frame.grid(row=0, column=0, sticky=W)

# ------// Images //------- #
print(various_age.current())
imageFrame = Frame(root, bg="purple")


imageCanvas = Canvas(imageFrame, width=600, height=400, bg="white")
drawing_centyl_grid_0()
imageCanvas.create_text(400, 10, text="siatka centylowa - bmi od wieku - dziewczynki 0-24 miesięce ")
#drawing_coordinates()
imageChange()
bmi_indicator = imageCanvas.create_oval(50000, 5000, 5000, 5000, fill="red")

imageCanvas.grid(row=0, column=0)
imageFrame.grid(row=1, column=0)






# ------// Status bar //------- #
staturBarFrame = Frame(root)
statusBar = Label(staturBarFrame, text="WYKONANO DLA WIOLETTY SIELSKIEJ",font=("bold",10), bd=5, anchor=W, relief=RIDGE)
statusBar.grid(row=0, column=0, sticky=(W, E))
staturBarFrame.grid(row=2, column=0, columnspan=4, sticky=(W, E))



root.mainloop()

