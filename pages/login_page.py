"""
Login Page Object Model
Handles all interactions with the login page
"""
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.config import BASE_URL, EXPLICIT_WAIT


class LoginPage:
    """
    Page Object Model for Login Page
    Contains locators and methods for login functionality
    """

    # Locators - Using common e-commerce patterns
    # Note: These selectors may need adjustment based on actual site structure
    EMAIL_INPUT = (By.ID, 'input-email')
    PASSWORD_INPUT = (By.ID, 'input-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"][value="Login"]')
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, 'Forgotten Password')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '.alert-danger')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')
    
    def __init__(self, driver):
        """
        Initialize LoginPage with WebDriver instance

        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)
        self.short_wait = WebDriverWait(
            driver, 3
        )  # Shorter wait for quick selector attempts
    
    def _find_element_with_selectors(
        self, selectors, condition=EC.presence_of_element_located
    ):
        """
        Helper method to find element using multiple selector strategies

        Args:
            selectors: List of (By, value) tuples
            condition: Expected condition to use (default: presence_of_element_located)

        Returns:
            WebElement if found, None otherwise
        """
        for selector in selectors:
            try:
                return self.short_wait.until(condition(selector))
            except TimeoutException:
                continue
        return None
    
    def navigate_to_login(self):
        """
        Navigate to login page
        This method assumes there's a login link/button on the homepage
        """
        # Try multiple strategies to navigate to login page
        try:
            # Strategy 1: Look for "Login" link
            login_link = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            login_link.click()
        except TimeoutException:
            try:
                # Strategy 2: Look for "My Account" link and click Login from dropdown
                account_link = self.wait.until(
                    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "My Account"))
                )
                account_link.click()
                # Wait a bit for dropdown to appear, then click Login
                login_link = self.wait.until(
                    EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
                )
                login_link.click()
            except TimeoutException:
                # Strategy 3: Direct navigation to login URL
                # Try multiple URL patterns
                base = BASE_URL.rstrip("/")
                login_urls = [
                    f"{base}/index.php?route=account/login",
                    f"{base}/account/login",
                    f"{base}/login",
                ]

                for login_url in login_urls:
                    try:
                        self.driver.get(login_url)
                        # Wait a bit and check if login form elements exist
                        try:

                            def has_login_form(driver):
                                selectors = [
                                    'input[type="email"]',
                                    'input[name="email"]',
                                    'input[type="password"]',
                                    'input[id*="email"]',
                                    'input[id*="password"]',
                                ]
                                for sel in selectors:
                                    if len(driver.find_elements(By.CSS_SELECTOR, sel)) > 0:
                                        return True
                                return False

                            self.short_wait.until(has_login_form)
                            break
                        except TimeoutException:
                            continue
                    except Exception:
                        continue

        # Wait for page to load completely
        self.wait.until(
            lambda driver: driver.execute_script("return document.readyState")
            == "complete"
        )

        # Wait for login page to load by checking for email field with multiple selectors
        email_selectors = [
            (By.ID, "input-email"),
            (By.NAME, "email"),
            (By.CSS_SELECTOR, 'input[type="email"]'),
            (By.CSS_SELECTOR, 'input[name="email"]'),
        ]
        email_field = self._find_element_with_selectors(email_selectors)
        if not email_field:
            # If still not found, wait with full timeout using first selector
            self.wait.until(EC.presence_of_element_located((By.ID, "input-email")))
    
    def enter_email(self, email: str):
        """
        Enter email address in the email input field

        Args:
            email: Email address to enter
        """
        selectors = [
            (By.ID, "input-email"),
            (By.NAME, "email"),
            (By.CSS_SELECTOR, 'input[type="email"]'),
            (By.CSS_SELECTOR, 'input[name="email"]'),
            (By.XPATH, '//input[@type="email"]'),
            (By.XPATH, '//input[contains(@name, "email")]'),
        ]

        email_field = self._find_element_with_selectors(selectors)
        if not email_field:
            # Fallback: try with full timeout on first selector
            email_field = self.wait.until(EC.presence_of_element_located(selectors[0]))

        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password: str):
        """
        Enter password in the password input field

        Args:
            password: Password to enter
        """
        selectors = [
            (By.ID, "input-password"),
            (By.NAME, "password"),
            (By.CSS_SELECTOR, 'input[type="password"]'),
            (By.CSS_SELECTOR, 'input[name="password"]'),
            (By.XPATH, '//input[@type="password"]'),
            (By.XPATH, '//input[contains(@name, "password")]'),
        ]

        password_field = self._find_element_with_selectors(selectors)
        if not password_field:
            # Fallback: try with full timeout on first selector
            password_field = self.wait.until(
                EC.presence_of_element_located(selectors[0])
            )

        password_field.clear()
        password_field.send_keys(password)
    
    def click_login_button(self):
        """
        Click the login button
        """
        selectors = [
            (By.CSS_SELECTOR, 'input[type="submit"][value="Login"]'),
            (By.CSS_SELECTOR, 'button[type="submit"]'),
            (By.CSS_SELECTOR, 'input[type="submit"]'),
            (By.XPATH, '//input[@type="submit" and contains(@value, "Login")]'),
            (By.XPATH, '//button[contains(text(), "Login")]'),
            (By.CSS_SELECTOR, "button.btn-primary"),
            (By.CSS_SELECTOR, "input.btn-primary"),
        ]

        login_btn = self._find_element_with_selectors(
            selectors, EC.element_to_be_clickable
        )
        if not login_btn:
            # Fallback: try with full timeout on first selector
            login_btn = self.wait.until(EC.element_to_be_clickable(selectors[0]))

        login_btn.click()

    def login(self, email: str, password: str):
        """
        Complete login flow: enter credentials and submit

        Args:
            email: Email address
            password: Password
        """
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

        # Wait for page to process login (either success or error)
        time.sleep(1)  # Brief wait for form submission
        self.wait.until(
            lambda driver: driver.execute_script("return document.readyState")
            == "complete"
        )
    
    def is_error_message_displayed(self) -> bool:
        """
        Check if error message is displayed after failed login

        Returns:
            True if error message is visible, False otherwise
        """
        # Try multiple selector strategies for error messages
        error_selectors = [
            (By.CSS_SELECTOR, ".alert-danger"),
            (By.CSS_SELECTOR, ".alert.alert-danger"),
            (By.CSS_SELECTOR, ".text-danger"),
            (By.CSS_SELECTOR, ".error"),
            (By.CSS_SELECTOR, '[class*="error"]'),
            (By.CSS_SELECTOR, '[class*="danger"]'),
            (
                By.XPATH,
                '//div[contains(@class, "alert") and contains(@class, "danger")]',
            ),
            (By.XPATH, '//div[contains(@class, "error")]'),
            (By.XPATH, '//*[contains(text(), "Warning")]'),
            (By.XPATH, '//*[contains(text(), "No match")]'),
            (By.XPATH, '//*[contains(text(), "incorrect")]'),
            (By.XPATH, '//*[contains(text(), "invalid")]'),
        ]

        # Try with short wait first
        error_element = self._find_element_with_selectors(
            error_selectors, EC.presence_of_element_located
        )

        if error_element:
            return error_element.is_displayed()

        # Fallback: try with full timeout on first selector
        try:
            error_msg = self.wait.until(
                EC.presence_of_element_located(self.ERROR_MESSAGE)
            )
            return error_msg.is_displayed()
        except TimeoutException:
            return False

    def get_error_message_text(self) -> str:
        """
        Get the text of error message

        Returns:
            Error message text
        """
        error_selectors = [
            (By.CSS_SELECTOR, ".alert-danger"),
            (By.CSS_SELECTOR, ".alert.alert-danger"),
            (By.CSS_SELECTOR, ".text-danger"),
            (By.CSS_SELECTOR, ".error"),
            (By.CSS_SELECTOR, '[class*="error"]'),
            (By.CSS_SELECTOR, '[class*="danger"]'),
            (
                By.XPATH,
                '//div[contains(@class, "alert") and contains(@class, "danger")]',
            ),
            (By.XPATH, '//div[contains(@class, "error")]'),
        ]

        error_element = self._find_element_with_selectors(
            error_selectors, EC.presence_of_element_located
        )

        if error_element:
            return error_element.text

        # Fallback
        try:
            error_msg = self.wait.until(
                EC.presence_of_element_located(self.ERROR_MESSAGE)
            )
            return error_msg.text
        except Exception:
            return ""
    
    def is_login_successful(self) -> bool:
        """
        Check if login was successful by looking for success indicators
        Common indicators: account page, welcome message, logout link

        Returns:
            True if login successful, False otherwise
        """
        try:
            # Check for common success indicators
            # Adjust these selectors based on actual site structure
            success_indicators = [
                (By.LINK_TEXT, "Logout"),
                (By.PARTIAL_LINK_TEXT, "My Account"),
                (By.CSS_SELECTOR, ".alert-success"),
            ]

            for locator in success_indicators:
                try:
                    element = self.wait.until(EC.presence_of_element_located(locator))
                    if element.is_displayed():
                        return True
                except Exception:
                    continue
            return False
        except Exception:
            return False

