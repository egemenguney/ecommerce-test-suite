"""
Test cases for Login functionality
Tests valid and invalid login scenarios
"""
import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from utils.config import TEST_USERNAME, TEST_PASSWORD


@pytest.mark.login
@pytest.mark.smoke
class TestLogin:
    """
    Test class for login functionality
    Contains test cases for various login scenarios
    """
    
    def test_valid_login(self, driver):
        """
        Test Case: Valid Login
        This test verifies that a user can successfully log in with valid credentials
        
        Steps:
        1. Navigate to login page
        2. Enter valid email and password
        3. Click login button
        4. Verify successful login
        """
        # Initialize LoginPage
        login_page = LoginPage(driver)
        
        # Navigate to login page
        login_page.navigate_to_login()
        
        # Perform login with valid credentials
        login_page.login(TEST_USERNAME, TEST_PASSWORD)
        
        # Assert: Verify login was successful
        assert login_page.is_login_successful(), \
            "Login should be successful with valid credentials"
    
    def test_invalid_email_login(self, driver):
        """
        Test Case: Invalid Email Login
        This test verifies that login fails with invalid email format
        
        Steps:
        1. Navigate to login page
        2. Enter invalid email and valid password
        3. Click login button
        4. Verify error message is displayed
        """
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        
        # Attempt login with invalid email
        login_page.login("invalid_email", TEST_PASSWORD)
        
        # Assert: Verify error message is displayed
        error_displayed = login_page.is_error_message_displayed()
        error_text = login_page.get_error_message_text()
        assert error_displayed, \
            f"Error message should be displayed for invalid email. Current page: {driver.current_url}. Error text found: '{error_text}'"
    
    def test_invalid_password_login(self, driver):
        """
        Test Case: Invalid Password Login
        This test verifies that login fails with incorrect password
        
        Steps:
        1. Navigate to login page
        2. Enter valid email and invalid password
        3. Click login button
        4. Verify error message is displayed
        """
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        
        # Attempt login with invalid password
        login_page.login(TEST_USERNAME, "wrong_password")
        
        # Assert: Verify error message is displayed
        assert login_page.is_error_message_displayed(), \
            "Error message should be displayed for invalid password"
    
    def test_empty_credentials_login(self, driver):
        """
        Test Case: Empty Credentials Login
        This test verifies that login fails when credentials are empty
        
        Steps:
        1. Navigate to login page
        2. Leave email and password fields empty
        3. Click login button
        4. Verify error message or validation is displayed
        """
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        
        # Attempt login with empty credentials
        login_page.login("", "")
        
        # Assert: Verify error message is displayed or form validation prevents submission
        # Note: Behavior may vary based on frontend validation
        error_displayed = login_page.is_error_message_displayed()
        # Some sites may have HTML5 validation that prevents form submission
        # Check if either error is shown OR form validation prevents submission (button might be disabled)
        try:
            login_btn = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"], button[type="submit"]')
            is_button_enabled = login_btn.is_enabled()
        except:
            is_button_enabled = True
        
        assert error_displayed or not is_button_enabled, \
            "Form should not accept empty credentials - either show error or prevent submission"
    
    def test_login_with_special_characters(self, driver):
        """
        Test Case: Login with Special Characters
        This test verifies handling of special characters in credentials
        
        Steps:
        1. Navigate to login page
        2. Enter email with special characters
        3. Click login button
        4. Verify appropriate error handling
        """
        login_page = LoginPage(driver)
        login_page.navigate_to_login()
        
        # Attempt login with special characters
        login_page.login("test@#$%^&*()", "password123")
        
        # Assert: Should handle special characters appropriately
        # Either show error message or login fails (both are acceptable behaviors)
        error_displayed = login_page.is_error_message_displayed()
        login_successful = login_page.is_login_successful()
        
        # System should either reject invalid email (show error) or prevent login
        assert error_displayed or not login_successful, \
            "System should handle special characters in email field - either show error or prevent login"

