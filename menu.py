from libraries import *
from search import *
from statistic import *
from artwork import *
from randomart import *
from homepage import *


#------WIDGETS & LINKS
def widgets_and_links():
    styles()
    #WIDGETS
    #frame
    menu_frame = ttk.Frame(root, style='menuFrame.TFrame')
    #img
    logo_label=ttk.Label(menu_frame, style='label.TLabel',cursor="hand2")
    logo = Image.open('logo.png').resize((70,70))
    photo = ImageTk.PhotoImage(logo)
    logo_label.configure(image=photo)
    logo_label.image = photo #so as to be kept in memory
    #labels
    art_artist_label = ttk.Label(menu_frame, text="Art & Artists", style='label.TLabel', cursor="hand2")
    statistics_label = ttk.Label(menu_frame, text="Statistics", style='label.TLabel', cursor="hand2")
    insert_label = ttk.Label(menu_frame, text="Insert Artwork", style='label.TLabel', cursor="hand2")
    #LINKS
    art_artist_label.bind("<Button-1>", lambda event: search())
    art_artist_label.bind("<Enter>", lambda event: art_artist_label.config(foreground="#4D455D"))
    art_artist_label.bind("<Leave>", lambda event: art_artist_label.config
    (foreground="black",))
    #statistics
    statistics_label.bind("<Button-1>", lambda event: statistic())
    statistics_label.bind("<Enter>", lambda event: statistics_label.config(foreground="#4D455D"))
    statistics_label.bind("<Leave>", lambda event: statistics_label.config(foreground="black"))
    #insert artwork
    insert_label.bind("<Button-1>", lambda event: artwork())
    insert_label.bind("<Enter>", lambda event: insert_label.config(foreground="#4D455D"))
    insert_label.bind("<Leave>", lambda event: insert_label.config(foreground="black"))
    #home
    logo_label.bind("<Button-1>", lambda event: main_frame())
    logo_label.bind("<Enter>", lambda event: logo_label.config(foreground="#4D455D"))
    # logoLabel.bind("<Leave>", lambda event: artistLabel.config(foreground="black"))
    return menu_frame, art_artist_label,statistics_label,insert_label,logo_label

#----STYLES
def styles():
    styles = ttk.Style()
    styles.configure('menuFrame.TFrame', background="white")
    styles.configure('label.TLabel',
                    background='white',
                    font=('Helvetica',14),
                    foreground='black',
                    padding=(15,6,15,6),
                    )

    return styles


#----GRID
def menu_grid(widgets_and_links):    
    #unpacking
    menu_frame, art_artist_label, statistics_label,insert_label,logo_label = widgets_and_links()
    #menu
    menu_frame.grid(row=0, column=0, sticky="nswe")
    menu_frame.rowconfigure(1, weight=1)
    menu_frame.columnconfigure(0, weight=1)
    #img
    logo_label.grid(row=0, column=0, sticky='w', pady=(1,2))
    #labels
    art_artist_label.grid(row=0, column=1, pady=(1,2))
    statistics_label.grid(row=0, column=2, pady=(1,2))
    insert_label.grid(row=0, column=3, pady=(1,2))    
    return






