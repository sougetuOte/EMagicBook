import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime

def create_diary_startup_screen():
    window = tk.Tk()
    window.title("Diary Startup Screen")
    
    # Date entry at the top
    date_frame = tk.Frame(window)
    date_frame.pack(pady=(10, 0), fill="x")
    
    date_label = tk.Label(date_frame, text="Date (YYYY-MM-DD):")
    date_label.pack(side="left", padx=(10, 0))
    
    date_var = tk.StringVar()
    date_entry = tk.Entry(date_frame, textvariable=date_var)
    date_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
    
    # Calendar in the center
    cal = Calendar(window)
    cal.pack(pady=(0, 10), fill="both", expand=True)
    
    # Update date entry with selected calendar date
    def on_date_selected(event):
        selected_date = cal.get_date()
        date_var.set(selected_date)

    cal.bind("<<CalendarSelected>>", on_date_selected)

    # 'Create New Diary' button at the bottom
    create_btn = tk.Button(window, text="Create New Diary", width=20)
    create_btn.pack(pady=(0, 10))
    
    # 'Close' button at the top right
    close_btn = tk.Button(window, text="X", command=window.destroy, width=3)
    close_btn.pack(side="right", anchor="n", padx=(0, 10), pady=(10, 0))

    window.mainloop()

# Test the layout function
create_diary_startup_screen()
