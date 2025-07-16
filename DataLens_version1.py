import csv
import os
import pandas as pd
import matplotlib.pyplot as plt

welcome = 'Welcome to DataLens'
print(f'{welcome:^100}')

intro = 'Insight into Data analysis for non-technical professionals'
print(f'{intro:^100}')

choice = input('Select one: \n1. Analysis \n2. Useability \n3. Graph \nEnter: ')
print('-' * 40)

print(f'You current directory: {os.getcwd()} \n')
try:
    path = input('Is the CSV file in that path? (Enter Y for yes and N for no): ')
    if path == 'N':
        file_location = input("Enter the file path: ")
        os.chdir(file_location)

    file = input("Enter the CSV file (include .csv): ")
    exceute = True
except:
    exceute = False
    print('Error')

def column():
    try:
        print('Columns Names: ')
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file)
            column_names = next(csv_reader)  # Read the first row as column names
        for n in column_names:
            print('\t' + str(n) + ',')    
    except:
        print('Error')

def Analysis():
    print('\nAnalysis')
    print('-' * 15)
    df = pd.read_csv(file)
    column_name = input("Enter the column name for analysis: ")
    column_data = df[column_name]
    
    mean_value = column_data.mean()
    print(f'Mean of {column_name}: {mean_value:.2f}')
    
    mode_value = column_data.mode()
    if len(mode_value) <= 3:
        for i in range(2):
            print(mode_value[i])
    else:
        print('Mode: \t To many modes contained in the dataset to be significant')
    print('-' * 15)
    
def Use():
    print('\nUseability')
    print('-' * 15)
    df = pd.read_csv(file)
    # Count null values per column
    null_count = df.isnull().sum()
    print("\nNumber of nulls per column:")
    print(null_count)

    duplicates = df.duplicated().any()
    print("\nAre there any duplicates in the dataset?", duplicates)
    print('-' * 15)
    print('\n')


def Graph():
    print('\nGraph')
    print('-' * 15)
    graph_choice = input('Enter H (Histogram) and SC (Scatter Plot): ')
    df = pd.read_csv(file)
    if graph_choice == 'H':
        column = input('Enter the column name for Histogram: ')
        plt.hist(df[column], bins=30, color = 'maroon', edgecolor='black')
 
        plt.title(f'Histogram of {column}')
        plt.xlabel('Value')
        plt.ylabel('Frequency')

        plt.show()
        print('-' * 15)
    else:
        cat = input('Enter x-axis: ')
        dog = input('Enter y-axis: ')

        x = df[cat]
        y = df[dog]
        plt.scatter(x, y)
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title('Simple Scatter Plot')

        plt.show()
    print('-' * 15)


if exceute == True:
    if choice == '1':
        Analysis()
        column()
    elif choice == '2':
        Use()
    else:
        Graph()
