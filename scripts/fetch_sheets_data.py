import os
import json
import gspread
from google.oauth2.service_account import Credentials
import re
import requests
from datetime import datetime

# Load Google Sheets credentials from GitHub secrets
google_sheets_credentials = json.loads(os.getenv('GOOGLE_SHEETS_CREDENTIALS'))

# Set up the Google Sheets API client
scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_info(google_sheets_credentials, scopes=scope)
client = gspread.authorize(creds)

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

# Loop through the rows (skipping the header row) and create a markdown file for new entries only
for row in rows[1:]:  # Skip the header row
    timestamp = row[0].strip()  # Timestamp
    name = row[2].strip()  # Name (example: Ronald Fisher)
    personal_info = row[3].strip()  # Personal information
    website = row[4].strip()  # Website URL
    image_url = row[5].strip()  # Image URL
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

        # Determine the file extension of the image (e.g., .png, .jpg)
        image_extension = os.path.splitext(image_url)[-1]

        # Download the image and save it to the _people directory with the shortname as the filename
        image_filename = f'{shortname}{image_extension}'
        image_filepath = os.path.join(people_dir, image_filename)

        # Download the image
        if image_url:
            try:
                response = requests.get(image_url)
                if response.status_code == 200:
                    with open(image_filepath, 'wb') as image_file:
                        image_file.write(response.content)
                    print(f"Image downloaded and saved as {image_filename}")
                else:
                    print(f"Failed to download image from {image_url}")
            except Exception as e:
                print(f"Error downloading image: {e}")

        # Create the markdown file content
        markdown_content = f"""
---
name: {name}
shortname: {shortname}
website: {website}
image: {image_filename}"
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
