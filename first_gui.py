import tkinter as tk
import customtkinter as ctk

root = ctk.CTk()

root.geometry("400x400")
root.title('tkinter&customtkinter project')

button = ctk.CTkButton(master=root, corner_radius=10, )
button.place(relx= 0.5, rely=0.5)

root.mainloop()