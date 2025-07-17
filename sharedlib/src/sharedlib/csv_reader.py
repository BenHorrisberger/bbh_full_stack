import csv

def csv_reader(path:str) -> list:
    """
    I'd split this into two.
    1. Read file into a list
    2. Clean the data in the list

    Also, don't bind it to "csv". Yeah, it will take a csv, but better call it "read_airline_data" or something.
    Then, test to make sure if it is a .csv and error if not.
    Then read in. Wrap in a try/except block to catch errors in reading the file.

    For V1, a list is fine.
    For v1.1, you could use a dataclass
    But for v2, you should upgrade to a full class: Aircrafts and Aircraft.


    While I'm at it - project structure.

    Look here: https://docs.astral.sh/uv/concepts/projects/workspaces/

    especially here: https://docs.astral.sh/uv/concepts/projects/workspaces/#workspace-layouts

    And look at your pyproject.toml file

    Also, "V1.0" isn't a great name for an app.

    I'd restructure to
    ./sharedlib
    ./apps/* (this will mimick what the astral docs say)

    This csv reader is part of one of those apps. right now, you'll only have one.

    """

    remove_data = ['cruise_speed', 'fuel_stop_hours', 'max_range', '\ufeffid', 'aircraft_make', 'aircraft_model', 'aircraft_variant', 'category_name', 'cabin_dimensions_height', 'cabin_dimensions_width', 'cabin_dimensions_length', 'baggage_capacity']

    with open(path, newline='') as csvfile:

        aircraft_dictionaries = csv.DictReader(csvfile)

        aircraft_list =  list(aircraft_dictionaries)

        for aircraft in aircraft_list:

            for data in remove_data:

                aircraft.pop(data, None)

            for key in aircraft.keys():

                if aircraft[key] == "":

                    aircraft[key] = 0

        return aircraft_list


if __name__ == '__main__':

    csv_reader("/home/lugnuts/dev/bbh_full_stack/aircraft_data/Aircraft.csv")
