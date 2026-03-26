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


# This function converts temperature from Fahrenheit to Celsius.
def convertData(value):
    return (value - 32) * 5 / 9


# This function inserts a comma-separated string into the csv file.
def insertData(file_path, data):
    try:
        with open(file_path, "a") as file:
            file.write(data + "\n")
    except:
        print("Error: unable to write to file")


# This function reads and displays the contents of the csv file.
def viewData(file_path):
    try:
        with open(file_path, "r") as file:
            print("The file C:\\Users\\student\\ZooData.csv")
            print(file.read(), end="")
    except:
        print("Error: unable to read file")


# This function handles user input and stores entries in the csv file.
def getInput():
    entries = int(input("How many entries are you inputting?\n"))

    for i in range(entries):
        date = input("Enter a date:\n")
        temp = float(input("Enter the highest temp for the inputted date:\n"))

        # convertData requires one numerical argument and returns the converted value.
        converted_value = convertData(temp)

        data = str(date) + "," + str(temp) + "," + str(converted_value)

        try:
            insertData("ZooData.csv", data)
            print("The following data was saved at " + str(datetime.now()))
            print(data)
        except:
            print("Error: unable to save data")


# Check the user menu choice and run the correct function.
if option == "1":
    print("You selected " + option + " at " + str(datetime.now()))
    getInput()
elif option == "2":
    print("You selected " + option + " at " + str(datetime.now()))
    viewData("ZooData.csv")
else:
    print("Error: The chosen functionality is not implemented yet")