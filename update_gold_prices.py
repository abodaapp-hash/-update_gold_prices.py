import requests
import os
import time

URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTEbahjTUJHIyenCbyZPGQBqKN_-BYloX3NZOWV8gaY1KZbM4Fx-_7kEPi4SZDP_si511ANpKLQhstb/pub?output=csv"

os.makedirs("data", exist_ok=True)

url_with_time = f"{URL}&t={int(time.time())}"

try:
    response = requests.get(url_with_time)

    if response.status_code == 200:
        response.encoding = "utf-8-sig"

        with open("data/latest.csv", "w", encoding="utf-8-sig") as f:
            f.write(response.text.strip())
            f.write(f"\n# Last Update: {time.ctime()}")

        print("✅ File updated successfully")

    else:
        print(f"❌ Error: {response.status_code}")

except Exception as e:
    print(f"❌ {e}")