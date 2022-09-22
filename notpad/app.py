from cgitb import text
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo


master = Tk()
master.title('Notepad')

# inicio das funções
def new_file():
    text_area.delete(1.0, 'end')
    
def save_file():
    content = text_area.get(1.0, 'end')
    with open('my_document.txt', 'w') as doc:
        doc.write(content)
        
    showinfo(message='your file has saved successfully')
    
def open_file():
    
    new_file()
    
    with open('my_document.txt', 'r') as doc:
        content = doc.read().strip()
        text_area.insert(1.0, content)
        
def update_font():
    font = spin_font.get()
    size = font_spin_size.get()
    
    if int(size) < 1:
        size = '1'
        font_spin_size.set('1')
        
    if int(size) > 60:
        size = '60'
        font_spin_size.set('60')
    
    text_area.config(font=f'"{font}" {size}')

# término das funções

# frame para sustentar o menu de configuração da fonte
frame = ttk.Frame(master,
                  relief='ridge',
                  borderwidth=1,
                  )
frame.pack(expand=True, fill='x', side='top')

# spinbox para escolher a font-familly
text_font = ttk.Label(frame,
                      text='Font:',
                      padding=5,
                      )
text_font.pack(side='left')

spin_font = ttk.Spinbox(frame,
                        values=('Arial',
                                'Times New Roman',
                                ),
                             )
spin_font.pack(side='left')

# spinbox para escolher o tamanho da fonte
text_size = ttk.Label(frame,
                      text='Font size:',
                      padding=5,
                      )
text_size.pack(side='left')

font_spin_size = ttk.Spinbox(frame,
                             from_=0,
                             to=60,
                             )
font_spin_size.pack(side='left')

# button para atualizar as configurações da fonte
button = ttk.Button(frame,
                    text='Update',
                    command=update_font,
                    )
button.pack(side='left')

# text area
text_area = Text(master,
                 width=500,
                 height=500,
                 )
text_area.pack(side='top', expand=True, fill='both')

# variável que cria uma instância de Menu()
master_menu = Menu(master)

# adicionando opções ao Menu()
file_menu = Menu(master_menu, tearoff=0)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Exit', command=master.quit)

# criando um menu do tipo 'cascade'
master_menu.add_cascade(label='File', menu=file_menu)

# adicionando o menu cascade ao master
master.configure(menu=master_menu)


master.mainloop()