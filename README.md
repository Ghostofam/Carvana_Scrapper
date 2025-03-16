# DP-Carvana Web Scraper

A specialized web scraping tool designed to extract vehicle listings from Carvana.com based on various vehicle categories and types, storing data in both SQLite database and Excel formats.

## Project Overview

This project is a web scraper built to automatically navigate through Carvana's website and extract vehicle listing URLs for different vehicle types and categories. It uses DrissionPage (a browser automation tool) along with Urban VPN for web access, and organizes the extracted data into both a SQLite database and an Excel spreadsheet.

### Key Features

- Automated scraping of Carvana vehicle listings
- Filtering by vehicle types (SUV, Sedan, Truck, etc.)
- Filtering by fuel types (Electric, Hybrid, Plug-In Hybrid)
- Multi-page data extraction
- VPN integration for reliable access
- Dual storage in SQLite database and Excel format
- Database-driven category management

## System Architecture

The system follows a modular workflow:

1. **Database Initialization**: Sets up the SQLite database schema with `db_init.py`
2. **Initialization**: Sets up the browser environment with VPN extension
3. **Category Management**: Retrieves vehicle categories from the database
4. **Web Navigation**: Visits each category URL and waits for dynamic content to load
5. **Data Extraction**: Scrapes vehicle listing links from the page
6. **Data Storage**: Stores links in both SQLite database and Excel workbook

## File and Directory Structure

```
DP-Carvana/
├── main.py                 # Main script containing the scraping logic
├── db_init.py              # Database initialization and management script
├── .env                    # Environment variables (VPN path)
├── carvana_links.xlsx      # Output Excel file containing scraped links
├── Carvana_data            # SQLite database file storing categories and car links
├── .gitignore              # Git ignore file
└── .venv/                  # Python virtual environment
```

### File Descriptions

- **main.py**: The core script that handles web scraping operations, including browser automation, link extraction, and data storage.
- **db_init.py**: Manages the SQLite database, including schema creation, data insertion, and querying.
- **.env**: Contains the path to the Urban VPN Chrome extension.
- **Carvana_data**: SQLite database file that stores vehicle categories and extracted car links.
- **carvana_links.xlsx**: Excel output file organized by vehicle category.

## Database Schema

The project uses a SQLite database with the following structure:

1. **Categories Table**:
   - `category_id` (TEXT): Primary key, identifier for the category (e.g., 'suv', 'sedan')
   - `category_name` (TEXT): The encoded filter value used in Carvana URLs

2. **Cars Table**:
   - `id` (INTEGER): Auto-incrementing primary key
   - `link` (TEXT): The full URL to the vehicle listing
   - `category_id` (TEXT): Foreign key referencing Categories table

## Installation and Setup

### Prerequisites

- Python 3.11 or higher
- Google Chrome browser
- Urban VPN extension for Chrome

### Environment Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/DP-Carvana.git
   cd DP-Carvana
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. Install required packages:
   ```
   pip install DrissionPage openpyxl python-dotenv sqlite3
   ```

