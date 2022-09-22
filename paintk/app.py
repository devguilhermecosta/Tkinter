from tkinter import Tk, ttk, Canvas, PhotoImage, colorchooser
from tkinter.messagebox import showinfo
from PIL import ImageGrab


class App:
    
    def __init__(self):
        
        # VARIABLES OF BRUSHS
        self.default_color = "black"
        self.brush_oval = True
        self.brush_line = False
        self.brush_square = False
        self.brush_eraser = False
        
        # MASTER
        self.master = Tk()
        self.master.title('PainTk')
        self.master.minsize(1280, 640)
        self.master.resizable(0, 0)
        
        # STYLE OF FRAME
        self.frame_style = ttk.Style()
        self.frame_style.configure('Frame.TFrame',
                                   background='#3b3b3b',
                                   )
        
        # STYLE OF LABEL MENU
        self.menu_colors_style = ttk.Style()
        self.menu_colors_style.configure('Label.TLabel',
                                         background='#3b3b3b',
                                         foreground='#fff',
                                         padding=5,
                                         )
        
        # COLOR'S STYLE
        self.list_colors = ('white', 'black', 'gray', 'orange',
                            'yellow', 'red', 'blue', 'green',
                            'pink', 'purple', 'violet', 'darkred',
                            'lightblue',
                            )
       
        # FRAME
        self.frame = ttk.Frame(self.master,
                               style='Frame.TFrame',
                               height=50,
                               )
        self.frame.pack(fill='x')
                
        # LABEL OF MENU FROM COLORS
        self.menu_colors = ttk.Label(self.frame,
                                     text='Colors:',
                                     style='Label.TLabel',
                                     )
        self.menu_colors.pack(side='left')
        
        # BUTTONS OF THE COLORS OF MENU + STYLE OF BUTTON MENU
        for c in self.list_colors:
            # STYLES
            self.button_colors_style = ttk.Style()
            self.button_colors_style.configure(f'{c}Button.TButton',
                                            background=c,
                                            width=3,
                                            padding=3,
                                            relief='raised',
                                            )

            # Buttons
            self.button_colors = ttk.Button(self.frame,
                                            style=f'{c}Button.TButton',
                                            command=lambda color=c: self.select_color(color),
                                            )
            self.button_colors.pack(side='left')
        
        # LABEL OF COLORCHOOSER
        self.label_colorchooser = ttk.Label(self.frame,
                                            text='Selected Color:',
                                            style='Label.TLabel',
                                            ).pack(side='left')
        
        # BUTTON OF COLORCHOOSER
        self.style_of_colorchooser = ttk.Style()
        self.style_of_colorchooser.configure(f'Button.TButton',
                                            background=self.default_color,
                                            width=3,
                                            padding=3,
                                            relief='raised',
                                            )
        self.button_colorchooser = ttk.Button(self.frame,
                                              style='Button.TButton',
                                              command=self.selected_color,
                                              ).pack(side='left')  
              
        # SIZE OF THE BRUSHS
        self.label_size_brush = ttk.Label(self.frame,
                                          text='Size:',
                                          style='Label.TLabel',
                                          ).pack(side='left')
        
        # SPINBOX TO SIZE OF THE BRUSHS
        self.size_brush = ttk.Spinbox(self.frame,
                                      from_=1,
                                      to=50,
                                      width=2,
                                      )
        self.size_brush.set('1')
        self.size_brush.pack(side='left')
            
        # BUTTONS OF BRUSHS
        # Style
        self.style_btn_brush = ttk.Style()
        self.style_btn_brush.configure('Brush.TButton',
                                        background='#3b3b3b',
                                        )
        # Images
        self.img_line = PhotoImage(file='icons/line.png')
        self.img_oval = PhotoImage(file='icons/oval.png')
        self.img_square = PhotoImage(file='icons/square.png')
        self.img_eraser = PhotoImage(file='icons/eraser.png')
        
        # Buttons
        self.label_brushs = ttk.Label(self.frame,
                                       text='Brushs:',
                                       style='Label.TLabel',
                                       ).pack(side='left')
        
        self.btn_brush_line = ttk.Button(self.frame,
                                         image=self.img_line,
                                         style='Brush.TButton',
                                         command=self.brush_line_func,
                                         ).pack(side='left')

        self.btn_brsuh_oval = ttk.Button(self.frame,
                                         image=self.img_oval,
                                         style='Brush.TButton',
                                         command=self.brush_oval_func,
                                         ).pack(side='left')
        
        self.btn_brush_square = ttk.Button(self.frame,
                                     image=self.img_square,
                                     style='Brush.TButton',
                                     command=self.brush_square_func,
                                     ).pack(side='left')
        
        self.btn_eraser = ttk.Button(self.frame,
                                     image=self.img_eraser,
                                     style='Brush.TButton',
                                     command=self.brush_eraser_func,
                                     ).pack(side='left')
        
        # OPTIONS
        # Image Options
        self.img_save = PhotoImage(file='icons/save.png')
        self.img_new = PhotoImage(file='icons/new.png')
        
        # Label of Options
        self.label_optons = ttk.Label(self.frame,
                                      text='Options:',
                                      style='Label.TLabel',
                                      ).pack(side='left')
        
        # Buttons of Options
        self.btn_option_save = ttk.Button(self.frame,
                                          image=self.img_save,
                                          style='Brush.TButton',
                                          command=self.save,
                                          ).pack(side='left')
        
        self.btn_option_new = ttk.Button(self.frame,
                                         image=self.img_new,
                                         style='Brush.TButton',
                                         command=self.clean,
                                         ).pack(side='left')
        
        # CANVAS
        self.canvas = Canvas(self.master,
                             background='#eaeaea',
                             width=1280,
                             height=590,
                             )
        self.canvas.pack()
        self.canvas.bind('<Button-1>', self.draw)
        self.canvas.bind('<B1-Motion>', self.draw)
        
        # SHORTCUTS
        self.master.bind('<F1>', self.clean)
        self.master.bind('<F2>', self.save)

        # INFINITE LOOP
        self.master.mainloop()
    
    # FUNCTIONS
    def draw(self, event):
        x, y = event.x, event.y
        new_x, new_y = event.x, event.y

        if self.brush_oval:
            self.canvas.create_oval(x, y, new_x, new_y,
                                    fill=self.default_color,
                                    outline=self.default_color,
                                    width=self.size_brush.get(),
                                    )
        
        elif self.brush_line:
            self.canvas.create_line(x-10, y-10, new_x, new_y,
                                    fill=self.default_color,
                                    width=self.size_brush.get(),
                                    )
            
        elif self.brush_square:
            self.canvas.create_rectangle(x, y, new_x, new_y,
                                    fill=self.default_color,
                                    outline=self.default_color,
                                    width=self.size_brush.get(),
                                    )

        elif self.brush_eraser:
            self.canvas.create_oval(x, y, new_x, new_y,
                                    fill='#eaeaea',
                                    outline='#eaeaea',
                                    width=self.size_brush.get(),
                                    )
        
    def select_color(self, color):
        self.default_color = color
        self.style_of_colorchooser.configure('Button.TButton',
                                            background=self.default_color,
                                            )

    def brush_oval_func(self):
        self.brush_oval = True
        self.brush_line = False
        self.brush_square = False
        self.brush_eraser = False
        
    def brush_line_func(self):
        self.brush_oval = False
        self.brush_line = True
        self.brush_square = False
        self.brush_eraser = False
        
    def brush_square_func(self):
        self.brush_oval = False
        self.brush_line = False
        self.brush_square = True
        self.brush_eraser = False

    def brush_eraser_func(self):
        self.brush_oval = False
        self.brush_line = False
        self.brush_eraser = True
    
    def selected_color(self):
        self.default_color = colorchooser.askcolor()[1]
        self.style_of_colorchooser.configure('Button.TButton',
                                            background=self.default_color,
                                            )

    def clean(self, *args):
        self.canvas.delete('all')
        
    def save(self, *args):
        x = self.master.winfo_rootx() + self.canvas.winfo_x()
        y = self.master.winfo_rooty() + self.canvas.winfo_y()
        x1 = self.master.winfo_rootx() + self.canvas.winfo_width()
        y1 = self.master.winfo_rooty() + self.frame.winfo_height() + self.canvas.winfo_height()
        
        image = ImageGrab.grab(bbox=(x, y, x1, y1))
        image.save('image.png', 'png')
        

App()