import requests
import pandas as pd
import json

API_URL = "https://api.frankfurter.dev/v2/rates"

PARAMS = {
    "base": "USD",
    "quotes": "EUR,GBP,INR,JPY"
}

try:
    response = requests.get(
        API_URL,
        params=PARAMS,
        timeout=60
    )

    response.raise_for_status()

    data = response.json()

    # Save JSON response
    with open("api_response.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    # Convert JSON to DataFrame
    df = pd.DataFrame(data)

    # Save as CSV
    df.to_csv("api_data.csv", index=False)

    print("\nAPI data extracted successfully!\n")
    print(df)

except requests.exceptions.Timeout:
    print("The API request timed out. Please check your internet connection and try again.")

except requests.exceptions.RequestException as e:
    print("API request failed:")
    print(e)