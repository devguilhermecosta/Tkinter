from tkinter import HORIZONTAL, Tk, Toplevel, ttk, PhotoImage, filedialog
from tkinter.messagebox import showerror
from pytube import YouTube


class Downloader:
    
    def __init__(self):
        
        # VARIABLES
        self.audio = False
        self.video = False
        
        # MASTER
        self.master = Tk()
        self.master.title('Youtube Downloader')
        self.master.geometry('800x640+300+50')
        self.master.resizable(0, 0)
        
        # IMAGES
        self.image_logo = PhotoImage(file='src/logo.png')
        
        # FRAMES
        self.frame_logo = ttk.Frame(self.master)
        self.frame_logo.pack(fill='x')
        
        self.frame_link = ttk.Frame(self.master,
                                    padding=20,
                                    )
        self.frame_link.pack()
        
        self.frame_options = ttk.Frame(self.master)
        self.frame_options.pack()
        
        # STYLES
        self.style_menu = ttk.Style()
        self.style_menu.configure('MLabel.TLabel',
                                  background='#3a3a3a',
                                  )
        
        self.style_button_link = ttk.Style()
        self.style_button_link.configure('TLink.TButton',
                                         background='darkred',
                                         foreground='white',
                                         )
                               
        # LABEL OF LOGO
        self.label_logo = ttk.Label(self.frame_logo,
                                    image=self.image_logo,
                                    style='MLabel.TLabel',
                                    padding=80,
                                    )
        self.label_logo.pack(fill='x')
        
        # LABEL OF ENTRY
        self.label_entry = ttk.Label(self.frame_link,
                                     text='Insert Link: ')
        self.label_entry.grid(row=0, column=0)
        
        # ENTRY OF LINK
        self.entry_link = ttk.Entry(self.frame_link,
                                    font='arial 16',
                                    width=30,
                                    )
        self.entry_link.grid(row=0, column=1)
        
        # BUTTON OF ENTRY
        self.button_entry = ttk.Button(self.frame_link,
                                       text='>',
                                       style='TLink.TButton',
                                       command=lambda :self.download(self.entry_link.get()),
                                       )
        self.button_entry.grid(row=0, column=2)
        
        # RADIOBUTTONS OPTIONS
        self.button_audio = ttk.Radiobutton(self.frame_options,
                                            text='Audio',
                                            value=0,
                                            command=self.validate_audio,
                                            )
        self.button_audio.grid(row=0, column=0)
        
        self.button_video = ttk.Radiobutton(self.frame_options,
                                            text='Video',
                                            value=1,
                                            command=self.validate_video,
                                            )
        self.button_video.grid(row=1, column=0)
        
        self.button_audio_video = ttk.Radiobutton(self.frame_options,
                                            text='Audio & Video',
                                            value=2,
                                            command=self.validate_audio_video,
                                            )
        self.button_audio_video.grid(row=3, column=0)
        
        # INFINITE LOOP
        self.master.mainloop()
    
    # FUNCTIONS
    def validate_audio(self):
        self.audio = True
        self.video = False
        
    def validate_video(self):
        self.audio = False
        self.video = True
        
    def validate_audio_video(self):
        self.audio = False
        self.video = False
    
    def download(self, link):
        if self.validate_link(link):
            if self.audio:
                directory = filedialog.askdirectory()
                YouTube(link).streams.filter(only_audio=True).first().download(directory)
                self.msg_complete()
            
            elif self.video:
                directory = filedialog.askdirectory()
                YouTube(link).streams.filter(only_video=True).first().download(directory)
                self.msg_complete()
                
            else:
                directory = filedialog.askdirectory()
                YouTube(link).streams.first().download(directory)
                self.msg_complete()


    def validate_link(self, link):
        if len(self.entry_link.get()) == 0:
            showerror(message='Informe um link para download.')
            return False
        else:
            return True

    def msg_complete(self):
        top_level = Toplevel()
        top_level.title('Download Complete')
        top_level.geometry('400x150+300+200')
        top_level.resizable(0, 0)
        
        msg = ttk.Label(top_level,
                        text='Download realizado com sucesso.',
                        ).pack()
        
        button = ttk.Button(top_level,
                            text='Fechar',
                            command=top_level.destroy,
                            ).pack() 


Downloader()
