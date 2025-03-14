import time
import os
import dotenv
from DrissionPage import ChromiumPage
from DrissionPage import ChromiumOptions
from openpyxl import Workbook


dotenv.load_dotenv()
co = ChromiumOptions()
urban_vpn = os.getenv("urban_vpn"," ")

co.add_extension(urban_vpn)
page = ChromiumPage(co)

base_url = "https://www.carvana.com/cars/filters?cvnaid="

filters = {
    'suv': 'eyJmaWx0ZXJzIjp7ImJvZHlTdHlsZXMiOlsiU3V2Il19fQ',
    'sedan': 'eyJmaWx0ZXJzIjp7ImJvZHlTdHlsZXMiOlsiU2VkYW4iXX19',
    'truck': 'eyJmaWx0ZXJzIjp7ImJvZHlTdHlsZXMiOlsiUGlja3VwIl19fQ',
    'coupe': 'eyJmaWx0ZXJzIjp7ImJvZHlTdHlsZXMiOlsiQ291cGUiXX19',
    'minivan': 'eyJmaWx0ZXJzIjp7ImJvZHlTdHlsZXMiOlsiTWluaVZhbiJdfX0',
    'convertible': 'eyJmaWx0ZXJzIjp7ImJvZHlTdHlsZXMiOlsiQ29udmVydGlibGUiXX19',
    'wagon': 'eyJmaWx0ZXJzIjp7ImJvZHlTdHlsZXMiOlsiV2Fnb24iXX19',
    'hatchback': 'eyJmaWx0ZXJzIjp7ImJvZHlTdHlsZXMiOlsiSGF0Y2hiYWNrIl19fQ',
    'electric': 'eyJmaWx0ZXJzIjp7ImZ1ZWxUeXBlcyI6WyJFbGVjdHJpYyJdfX0',
    'pluginhybrid': 'eyJmaWx0ZXJzIjp7ImZ1ZWxUeXBlcyI6WyJQbHVnLUluIEh5YnJpZCJdfX0',
    'hybrid': 'eyJmaWx0ZXJzIjp7ImZ1ZWxUeXBlcyI6WyJIeWJyaWQiXX19'
}

# Wait for the Urban VPN extension to activate
print("Waiting for Urban VPN to activate...")
time.sleep(15)  # Adjust this delay if needed

workbook = Workbook()
workbook.remove(workbook.active)  # Remove the default sheet

# Iterate through filters and open each URL one by one
for car_type, filter_value in filters.items():
    extracted_links = []  # To store all links for the current filter (both pages)
    
    for page_number in [None, 2]:  # None for Page 1, 2 for Page 2
        # Construct the URL
        if page_number is None:
            url = f"{base_url}{filter_value}"  # Page 1 URL
        else:
            url = f"{base_url}{filter_value}&page={page_number}"  # Page 2 URL
        
        print(f"Opening URL for {car_type.upper()} (Page {page_number or 1}): {url}")
        
        # Navigate to the URL
        page.get(url)
        
        # Wait for dynamic content to load
        time.sleep(10)  # Initial wait
        
        # Locate all <a> elements using the CSS selector
        try:
            links = page.eles('css:.h-full > a')  # Use the provided selector
            print(f"Found {len(links)} links on the page.")
            
            # Extract href attributes from each link
            for link in links:
                href = link.attr('href')  # Get the href attribute
                if href:
                    full_link = f"https://www.carvana.com{href}" if href.startswith('/') else href
                    extracted_links.append(full_link)  # Add link to the list
                    print(full_link)
                else:
                    print("Skipping invalid link (no href attribute).")
        except Exception as e:
            print(f"Error extracting links: {e}")
    
    # Add a new sheet to the workbook for this filter
    sheet = workbook.create_sheet(title=car_type.upper())  # Create a new sheet named after the filter
    sheet.append(["Links"])  # Add a header row
    for link in extracted_links:
        sheet.append([link])  # Add each link as a new row

# Save the Excel workbook
output_file = "carvana_links.xlsx"
workbook.save(output_file)
print(f"All links saved to {output_file}")

page.close()