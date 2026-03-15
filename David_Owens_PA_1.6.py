from datetime import datetime

student_id = input("Enter your student ID: ")

print(student_id + "'s Spreadsheet Automation Menu")

menu_options = [
    "1 Input Data",
    "2 View Current Data",
    "3 Generate Report"
]

print("Choose a number from the following options")

for option_text in menu_options:
    print(option_text)

# The next line retrieves the inputted option and stores into the variable called option.
option = input()

if option == "1" or option == "2" or option == "3":
    print("You selected " + option + " at " + str(datetime.now()))
else:
    print("Error: invalid choice selected")