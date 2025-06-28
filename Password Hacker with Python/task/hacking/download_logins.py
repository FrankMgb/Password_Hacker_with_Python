import urllib.request
import os

# URL of the logins dictionary
url = "https://cogniterra.org/media/attachments/lesson/24447/logins.txt"

try:
    # Download the file
    with urllib.request.urlopen(url) as response:
        data = response.read()
        # Save the file in the current directory
        with open("logins.txt", "wb") as f:
            f.write(data)
        print("Logins dictionary downloaded successfully.")
except Exception as e:
    print(f"Failed to download the logins dictionary. Error: {e}")