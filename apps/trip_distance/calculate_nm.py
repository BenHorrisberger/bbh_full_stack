from dotenv import load_dotenv
import sys
import os
import requests
import math

def haversine(lat1:float, lng1:float, lat2:float, lng2:float)->float:
    """
    Calculate notical miles between two points

    Args:
        lat1 (float): Latitude of point 1 in degrees
        lng1 (float): Longitude of point 1 in degrees
        lat2 (float): Latitude of point 2 in degrees
        lng2 (float): Longitude of point 2 in degrees

    Returns:
        float: distance in miles
    """
    # radius of earth in nm
    r = 3440
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lamda = math.radians(lng2 - lng1)

    term1 = math.sin(delta_phi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lamda / 2)**2
    miles = 2 * r * math.asin(math.sqrt(term1))

    #convert from mi to nm
    return math.ceil(miles)

def get_coords(airport_name:str)->tuple[float, float]:
    """makes a call to the Google Geocode API
    
    Args:
        airport (str) : the IATA code of the airport

    Returns:
        tuple : [0] is lat, [1] is lng
    """

    load_dotenv()
    API_KEY = os.getenv("GOOGLE_API_KEY")

    url = "https://maps.googleapis.com/maps/api/geocode/json"

    params = {
        "address" : f"{airport_name} airport",
        "key" : API_KEY
    }

    api_response = requests.get(url=url, params=params)
    api_response_dict = api_response.json()

    if api_response_dict["status"] == "OK":
        coords = api_response_dict["results"][0]["geometry"]["location"]
        return (coords["lat"], coords["lng"])
    else:
        #this will exit if there are no airports by the IATA code given
        print(f"Google API Error: {api_response_dict["status"]} for airport name \"{airport_name}\"")
        sys.exit(1)
        
    
def get_notical_miles(origin:str, destination:str)->float:

    coords_o = get_coords(origin)
    coords_d = get_coords(destination)

    return haversine(coords_o[0], coords_o[1], coords_d[0], coords_d[1])


if __name__ == "__main__":
    
    pass