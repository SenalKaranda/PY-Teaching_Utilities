import openpyxl
import random

# Load the Excel file
workbook = openpyxl.load_workbook('students.xlsx')

# Get the default sheet
sheet = workbook.active

# Initialize an empty list to store the names
names = []

# Loop through the rows in the sheet and add each name to the list
for row in sheet.iter_rows():
    name = row[0].value
    if name:
        names.append(name)

# Choose a random name from the list
random_name = random.choice(names)

# Print the random name
print(random_name)
