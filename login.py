import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
t = tk.Tk()
t.title(" Login system")

t.geometry("600x600")
t.configure(background="#040D5A")


#func aaction
def action():
    username = user_var.get()
    password = pass_var.get()
    import csv
    with open('ids.csv', 'a', newline='') as f:
        found = 0
        yes = 0
        w = csv.DictWriter(f, fieldnames = ['id', 'password'])
        w.writerow({'id': username,
                    'password': password})

# main projects starts
ttk.Label(t, text="Login System",font="serif 20", background="#040D5A", foreground="#F9E900").pack(pady=30)

#username
userlab = ttk.Label(t, text="Enter Username",font="serif 12", background="#040D5A", foreground="#ffffff").pack(pady=30)
user_var = tk.StringVar()
user = ttk.Entry(t, width=30, textvariable = user_var).pack(pady=10)


#password
passlab = ttk.Label(t, text="Enter Password",font="serif 12", background="#040D5A", foreground="#ffffff").pack(pady=30)

pass_var = tk.StringVar()
passw = ttk.Entry(t, width=30, textvariable = pass_var).pack(pady=10)

#button
ttk.Button(t, text="Submit",command=action).pack(pady=20)

t.mainloop()
