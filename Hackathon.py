import csv

def read():
    try:
        file = input("Enter the CSV file (include .csv): ")
        with open(file, 'r') as file_open:
            file_content = csv.reader(file_open)
            header = next(file_content)
    except:
        print('Invalid file name')

read()