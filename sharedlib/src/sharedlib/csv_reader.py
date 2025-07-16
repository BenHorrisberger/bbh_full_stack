import csv

def csv_reader(path:str) -> list:
    
    with open(path, newline='') as csvfile:

        reader = csv.DictReader(csvfile)

        return list(reader)
    
    