import csv
import os
import pandas as pd
import matplotlib.pyplot as plt

print('\n')
welcome = 'Welcome to DataLens'
print(f'{welcome:^100}')

intro = 'Insight into Data analysis for non-technical professionals'
tag = 'Analyze Your Data, No Code, No Uploads, No Risk of Leaks—Just Insights'
print(f'{intro:^100}')
print(f'{tag:^105}')

# choice = input('\nSelect one: \n1. Analysis \n2. Useability \n3. Graph \n\nEnter: ')
# print('-' * 40)
choice = 0

def column():
    try:
        print('\nAnalysis')
        print('-' * 25)
        print('\nColumns Names: ')
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file)
            column_names = next(csv_reader)  # Read the first row as column names
        for n in column_names:
            print('\t' + str(n) + ',')    
    except:
        print('Error')

def Analysis():
    try:
        #data = pd.read_csv(file)
        print('\n')
        print(f"\nStatistics for Numerical Columns in {file}:\n")
        print(data.describe())

        export = input('\nWould you like to export this information into a csv file? (Y or N): ')
        if export == 'Y':
            name = input('Name of the exported file (include .csv): ')
            data.describe().to_csv(name)
            print(f'{name} has been exported to the current directory.\n')
    except:
        print('Error try again')

    print('-' * 40)
    
def Use():
    print('\nUseability')
    print('-' * 25)
    #data = pd.read_csv(file)
    
    null_count = data.isnull().sum()
    print("\nNumber of nulls per column:\n")
    print(null_count)

    duplicates = data.duplicated().any()
    print("\nAre there any duplicates in the dataset?", duplicates)
    print('\n')

    num = data.select_dtypes(include=['float64', 'int64']).columns
    data[num].boxplot(figsize=(10, 6))
    plt.title("Boxplots for Numeric Columns")
    plt.xticks(rotation=45)
    plt.show()
    
    print('-' * 40)


def Graph():
    print('\nGraph')
    print('-' * 25)
    graph_choice = input('Enter H (Histogram) and SC (Scatter Plot): ')
    #data = pd.read_csv(file)

    if graph_choice == 'H':
        column = input('Enter the column name for Histogram: ')

        plt.hist(data[column], bins=30, color = 'maroon', edgecolor='black')
 
        plt.title(f'Histogram of {column}')
        plt.xlabel('Value')
        plt.ylabel('Frequency')

        plt.show()

    elif graph_choice == 'SC':
        cat = input('Enter x-axis: ')
        dog = input('Enter y-axis: ')

        x = data[cat]
        y = data[dog]
        plt.scatter(x, y)
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title('Simple Scatter Plot')

        plt.show()
    else:
        print('Invalid graph name')
        Graph()
    print('-' * 40)

# print(f'You current directory: {os.getcwd()} \n')
# path = input('Is the CSV file in that path? (Enter Y for yes and N for no): ')
# if path == 'N':
#      file_location = input("Enter the file path: ")
#      os.chdir(file_location)

# file = input("Enter the CSV file (include .csv): ")
# Graph()

while choice != '4':
    try:
        choice = input('\nSelect one: \n1. Analysis \n2. Useability \n3. Graph \n4. End \n\nEnter: ')
        if choice == '4':
            break
        print('-' * 40)

        print(f'You current directory: {os.getcwd()} \n')
        path = input('Is the CSV file in the current path? (yes or no): ')

        if path == 'no':
            file_location = input("Enter the file path: ")
            os.chdir(file_location)

        file = input("Enter the CSV file (include .csv): ")
        data = pd.read_csv(file)

        exceute = True

        if exceute == True:
            if choice == '1':
                column()
                Analysis()
            elif choice == '2':
                Use()
            elif choice == '3':
                Graph()
    except:
        print('\nError try again')
        print('-' * 40)