from datetime import datetime

# Ask the user for their student ID
student_id = input("Enter your student ID: ")

# Display the menu title
print(student_id + "'s Spreadsheet Automation Menu")

# Store menu options in a list
menu_options = [
    "1 Input Data",
    "2 View Current Data",
    "3 Generate Report"
]

print("Choose a number from the following options")

# Loop through the list and print each menu option
for option_text in menu_options:
    print(option_text)

# The next line retrieves the inputted option and stores into the variable called option.
option = input()


# This function converts temperature from Fahrenheit to Celsius
# It takes one numerical value and returns the converted result
def convertData(value):
    return (value - 32) * 5 / 9


# This function handles user input and processes multiple entries
def getInput():
    # Ask how many entries the user wants to input
    entries = int(input("How many entries are you inputting?\n"))

    # Loop through the number of entries
    for i in range(entries):
        # Get the date from the user
        date = input("Enter a date:\n")

        # Get the temperature value from the user
        temp = float(input("Enter the highest temp for the inputted date:\n"))

        # convertData requires one numerical argument and returns the converted value.
        converted_value = convertData(temp)

        # Print the saved data with timestamp
        print("The following was saved at " + str(datetime.now()) + " :")
        print(str(date) + "," + str(temp) + "," + str(converted_value))


# Check if the user selected option 1
if option == "1":
    print("You selected " + option + " at " + str(datetime.now()))
    getInput()
else:
    # If anything other than 1 is selected
    print("Error: The chosen functionality is not implemented yet")