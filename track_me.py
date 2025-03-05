import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import requests

def phone_gw():
    # Input the phone number
    user_phone = input("\nEnter phone number (Ex: +6281xxxxxxxxx): ")
    default_region = "ID"  # Change this to your preferred default region

    try:
        parsed_number = phonenumbers.parse(user_phone, default_region)

        print("\n========== SHOW INFORMATION PHONE NUMBERS ==========")

        # Using the geocoder to get the location
        location = geocoder.description_for_number(parsed_number, 'en')
        if location:
            print(f"Location        : {location}")

            # Fetching latitude and longitude using OpenCage Geocoder API
            api_key = "16325c0d662f4b23ab5871fee4059d01"  # Replace with your OpenCage API key
            url = f"https://api.opencagedata.com/geocode/v1/json?q={location}&key={api_key}"

            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if 'results' in data and data['results']:
                    latitude = data['results'][0]['geometry']['lat']
                    longitude = data['results'][0]['geometry']['lng']
                    print(f"Latitude        : {latitude}")
                    print(f"Longitude       : {longitude}")
                else:
                    print("Unable to fetch latitude and longitude. Please check the location.")
            else:
                print("Failed to connect to the OpenCage API. Please check your API key or connection.")
        else:
            print("Location could not be determined.")

        # Other phone number details
        print(f"Operator        : {carrier.name_for_number(parsed_number, 'en')}")
        print(f"Timezone        : {', '.join(timezone.time_zones_for_number(parsed_number))}")
        print(f"Valid Number    : {phonenumbers.is_valid_number(parsed_number)}")
        print(f"Possible Number : {phonenumbers.is_possible_number(parsed_number)}")

    except phonenumbers.NumberParseException as e:
        print(f"Error parsing the phone number: {e}")

# Run the function
phone_gw()