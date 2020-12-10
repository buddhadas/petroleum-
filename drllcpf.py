import tkinter as tk
window = tk.Tk()
window.title("DRILLING COST PER FOOT CALCULATOR ~ Buddha_Das")
window.geometry("650x380")

#=========DISPLAY==========

def calculation():

    t= float(entry1.get())
    bit_cost=float(entry2.get())
    CR_rigcost= float(entry3.get())
    T_roundtrip=float(entry4.get())
    fperbit= float(entry5.get())

    aaa = t + T_roundtrip
    ct= ( bit_cost + CR_rigcost * aaa )/fperbit

    # display

    titled=tk.Label(text="COST PER FOOT IN $ IS :" )
    titled.grid(column=1, row=10)

    qdisplay=tk.Text(master=window, height=1, width=10)
    qdisplay.grid(column=2, row=10)
    qdisplay.insert(tk.END, ct)

# ==========LABEL==========

title =tk.Label(text="SIMPLE DRILLING COST\n PER FOOT CALCULATOR \n  ", font=("Times New Roman", 18) )
title.grid(column=0,row=0)

 #===========
title1= tk.Label(text=" t  : enter_here>>",font=("Times New Roman", 16))
title1.grid(column=0, row=2)

title2= tk.Label(text="B  : enter_here>>",font=("Times New Roman", 16))
title2.grid(column=0, row=3)

title3= tk.Label(text=" CR : enter_here>>", font=("Times New Roman",16))
title3.grid(column=0, row=4)

title4= tk.Label(text=" T  : enter_here>>",font=("Times New Roman", 16))
title4.grid(column=0, row=5)

title5= tk.Label(text=" F  : enter_here>>",font=("Times New Roman", 16))
title5.grid(column=0, row=6)

#third row

title1= tk.Label(text="drilling time in hours ",font=("Times New Roman", 16))
title1.grid(column=2, row=2)

title2= tk.Label(text="bit cost in $ ",font=("Times New Roman", 16))
title2.grid(column=2, row=3)

title3= tk.Label(text=" rig cost in $ per hr ", font=("Times New Roman",16))
title3.grid(column=2, row=4)

title4= tk.Label(text="round trip time in hours  ",font=("Times New Roman", 16))
title4.grid(column=2, row=5)

title5= tk.Label(text="footage per bit in ft",font=("Times New Roman", 16))
title5.grid(column=2, row=6)

#======ENTRY FIELD========

entry1 = tk.Entry()
entry1.grid(column=1, row=2)

entry2 = tk.Entry()
entry2.grid(column=1, row=3)

entry3 = tk.Entry()
entry3.grid(column=1, row=4)

entry4 = tk.Entry()
entry4.grid(column=1, row=5)

entry5 = tk.Entry()
entry5.grid(column=1, row=6)

#=========BUTTON============

button1= tk.Button(text="CLICK FOR COST \nPER FOOT !",bg="red", fg="white", font=("Times New Roman", 15), command=calculation)
button1.grid(column=0,row=9)


window.mainloop()
