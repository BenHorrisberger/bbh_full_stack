from invoke import task
from tabulate import tabulate

from apps.read_aircraft_data.read_data import read_aircraft_data


@task(help={
    "path": "file path to the .csv, default=aircraft_data/Aircraft.csv",
    "distance": "the distance in miles required, default=0",
    "seats": "the number of seats required, default=0",
    "bags": "the number of bags required, default=0"

})
def list_viable(c, path="aircraft_data/Aircraft.csv", distance=0, seats=0, bags=0):
    """List viable aircraft based on a range, seats, bags requirements"""

    task_aircraft_list = read_aircraft_data(path)

    header_list = ["manufacturer", "full_aircraft_type", "range in miles", "seats", "bags"]
    table = [[ac.manufacturer, ac.full_aircraft_type, ac.range, ac.seats, ac.bags] for ac in task_aircraft_list.entries if ac.range >= int(distance) and ac.seats >= int(seats) and ac.bags >= int(bags)]
    
    print(tabulate(table, headers=header_list, tablefmt="grid"))


