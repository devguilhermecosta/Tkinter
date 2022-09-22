from tkinter import ACTIVE, ANCHOR, Tk, ttk, Listbox, PhotoImage, filedialog
from turtle import width
from ttkthemes import ThemedTk
from tkinter.messagebox import showerror, showinfo
import os
from pygame import mixer


class PyPlayer:
    
    def __init__(self):
        
        # VARIABLES
        with open('locals.txt', 'r') as loc:
            self.local = loc.readline()
        self.status = True
        
        # LOAD MIXER OF THE PYGAME
        mixer.init()
        
        # MASTER
        self.master = ThemedTk(theme='black')
        self.master.title('Py Player V1.0.0')
        self.master.configure(background='#444444', )
        
        # EDIT THE GEOMETRY OF MASTER
        screen_width = int((self.master.winfo_screenwidth() / 2) - 160 )
        screen_height = int((self.master.winfo_screenheight() / 2) - 225)
        self.master.geometry(f'320x450+{str(screen_width)}+{str(screen_height)}')
        self.master.resizable(0, 0)
        
        # IMAGES
        self.img_remove = PhotoImage(file='images/remove.png')
        self.img_add = PhotoImage(file='images/add.png')
        self.img_previous = PhotoImage(file='images/previous.png')
        self.img_play = PhotoImage(file='images/play.png')
        self.img_pause = PhotoImage(file='images/pause.png')
        self.img_next = PhotoImage(file='images/next.png')
        
        # CREATE A LISTBOX
        self.list_box = Listbox(self.master,
                                bg='#555555',
                                height=12,
                                relief='flat',
                                foreground='white',
                                font='arial 12',
                                selectbackground='#6868e6',
                                )
        self.list_box.pack(fill='x', padx=5, pady=5)
        
        # CHOICE LOCAL OF MUSICS
        self.button_local_music = ttk.Button(self.master, 
                                             text='Directory',
                                             command=self.set_local_musics,
                                             )
        self.button_local_music.pack()
                
        # FRAME FROM BUTTONS OF REMOVE AND ADD MUSIC
        self.frame_add_and_remove = ttk.Frame(self.master)
        self.frame_add_and_remove.pack(pady=10)
        
        # FRAME FROM BUTTONS PLAY, PREVIOUS AND NEXT
        self.frame_start = ttk.Frame(self.master)
        self.frame_start.pack(pady=10)
        
        # BUTTONS FROM ADD AND REMOVE THE MUSICS
        self.button_remove = ttk.Button(self.frame_add_and_remove,
                                    image=self.img_remove,
                                    command=self.delete_music,
                                    )
        self.button_remove.grid(row=0, column=0, padx=5)
    
        self.button_add = ttk.Button(self.frame_add_and_remove,
                                     image=self.img_add,
                                     command=self.list_musics(),
                                     )
        self.button_add.grid(row=0, column=1, padx=5)        
        
        # BUTTONS FROM PLAY, PREVIOUS AND NEXT
        self.button_previous = ttk.Button(self.frame_start,
                                          image=self.img_previous,
                                          command=self.previous_music,
                                          )
        self.button_previous.grid(row=0, column=0, padx=5)
        
        self.button_play = ttk.Button(self.frame_start,
                                      image=self.img_play,
                                      command=self.play_music,
                                      )
        self.button_play.grid(row=0, column=1, padx=5)
        
        self.button_next = ttk.Button(self.frame_start,
                                      image=self.img_next,
                                      command=self.next_music,
                                      )
        self.button_next.grid(row=0, column=2, padx=5)
        
        # SCALE OF SOUND        
        self.scale = ttk.Scale(self.master, from_=0, to=1, value=10, command=self.set_volume)
        self.scale.pack(fill='x', padx=30)

        # INFINITE LOOP
        self.master.mainloop()
        
    # FUNCTIONS
    def list_musics(self):
        
        doc = open('locals.txt', 'r')            
        files = os.listdir(doc.readline())
        doc.close()
        
        for file in files:
            self.list_box.insert('end', file)

    def delete_music(self):
        self.list_box.delete('anchor')
        
    def next_music(self):
        try:
            music = self.list_box.curselection()[0] + 1
            self.list_box.select_clear(0, 'end')
            self.list_box.activate(music)
            self.list_box.select_set(music)
            self.list_box.yview(music)
            
            self.play_music()
            
        except Exception:
            showinfo(message='Fim da lista')

    def previous_music(self):
        try:
            music = self.list_box.curselection()[0] - 1
            self.list_box.select_clear(0, 'end')
            self.list_box.activate(music)
            self.list_box.select_set(music)
            self.list_box.yview(music)
            
            self.play_music()
            
        except Exception:
            showinfo(message='Não há musicas para trás')
        
    def play_music(self):
        try:
            if self.status:
                music = str(self.local + '/' + self.list_box.get(ACTIVE))
                mixer.music.load(music)
                mixer.music.play()
                self.button_play.config(image=self.img_pause)
                self.status = False
            else:
                mixer.music.pause()
                self.button_play.config(image=self.img_play)
                self.status = True
                
        except Exception:
            showerror(message='Carregue suas músicas')
            
    def set_volume(self, *args):
        mixer.music.set_volume(self.scale.get())
        
    def set_local_musics(self):
        directory = filedialog.askdirectory()
        self.local = open('locals.txt', 'w')
        self.local.write(directory)
        self.local.close()
        
        self.list_box.delete(0, 'end')
        
        self.local = str(directory)
        self.list_musics()

PyPlayer()    
