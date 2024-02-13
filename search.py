from libraries import *

def search():
    
    #-----WIDGETS  
    #Frames
    artistFrame=ttk.Frame(root,style='artist.TFrame')
    #Mainframe IMG
    artistLabels=ttk.Label(artistFrame, text="artist", style='label.TLabel') 
    

    #-----STYLING
    style=ttk.Style()
    style.configure('artist.TFrame', background='orange',relief="solid")
    #labels
    style.configure('label.TLabel',
                background='white',
                font=('Helvetica',14),
                foreground='black',
                # L T R B
                padding=(15,6,15,6))

    root.configure(background='orange')
    #----- GRID CONFIGURATIONS 
    #window resize
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    #main frame display and resize
    artistFrame.grid(row=1,column=0,sticky="nsew")
    artistFrame.rowconfigure(0, weight=1)
    artistFrame.columnconfigure(0, weight=1)
    artistLabels.grid(row=0,column=0)
    artistLabels.rowconfigure(0, weight=1)
    artistLabels.columnconfigure(0, weight=1)
    
#event loop
    root.mainloop()




