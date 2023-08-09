# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime
import calendar

# Take input for the date
m, d, y = map(int, input("Enter date (MM DD YYYY): ").split( ))
input_date = datetime.date(y, m, d)

# Get the day of the week
day_of_week = calendar.day_name[input_date.weekday()]

# Define ANSI escape codes for text colors
color_codes = {
    "MONDAY": "\033[91m",  # Red
    "TUESDAY": "\033[92m",  # Green
    "WEDNESDAY": "\033[93m",  # Yellow
    "THURSDAY": "\033[94m",  # Blue
    "FRIDAY": "\033[95m",  # Magenta
    "SATURDAY": "\033[96m",  # Cyan
    "SUNDAY": "\033[97m"  # White
}

# Check if the day of the week is a key in the color_codes dictionary
if day_of_week.upper() in color_codes:
    colored_day = color_codes[day_of_week.upper()] + day_of_week + "\033[0m"  # Reset color after the text
else:
    colored_day = day_of_week

# Print the formatted day of the week
print("The day of the week is:", colored_day)




