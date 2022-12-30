import os
import csv

csvpath = os.path.join('..','Resources', 'comic_books.csv')

# Prompt user for title lookup
user_book = input("What book title would like to read?")

# Set variable to check if we found the book
found = False

# Open the CSV
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the book
    for row in csvreader:
        if row[0] == user_book:
            print(row[0] + " was published by " + row[8] + " in " + row[9])

            # Set variable to confirm we have found the book
            found = True


    # If the book is never found, alert the user
    if found is False:
        print("Sorry about this, we don't seem to have what you are looking for!")
