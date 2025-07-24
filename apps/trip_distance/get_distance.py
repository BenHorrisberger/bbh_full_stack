from dotenv import load_dotenv
import os
import requests
import math

def haversine(lat1:float, long1:float, lat2:float, long2:float)->float:
    """
    Calculate notical miles between two points

    Args:
        lat1 (float): Latitude of point 1 in degrees
        long1 (float): Longitude of point 1 in degrees
        lat2 (float): Latitude of point 2 in degrees
        lon2 (float): Longitude of point 2 in degrees

    Returns:
        float: distance in miles
    """
    # radius of earth
    r = 3959

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)

    delta_phi = math.radians(lat2 - lat1)
    delta_lamda = math.radians(long2 - long1)

    result = (1 - math.cos(delta_phi) + math.cos(phi1) * math.cos(phi2) * (1 - math.cos(delta_lamda))) / 2
    result = 2 * r * math.asin(math.sqrt(result))

    #convert from mi to nm
    return math.ceil(result / 1.1507794480235)

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
        print(f"GOOGLE API ERROR: {api_response_dict["status"]}")
        return None

if __name__ == "__main__":
    
    coords = get_coords("PHI")
    print(f"@ {coords}")