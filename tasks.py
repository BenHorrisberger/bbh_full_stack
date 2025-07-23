from invoke import task
from invoke.exceptions import Exit

from apps.read_aircraft_data.read_data import read_aircraft_data


def check_input(name:str, input:str):
    try:
        return int(input)
    except ValueError:
        raise Exit(f"Argument Error: {name} must be entered as an int")

@task(help={
    "path": "file path to the .csv, default=aircraft_data/Aircraft.csv",
    "distance": "the distance in miles required, default=0",
    "seats": "the number of seats required, default=0",
    "bags": "the number of bags required, default=0"

})
def list_viable(c, distance="0", seats:int="0", bags:int="0", path:str="aircraft_data/Aircraft.csv"):
    """List viable aircraft based on a distance, seats, bags requirements"""

    distance = check_input("--distance",distance)
    seats = check_input("--seats", seats)
    bags = check_input("--bags", bags)

    # pass off inputs to list_vaible methode of AircraftList
    task_aircraft_list = read_aircraft_data(path)
    task_aircraft_list.quary(distance, seats, bags)

@task
def test(c):
    """run tests on the read_data.py functionality"""

    c.run("pytest")

@task
def check(c):

    c.run("uv run ruff check")

@task
def clean(c):
    """Remove cache files"""
    c.run("find . -type d -name '__pycache__' -exec rm -r {} +", warn=True)
    c.run("find . -type f -name '*.pyc' -delete", warn=True)