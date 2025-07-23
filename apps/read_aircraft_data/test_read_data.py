import pytest

from apps.read_aircraft_data.read_data import Aircraft, AircraftList, read_aircraft_data

def test_Aircraft():

    ac = Aircraft("test_man", "test_type", 10, 10, 1000, 12, {"manufactorer": "test_man"})

    assert ac.manufacturer == "test_man"
    assert ac.full_aircraft_type == "test_type"
    assert ac.seats == 10
    assert ac.bags == 10
    assert ac.range == 1000
    assert ac.id == 12
    assert type(ac.csv_entry) is dict

def test_AircraftList():

    acl = AircraftList()

    ac1 = Aircraft()
    ac2 = Aircraft()
    ac3 = Aircraft()

    acl.add_aircraft(ac1)
    acl.add_aircraft(ac2)
    acl.add_aircraft(ac3)

    assert acl.number_of_entries == 3
    assert type(acl.entries[0]) is Aircraft

def test_read_data_not_found():

    with pytest.raises(FileNotFoundError):

        read_aircraft_data("notfound.txt")

def test_read_data_not_csv():

    with pytest.raises(ValueError):

        read_aircraft_data("aircraft_data/badfile.txt")

def test_AircraftList_quary(capsys):

    acl = read_aircraft_data("aircraft_data/test.csv")

    acl.quary(0,0,0)

    captured = capsys.readouterr()

    assert """+------+----------------+----------------------+------------------+---------+--------+
|   ID | Manufacturer   | Full_aircraft_type   |   Range in Miles |   Seats |   Bags |
+======+================+======================+==================+=========+========+
|    0 | Bombardier     | Learjet 31 A         |             1000 |       7 |      6 |
+------+----------------+----------------------+------------------+---------+--------+
|    1 | Beechcraft     | Beechjet 400         |             1000 |       7 |      8 |
+------+----------------+----------------------+------------------+---------+--------+
|    2 | Beechcraft     | Beechjet 400A        |             1000 |       7 |      8 |
+------+----------------+----------------------+------------------+---------+--------+
|    3 | cessna         | cessna 414           |             1000 |       6 |      3 |
+------+----------------+----------------------+------------------+---------+--------+
|    4 | Cessna         | Cessna Longitude     |             3500 |      12 |     16 |
+------+----------------+----------------------+------------------+---------+--------+""" in captured.out