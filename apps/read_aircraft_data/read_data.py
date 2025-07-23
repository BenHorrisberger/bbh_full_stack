import csv
import os
import sys

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

        TODO
        
        # Probably better to be ints, etc, and force your CLI to do the conversion.
            - make conversion happen inside list_viable task?

        # Add a unique id = the index in the list. Just seems good to have.
            - need to add this functionality to the AircraftList class

        # Great that you did this! But a little ugly. How about using f-strings and consistent spacing?
        (add some better printing to the __str__() method)
        
        """

        self.id
        self.manufacturer = manufacturer
        self.full_aircraft_type = full_aircraft_type
        self.seats = int(seats)
        self.bags = int(bags)
        self.range = int(range)
        self.csv_entry = csv_entry

    def __str__(self)->None:
        return f"{self.manufacturer}  {self.full_aircraft_type}  {self.range}  {self.seats}  {self.bags}"


class AircraftList:
    """
    Holds a list of Aircraft types

    Attributes:
        num_entries (int)        : The number of aircraft in the list
        entries (list[Aircraft]) : A list of Aircraft types

    Methods:
        add_aircraft(aircraft:Aircraft): adds an Aircraft type to entries
        __str__(): prints out entries one aircraft per line

    TODO

    # change this to be a derived property. Less effiicent, but this is a small list.
    (change num_entries to be a derived property)

    """
    def __init__(self):

        self.num_entries = 0 
        self.entries: list[Aircraft|None] = []


    def __str__(self)->None:

        print(f"Number of Aircrafts: {self.num_entries}")
        for entry in self.entries:

            print(entry)

    def add_aircraft(self, aircraft:Aircraft)->None:

        self.num_entries += 1
        self.entries.append(aircraft)



def read_aircraft_data(path:str)->None:
    """
    Reads a csv file into the AircraftList.entries:List[Aircraft] structure.
    checks to make sure the path exists and is a csv file.
    
    Args:
        path (str) : path to the csv file, example "dir/file.csv"
    
    TODO

    # Some docs. What is the format you are expeecting? Show a line or two.
    """


    if not os.path.isfile(path):

        print(f"\nError: file <{path}> not found")

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

                # It's not obvious what this does. Makes sure empty values are 0? Explain.
                # also, I bet instead of iteratring on keys, you can iterate on items() and get the value, so if value == ""
                for key in aircraft.keys():

                    if aircraft[key] == "":

                        aircraft[key] = 0

                # Do you see squiggly lines telling you the types are not consistent? it's a pain, but figure out how to make it clean. Typing makes your code more robust.
                new_entry = Aircraft(aircraft.get("manufacturer"), aircraft.get("full_aircraft_type"), aircraft.get("total_seats"), aircraft.get("num_bags"), aircraft.get("fuel_stop_distance"), aircraft)

                aircraft_list.add_aircraft(new_entry)

            return aircraft_list

    except Exception as error:
        # Very broad, which is frowned on, but I like. But is the only error "reading"? Shouldn't it be "error processing file <path>"?
        # Also, maybe raise the error so python gives you a full dump.

        print(f"Error reading <{path}>\n{error}")

        sys.exit(1)


if __name__ == "__main__":

    # Great! Now add some pytests

    my_list = read_aircraft_data("/home/lugnuts/dev/bbh_full_stack/aircraft_data/test.csv")

    print(my_list)
