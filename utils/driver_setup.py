"""
Driver setup utility for Selenium WebDriver
Handles browser initialization and configuration
"""
import os
from typing import Optional
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utils.config import BROWSER, HEADLESS, IMPLICIT_WAIT, BASE_URL


def _get_chromedriver_path():
    """
    Get the correct chromedriver executable path.
    Fixes issue where webdriver-manager returns wrong file path on Windows.
    
    Returns:
        str: Path to chromedriver.exe
    """
    driver_path = ChromeDriverManager().install()
    
    # Normalize path separators
    driver_path = os.path.normpath(driver_path)
    
    # Check if path exists and is a file
    if os.path.isfile(driver_path) and driver_path.endswith('.exe'):
        return driver_path
    
    # If path is a directory or wrong file, search for chromedriver.exe
    if os.path.isdir(driver_path):
        search_dir = driver_path
    else:
        search_dir = os.path.dirname(driver_path)
    
    # Look for chromedriver.exe in the directory
    for root, dirs, files in os.walk(search_dir):
        for file in files:
            if file == 'chromedriver.exe':
                return os.path.join(root, file)
    
    # Fallback: try common locations
    possible_paths = [
        os.path.join(search_dir, 'chromedriver.exe'),
        os.path.join(os.path.dirname(search_dir), 'chromedriver.exe'),
    ]
    
    for path in possible_paths:
        if os.path.isfile(path):
            return path
    
    # If all else fails, return original path (might work on non-Windows)
    return driver_path


from typing import Optional

def create_driver(browser_name: Optional[str] = None, headless: Optional[bool] = None):
    """
    Create and configure a WebDriver instance
    
    Args:
        browser_name: Browser to use (chrome, firefox, edge). Defaults to config.
        headless: Run in headless mode. Defaults to config.
    
    Returns:
        WebDriver instance
    """
    browser = browser_name or BROWSER
    is_headless = headless if headless is not None else HEADLESS
    
    driver = None
    
    if browser.lower() == 'chrome':
        chrome_options = ChromeOptions()
        if is_headless:
            chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        driver_path = _get_chromedriver_path()
        service = ChromeService(driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
    
    elif browser.lower() == 'firefox':
        firefox_options = FirefoxOptions()
        if is_headless:
            firefox_options.add_argument('--headless')
        
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=firefox_options)
    
    elif browser.lower() == 'edge':
        edge_options = EdgeOptions()
        if is_headless:
            edge_options.add_argument('--headless')
        
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=edge_options)
    
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    
    # Set implicit wait
    driver.implicitly_wait(IMPLICIT_WAIT)
    
    # Maximize window
    driver.maximize_window()
    
    # Navigate to base URL
    driver.get(BASE_URL)
    
    return driver


def quit_driver(driver):
    """
    Safely quit the WebDriver instance
    
    Args:
        driver: WebDriver instance to quit
    """
    if driver:
        try:
            driver.quit()
        except Exception as e:
            print(f"Error quitting driver: {e}")

