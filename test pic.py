import tkinter as tk
from tkinter import ttk
import sqlite3

conn = sqlite3.connect('data.db')  # Replace 'your_database.db' with the actual database file
cursor = conn.cursor()
cursor.execute("SELECT * FROM artists")  # Replace 'your_table' with the actual table name
results = cursor.fetchall()

window = tk.Tk()
window.title("Query Results")

frame = ttk.LabelFrame(window, text="Results")
frame.pack(padx=10, pady=10)

for row_num, row in enumerate(results):
    for col_num, col_value in enumerate(row):
        label = ttk.Label(frame, text=str(col_value))
        label.grid(row=row_num, column=col_num, padx=5, pady=5)

conn.close()

window.mainloop()