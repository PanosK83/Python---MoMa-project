# ΔΕΝ ΔΙΑΒΑΖΕΙ ΤΟΝ ΚΑΛΛΙΤΕΧΝΗ ΟΤΑΝ ΕΧΕΙ UTF PROBLEMS
# ΔΕΝ ΠΑΙΡΝΕΙ ΠΑΝΤΑ ΤΗΝ ΣΩΣΤΗ ΗΜΕΡΟΜΗΝΙΑ (πχ αφήνει το 41 αντί για 1941)//δεν αθρο΄ίζει πάντα
#σωστά
#να φτιάξω στον πίνακα  scrollbar)
#bind ta dedomena να με πηγαίνουν στο artwork 

from libraries import *

def styles():
    style = ttk.Style()
    style.configure('artist.TFrame', background='white')
    style.configure('label.TLabel',
                    background='white',
                    font=(12),
                    foreground='black',
                    padding=(15,6,15,6)
                    )
    style.configure("Treeview", font=("Segoe UI", 12))#,rowheight=30,borderwidth=2)
    style.configure("Treeview.Heading", font=("Segoe UI", 12, "bold"), foreground="#007acc", background="#f5f5f5", anchor="center")
    style.configure("Treeview.Cell", font=("Segoe UI", 10), foreground="#333333", background="#f5f5f5")  


def artist_queries(name):
#---------QUERY DB
    conn = sqlite3.connect('data.db')  
    c = conn.cursor()
    #artist table
    c.execute("SELECT * FROM artists WHERE artist_name LIKE ?", ('%'+name+'%',))  
    artist_result = c.fetchone()    
    if artist_result:
        name = artist_result[1]
        gender = artist_result[4]
        artist_bio = artist_result[2]    
    #artwork table
    c.execute("SELECT  title, medium, date, department FROM artwork WHERE artist_name = ?", (name,))
    artwork_result = c.fetchall()
    #tuple list
    rows = []
    if artwork_result:
        #create tuple
        for row in artwork_result:
            title = row[0]
            medium = row[2]
            date = row[1]
            department = row[3]
            #send to list
            rows.append((title, medium, date, department))
    #statistics
    c.execute("SELECT department FROM artwork WHERE artist_name = ?", (name,))
    department_result = c.fetchall()
    c.execute("SELECT date, title FROM artwork WHERE artist_name = ?", (name,))
    date_artwork_result = c.fetchall()
   
#-----------APPLY STYLE
    styles()

#----------- FRAMES
    main_frame = ttk.Frame(root, style='artist.TFrame')
    main_frame.grid(row=1,column=0,sticky="nsew", pady=(5,0))
    main_frame.rowconfigure(0, weight=1)
    main_frame.columnconfigure(0, weight=1) 
#-------------- LABELS & GRID
    # BIO INFO 
    artist_name = ttk.Label(main_frame, text=f'Artist:{name}', style='label.TLabel')
    artist_bio= ttk.Label(main_frame, text=f"Artist Bio:{artist_bio}", style='label.TLabel', )
    gender = ttk.Label(main_frame, text=f"Gender:{gender}", style='label.TLabel')
    artist_name.grid(row=1, column=0, columnspan=2, pady=5)#στοιχίζει στοιχεία
    artist_bio.grid(row=2,column=0,columnspan=2,sticky='w')
    gender.grid(row=3,column=0,columnspan=2,sticky='w',pady=(0,20))
    #ARTWORK TABLE
    artworks= ttk.Label(main_frame, text=f"Total Artworks: {len(rows)}", style='label.TLabel')
    tree = ttk.Treeview(main_frame, columns=("Title", "Date", "Medium", "Department"), show="headings")
    tree.heading("Title", text="Title")
    tree.heading("Date", text="Date")
    tree.heading("Medium", text="Medium")
    tree.heading("Department", text="Department")
    artworks.grid(row=4,column=0)
    tree.grid(row=5,column=0,columnspan=2,pady=(0,20))
    for index, row in enumerate(rows):
        tree.insert('', 'end', text=str(index), values=row)
    tree['height'] = 3
         
#------------STATISTICS
  #DEPARTMENT PIE
    category_counts = {}
    for item in department_result:
        category = item[0]
        category_counts[category] = category_counts.get(category, 0) + 1    
    categories = list(category_counts.keys())
    counts = list(category_counts.values())
    fig = plt.figure(figsize=(6, 7), dpi=40)
    plt.pie(counts,textprops={'fontsize': 30},autopct='%1.1f%%')
    plt.title(' Department',fontsize=30)
    canvas = FigureCanvasTkAgg(fig, master=main_frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=6,column=0)
    plt.legend(categories, loc='lower center', bbox_to_anchor=(0.5,- 0.1), ncol=1,fontsize=20)
    #ARTWORKS BY YEARS TABLE
    artwork_counts = {}
    for row in date_artwork_result:
        date = row[0]
        title = row[1]
        if date is None:
            date = 0
        if date in artwork_counts:
            artwork_counts[date] += 1
        else:
            artwork_counts[date] = 1
    dates = list(artwork_counts.keys())
    total_artworks = list(artwork_counts.values())
    #regex
    extracted_years = []
    for date in dates:
        date = str(date)
        if date is None or date == "None":
            extracted_years.append(0) 
        else:
            match = re.search(r"\b\d{4}\b", date)  # Match four-digit year
            if match:
                extracted_years.append(int(match.group()))
            else:
                match = re.search(r"\b\d{2}(?:th|st|nd|rd)?\b", date)  # Match two-digit year with optional ordinal suffix =>AYTO MALLON DEN ΔΟΥΛΕΥΕΙ
                if match:
                    extracted_years.append(int(match.group()))
                else:
                    extracted_years.append(0)  
    artwork_stats = list(zip(extracted_years, total_artworks))
    sorted_artwork_stats = sorted(artwork_stats, key=lambda x: int(x[0]))
    tree = ttk.Treeview(main_frame, columns=("Date", "Number of Artworks"), show="headings")
    tree.heading("Date", text="Date")
    tree.heading("Number of Artworks", text="Number of Artworks")
    tree.grid(row=6,column=1,columnspan=2,padx=(0,70))
    for index, row in enumerate(sorted_artwork_stats):
        tree.insert('', 'end', text=str(index), values=row)
    tree['height'] = 4
    
    return
   
       