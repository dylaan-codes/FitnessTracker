# This GUI layout was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
# GUI design and code by Dylan Nguyen
from FitnessTracker.my_functions import *
from FitnessTracker.my_validations import *
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/frame2")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

reps_window = Tk()

reps_window.geometry("800x600")
reps_window.title("max_rep form")
reps_window.configure(bg="#FFFFFF")
vcmd = get_vcmd(reps_window)

canvas = Canvas(
    reps_window,
    bg = "#FFFFFF",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    400.0,
    0.0,
    800.0,
    600.0,
    fill="#395271",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    200.0,
    300.0,
    image=image_image_1
)

canvas.create_text(
    432.0,
    11.0,
    anchor="nw",
    text="Max Reps Input \nForm",
    fill="#FFFFFF",
    font=("Inter Bold", 36 * -1)
)

canvas.create_text(
    432.0,
    107.0,
    anchor="nw",
    text="Week",
    fill="#FFFFFF",
    font=("Inter Medium", 20 * -1)
)

canvas.create_text(
    624.0,
    107.0,
    anchor="nw",
    text="Date ",
    fill="#FFFFFF",
    font=("Inter Medium", 20 * -1)
)

canvas.create_text(
    610.0,
    188.0,
    anchor="nw",
    text="Pushups",
    fill="#FFFFFF",
    font=("Inter Medium", 20 * -1)
)

canvas.create_text(
    432.0,
    192.0,
    anchor="nw",
    text="Pullups",
    fill="#FFFFFF",
    font=("Inter Medium", 20 * -1)
)

canvas.create_text(
    432.0,
    275.0,
    anchor="nw",
    text="Dips",
    fill="#FFFFFF",
    font=("Inter Medium", 20 * -1)
)

canvas.create_text(
    610.0,
    279.0,
    anchor="nw",
    text="Squats",
    fill="#FFFFFF",
    font=("Inter Medium", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    684.0,
    319.0,
    image=entry_image_1
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    506.0,
    319.0,
    image=entry_image_2
)



entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    506.0,
    232.0,
    image=entry_image_3
)



entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    684.0,
    232.0,
    image=entry_image_4
)


entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    682.0,
    152.0,
    image=entry_image_5
)




entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    491.5,
    152.0,
    image=entry_image_6
)




entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    464.5,
    407.0,
    image=entry_image_7
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    569.5,
    407.0,
    image=entry_image_8
)


canvas.create_text(
    432.0,
    363.0,
    anchor="nw",
    text="Plank Hold [min+s]",
    fill="#FFFFFF",
    font=("Inter Medium", 20 * -1)
)
week_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
date_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
pullups_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
pushups_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
dips_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
squats_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
plank_min_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
plank_sec_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
max_rep_submit_button = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print("max_rep submit clicked"), get_data()],
    relief="flat"
)

def get_data():
    if validate_empty(pushups_entry.get(), pullups_entry.get(), dips_entry.get(), squats_entry.get(), plank_min_entry.get(), plank_sec_entry.get()) == 1:
        messagebox.showerror("Error", "No Null Values,\nplease and thank you!")
    else:
        response = messagebox.askyesno("Confirm", f'Pullups: {pullups_entry.get()} | Pushups: {pushups_entry.get()}'
                                                  f'\nDips: {dips_entry.get()} | Squats: {squats_entry.get()} '
                                                  f'\nPlank: {plank_min_entry.get()}m {plank_sec_entry.get()}s, '
                                                  f'Correct?')
        if response:  # If user clicks "Yes"
            print(f'{date_entry.get()} | {week_entry.get()} | pullups: {pullups_entry.get()} | pushups: {pushups_entry.get()}')
            print(f'\tdips: {dips_entry.get()} |  squats: {squats_entry.get()} | plank: {plank_min_entry.get()}m {plank_sec_entry.get()}s')
            max_reps(pullups_entry.get(), pushups_entry.get(), dips_entry.get(), squats_entry.get(), plank_min_entry.get(), plank_sec_entry.get())
            messagebox.showinfo("Success", "Bidding accomplished!")
            reps_window.destroy()

        else:  # If user clicks "No"
            print(f'aborted')
            messagebox.showinfo("Cancelled", "Action cancelled!")


# Validation
pushups_entry.config(validate="key", validatecommand=vcmd["int"])
pullups_entry.config(validate="key", validatecommand=vcmd["int"])
dips_entry.config(validate="key", validatecommand=vcmd["int"])
squats_entry.config(validate="key", validatecommand=vcmd["int"])
plank_min_entry.config(validate="key", validatecommand=vcmd["int"])
plank_sec_entry.config(validate="key", validatecommand=vcmd["int"])

# Place all widgets at the bottom
week_entry.place(x=432.0, y=138.0, width=119.0, height=26.0)
date_entry.place(x=624.0, y=138.0, width=116.0, height=26.0)
pullups_entry.place(x=432.0, y=217.0, width=148.0, height=28.0)
pushups_entry.place(x=610.0, y=217.0, width=148.0, height=28.0)
dips_entry.place(x=432.0, y=304.0, width=148.0, height=28.0)
squats_entry.place(x=610.0, y=304.0, width=148.0, height=28.0)
plank_min_entry.place(x=432.0, y=391.0, width=65.0, height=30.0)
plank_sec_entry.place(x=515.0, y=391.0, width=109.0, height=30.0)
max_rep_submit_button.place(x=474.0, y=470.0, width=240.0, height=80.0)

week_entry.delete(0, "end")
week_entry.insert(0, weeks_since(START_DATE))
week_entry.config(state="readonly")

date_entry.delete(0, "end")
date_entry.insert(0, todays_date())
date_entry.config(state="readonly")

#max_rep_submit_button.config(command=get_data)


reps_window.resizable(False, False)
reps_window.mainloop()
