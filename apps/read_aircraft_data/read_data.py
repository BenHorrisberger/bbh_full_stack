import csv
import os
import sys

class Aircraft:

    def __init__(self, manufacturer:str, full_aircraft_type:str, seats, bags, range, csv_entry:dict|None=None):
        # seats, bags, etc - you want to be strings? or int or strings? Or force to ints only or strings only? All fine but use a type hint.
        # Probably better to be ints, etc, and force your CLI to do the conversion.

        # Add a unique id = the index in the list. Just seems good to have.
        self.manufacturer = manufacturer
        self.full_aircraft_type = full_aircraft_type
        self.seats = int(seats)
        self.bags = int(bags)
        self.range = int(range)
        self.csv_entry = csv_entry

    def __str__(self):
        # Great that you did this! But a little ugly. How about using f-strings and consistent spacing?
        return f"{self.manufacturer}  {self.full_aircraft_type}  {self.range}  {self.seats}  {self.bags}"


class AircraftList: # Maybe rename "Aircrafts" with an S? Your choice - easy to miss the s, but still pretty common.

    def __init__(self):

        self.num_entries = 0 # change this to be a derived property. Less effiicent, but this is a small list.
        self.entries: list[Aircraft|None] = []

    def add_aircraft(self, operand:Aircraft):
        # operand? yuck. Call it "aircaft" of type Aircraft. And use F2 to have VSCODE refactor it

        self.num_entries += 1
        self.entries.append(operand)

    def __str__(self):

        # num entries? Yuck! Number of Aircrafts: xxx
        print(f"num_entries = {self.num_entries}")
        for entry in self.entries:

            print(entry)

        return "" # don't need to return anything.


def read_aircraft_data(path:str):
    # Some docs. What is the format you are expeecting? Show a line or two.

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
    #fail1 = read_aircraft_data("/home/lugnuts/dev/bbh_full_stack/aircraft_data/badfile.txt")
    #fail2 = read_aircraft_data("/home/lugnuts/dev/bbh_full_stack/aircraft_data/notfound.txt")

    my_list = read_aircraft_data("/home/lugnuts/dev/bbh_full_stack/aircraft_data/test.csv")

    print(my_list)
