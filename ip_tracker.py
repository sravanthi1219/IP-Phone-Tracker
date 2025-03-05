import requests
import json
import time

def ip_track():
    ip = input("\nEnter IP target: ")
    print("\n============= SHOW INFORMATION IP ADDRESS =============")
    req_api = requests.get(f"http://ipwho.is/{ip}")
    ip_data = json.loads(req_api.text)
    time.sleep(2)

    if ip_data.get('success'):
        print(f"\nIP target       : {ip}")
        print(f"Type IP         : {ip_data['type']}")
        print(f"Country         : {ip_data['country']}")
        print(f"City            : {ip_data['city']}")
        print(f"Latitude        : {ip_data['latitude']}")
        print(f"Longitude       : {ip_data['longitude']}")
        print(f"Maps            : https://www.google.com/maps/@{ip_data['latitude']},{ip_data['longitude']},8z")
    else:
        print("Failed to fetch IP details.")
