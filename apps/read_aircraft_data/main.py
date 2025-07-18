import csv
import os
import sys

class Aircraft:

    def __init__(self, manufacturer:str, full_name:str, seats:int, bags:int, range:int, csv_entry:dict=None):

        self.manufacturer = manufacturer
        self.full_name = full_name
        self.seats = seats
        self.bags = bags
        self.range = range
        self.csv_entry = csv_entry

    def __str__(self):

        return f"{self.manufacturer}  {self.full_name}  {self.range}  {self.seats}  {self.seats}"
    
    
class AircraftList:

    def __init__(self):

        self.num_entries = 0
        self.entries = []

    def add_aircraft(self, operand:Aircraft):

        self.num_entries += 1
        self.entries.append(operand)

    def __str__(self):

        print(f"num_entries = {self.num_entries}")
        for entry in self.entries:

            print(entry)

        return ""


def read_aircraft_data(path:str):
     
    if not os.path.isfile(path):
        
        print()
        print(f"Error: file <{path}> not found")

        sys.exit(1)
    
    if not path.lower().endswith(".csv"):

        print()
        print(f"Error: expected .csv, got <{path}>")

        sys.exit(1)
     

    try:
        
        aircraft_list = AircraftList()

        with open(path, newline='') as csvfile:

            aircrafts = list(csv.DictReader(csvfile))

            for aircraft in aircrafts:

                new_entry = Aircraft(aircraft.get("manufacturer"), aircraft.get("full_aircraft_type"), aircraft.get("total_seats"), aircraft.get("num_bags"), aircraft.get("fuel_stop_distance"), aircraft)

                aircraft_list.add_aircraft(new_entry)

            return aircraft_list

    except Exception as error:

        print(f"Error reading <{path}>\n{error}")

        sys.exit(1)


if __name__ == "__main__":

    #fail1 = read_aircraft_data("/home/lugnuts/dev/bbh_full_stack/aircraft_data/badfile.txt")
    #fail2 = read_aircraft_data("/home/lugnuts/dev/bbh_full_stack/aircraft_data/notfound.txt")

    my_list = read_aircraft_data("/home/lugnuts/dev/bbh_full_stack/aircraft_data/test.csv")

    print(my_list)