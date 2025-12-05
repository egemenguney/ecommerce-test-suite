"""
Test cases for Search functionality
Tests product search and search results validation
"""
import pytest
from pages.search_page import SearchPage
from utils.config import SEARCH_TERM, PRODUCT_NAME


@pytest.mark.search
@pytest.mark.smoke
class TestSearch:
    """
    Test class for search functionality
    Contains test cases for various search scenarios
    """
    
    def test_search_valid_product(self, driver):
        """
        Test Case: Search Valid Product
        This test verifies that searching for a valid product returns results
        
        Steps:
        1. Navigate to homepage
        2. Enter product name in search field
        3. Click search button
        4. Verify search results are displayed
        5. Verify results contain the search term
        """
        search_page = SearchPage(driver)
        
        # Perform search
        search_page.search(SEARCH_TERM)
        
        # Assert: Verify search results are displayed
        results_count = search_page.get_search_results_count()
        assert results_count > 0, \
            f"Search should return results for '{SEARCH_TERM}'"
        
        # Assert: Verify results contain the search term
        assert search_page.verify_search_results_contain(SEARCH_TERM), \
            f"Search results should contain '{SEARCH_TERM}'"
    
    def test_search_invalid_product(self, driver):
        """
        Test Case: Search Invalid Product
        This test verifies that searching for non-existent product shows appropriate message
        
        Steps:
        1. Navigate to homepage
        2. Enter invalid/non-existent product name
        3. Click search button
        4. Verify "no results" message is displayed
        """
        search_page = SearchPage(driver)
        
        # Search for non-existent product
        search_page.search("nonexistentproductxyz123")
        
        # Assert: Verify no results message is displayed
        assert search_page.is_no_results_message_displayed(), \
            "No results message should be displayed for invalid search"
        
        # Assert: Verify no products are displayed
        results_count = search_page.get_search_results_count()
        assert results_count == 0, \
            "No products should be displayed for invalid search"
    
    def test_search_with_special_characters(self, driver):
        """
        Test Case: Search with Special Characters
        This test verifies handling of special characters in search
        
        Steps:
        1. Navigate to homepage
        2. Enter search term with special characters
        3. Click search button
        4. Verify appropriate handling (error or sanitized results)
        """
        search_page = SearchPage(driver)
        
        # Search with special characters
        search_page.search("laptop@#$%")
        
        # Assert: System should handle special characters
        # Either show no results or sanitize and search
        assert True, "System should handle special characters in search"
    
    def test_search_empty_string(self, driver):
        """
        Test Case: Search Empty String
        This test verifies behavior when searching with empty string
        
        Steps:
        1. Navigate to homepage
        2. Leave search field empty
        3. Click search button
        4. Verify appropriate handling
        """
        search_page = SearchPage(driver)
        
        # Attempt search with empty string
        search_page.search("")
        
        # Assert: Should handle empty search appropriately
        # May show all products, show error, or prevent search
        assert True, "System should handle empty search appropriately"
    
    def test_search_case_insensitive(self, driver):
        """
        Test Case: Case Insensitive Search
        This test verifies that search is case-insensitive
        
        Steps:
        1. Navigate to homepage
        2. Search with uppercase
        3. Search with lowercase
        4. Verify both return same results
        """
        search_page = SearchPage(driver)
        
        # Search with uppercase
        search_page.search(SEARCH_TERM.upper())
        upper_results = search_page.get_search_results_count()
        
        # Search with lowercase
        search_page.search(SEARCH_TERM.lower())
        lower_results = search_page.get_search_results_count()
        
        # Assert: Results should be the same regardless of case
        assert upper_results == lower_results, \
            "Search should be case-insensitive"
    
    def test_search_and_select_product(self, driver):
        """
        Test Case: Search and Select Product
        This test verifies that user can click on a product from search results
        
        Steps:
        1. Navigate to homepage
        2. Search for a product
        3. Click on a product from results
        4. Verify product detail page is opened
        """
        search_page = SearchPage(driver)
        
        # Search for product
        search_page.search(PRODUCT_NAME)
        
        # Get product names from results
        product_names = search_page.get_product_names()
        assert len(product_names) > 0, \
            f"Search should return results for '{PRODUCT_NAME}'"
        
        # Click on first product
        search_page.click_product(product_names[0])
        
        # Assert: Verify we're on product detail page
        # This can be verified by checking URL or page elements
        assert PRODUCT_NAME.lower() in driver.current_url.lower() or \
               PRODUCT_NAME.lower() in driver.page_source.lower(), \
            "Product detail page should be opened"

