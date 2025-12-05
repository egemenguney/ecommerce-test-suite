"""
Search Page Object Model
Handles product search functionality
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from utils.config import EXPLICIT_WAIT


class SearchPage:
    """
    Page Object Model for Search Page
    Contains locators and methods for search functionality
    """
    
    # Locators
    SEARCH_INPUT = (By.NAME, 'search')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[type="button"] i.fa-search')
    SEARCH_RESULTS = (By.CSS_SELECTOR, '.product-layout')
    NO_RESULTS_MESSAGE = (By.XPATH, '//p[contains(text(), "There is no product")]')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product-layout h4 a')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.price')
    SORT_DROPDOWN = (By.ID, 'input-sort')
    
    def __init__(self, driver):
        """
        Initialize SearchPage with WebDriver instance
        
        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)
    
    def enter_search_term(self, search_term: str):
        """
        Enter search term in the search input field
        
        Args:
            search_term: Product name or keyword to search
        """
        search_input = self.wait.until(
            EC.presence_of_element_located(self.SEARCH_INPUT)
        )
        search_input.clear()
        search_input.send_keys(search_term)
    
    def click_search_button(self):
        """
        Click the search button
        """
        search_btn = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        )
        search_btn.click()
    
    def search(self, search_term: str):
        """
        Complete search flow: enter term and submit
        
        Args:
            search_term: Product name or keyword to search
        """
        self.enter_search_term(search_term)
        self.click_search_button()
    
    def search_with_enter(self, search_term: str):
        """
        Search by pressing Enter key instead of clicking button
        
        Args:
            search_term: Product name or keyword to search
        """
        search_input = self.wait.until(
            EC.presence_of_element_located(self.SEARCH_INPUT)
        )
        search_input.clear()
        search_input.send_keys(search_term)
        search_input.send_keys(Keys.RETURN)
    
    def get_search_results_count(self) -> int:
        """
        Get the number of search results displayed
        
        Returns:
            Number of search results
        """
        try:
            results = self.wait.until(
                EC.presence_of_all_elements_located(self.SEARCH_RESULTS)
            )
            return len(results)
        except:
            return 0
    
    def is_no_results_message_displayed(self) -> bool:
        """
        Check if "no results" message is displayed
        
        Returns:
            True if no results message is visible, False otherwise
        """
        try:
            no_results = self.wait.until(
                EC.presence_of_element_located(self.NO_RESULTS_MESSAGE)
            )
            return no_results.is_displayed()
        except:
            return False
    
    def get_product_names(self) -> list:
        """
        Get list of product names from search results
        
        Returns:
            List of product names
        """
        try:
            product_elements = self.wait.until(
                EC.presence_of_all_elements_located(self.PRODUCT_NAME)
            )
            return [product.text for product in product_elements]
        except:
            return []
    
    def click_product(self, product_name: str):
        """
        Click on a specific product by name
        
        Args:
            product_name: Name of the product to click
        """
        try:
            product_link = self.wait.until(
                EC.element_to_be_clickable(
                    (By.LINK_TEXT, product_name)
                )
            )
            product_link.click()
        except:
            # Fallback: Try partial link text
            product_link = self.wait.until(
                EC.element_to_be_clickable(
                    (By.PARTIAL_LINK_TEXT, product_name)
                )
            )
            product_link.click()
    
    def sort_results(self, sort_option: str):
        """
        Sort search results by given option
        
        Args:
            sort_option: Sort option (e.g., "Price (Low > High)")
        """
        try:
            sort_dropdown = Select(
                self.wait.until(
                    EC.presence_of_element_located(self.SORT_DROPDOWN)
                )
            )
            sort_dropdown.select_by_visible_text(sort_option)
        except:
            # If dropdown doesn't exist, skip sorting
            pass
    
    def verify_search_results_contain(self, search_term: str) -> bool:
        """
        Verify that search results contain the search term
        
        Args:
            search_term: Term to verify in results
        
        Returns:
            True if results contain the term, False otherwise
        """
        product_names = self.get_product_names()
        search_term_lower = search_term.lower()
        
        # Check if any product name contains the search term
        for product_name in product_names:
            if search_term_lower in product_name.lower():
                return True
        return False

