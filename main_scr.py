import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk, filedialog, messagebox
import funcs
import pickle, os.path, shutil
from distutils.dir_util import copy_tree
from os import path

class App:

    def __init__(self, root):
        #setting title
        root.title("Backup To USB")
        #setting window size

        global drives
        drives = funcs.get_drives()

        global my_list
        if path.exists('fpaths'):
            my_list = list(funcs.load_data('fpaths'))
        else:
            funcs.store_data([], 'fpaths')
            my_list = []

        width=409
        height=492
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        usb_lbl = tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        usb_lbl["font"] = ft
        usb_lbl["fg"] = "#333333"
        usb_lbl["justify"] = "center"
        usb_lbl["text"] = "Flash Drive"
        usb_lbl["relief"] = "flat"
        usb_lbl.place(x=50,y=50,width=104,height=30)

        rmv_lbl = tk.Button(root)
        rmv_lbl["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        rmv_lbl["font"] = ft
        rmv_lbl["fg"] = "#000000"
        rmv_lbl["justify"] = "center"
        rmv_lbl["text"] = "Remove Folder"
        rmv_lbl["relief"] = "groove"
        rmv_lbl.place(x=250,y=240,width=120,height=42)
        rmv_lbl["command"] = self.rmv_lbl_command

        add_lbl = tk.Button(root)
        add_lbl["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        add_lbl["font"] = ft
        add_lbl["fg"] = "#000000"
        add_lbl["justify"] = "center"
        add_lbl["text"] = "Add Folder"
        add_lbl["relief"] = "groove"
        add_lbl.place(x=250,y=190,width=120,height=42)
        add_lbl["command"] = self.add_lbl_command

        global GListBox_995
        GListBox_995=tk.Listbox(root)
        GListBox_995["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_995["font"] = ft
        GListBox_995["fg"] = "#333333"
        GListBox_995["justify"] = "left"
        GListBox_995.place(x=30,y=140,width=180,height=280)
        if path.exists('fpaths'):
            shown_list = funcs.load_data('fpaths')
            for t in shown_list:
                GListBox_995.insert(tk.END, t.split("\\", 2)[-1])

        backup_btn = tk.Button(root)
        backup_btn["bg"] = "#5cdb5c"
        ft = tkFont.Font(family='Times',size=10)
        backup_btn["font"] = ft
        backup_btn["fg"] = "#ffffff"
        backup_btn["justify"] = "center"
        backup_btn["text"] = "Back Up"
        backup_btn["relief"] = "groove"
        backup_btn.place(x=260,y=420,width=123,height=46)
        backup_btn["command"] = self.backup_btn_command

        global drv_choice
        drv_choice = ttk.Combobox(root)
        ft = tkFont.Font(family='Times',size=10)
        drv_choice["font"] = ft
        drv_choice["justify"] = "center"
        drv_choice["text"] = "Choose FlashDrive"
        drv_choice["values"] = drives
        drv_choice.place(x=160,y=50,width=180,height=30)

    def add_lbl_command(self):
        chosen_folder = funcs.choose_folder()
        my_list.append(str(chosen_folder))
        chosen_folder = chosen_folder.split("\\", 2)[-1]
        GListBox_995.insert(tk.END, chosen_folder)

    def rmv_lbl_command(self):
        sel_index = self.selected_item()
        GListBox_995.delete(sel_index)
        del my_list[sel_index]

    def selected_item(self):
            for index in GListBox_995.curselection():
                return index

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Would you like to save current datapaths?"):
            funcs.store_data(my_list, 'fpaths')
            root.destroy()
        else:
            root.destroy()

    def backup_btn_command(self):
        dist = drv_choice.get()
        if dist not in drives:
            tk.messagebox.showerror(title='Wrong Drive', message='Drive not found')
        else:
            for dir in my_list:
                leaf = my_list[0].split("\\")[len(my_list[0].split("\\")) - 1]
                drv_dist = dist + '\\' + leaf
                funcs.is_exist_create(drv_dist)
                copy_tree(dir, drv_dist)






if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.protocol('WM_DELETE_WINDOW', app.on_closing)
    root.mainloop()
