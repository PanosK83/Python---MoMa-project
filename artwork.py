from libraries import *

def artwork(title):
    
    #-----WIDGETS  
    #Frames
    artworkFrame=ttk.Frame(root,style='artwork.TFrame')
    #Mainframe IMG
    artworkLabels=ttk.Label(artworkFrame, text="artwork", style='label.TLabel') 
    
    #-----STYLING
    style=ttk.Style()
    style.configure('artwork.TFrame', background='purple',relief="solid")
    #labels
    style.configure('label.TLabel',
                background='white',
                font=('Helvetica',14),
                foreground='black',
                # L T R B
                padding=(15,6,15,6))

    root.configure(background='purple')
    #----- GRID CONFIGURATIONS 
    #window resize
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    #main frame display and resize
    artworkFrame.grid(row=1,column=0,sticky="nsew")
    artworkFrame.rowconfigure(0, weight=1)
    artworkFrame.columnconfigure(0, weight=1)
    artworkLabels.grid(row=0,column=0)
    artworkLabels.rowconfigure(0, weight=1)
    artworkLabels.columnconfigure(0, weight=1)
    
#event loop
    root.mainloop()

