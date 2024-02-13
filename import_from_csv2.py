from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import messagebox
import pandas as pd



#create first a table to insert the data from csv file and then a table to rename the columns
conn = sqlite3.connect('data.db')
c = conn.cursor()
conn = sqlite3.connect('data.db')
conn.execute("""drop table if exists artist_csv_import """)
table_artist_create_query = '''create table artist_csv_import 
                    (
                     constituent_id integer,
                     artist_name varchar, 
                     artist_bio varchar,  
                     nationality varchar,
                     gender varchar, 
                     begin_date date,
                     end_date date,
                     wiki_qid integer,
                     ulan integer
                     )
            '''
conn.execute(table_artist_create_query)

conn.execute("""drop table if exists artists """)
conn.execute('''create table artists 
                    (constituent_id integer primary key,
                     artist_name varchar, 
                     artist_bio varchar,  
                     nationality varchar,
                     gender varchar, 
                     begin_date date,
                     end_date date,
                     wiki_qid integer,
                     ulan integer
                     )
            ''')



df = pd.read_csv('artists.csv')
df.to_sql('artist_csv_import', conn, if_exists='replace')

#to ConstituentID kathorisei kathe record sto arxeio monadika opote to kanw primary key.Mporw na balw kai diko mou key
#apla yparxei to ConstituentID kai sto artwork file kai einai foreign key.Ekei mporoume na exoume to id polles fores
#gia kathe artist me diaforetiko ergo.To foreign key dilwnei oti tha exw ws artist ayton pou exei to idio artist_id
#sto artist table.

conn.execute("""insert into artists (constituent_id,artist_name,artist_bio,nationality,gender,begin_date,end_date,wiki_qid,ulan) 
                select ConstituentID,DisplayName,ArtistBio,Nationality,Gender,BeginDate,EndDate,"Wiki QID",ULAN
                from artist_csv_import
                """)

#insert artwork data
#bazw ta data apo to csv se ena table stin basi
conn.execute("""drop table if exists artwork_csv_import """)
table_artwork_create_query = '''create table artwork_csv_import 
                    (
                     title varchar,
                     artist_name varchar, 
                     constituent_id integer,
                     artist_bio varchar,   
                     nationality varchar,                      
                     begin_date date,
                     end_date date,
                     gender varchar,
                     date date,
                     medium varchar,
                     dimensions  varchar,
                     creditline varchar,
                     accession_number numeric,
                     classification varchar,
                     department varchar,
                     dateacquired date,
                     cataloged varchar,
                     objectid integer,
                     url varchar,
                     thumbnailurl varchar,
                     circumference_cm  numeric,
                     depth_cm numeric,
                     diameter numeric,
                     height_cm  numeric,
                     length_cm  numeric,
                     weight_kg  numeric,
                     width_cm numeric,
                     seat_height_cm  numeric,
                     duration_sec integer
                     )
            '''
conn.execute(table_artwork_create_query)

#kanw create ena table me primary key ena neo field kai san foreign  to constituent_id
conn.execute("""drop table if exists artwork""")
conn.execute( '''create table artwork 
                    (
                     artwork_id integer primary key,
                     title varchar,
                     artist_name varchar, 
                     constituent_id integer , 
                     artist_bio varchar,   
                     nationality varchar,                      
                     begin_date date,
                     end_date date,
                     gender varchar,
                     date date,
                     medium varchar,
                     dimensions  varchar,
                     creditline varchar,
                     accession_number numeric,
                     classification varchar,
                     department varchar,
                     dateacquired date,
                     cataloged varchar,
                     objectid integer,
                     url varchar,
                     thumbnailurl varchar,
                     circumference_cm  numeric,
                     depth_cm numeric,
                     diameter numeric,
                     height_cm  numeric,
                     length_cm  numeric,
                     weight_kg  numeric,
                     width_cm numeric,
                     seat_height_cm  numeric,
                     duration_sec integer,
                     FOREIGN KEY(constituent_id) REFERENCES artists(constituent_id)
                     )
            ''')

df = pd.read_csv('artwork_2.csv')
df.to_sql('artwork_csv_import', conn, if_exists='replace')

# ta bazw sto teliko table me ta names pou thelw
conn.execute("""insert into artwork 
                     (title ,
                     artist_name , 
                     constituent_id ,
                     artist_bio ,   
                     nationality ,                      
                     begin_date ,
                     end_date ,
                     gender ,
                     date ,
                     medium ,
                     dimensions  ,
                     creditline ,
                     accession_number ,
                     classification ,
                     department ,
                     dateacquired ,
                     cataloged ,
                     objectid ,
                     url ,
                     thumbnailurl ,
                     circumference_cm  ,
                     depth_cm ,
                     diameter ,
                     height_cm  ,
                     length_cm  ,
                     weight_kg  ,
                     width_cm ,
                     seat_height_cm ,
                     duration_sec ) 
                select
                     "Title",
                     "Artist",
                     "ConstituentID",
                     "ArtistBio",
                     "Nationality",
                     "BeginDate",
                     "EndDate",
                     "Gender",
                     "Date",
                     "Medium",
                     "Dimensions",
                     "CreditLine",
                     "AccessionNumber",
                     "Classification",
                     "Department",
                     "DateAcquired",
                     "Cataloged",
                     "ObjectID",
                     "URL",
                     "ThumbnailURL",
                     "Circumference (cm)",
                     "Depth (cm)",
                     "Diameter (cm)",
                     "Height (cm)",
                     "Length (cm)",
                     "Weight (kg)",
                     "Width (cm)",
                     "Seat Height (cm)",
                     "Duration (sec.)"
                from artwork_csv_import
                """)


#c.execute("""SELECT * FROM artists""")

print(c.fetchall())
conn.commit()


