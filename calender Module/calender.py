import datetime
import calendar
import tkinter as tk
from tkinter import ttk

def get_day_of_week():
    d = int(day_var.get())
    m = int(month_var.get())
    y = int(year_var.get())
    input_date = datetime.date(y, m, d)
    day_of_week = calendar.day_name[input_date.weekday()]
    result_label.config(text="The day of the week is: " + day_of_week, font=("Helvetica", 23))

# Create the main window
root = tk.Tk()
root.title("Day of the Week Checker")

# Center the window on the screen
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create and place the centered box
center_frame = ttk.Frame(root)
center_frame.grid(row=0, column=0, padx=20, pady=20)
center_frame.columnconfigure(0, weight=1)
center_frame.columnconfigure(1, weight=1)

# Create and place input widgets and messages with gaps between rows in parallel columns
ttk.Label(center_frame, text="Enter day:", foreground="blue",font=("Helvetica", 15)).grid(row=0, column=0, sticky="e", pady=(0, 5))
day_var = tk.StringVar()
ttk.Entry(center_frame,textvariable=day_var).grid(row=0, column=1, sticky="w", pady=(0, 5))

ttk.Label(center_frame, text="Enter month:", foreground="green",font=("Helvetica", 15)).grid(row=1, column=0, sticky="e", pady=(0, 5))
month_var = tk.StringVar()
ttk.Entry(center_frame, textvariable=month_var).grid(row=1, column=1, sticky="w", pady=(0, 5))

ttk.Label(center_frame, text="Enter year:", foreground="red",font=("Helvetica", 15)).grid(row=2, column=0, sticky="e", pady=(0, 5))
year_var = tk.StringVar()
ttk.Entry(center_frame, textvariable=year_var).grid(row=2, column=1, sticky="w", pady=(0, 5))

# Create and place the "Check Day" button in the centered box
check_button = ttk.Button(center_frame, text="Check Day", command=get_day_of_week)
check_button.grid(row=3, columnspan=2, pady=(10, 20))

# Create and place the result label in the centered box
result_label = ttk.Label(center_frame, text="", font=("Helvetica", 30))  # Increase font size to 30
result_label.grid(row=4, columnspan=2)
# Start the GUI event loop
root.mainloop()








