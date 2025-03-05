import requests

def show_ip():
    print("\n========== SHOW INFORMATION YOUR IP ==========")
    response = requests.get('https://api.ipify.org/')
    print(f"\nYour IP Address : {response.text}")
