# Configuration file template for Location Photo App
# Copy this file to the root directory as 'config.py' and fill in your actual values

# Unsplash API Configuration
# Get your Access Key from: https://unsplash.com/developers
UNSPLASH_ACCESS_KEY = "YOUR_UNSPLASH_ACCESS_KEY_HERE"

# Location search terms based on coordinates (expand as needed)
LOCATION_QUERIES = {
    "urban": ["city", "street", "architecture", "urban", "downtown"],
    "nature": ["nature", "landscape", "forest", "mountains", "wilderness"],
    "coastal": ["beach", "ocean", "coast", "sea", "waves"],
    "desert": ["desert", "sand", "arid", "dunes"],
    "rural": ["countryside", "farm", "village", "pastoral"],
    "tropical": ["tropical", "palm", "paradise", "island"]
}

# GPS Settings
GPS_TIMEOUT = 30  # seconds
GPS_ACCURACY = 100  # meters

# App Settings
DEFAULT_QUERY = "landscape"
IMAGE_CACHE_SIZE = 10