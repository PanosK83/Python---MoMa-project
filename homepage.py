from libraries import *
from randomart import *

#-----WIDGETS
def main_frame():
    main_frame_styles()
    #frame & grid
    main_frame=ttk.Frame(root,style='mainFrame.TFrame')
    main_frame.grid(row=1,column=0,sticky="nsew")
    main_frame.rowconfigure(0, weight=1)
    main_frame.columnconfigure(0, weight=1)
    #img & grid
    image = Image.open('index.jpg').resize((900,550))
    photo1 = ImageTk.PhotoImage(image)
    img_label = ttk.Label(main_frame, image=photo1, style='label.TLabel',)
    img_label.configure(image=photo1, background="white")
    img_label.image=photo1
    img_label.grid(row=0, column=0, pady=30,)
    #btn & grid
    btn = ttk.Button(main_frame, text="Random Artwork", style='button.TButton',cursor="hand2", command=lambda: randomArt(queries))#prevents rendering
    btn.grid(row=0, column=0,pady=(340,0), padx=(0,190),sticky='e')
    return
    
#-------STYLES
def main_frame_styles():
    style = ttk.Style()
    style.configure('mainFrame.TFrame', background='white', relief="raised")
    style.configure('label.TLabel',
                    background='white',
                    font=('Helvetica',14),
                    foreground='black',
                    padding=(15,6,15,6),
                    )
    style.configure('button.TButton', 
                    font=('Helvetica', 14, 'bold'),
                    background='white',
                    foreground='#181823',
                    padding=(15,15,15,15),
                    relief="raised")
    return


#Photo by 隔壁光头老王 WangMing'Photo: https://www.pexels.com/photo/assorted-paintings-on-green-wall-354939/