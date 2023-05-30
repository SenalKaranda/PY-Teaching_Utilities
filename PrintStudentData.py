import openpyxl

# Open the Excel file and select the sheet
workbook = openpyxl.load_workbook('emails.xlsx')
sheet = workbook['Primary']

# Open the text file for appending
with open('student-data.txt', 'a') as file:

    # Loop through each row in the sheet, starting from the second row
    for row in sheet.iter_rows(min_row=2, values_only=True):

        # Extract the data from columns 1-3 and format accordingly.
        name = str(row[0]) + ' ' + str(row[1])
        email = ','.join([str(row[2])])
        data = name + ', ' + email
        
        # Append the data to the text file
        file.write(data + '\n')
