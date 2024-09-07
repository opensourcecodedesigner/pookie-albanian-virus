import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def install():
    # Show a pop-up alert with a fake downloading animation
    downloading_root = tk.Toplevel(root)
    downloading_label = tk.Label(downloading_root, text="Downloading...")
    downloading_label.pack()
    progress_bar = ttk.Progressbar(downloading_root, orient="horizontal", length=200, mode="determinate")
    progress_bar.pack()
    downloading_root.deiconify()  # Show the window
    downloading_root.geometry("250x100+300+200")  # Set the window size and position
    for i in range(101):
        progress_bar['value'] = i
        downloading_root.update_idletasks()  # Update the GUI
        downloading_root.update()  # Update the GUI again
        downloading_root.after(50)  # simulate a 50ms delay
    messagebox.showinfo("Thank you!", "Thank you, you're too kind for leting me to install virus!")
    downloading_root.destroy()

def dont_install():
    # Show a pop-up alert asking the user to install
    messagebox.showinfo("Please Install", "Please install the virus i don't have the the automatically installing feature please be kind and install")

def cancel():
    # Close the alert box
    root.destroy()

root = tk.Tk()
root.title("Your dangerours pookie Albanian Virus")
root.geometry("400x106")

label = tk.Label(root, text="Hi, I am an Albanian virus but because of poor technology in my country unfortunately I am not able to harm your computer my self. Please be so kind to install one of our important virus files yourself and then ur data will be forwarded me and to other users. Many thanks for your cooperation! Best regards, Albanian virus", wraplength=400)
label.pack()

button_frame = tk.Frame(root)
button_frame.pack()

install_button = tk.Button(button_frame, text="Install", command=install)
install_button.pack(side=tk.LEFT)

dont_install_button = tk.Button(button_frame, text="Don't Install", command=dont_install)
dont_install_button.pack(side=tk.LEFT)

cancel_button = tk.Button(button_frame, text="Cancel", command=cancel)
cancel_button.pack(side=tk.LEFT)

root.mainloop()