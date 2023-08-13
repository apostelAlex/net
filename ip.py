# type this into the command line:
# crontab -e
# add this to the end
# @reboot /usr/bin/python3 /path/to/your/script.py





import requests
import os

def get_public_ipv6():
    try:
        # Abrufen der öffentlichen IPv6-Adresse
        response = requests.get('https://api64.ipify.org?format=json')
        ipv6 = response.json().get('ip')
        return ipv6
    except Exception as e:
        print(f"Fehler beim Abrufen der IPv6-Adresse: {e}")
        return None

def send_ipv6_to_nas(ipv6):
    # Hier können Sie den Code hinzufügen, um die IP an Ihr NAS zu senden.
    # Zum Beispiel, wenn Sie eine Datei auf dem NAS aktualisieren möchten:
    nas_path = "/path/to/your/NAS/file.txt"
    with open(nas_path, 'w') as file:
        file.write(ipv6)

if __name__ == "__main__":
    ipv6 = get_public_ipv6()
    if ipv6:
        send_ipv6_to_nas(ipv6)

