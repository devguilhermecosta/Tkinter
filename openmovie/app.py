from tkinter import Tk, ttk, Listbox
from typing import List
from ttkthemes import ThemedTk
import requests
import json


class OpenMovie:

    def __init__(self):

        # MASTER WINDOW
        self.master = ThemedTk(theme='black')
        self.master.title('OpenMovie API')
        self.master.configure(background='#444444')
        master_w = int(self.master.winfo_screenwidth() / 2 - 300)
        master_h = int(self.master.winfo_screenheight() / 2 - 210)
        self.master.geometry(f'600x420+{str(master_w)}+{str(master_h)}')
        self.master.resizable(0, 0)

        # FRAME FOR ENTRY AND BUTTON SEARCH
        self.frame = ttk.Frame(self.master)
        self.frame.pack()

        # ENTRY FOR SEARCH
        self.entry = ttk.Entry(self.frame,
                                font='arial 16',
                                width=30,
                                )
        self.entry.grid(row=0, column=0, padx=5, pady=5)

        # BUTTON FOR SEARCH
        self.button = ttk.Button(self.frame,
                                text='Search',
                                padding=5,
                                command=self.search,
                                )
        self.button.grid(row=0, column=1, padx=5, pady=5)

        # LISTBOX
        self.list = Listbox(self.master)
        self.list.pack(expand='yes', fill='both', padx=5, pady=5)

        # MAINLOOP
        self.master.mainloop()

    # FUNCTIONS
    def search(self):
        open_movie = requests.get(f'http://www.omdbapi.com/?s={self.entry.get()}&apikey=5b5678a&')
        open_movie_list = dict(json.loads(open_movie.text))

        for key, value in open_movie_list.items():
            print(key)

            # for i in value:
                # self.list.insert('end', (f"Title: {i['Title']}"))
                # self.list.insert('end', '')



OpenMovie()
