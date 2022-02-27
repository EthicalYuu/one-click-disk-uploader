import os.path
from os import path
import os, string, pickle
from tkinter import ttk, filedialog

def get_drives():
    available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
    return available_drives

def choose_folder():
    folder = filedialog.askdirectory()
    if folder:
        filepath = os.path.abspath(folder)
    if filepath:
        return filepath

def store_data(data, pickle_file):
    dbfile = open(pickle_file, 'wb')
    pickle.dump(data, dbfile)
    dbfile.close()

def load_data(pickle_file):
    dbfile = open(pickle_file, 'rb')
    db = pickle.load(dbfile)
    dbfile.close()
    return db

def is_exist_create(path):
    is_exist = os.path.exists(path)
    if not is_exist:
        os.makedirs(path)
