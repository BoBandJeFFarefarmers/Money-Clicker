import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

count = 0
x = 1

def click():
    global count, x
    count += x
    score.config(text="$"+str(count))

root = customtkinter.CTk()
root.title("Money Clicker")
root.geometry("1000x500")

label = customtkinter.CTkLabel(root, text="Make some money!!!", text_font=("Comic Sans MS", 36))
label.pack()

button = customtkinter.CTkButton(root, text="$$$$$", text_font=("Comic Sans MS", 36), command=click)
button.pack(pady=10)

score = customtkinter.CTkLabel(root, text="$"+"0", text_font=("Comic Sans MS", 50))
score.pack(pady=20)

root.mainloop()