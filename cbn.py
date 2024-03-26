import re
import os

# Regular expression to match https URLs
url_pattern = re.compile(r'https?://[^\s<>"]+')

# Function to filter URLs containing 'cdn'
def filter_urls(urls):
    return [url for url in urls if 'cdn' not in url]

# Function to process file and extract URLs
def process_file(input_path):
    https_urls = []
    with open(input_path, 'r', encoding='utf-8') as file:
        for line in file:
            matches = url_pattern.findall(line)
            https_urls.extend(matches)
    return https_urls

# Function to write URLs to output file
def write_output(urls, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        for url in urls:
            file.write(url + '\n')

# Get input file from user
input_path = input("Enter the path to the input file: ")

# Check if the file exists
if not os.path.exists(input_path):
    print("File not found!")
else:
    # Get file name without extension
    file_name = os.path.splitext(os.path.basename(input_path))[0]
    # Generate output file path
    output_path = f"{file_name}_filtered.txt"
    # Process file
    https_urls = process_file(input_path)
    # Filter URLs containing 'cdn'
    filtered_urls = filter_urls(https_urls)
    # Write filtered URLs to output file
    write_output(filtered_urls, output_path)
    print(f'Done! Extracted {len(filtered_urls)} non-cdn URLs to {output_path}.')
