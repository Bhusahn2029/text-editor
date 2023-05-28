import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    if file_path:
        with open(file_path, 'r') as file:
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=[('Text Files', '*.txt')])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_box.get(1.0, tk.END))

root = tk.Tk()
root.title("Text Editor")

text_box = tk.Text(root)
text_box.pack(fill=tk.BOTH, expand=True)

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()
