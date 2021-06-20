from pathlib import Path
import csv
import json
import sqlite3

# lists customers.csv file
# with open("customers.csv", "r", newline="") as file:
#     reader = csv.reader(file)
#     data = list(reader)
#     print(data)

# db_name = "chinook.db"
# with sqlite3.connect(db_name) as conn:
#     sql_command = "INSERT INTO customers (Company, FirstName, LastName, Address, City, PostalCode, Country, Email) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
#     for customer in customers:  # was json file in homework chapter 9
#         customer_values = tuple(customer.values())
#         conn.execute(sql_command, customer_values)
#     conn.commit()
#     print("Data written to the database.")

# Function to convert a CSV to JSON
# Takes the file paths as arguments


def make_json(csvFilePath, jsonFilePath):

    # create a dictionary
    data = {}

    # Open a csv reader called DictReader
    with open(csvFilePath, 'w', newline="") as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:

            # Assuming a column named 'No' to
            # be the primary key
            key = rows['CustomerId']
            data[key] = rows

    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', newline="") as jsonf:
        jsonf.write(json.dumps(data, indent=4))

# Driver Code


# Decide the two file paths according to your
# computer system
csvFilePath = 'customers2.csv'
jsonFilePath = 'customers2.json'

# Call the make_json function
make_json(csvFilePath, jsonFilePath)

############################################################

# con = sqlite3.connect("chinook.db")
# cur = con.cursor()

# a_file = open("customers.csv")
# rows = csv.reader(a_file)
# cur.executemany(
#     "INSERT INTO customers (Company, FirstName, LastName, Address, City, PostalCode, Country, Email) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", rows)
# print(cur.fetchall())

# con.commit()
# con.close()
#############################################################
