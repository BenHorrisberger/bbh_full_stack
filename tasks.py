from invoke import task
from invoke.exceptions import Exit

from apps.read_aircraft_data.read_data import read_aircraft_data


def check_input_int(flag:str, input:str):
    try:
        return int(input)
    except ValueError:
        raise Exit(f"Argument Error: {flag} must be entered as an int")
    
def check_IATA(flag:str, input:str):
    input_len = len(input)
    if (input_len > 3 or input_len < 3 or any(char.isdigit() for char in input)):
        raise Exit(f"Argument Error: {flag} must be a IATA code, Example: PWM")

@task(help={
    "origin": "IATA code of the trip origin",
    "destination": "IATA code of the trip destination",
    "path": "file path to the .csv, default=aircraft_data/Aircraft.csv",
    "seats": "the number of seats required, default=0",
    "bags": "the number of bags required, default=0"

})
def list_viable(c, origin:str="", destination:str="", seats:int="0", bags:int="0", path:str="aircraft_data/Aircraft.csv"):
    """List viable aircraft based on a distance, seats, bags requirements"""

    check_IATA("--origin", origin)
    check_IATA("--destination", destination)
    seats = check_input_int("--seats", seats)
    bags = check_input_int("--bags", bags)

    task_aircraft_list = read_aircraft_data(path)
    task_aircraft_list.query(origin, destination, seats, bags)


@task
def test(c):
    """run tests on the read_data.py functionality"""

    c.run("pytest")

@task
def check(c):

    c.run("uv run ruff check")

@task
def clean(c):
    #need to know what actually needs to be cleaned
    """Remove cache files"""
    c.run("find . -type d -name '__pycache__' -exec rm -r {} +", warn=True)
    c.run("find . -type f -name '*.pyc' -delete", warn=True)