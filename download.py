import requests
import os

# Source URL on PythonAnywhere pointing to the folder
source_url = "https://www.pythonanywhere.com/user/sanu0711/files/home/sanu0711/mysite/static/"

# Destination folder on your local machine
# Destination folder on your local machine
# Destination folder on your local machine
destination_path = r"C:\Users\Abhishek Yadav\Downloads\onlinequiz-master"

# Make a GET request to the source URL to retrieve a list of files in the folder
response = requests.get(source_url)

# Check if the request was successful
if response.status_code == 200:
    # Create the destination directory if it doesn't exist
    os.makedirs(destination_path, exist_ok=True)
    
    # Parse the HTML content to extract file links (you may need to adjust this part)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    file_links = [a['href'] for a in soup.find_all('a', href=True)]
    
    # Download each file in the folder
    for file_link in file_links:
        file_url = source_url + file_link
        local_filename = os.path.join(destination_path, file_link)
        
        # Make a GET request to download the file
        file_response = requests.get(file_url)
        
        if file_response.status_code == 200:
            with open(local_filename, "wb") as local_file:
                local_file.write(file_response.content)
            print(f"Downloaded {file_link} to {local_filename}")
        else:
            print(f"Failed to download {file_link}. Status code:", file_response.status_code)
else:
    print("Failed to retrieve the folder content. Status code:", response.status_code)
