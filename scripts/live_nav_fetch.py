import requests
import pandas as pd
from pathlib import Path

schemes = {
    "SBI_Bluechip": "119551",
    "ICICI_Bluechip": "120503",
    "Nippon_LargeCap": "118632",
    "Axis_Bluechip": "119092",
    "Kotak_Bluechip": "120841"
}

for name, code in schemes.items():
    #print(f"Fetching NAV for {name} with AMFI code {code}")
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        df = pd.DataFrame(data["data"])

        output = Path(f"data/raw/{name}_live_nav.csv")

        df.to_csv(output, index=False)

        print(f" {name} downloaded")

    else:
        print(f" Failed: {name}")