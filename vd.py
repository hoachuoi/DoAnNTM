import requests
import os

# URL of the file you want to download
url = "http://127.0.0.1:5000/bac.txt"

# Local file path where you want to save the downloaded file
local_path = "E:/block/downbac.txt"

try:
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the request fails

    # Open the local file for writing and save the content
    with open(local_path, "wb") as file:
        file.write(response.content)

    print(f"File downloaded successfully to {local_path}")
except requests.exceptions.RequestException as e:
    print(f"Failed to download the file: {e}")
except IOError as e:
    print(f"Failed to write the file: {e}")
