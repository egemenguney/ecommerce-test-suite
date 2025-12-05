"""
Checkout Page Object Model
Handles checkout process functionality
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from utils.config import EXPLICIT_WAIT


class CheckoutPage:
    """
    Page Object Model for Checkout Page
    Contains locators and methods for checkout process
    """

    # Billing Details Locators
    FIRST_NAME_INPUT = (By.ID, 'input-payment-firstname')
    LAST_NAME_INPUT = (By.ID, 'input-payment-lastname')
    EMAIL_INPUT = (By.ID, 'input-payment-email')
    TELEPHONE_INPUT = (By.ID, 'input-payment-telephone')
    ADDRESS_INPUT = (By.ID, 'input-payment-address-1')
    CITY_INPUT = (By.ID, 'input-payment-city')
    POSTCODE_INPUT = (By.ID, 'input-payment-postcode')
    COUNTRY_SELECT = (By.ID, 'input-payment-country')
    REGION_SELECT = (By.ID, 'input-payment-zone')
    
    # Shipping Method Locators
    SHIPPING_METHOD_RADIO = (By.CSS_SELECTOR, 'input[name="shipping_method"]')
    FLAT_RATE_OPTION = (By.CSS_SELECTOR, 'input[value="flat.flat"]')
    
    # Payment Method Locators
    PAYMENT_METHOD_RADIO = (By.CSS_SELECTOR, 'input[name="payment_method"]')
    CASH_ON_DELIVERY = (By.CSS_SELECTOR, 'input[value="cod"]')
    
    # Terms and Conditions
    TERMS_CHECKBOX = (By.CSS_SELECTOR, 'input[name="agree"]')
    
    # Buttons
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'input[type="button"][value="Continue"]')
    CONFIRM_ORDER_BUTTON = (By.CSS_SELECTOR, 'input[type="button"][value="Confirm Order"]')
    
    # Success Message
    SUCCESS_MESSAGE = (By.XPATH, '//h1[contains(text(), "Your order has been placed")]')
    ORDER_ID = (By.CSS_SELECTOR, '.order-id')
    
    def __init__(self, driver):
        """
        Initialize CheckoutPage with WebDriver instance

        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)
    
    def fill_billing_details(
        self,
        first_name: str,
        last_name: str,
        email: str,
        telephone: str,
        address: str,
        city: str,
        postcode: str,
        country: str,
        region: str,
    ):
        """
        Fill in billing details form

        Args:
            first_name: First name
            last_name: Last name
            email: Email address
            telephone: Phone number
            address: Street address
            city: City name
            postcode: Postal code
            country: Country name
            region: State/Region name
        """
        # Fill text inputs
        self.wait.until(
            EC.presence_of_element_located(self.FIRST_NAME_INPUT)
        ).send_keys(first_name)
        
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.TELEPHONE_INPUT).send_keys(telephone)
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)
        self.driver.find_element(*self.CITY_INPUT).send_keys(city)
        self.driver.find_element(*self.POSTCODE_INPUT).send_keys(postcode)
        
        # Select country
        country_select = Select(
            self.wait.until(
                EC.presence_of_element_located(self.COUNTRY_SELECT)
            )
        )
        country_select.select_by_visible_text(country)
        
        # Wait for region dropdown to load (depends on country)
        self.wait.until(
            EC.presence_of_element_located(self.REGION_SELECT)
        )
        
        # Select region
        region_select = Select(
            self.driver.find_element(*self.REGION_SELECT)
        )
        region_select.select_by_visible_text(region)
    
    def select_shipping_method(self, method: str = "Flat Rate"):
        """
        Select shipping method

        Args:
            method: Shipping method name (default: "Flat Rate")
        """
        try:
            if method.lower() == "flat rate":
                shipping_option = self.wait.until(
                    EC.element_to_be_clickable(self.FLAT_RATE_OPTION)
                )
                shipping_option.click()
            else:
                # Generic shipping method selection
                shipping_radio = self.wait.until(
                    EC.element_to_be_clickable(self.SHIPPING_METHOD_RADIO)
                )
                shipping_radio.click()
        except:
            pass
    
    def select_payment_method(self, method: str = "Cash On Delivery"):
        """
        Select payment method

        Args:
            method: Payment method name (default: "Cash On Delivery")
        """
        try:
            if method.lower() == "cash on delivery":
                payment_option = self.wait.until(
                    EC.element_to_be_clickable(self.CASH_ON_DELIVERY)
                )
                payment_option.click()
            else:
                # Generic payment method selection
                payment_radio = self.wait.until(
                    EC.element_to_be_clickable(self.PAYMENT_METHOD_RADIO)
                )
                payment_radio.click()
        except:
            pass
    
    def accept_terms_and_conditions(self):
        """
        Accept terms and conditions by checking the checkbox
        """
        terms_checkbox = self.wait.until(
            EC.element_to_be_clickable(self.TERMS_CHECKBOX)
        )
        if not terms_checkbox.is_selected():
            terms_checkbox.click()
    
    def click_continue(self):
        """
        Click continue button to proceed to next step
        """
        continue_btn = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )
        continue_btn.click()
    
    def confirm_order(self):
        """
        Confirm the order by clicking confirm order button
        """
        self.accept_terms_and_conditions()
        confirm_btn = self.wait.until(
            EC.element_to_be_clickable(self.CONFIRM_ORDER_BUTTON)
        )
        confirm_btn.click()
    
    def is_order_successful(self) -> bool:
        """
        Check if order was placed successfully

        Returns:
            True if order success message is displayed, False otherwise
        """
        try:
            success_msg = self.wait.until(
                EC.presence_of_element_located(self.SUCCESS_MESSAGE)
            )
            return success_msg.is_displayed()
        except:
            return False
    
    def get_order_id(self) -> str:
        """
        Get the order ID from success page

        Returns:
            Order ID as string
        """
        try:
            order_id_element = self.wait.until(
                EC.presence_of_element_located(self.ORDER_ID)
            )
            return order_id_element.text
        except:
            return ""
    
    def complete_checkout(
        self,
        billing_details: dict,
        shipping_method: str = "Flat Rate",
        payment_method: str = "Cash On Delivery",
    ):
        """
        Complete the entire checkout process

        Args:
            billing_details: Dictionary containing billing information
            shipping_method: Shipping method to use
            payment_method: Payment method to use
        """
        # Fill billing details
        self.fill_billing_details(**billing_details)
        self.click_continue()
        
        # Select shipping method
        self.select_shipping_method(shipping_method)
        self.click_continue()
        
        # Select payment method
        self.select_payment_method(payment_method)
        self.accept_terms_and_conditions()
        self.confirm_order()

