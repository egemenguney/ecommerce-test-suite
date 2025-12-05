"""
Pytest configuration file
Contains fixtures and test setup/teardown
"""
import os

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from utils.config import BROWSER, HEADLESS
from utils.driver_setup import create_driver, quit_driver


def pytest_addoption(parser):
    """
    Add custom command line options for pytest
    """
    parser.addoption(
        "--browser",
        action="store",
        default=None,
        help="Browser to use for tests (chrome, firefox, edge). Overrides BROWSER env var.",
    )


@pytest.fixture(scope="function")
def driver(request):
    """
    Fixture to create and manage WebDriver instance
    Creates a new driver for each test and quits after test completion

    Yields:
        WebDriver instance
    """
    # Get browser from CLI argument or use default from config
    browser_arg = request.config.getoption("--browser")
    browser_name = browser_arg if browser_arg else None

    driver = None
    try:
        # Create driver instance with optional browser override
        driver = create_driver(browser_name=browser_name)
        yield driver
    finally:
        # Cleanup: Quit driver after test
        if driver:
            quit_driver(driver)


@pytest.fixture(scope="session")
def session_driver(request):
    """
    Fixture to create a WebDriver instance for the entire test session
    Use this for tests that need to maintain state across multiple test functions

    Yields:
        WebDriver instance
    """
    # Get browser from CLI argument or use default from config
    browser_arg = request.config.getoption("--browser")
    browser_name = browser_arg if browser_arg else None

    driver = None
    try:
        driver = create_driver(browser_name=browser_name)
        yield driver
    finally:
        if driver:
            quit_driver(driver)


@pytest.fixture(autouse=True)
def setup_screenshot_dir():
    """
    Auto-use fixture to create screenshot directory if it doesn't exist
    """
    screenshot_dir = "screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    yield
    # Cleanup can be added here if needed


def pytest_configure(config):
    """
    Pytest configuration hook
    Can be used to add custom markers, configure plugins, etc.
    """
    # Register custom markers
    config.addinivalue_line(
        "markers", "smoke: marks tests as smoke tests"
    )
    config.addinivalue_line(
        "markers", "regression: marks tests as regression tests"
    )
    config.addinivalue_line(
        "markers", "login: marks tests related to login functionality"
    )
    config.addinivalue_line(
        "markers", "search: marks tests related to search functionality"
    )
    config.addinivalue_line(
        "markers", "cart: marks tests related to cart functionality"
    )
    config.addinivalue_line(
        "markers", "checkout: marks tests related to checkout functionality"
    )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture screenshot on test failure
    """
    outcome = yield
    rep = outcome.get_result()

    # Check if test failed and screenshot is enabled
    if rep.when == "call" and rep.failed:
        # Get driver from fixture if available
        if "driver" in item.fixturenames:
            driver = item.funcargs.get("driver")
            if driver:
                screenshot_path = f"screenshots/{item.name}_failure.png"
                try:
                    driver.save_screenshot(screenshot_path)
                    print(f"\nScreenshot saved: {screenshot_path}")
                except Exception as e:
                    print(f"\nFailed to save screenshot: {e}")

