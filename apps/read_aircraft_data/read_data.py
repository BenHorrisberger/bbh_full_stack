import csv
import os
from tabulate import tabulate


class Aircraft:

    def __init__(self, manufacturer:str="Not specified", full_aircraft_type:str="Not specified", seats:int=0, bags:int=0, range:int=0, id:int=0, csv_entry:dict|None=None):
        """
        Represents a aircraft and holds relevant data to the aircraft

        Attributes:
            id (int)                 : If put into a AircraftList, id represents the index.
            manufacturer (str)       : The name of the manufacturer
            full_aircraft_type (str) : The aircraft_make, aircraft_model, aircraft_variant in one str
            seats (int)              : The number of seats on the aircraft
            bags (int)               : The number of bags the aircraft can hold
            range (int)              : The range in miles until refueling is needed
            csv_entry (dict)         : A dictionary containing the whole csv entry for the aircraft

        Methods:
            __str__(): print out the aircraft data in line

        TODO

        # Great that you did this! But a little ugly. How about using f-strings and consistent spacing?
        (add some better printing to the __str__() method)
        
        """

        self.id = id
        self.manufacturer = manufacturer
        self.full_aircraft_type = full_aircraft_type
        self.seats = int(seats)
        self.bags = int(bags)
        self.range = int(range)
        self.csv_entry = csv_entry

    def __str__(self)->None:

        return f"{self.id} {self.manufacturer}  {self.full_aircraft_type}  {self.range}  {self.seats}  {self.bags}"


class AircraftList:
    """
    Holds a list of Aircraft types

    Attributes:
        num_entries (int)        : The number of aircraft in the list
        entries (list[Aircraft]) : A list of Aircraft types

    Methods:
        __str__(): prints out entries one aircraft per line
        add_aircraft(aircraft:Aircraft): adds an Aircraft type to entries
        quarry(self, distance:int, seats:int, bags:int)->None: returns a tabulate table of aircraft that satisfy the arguments
    """

    def __init__(self):

        self.entries: list[Aircraft|None] = []


    def __str__(self)->str:

        print(f"Number of Aircrafts: {self.number_of_entries}")
        for entry in self.entries:

            print(entry)

        return ""

    @property
    def number_of_entries(self)->int:

        return len(self.entries)

    def add_aircraft(self, aircraft:Aircraft)->None:

        self.entries.append(aircraft)

    def quarry(self, distance:int, seats:int, bags:int)->None:

        header_list = ["ID", "Manufacturer", "Full_aircraft_type", "Range in Miles", "Seats", "Bags"]
        table = [[ac.id, ac.manufacturer, ac.full_aircraft_type, ac.range, ac.seats, ac.bags] for ac in self.entries if ac.range >= distance and ac.seats >= seats and ac.bags >= bags]
        print(tabulate(table, headers=header_list, tablefmt="grid"))


def read_aircraft_data(path:str)->AircraftList:
    """
    Reads a csv file into the AircraftList.entries:List[Aircraft] structure.
    checks to make sure the path exists and is a csv file.
    
    Args:
        path (str) : path to the csv file, example "dir/file.csv"
    """

    if not os.path.exists(path):

        raise FileNotFoundError(f"File not found: <{path}>")

    if not path.lower().endswith(".csv"):

        raise ValueError(f"Expected .csv file, got <{path}>")

    try:

        aircraft_list = AircraftList()

        with open(path, newline='') as csvfile:

            aircrafts = list(csv.DictReader(csvfile))
            aircraft_list_index = 0

            for aircraft in aircrafts:

                # if there is a "" as an value, this is becasuse the DictReader found an empty catagory in the csv
                # need to replace them with 0's so we can run quarry on the Aircraft and not compare an int with a str
                aircraft = {key: (value if value != "" else 0) for key, value in aircraft.items()}

                new_entry = Aircraft(aircraft.get("manufacturer"), aircraft.get("full_aircraft_type"), aircraft.get("total_seats"), aircraft.get("num_bags"), aircraft.get("fuel_stop_distance"), aircraft_list_index, aircraft)
                aircraft_list.add_aircraft(new_entry)
                aircraft_list_index += 1

            return aircraft_list

    except Exception as error:

        print(f"\nError processing <{path}> raising error message:\n")
        raise error

if __name__ == "__main__":

    # Great! Now add some pytests
    my_list = read_aircraft_data("/home/lugnuts/dev/bbh_full_stack/aircraft_data/test.csv")
    print(my_list)
