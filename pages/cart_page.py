"""
Cart Page Object Model
Handles shopping cart functionality
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.config import EXPLICIT_WAIT


class CartPage:
    """
    Page Object Model for Shopping Cart Page
    Contains locators and methods for cart operations
    """
    
    # Locators
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'button[onclick*="cart.add"]')
    CART_ICON = (By.CSS_SELECTOR, '#cart')
    CART_ITEMS = (By.CSS_SELECTOR, '.table tbody tr')
    REMOVE_BUTTON = (By.CSS_SELECTOR, 'button[data-original-title="Remove"]')
    UPDATE_QUANTITY_INPUT = (By.CSS_SELECTOR, 'input[type="text"][name*="quantity"]')
    UPDATE_BUTTON = (By.CSS_SELECTOR, 'button[data-original-title="Update"]')
    EMPTY_CART_MESSAGE = (By.XPATH, '//p[contains(text(), "Your shopping cart is empty")]')
    CART_TOTAL = (By.CSS_SELECTOR, '.table tfoot tr:last-child td:last-child')
    CHECKOUT_BUTTON = (By.LINK_TEXT, 'Checkout')
    CONTINUE_SHOPPING_BUTTON = (By.LINK_TEXT, 'Continue Shopping')
    
    def __init__(self, driver):
        """
        Initialize CartPage with WebDriver instance

        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)
    
    def add_product_to_cart(self):
        """
        Add product to cart from product page
        This method assumes we're on a product detail page
        """
        add_to_cart_btn = self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
        )
        add_to_cart_btn.click()
    
    def open_cart(self):
        """
        Open shopping cart by clicking cart icon
        """
        cart_icon = self.wait.until(
            EC.element_to_be_clickable(self.CART_ICON)
        )
        cart_icon.click()
    
    def get_cart_items_count(self) -> int:
        """
        Get the number of items in the cart

        Returns:
            Number of items in cart
        """
        try:
            items = self.wait.until(
                EC.presence_of_all_elements_located(self.CART_ITEMS)
            )
            return len(items)
        except Exception:
            return 0
    
    def remove_item_from_cart(self, item_index: int = 0):
        """
        Remove an item from cart by index

        Args:
            item_index: Index of item to remove (default: 0 for first item)
        """
        try:
            remove_buttons = self.wait.until(
                EC.presence_of_all_elements_located(self.REMOVE_BUTTON)
            )
            if item_index < len(remove_buttons):
                remove_buttons[item_index].click()
        except Exception:
            # Alternative: Remove by product name if available
            pass
    
    def update_quantity(self, quantity: int, item_index: int = 0):
        """
        Update quantity of an item in cart

        Args:
            quantity: New quantity value
            item_index: Index of item to update (default: 0)
        """
        try:
            quantity_inputs = self.wait.until(
                EC.presence_of_all_elements_located(self.UPDATE_QUANTITY_INPUT)
            )
            if item_index < len(quantity_inputs):
                quantity_inputs[item_index].clear()
                quantity_inputs[item_index].send_keys(str(quantity))

                # Click update button
                update_btn = self.wait.until(
                    EC.element_to_be_clickable(self.UPDATE_BUTTON)
                )
                update_btn.click()
        except Exception:
            pass
    
    def is_cart_empty(self) -> bool:
        """
        Check if cart is empty

        Returns:
            True if cart is empty, False otherwise
        """
        try:
            empty_message = self.wait.until(
                EC.presence_of_element_located(self.EMPTY_CART_MESSAGE)
            )
            return empty_message.is_displayed()
        except Exception:
            # If empty message not found, check item count
            return self.get_cart_items_count() == 0
    
    def get_cart_total(self) -> str:
        """
        Get the total price of items in cart

        Returns:
            Cart total as string
        """
        try:
            total_element = self.wait.until(
                EC.presence_of_element_located(self.CART_TOTAL)
            )
            return total_element.text
        except Exception:
            return ""
    
    def click_checkout(self):
        """
        Click checkout button to proceed to checkout
        """
        checkout_btn = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        checkout_btn.click()
    
    def click_continue_shopping(self):
        """
        Click continue shopping button
        """
        continue_btn = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_SHOPPING_BUTTON)
        )
        continue_btn.click()
    
    def verify_product_in_cart(self, product_name: str) -> bool:
        """
        Verify that a specific product is in the cart

        Args:
            product_name: Name of product to verify

        Returns:
            True if product is in cart, False otherwise
        """
        try:
            # Look for product name in cart items
            product_element = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, f'//td[contains(text(), "{product_name}")]')
                )
            )
            return product_element.is_displayed()
        except Exception:
            return False

