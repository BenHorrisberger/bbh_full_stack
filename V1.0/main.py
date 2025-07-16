from pathlib import Path
import argparse
from sharedlib.csv_reader import csv_reader
import sys

def main():

    if('-h' in sys.argv or '--help' in sys.argv):

        print("USAGE: list_viable <range> <seats> <bags>")
        print("<range> type=int the range in miles of trip")
        print("<seats> type=int the number of seats required")
        print("<bags>  type=int the number of bags required")

        sys.exit(0)

    elif len(sys.argv) < 2:
    
        print("USAGE ERROR: no parameters given. use -h or --help for usage instructions")
        sys.exit(1)

    elif len(sys.argv) < 4:

        print("USAGE ERROR: too few parameters given. use -h or --help for usage instructions")
        sys.exit(1)        


    range_parameter = int(sys.argv[1])
    seats_parameter = int(sys.argv[2])
    bags_parameter = int(sys.argv[3])

    aircraft_list = csv_reader("/home/lugnuts/dev/bbh_full_stack/aircraft_data/Aircraft.csv")

    headers = list(aircraft_list[0].keys())

    align_widths = {key: max(len(str(entry.get(key, ""))) for entry in aircraft_list + [dict.fromkeys(headers, key)]) + 2 for key in headers}

    print()

    #print CLI header
    for key in headers:
        print(key.ljust(align_widths[key]), end='')

    print()

    for key in headers:
        print("-" * align_widths[key], end='')

    print()

    for aircraft in aircraft_list:

        if (int(aircraft.get("fuel_stop_distance")) >= range_parameter and int(aircraft.get("total_seats")) >= seats_parameter and int(aircraft.get("num_bags")) >= bags_parameter):

            for key in headers:

                print(str(aircraft.get(key, '')).ljust(align_widths[key]), end='')

            print()
    
    return