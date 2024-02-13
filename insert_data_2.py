import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import pandas as pd

#κανω create το window και το πρωτο frame
window = tkinter.Tk()
window.title("Data Entry Form")
window.configure(bg='blue')
frame = tkinter.Frame(window, bg='black')
frame.pack()

#create ενα labelframe μεσα στο πρωτο frame που θελω να βαλω labels
user_info_frame = tkinter.LabelFrame(frame, text="Artists")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

#Κανω create labels με master το labelframe και βαζω ολα τα πεδια που θα εχω ως επιλογες για καταχωρηση στο artists
artist_name_label = tkinter.Label(user_info_frame, text="Artist Name")
artist_name_label.grid(row=0, column=0)
artist_bio_label = tkinter.Label(user_info_frame, text="Artist Bio")
artist_bio_label.grid(row=0, column=1)
nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_label.grid(row=0, column=2)
gender_label = tkinter.Label(user_info_frame, text="Gender")
gender_label.grid(row=0, column=3)
#εδω θελω να βαλω απο κατω τα υπολοιπα label αλλα τα βαζω στο row=2 οχι 1 γιατι στο 1 σκοπευω να βαλω τα entry
begin_date_label = tkinter.Label(user_info_frame, text="Begin Date")
begin_date_label.grid(row=2, column=0)
end_date_label = tkinter.Label(user_info_frame, text="End Date")
end_date_label.grid(row=2, column=1)
wiki_label = tkinter.Label(user_info_frame, text="Wiki QID")
wiki_label.grid(row=2, column=2)
ulan_label = tkinter.Label(user_info_frame, text="ULAN")
ulan_label.grid(row=2, column=3)


#εδω κανουμε create entries στο labelframe
artist_name_entry = tkinter.Entry(user_info_frame)
artist_bio_entry = tkinter.Entry(user_info_frame)
nationality_entry = tkinter.Entry(user_info_frame)
gender_entry = tkinter.Entry(user_info_frame)
begin_date_entry = tkinter.Entry(user_info_frame)
end_date_entry = tkinter.Entry(user_info_frame)
wiki_entry = tkinter.Entry(user_info_frame)
ulan_entry = tkinter.Entry(user_info_frame)


#Εδω σκοπος ειναι να εμφανιστουν κατω απο το label για τα οποια θα κανουμε entry
artist_name_entry.grid(row=1, column=0)
artist_bio_entry.grid(row=1, column=1)
nationality_entry.grid(row=1, column=2)
gender_entry.grid(row=1, column=3)
begin_date_entry.grid(row=3, column=0)
end_date_entry.grid(row=3, column=1)
wiki_entry.grid(row=3, column=2)
ulan_entry.grid(row=3, column=3)

#Εδω ομαδοποιω ολα τα widgets αντι να βαλω σε καθε ενα ξεχωριστα pad τα βαζω ολα σε ενα στο winfo_children
#και κανω το conf για ολα μαζι
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Κανω μια function στην οποια οποτε την καλω θα καταχωρει τις τιμες που βαζω στο entry σε μια variable.
#με σκοπο να καταχωρησει αυτες τις τιμες στο table artists

def insert_artists():
#καταχωρω εδω τις τιμες του χρηστη στα entry σε μεταβλητες
 artist_name = artist_name_entry.get()
 artist_bio = artist_bio_entry.get()
 nationality = nationality_entry.get()
 gender = gender_entry.get()
 begin_date = begin_date_entry.get()
 end_date = end_date_entry.get()
 wiki = wiki_entry.get()
 ulan = ulan_entry.get()
#βαζω ενα QC να μην μπορει να καταχωρει με τα πεδια κενα
 if artist_name and artist_bio != '':

#καλω συνδεση στην βαση που καναμε create σε αλλο module
        conn = sqlite3.connect('data.db')

            # Insert Data
#βαζω σε ενα tuple ολα τα entries και τα κανω insert στο table το καθενα στο σωστο πεδιο βαζοντας την σειρα που πρεπει
        data_insert_tuple = (artist_name, artist_bio, nationality, gender, begin_date, end_date, wiki, ulan)
        data_insert_query = '''insert into artists ( artist_name, artist_bio, nationality,
            gender, begin_date, end_date, wiki_qid,ulan) VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?)'''

        cursor = conn.cursor()
        cursor.execute(data_insert_query, data_insert_tuple)

#Μηνυμα που επιβεβαιωνει οτι εγινε καταχωρηση
        tkinter.messagebox.showwarning(title="Entry msg", message="Data Inserted Succesfully")
        conn.commit()
        conn.close()
#Αν δεν ισχυει η συνθηκη που θεσαμε τοτε δεν κανει το insert και δινει αυτο το μηνυμα
 else:
      tkinter.messagebox.showwarning(title="Error", message="Artist name and Artist Bio is required.")

#βγαινω απο την function

#Κανω ενα button το οποιο θα καλει την function για καταχωρηση
button = tkinter.Button(user_info_frame, text="Insert data", command=insert_artists)
button.grid(row=5, column=0, sticky="news", padx=20, pady=10)


# Κανω ενα δευτερο labelframe να βαζω τιμες για Artwork ομοια με πανω
artwork_frame = tkinter.LabelFrame(frame,text='Artwork')
artwork_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)



year_label = tkinter.Label(artwork_frame, text="Year")
artwork_name_label = tkinter.Label(artwork_frame, text="Name")

year_entry = tkinter.Entry(artwork_frame)
artwork_name_entry = tkinter.Entry(artwork_frame)

year_label.grid(row=0, column=1)
artwork_name_label.grid(row=0, column=2)
year_entry.grid(row=1, column=1)
artwork_name_entry.grid(row=1, column=2)


for widget in artwork_frame.winfo_children():
     widget.grid_configure(padx=10, pady=5)


#edw thelw na kanw insert sto allo table to artworks
def insert_artworks():
    pass

window.mainloop()




