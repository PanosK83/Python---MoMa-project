from libraries import *
from urllib.request import Request, urlopen
from io import BytesIO
from artist import *

def styles():
    style = ttk.Style()
    style.configure('artwork.TFrame', background='white')
    style.configure('label.TLabel',
                    background='white',
                    font=(12),
                    foreground='black',
                    padding=(15,6,15,6)
                    )
    style.configure("Treeview", font=("Segoe UI", 12))#,rowheight=30,borderwidth=2)
    style.configure("Treeview.Heading", font=("Segoe UI", 12, "bold"), foreground="#007acc", background="#f5f5f5", anchor="center")
    style.configure("Treeview.Cell", font=("Segoe UI", 10), foreground="#333333", background="#f5f5f5")  


def artwork_queries(title,name):
#---------QUERY DB
    conn = sqlite3.connect('data.db')  
    c = conn.cursor()
    #ΣΤΟΙΧΕΙΑ ΓΙΑ ΝΑ ΦΤΙΑΞΩ ΠΙΝΑΚΑ 
    c.execute("SELECT title, artist_name, date, medium, dimensions, department, thumbnailurl FROM artwork WHERE title LIKE ? AND artist_name LIKE ?", ('%' + title + '%', '%' + name + '%'))
    artwork_result = c.fetchall()    
    rows = []
    if artwork_result:
        #create LIST OF tupleS
        for row in artwork_result:
            title = row[0]
            date = row[2]
            medium = row[3]
            dimensions = row[4]
            department=row[5]
            artist_name=row[1]
            #send to list
            rows.append((title, date, medium,dimensions,department,artist_name))
    print(rows)

   # display image
    c.execute("SELECT thumbnailurl FROM artwork WHERE title LIKE ? AND artist_name LIKE ?", ('%' + title + '%', '%' + name + '%'))

    row = c.fetchone()
    if row is None:
         return None
    url = row[0]   
    headers = {'User-Agent': "My User Agent 1.0"}
    req = Request(url, headers=headers)
    response = urlopen(req)
    image_data = response.read() 
      
#ARTIST SOS B
 #if ',' in artist_name:
  #      artist_name = artist_name.split(',')
   
#-----------APPLY STYLE
    styles()

#----------- FRAMES
    main_frame = ttk.Frame(root, style='artwork.TFrame')
    main_frame.grid(row=1,column=0,sticky="nsew", pady=(5,0))
    main_frame.rowconfigure(0, weight=1)
    main_frame.columnconfigure(0, weight=1) 
#-------------- LABELS & GRID
    #Image
    img_label=ttk.Label(main_frame)
#εδω βαζω τη μεταβλητή που πήρα απο τη βαση {image_data}
    img = Image.open(BytesIO(image_data)).resize((500,300))
    artwork = ImageTk.PhotoImage(img)
    img_label.configure(image=artwork)
    img_label.image=artwork
    img_label.grid(row=1, column=0, pady=(10, 40), padx=(50,150), columnspan=2)
#ARTWORK 
    title= ttk.Label(main_frame, text=f"Title:{title}", style='label.TLabel')
    date= ttk.Label(main_frame, text=f"Date:{date}", style='label.TLabel')
    medium= ttk.Label(main_frame, text=f"Medium:{medium}", style='label.TLabel')
    dimensions= ttk.Label(main_frame, text=f"Dimensions:{dimensions}", style='label.TLabel')
    department= ttk.Label(main_frame, text=f"Department:{department}", style='label.TLabel')
    artist= ttk.Label(main_frame, text=f"Artist:{artist_name}", style='label.TLabel')
    artist.bind("<Button-1>", lambda event:artist_queries(artist_name))
    artist.bind("<Enter>", lambda event: artist.config(foreground="#4D455D"))
    artist.bind("<Leave>", lambda event: artist.config
    (foreground="black",))
#GRID
    title.grid(row=0,column=1,padx=(0, 430))
    date.grid(row=2,column=1,padx=(0, 430))
    medium.grid(row=3,column=1,padx=(0, 430))
    dimensions.grid(row=4,column=1,padx=(0, 430))
    artist.grid(row=5,column=1,padx=(0, 430))
    department.grid(row=6,column=1,padx=(0, 430))
    return 


