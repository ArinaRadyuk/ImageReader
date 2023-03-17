from tkinter import filedialog
import PIL.Image
from tkinter import *
from tkinter import ttk
import os


def process_image(filename):
    with PIL.Image.open(filename) as image:
        width, height = image.size
        color_depth = image.mode
        resolution = image.info.get("dpi")
        compression = image.info.get("compression")
        image_format = image.format
    tree.insert('', 'end', values=(width, height, color_depth, resolution, compression, image_format))


def file_action():
    filename = filedialog.asksaveasfilename()
    process_image(filename)


def folder_action():
    custom_dir = filedialog.askdirectory()
    for path in os.listdir(custom_dir):
        filename = os.path.join(custom_dir, path)
        if os.path.isfile(filename):
            process_image(filename)


if __name__ == "__main__":
    win = Tk()

    # Set the size of the tkinter window
    win.geometry("1500x700")
    s = ttk.Style()
    s.theme_use('clam')

    # Add a Treeview widget
    tree = ttk.Treeview(win, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings', height=30)

    verscrlbar = ttk.Scrollbar(win,
                               orient="vertical",
                               command=tree.yview)

    # Calling pack method w.r.to vertical
    # scrollbar
    verscrlbar.pack(side='right', fill='x')

    # Configuring treeview
    tree.configure(xscrollcommand=verscrlbar.set)

    tree.column("# 1", anchor=CENTER,  width=250)
    tree.heading("# 1", text="Width")
    tree.column("# 2", anchor=CENTER,  width=250)
    tree.heading("# 2", text="Height")
    tree.column("# 3", anchor=CENTER,  width=250)
    tree.heading("# 3", text="Color mode")
    tree.column("# 4", anchor=CENTER, width=250)
    tree.heading("# 4", text="Resolution")
    tree.column("# 5", anchor=CENTER,  width=250)
    tree.heading("# 5", text="Compression")
    tree.column("# 6", anchor=CENTER,  width=250)
    tree.heading("# 6", text="Format")

    tree.pack()

    btn_file = Button(win, text="File", command=lambda: file_action(), width=30)
    btn_folder = Button(win, text="Folder", command=lambda: folder_action(), width=30)
    btn_file.place(x=200, y=650)
    btn_folder.place(x=1000, y=650)
    win.mainloop()






