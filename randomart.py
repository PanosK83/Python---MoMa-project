
from libraries import *
from urllib.request import Request, urlopen
from io import BytesIO
import sqlite3
from artist import *
from artwork_stat import *

#------DATABASE QUERIES
def queries():
#παιρνω από τη βάση πινακα ΑRΤWORK τις μεταβλητές που χρειάζομαι 
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT thumbnailurl, title, artist_name, date FROM artwork WHERE thumbnailurl IS NOT NULL ORDER BY RANDOM() LIMIT 1")
    row = cursor.fetchone()
    if row is None:
         return None
    url = row[0]   
    headers = {'User-Agent': "My User Agent 1.0"}
    req = Request(url, headers=headers)
    response = urlopen(req)
    image_data = response.read() 
    title, artist_name, date = row[1:]  
    if ',' in artist_name:
        artist_name = artist_name.split(',')
#επιστρέφω τις μεταβλη΄τες για να τις χρησιμοποιήσω στις άλλες συναρτήσεις
    return image_data, title, artist_name, date

#--------STYLES
def styles():
    style = ttk.Style()
    style.configure('randomArt.TFrame', background='white',relief="solid")
    style.configure('label.TLabel',
                    background='white',
                    font=('Helvetica',14),
                    foreground='black',
                    padding=(15,6,15,6),
                    )
    style.configure('button.TButton', 
                    font=('Helvetica', 15, 'bold'),
                    background='white',
                    foreground='#181823',
                    padding=(5,5,5,5),
                    relief="raised")


#----------WIDGETS & GRID
def randomArt(queries):
#κανω unpack τις μεταβλητές  που πήρα από τη βαση για να τις χρησιμοποιήσω
    image_data,title,artist_name,date =queries()
    styles()
    #Frame
    artworkFrame=ttk.Frame(root,style='randomArt.TFrame')#, style='randomArt.TFrame')
    artworkFrame.grid(row=1,column=0,sticky="nsew")
    artworkFrame.rowconfigure(0, weight=1)
    artworkFrame.columnconfigure(0, weight=1)
    #Image
    img_label=ttk.Label(artworkFrame)
#εδω βαζω τη μεταβλητή που πήρα απο τη βαση {image_data}
    img = Image.open(BytesIO(image_data)).resize((500,300))
    artwork = ImageTk.PhotoImage(img)
    img_label.configure(image=artwork)
    img_label.image=artwork
    #Title
    #max_title_length = 20 
    #if len(title) > max_title_length:
      #  title = title[:max_title_length] + '...'
#εδω βαζω τη μεταβλητή που πήρα απο τη βαση {title}                                       
    title_label = ttk.Label(artworkFrame, text=f"Title: {title}", style='label.TLabel')
    #όταν κανω κλικ να καλειται η συναρτηση artist_queries() με argument τον εκαστοτε καλλιτεχνη που εχω πάρει random από τη β΄άση => αυτό πρακτικά μας οδηγεί την καρτελα του καλλιτεχνη
    title_label.bind("<Button-1>", lambda event:artwork_queries(title,artist_name))
    title_label.bind("<Enter>", lambda event: title_label.config(foreground="#4D455D"))
    title_label.bind("<Leave>", lambda event: title_label.config
    (foreground="black",))
    #Date
    date=str(date)
    max_date_length = 20  
    if len(date) > max_date_length:
        date = date[:max_date_length] + '...'
#βαζω τη μεταβλητή που πήρα απο τη βαση {date}
    date_label = ttk.Label(artworkFrame, text=f"Date: {date}", style='label.TLabel')
    #Artist
#βαζω τη μεταβλητή που πήρα απο τη βαση {artist_name}
    if isinstance(artist_name, list):
#διαχωριζω αν εχω πολλούς ή εναν καλλιτέχνη
        for i in range(len(artist_name)):
            artist = artist_name[i].strip()
#αν εχω πολλο΄ύς καλλιτεχνες να τους εμφανίσω όλους
            artist_label = ttk.Label(artworkFrame, text=f"Artist {i + 1}: {artist}",style='label.TLabel')
#όταν κανω κλικ να καλειται η συναρτηση artist_queries() με argument τον εκαστοτε καλλιτεχνη που εχω πάρει random από τη β΄άση => αυτό πρακτικά μας οδηγεί την καρτελα του καλλιτεχνη
            artist_label.bind("<Button-1>", lambda event, artist=artist: artist_queries(artist)) 
            artist_label.bind("<Enter>", lambda event, label=artist_label: label.config(foreground="#4D455D"))
            artist_label.bind("<Leave>", lambda event, label=artist_label: label.config(foreground="black"))
            artist_label.grid(row=i+3,column=1,padx=(0, 430))
            date_label.grid(row=i+4,column=1,padx=(0, 430))
    else:
        artist_label = ttk.Label(artworkFrame, text=f"Artist: {artist_name}", style='label.TLabel')
        artist_label.bind("<Button-1>", lambda event:artist_queries(artist_name))
        artist_label.bind("<Enter>", lambda event: artist_label.config(foreground="#4D455D"))
        artist_label.bind("<Leave>", lambda event: artist_label.config
        (foreground="black",))
        artist_label.grid(row=3,column=1,padx=(0, 430))
        date_label.grid(row=4,column=1,padx=(0, 430))
    #Button
    btn = ttk.Button(artworkFrame, text="Random Image", style='button.TButton',
    #καλώ τη συνάρτηση για να κάνει display αλλο εργο random
    cursor="hand2", command=lambda: randomArt(queries))#prevents rendering 
    img_label.grid(row=1, column=0, pady=(10, 40), padx=(50,150), columnspan=2)
    title_label.grid(row=2,column=1,padx=(0, 430))
    btn.grid(row=6, column=0, sticky="e",pady=(10, 20), padx=(0,150),columnspan=2)
    root.mainloop() 
    return   


#Aυτά είναι για τεστ, σβήστα στο τέλος
# randomArt()
# root.mainloop()


