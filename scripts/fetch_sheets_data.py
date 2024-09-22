import os
import json
import gspread
from google.oauth2.service_account import Credentials
import re
import requests
from datetime import datetime
import mimetypes

# Load Google Sheets credentials from GitHub secrets
google_sheets_credentials = json.loads(os.getenv('GOOGLE_SHEETS_CREDENTIALS'))

# Set up the Google Sheets API client
scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_info(google_sheets_credentials, scopes=scope)
client = gspread.authorize(creds)

# Google Drive API setup
from googleapiclient.discovery import build
drive_service = build('drive', 'v3', credentials=creds)

# Get the Google Sheets ID from environment variable (GitHub secret)
spreadsheet_id = os.getenv('GOOGLE_SHEETS_ID')

# Open the Google Sheet
sheet = client.open_by_key(spreadsheet_id).worksheet('Form responses 1')  # Adjust the sheet name if needed

# Fetch all rows (form responses)
rows = sheet.get_all_values()

# Path to the _people directory and last_processed file
people_dir = '../_people'
last_processed_file = 'last_processed.txt'

# Ensure the _people directory exists
if not os.path.exists(people_dir):
    os.makedirs(people_dir)

# Read the last processed timestamp
if os.path.exists(last_processed_file):
    with open(last_processed_file, 'r') as f:
        last_processed = f.read().strip()  # Get the last processed timestamp
else:
    last_processed = '1970-01-01 00:00:00'  # Default starting point

last_processed_dt = datetime.strptime(last_processed, '%Y-%m-%d %H:%M:%S')

# Track the latest timestamp processed during this run
latest_processed_dt = last_processed_dt

# Function to extract the file ID from Google Drive URL
def extract_file_id(drive_url):
    if "id=" in drive_url:
        return drive_url.split("id=")[1]
    elif "/d/" in drive_url:
        return drive_url.split("/d/")[1].split("/")[0]
    return None

# Function to download an image from Google Drive and save it
def download_image_from_drive(file_id, destination):
    try:
        # Using a simplified Google Drive URL for downloading the file
        response = requests.get(f"https://drive.google.com/uc?export=download&id={file_id}")
        if response.status_code == 200:
            with open(destination, 'wb') as image_file:
                image_file.write(response.content)
            print(f"Image downloaded and saved to {destination}")
        else:
            print(f"Failed to download image from Google Drive. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading image: {e}")

# Loop through the rows (skipping the header row) and create a markdown file for new entries only
for row in rows[1:]:  # Skip the header row
    timestamp = row[0].strip()  # Timestamp
    name = row[2].strip()  # Name (example: Ronald Fisher)
    personal_info = row[3].strip()  # Personal information
    website = row[4].strip()  # Website URL
    image_url = row[5].strip()  # Google Drive Image URL
    email = row[6].strip()  # Email

    # Convert timestamp to datetime object
    try:
        entry_timestamp_dt = datetime.strptime(timestamp, '%d/%m/%Y %H:%M:%S')
    except ValueError:
        continue  # Skip entries with invalid timestamps

    # Only process entries that are newer than the last processed entry
    if entry_timestamp_dt > last_processed_dt:
        # Update the latest processed timestamp
        if entry_timestamp_dt > latest_processed_dt:
            latest_processed_dt = entry_timestamp_dt

        # Create a valid filename by removing spaces and periods from the name
        filename = re.sub(r'[ .]', '', name).lower() + '.md'  # e.g., Ronald Fisher -> ronaldfisher.md

        # Create the shortname by taking the first letters of the name
        shortname = ''.join([part[0].lower() for part in name.split()])  # e.g., Ronald Fisher -> rf

        # Extract the Google Drive file ID from the URL
        file_id = extract_file_id(image_url)

        # Set the default image filename (with a placeholder extension)
        image_filename = f'{shortname}.png'  # Default to .png; adjust after download if necessary
        image_filepath = os.path.join(people_dir, image_filename)

        # Download the image from Google Drive if file_id exists
        if file_id:
            download_image_from_drive(file_id, image_filepath)

            # Attempt to detect the correct extension based on the MIME type
            mime_type = mimetypes.guess_type(image_filepath)[0]
            if mime_type == 'image/jpeg':
                image_filename = f'{shortname}.jpg'
            elif mime_type == 'image/png':
                image_filename = f'{shortname}.png'
            else:
                print(f"Unknown file type for {file_id}, using default extension")

            # Rename the image file if necessary
            new_image_filepath = os.path.join(people_dir, image_filename)
            os.rename(image_filepath, new_image_filepath)

        # Create the markdown file content
        markdown_content = f"""
---
name: {name}
shortname: {shortname}
website: {website}
image: {image_filename}
---

{personal_info}
"""

        # Save the markdown file in the _people directory using the cleaned full name as the filename
        markdown_filepath = os.path.join(people_dir, filename)

        with open(markdown_filepath, 'w') as markdown_file:
            markdown_file.write(markdown_content)

        print(f"Markdown file created: {filename}")

# After processing, update the last processed timestamp
with open(last_processed_file, 'w') as f:
    f.write(latest_processed_dt.strftime('%Y-%m-%d %H:%M:%S'))

print("All new entries processed and markdown files created successfully.")
