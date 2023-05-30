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

# Shuffle the list of names
random.shuffle(names)

# Determine the size of each group
num_groups = int(input("Number of Groups: "))
group_size = len(names) // num_groups
remainder = len(names) % num_groups

# Initialize a dictionary to store the groups
groups = {}

# Loop through the number of groups
for i in range(num_groups):
    # Calculate the start and end index for this group
    start_index = i * group_size
    end_index = start_index + group_size
    
    # If there's a remainder, add one name to each of the first few groups
    if remainder > 0:
        end_index += 1
        remainder -= 1
    
    # Add this group to the dictionary
    group_name = 'Group{}'.format(i+1)
    groups[group_name] = names[start_index:end_index]

# Print out the groups
for group_name, group_members in groups.items():
    print('{}:'.format(group_name))
    for member in group_members:
        print('- {}'.format(member))
    print()  # Empty line after each group