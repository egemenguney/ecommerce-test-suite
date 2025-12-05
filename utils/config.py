"""
Configuration file for E-commerce Test Suite
Contains environment variables, URLs, and test data
"""
import os
from typing import Final
from dotenv import load_dotenv

# Note: Final type hint requires Python 3.8+
# For older Python versions, remove Final annotations

# Load environment variables from .env file
load_dotenv()

# Base URL for the e-commerce site
# Default: local demo site (run: python -m http.server 8000 in demo-site folder)
BASE_URL: Final[str] = os.getenv('BASE_URL', 'http://localhost:8000/')

# Test credentials
TEST_USERNAME: Final[str] = os.getenv('TEST_USERNAME', 'test@example.com')
TEST_PASSWORD: Final[str] = os.getenv('TEST_PASSWORD', 'test123')

# Browser configuration
BROWSER: Final[str] = os.getenv('BROWSER', 'chrome')  # chrome, firefox, edge
HEADLESS: Final[bool] = os.getenv('HEADLESS', 'False').lower() == 'true'
IMPLICIT_WAIT: Final[int] = int(os.getenv('IMPLICIT_WAIT', '10'))
EXPLICIT_WAIT: Final[int] = int(os.getenv('EXPLICIT_WAIT', '20'))

# Screenshot configuration
SCREENSHOT_DIR: Final[str] = os.getenv('SCREENSHOT_DIR', 'screenshots')
SCREENSHOT_ON_FAILURE: Final[bool] = os.getenv('SCREENSHOT_ON_FAILURE', 'True').lower() == 'true'

# Test data
SEARCH_TERM: Final[str] = 'laptop'
PRODUCT_NAME: Final[str] = 'MacBook'

