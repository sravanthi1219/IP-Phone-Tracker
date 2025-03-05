import phonenumbers
from phonenumbers import carrier, geocoder, timezone

def phone_gw():
    user_phone = input("\nEnter phone number (Ex: +6281xxxxxxxxx): ")
    default_region = "ID"
    parsed_number = phonenumbers.parse(user_phone, default_region)

    print("\n========== SHOW INFORMATION PHONE NUMBERS ==========")
    print(f"Location        : {geocoder.description_for_number(parsed_number, 'en')}")
    print(f"Operator        : {carrier.name_for_number(parsed_number, 'en')}")
    print(f"Timezone        : {', '.join(timezone.time_zones_for_number(parsed_number))}")
    print(f"Valid Number    : {phonenumbers.is_valid_number(parsed_number)}")
    print(f"Possible Number : {phonenumbers.is_possible_number(parsed_number)}")
