import requests

def track_username():
    username = input("\nEnter Username: ")
    social_media = [
        {"url": "https://www.facebook.com/{}", "name": "Facebook"},
        {"url": "https://www.twitter.com/{}", "name": "Twitter"},
        {"url": "https://www.instagram.com/{}", "name": "Instagram"},
        # Add more platforms as needed
    ]

    print("\n========== SHOW INFORMATION USERNAME ==========")
    for site in social_media:
        url = site['url'].format(username)
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{site['name']}: Found at {url}")
        else:
            print(f"{site['name']}: Not Found")
