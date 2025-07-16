import csv

def csv_reader(path:str) -> list:
    
    remove_data = ['\ufeffid', 'aircraft_make', 'aircraft_model', 'aircraft_variant', 'category_name', 'cabin_dimensions_height', 'cabin_dimensions_width', 'cabin_dimensions_length', 'baggage_capacity']

    with open(path, newline='') as csvfile:

        aircraft_dictionaries = csv.DictReader(csvfile)

        aircraft_list =  list(aircraft_dictionaries)

        for aircraft in aircraft_list:

            for data in remove_data:

                aircraft.pop(data, None)

        return aircraft_list 


if __name__ == '__main__':

    csv_reader("/home/lugnuts/dev/bbh_full_stack/aircraft_data/Aircraft.csv")
