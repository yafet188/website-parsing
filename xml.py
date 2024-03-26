import re

sitemap_path = 'yeahRacingSitemap1.xml'
output_path = 'yeahRacingSitemap.txt'

# Regular expression to match https URLs
url_pattern = re.compile(r'https://[^\s<>"]+|https://[^\s<>"]+')

https_urls = []

# Read the file line by line and search for https URLs
# Specify the encoding explicitly
with open(sitemap_path, 'r', encoding='utf-8') as file:
    for line in file:
        matches = url_pattern.findall(line)
        https_urls.extend(matches)

# Write the found https URLs to the output file
with open(output_path, 'w', encoding='utf-8') as file:
    for url in https_urls:
        file.write(url + '\n')

print(f'Done! Extracted {len(https_urls)} https URLs to {output_path}.')