4. Configure the `.env` file:
   - Install the Urban VPN extension in Chrome
   - Locate the extension directory (typically in Chrome's user data directory)
   - Create a `.env` file with the following content:
     ```
     urban_vpn = "path/to/your/urban_vpn/extension/directory"
     ```
   - Example path format: `C:/Users/username/AppData/Local/Google/Chrome/User Data/Default/Extensions/extensionid/version_number`

### Database Initialization

Before running the main script, you need to initialize the database:

1. Uncomment the relevant sections in `db_init.py` to:
   - Create the Categories table
   - Create the Cars table
   - Insert category data

2. Run the database initialization script:
   ```
   python db_init.py
   ```

3. Verify that the tables are created correctly by checking the output.

## Usage

1. Ensure your `.env` file is properly configured with the Urban VPN extension path.

2. Make sure the database is initialized with category data.

3. Run the main script:
   ```
   python main.py
   ```

4. The script will:
   - Initialize the browser with the VPN extension
   - Wait for the VPN to activate (15 seconds by default)
   - Retrieve categories from the database
   - Navigate through each vehicle category
   - Extract links from the first two pages of each category
   - Save extracted links to both the SQLite database and Excel file

5. The Excel file will contain separate sheets for each vehicle category with the corresponding vehicle listing URLs.

6. To query the database after scraping:
   ```
   python db_init.py
   ```
   This will display all car links stored in the database.

## Configuration Options

### Vehicle Categories

The project uses a database-driven approach for managing vehicle categories. Categories are stored in the `Categories` table with the following structure:

- **Body Styles**: SUV, Sedan, Truck, Coupe, Minivan, Convertible, Wagon, Hatchback
- **Fuel Types**: Electric, Plug-In Hybrid, Hybrid

Each category has an encoded filter value that Carvana uses for filtering. These are base64-encoded JSON objects.

### Timing Parameters

- **VPN Activation Wait**: 15 seconds (adjustable in the script)
- **Page Load Wait**: 10 seconds (adjustable in the script)

## Extending the Project

### Adding New Categories

To add new categories:

1. Identify the encoded filter value by:
   - Using the filter on Carvana's website
   - Copying the `cvnaid` parameter from the URL

2. Add the new category to the database:
   ```python
   cursor.execute("""
   INSERT OR REPLACE INTO Categories (category_id, category_name)
   VALUES (?, ?);
   """, ('new_category_id', 'encoded_filter_value'))
   ```

### Modifying Page Navigation

The script currently extracts data from the first two pages of each category. To change this behavior, modify the `page_number` loop in `main.py`:

```python
# Example: Extract from first three pages
for page_number in [None, 2, 3]:
    # Existing code...
```

### Enhancing Data Collection

To collect more detailed information about each vehicle:

1. Modify the `Cars` table schema to include additional fields
2. Update the scraping logic to extract more details from each listing
3. Adjust the data storage code to save the additional information

## Troubleshooting

### Common Issues

1. **VPN Connection Problems**:
   - Ensure the Urban VPN extension path in `.env` is correct
   - Increase the VPN activation wait time if needed
   - Verify the VPN extension is properly installed in Chrome

2. **No Links Found**:
   - Check if the CSS selector `.h-full > a` is still valid on Carvana's website
   - Increase the page load wait time to ensure dynamic content loads
   - Check if Carvana has implemented anti-scraping measures

3. **Database Issues**:
   - Verify that the database file exists and has the correct schema
   - Check for SQL syntax errors in the queries
   - Ensure proper foreign key relationships between tables

4. **Browser Automation Issues**:
   - Update DrissionPage to the latest version
   - Ensure Chrome is updated to a compatible version
   - Check for any Chrome extensions that might interfere with automation

## Future Development

Potential enhancements for future versions:

1. **Advanced Filtering**: Implement more complex filtering options based on price, mileage, year, etc.
2. **Detailed Data Extraction**: Extract comprehensive vehicle details beyond just the listing URL
3. **Scheduled Scraping**: Add functionality to run the scraper on a schedule
4. **Proxy Rotation**: Implement multiple VPN/proxy options for better reliability
5. **Data Analysis**: Add tools for analyzing the collected vehicle data
6. **Web Interface**: Create a simple web interface for viewing and filtering the collected data

## License

This project is for educational purposes only. Use responsibly and in accordance with Carvana's terms of service.

## Credits and Acknowledgments

- [DrissionPage](https://github.com/g1879/DrissionPage) - Browser automation library
- [OpenPyXL](https://openpyxl.readthedocs.io/) - Excel file manipulation
- [python-dotenv](https://github.com/theskumar/python-dotenv) - Environment variable management
- [SQLite](https://www.sqlite.org/) - Embedded database engine 