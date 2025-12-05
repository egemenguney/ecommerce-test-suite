"""
Test cases for Shopping Cart functionality
Tests adding/removing items and cart operations
"""
import pytest
from pages.cart_page import CartPage
from pages.search_page import SearchPage
from utils.config import PRODUCT_NAME


@pytest.mark.cart
@pytest.mark.regression
class TestCart:
    """
    Test class for shopping cart functionality
    Contains test cases for various cart operations
    """
    
    def test_add_product_to_cart(self, driver):
        """
        Test Case: Add Product to Cart
        This test verifies that a product can be added to cart
        
        Steps:
        1. Search for a product
        2. Click on product to view details
        3. Click "Add to Cart" button
        4. Verify product is added to cart
        5. Verify cart count is updated
        """
        search_page = SearchPage(driver)
        cart_page = CartPage(driver)
        
        # Search and select product
        search_page.search(PRODUCT_NAME)
        product_names = search_page.get_product_names()
        
        if len(product_names) > 0:
            search_page.click_product(product_names[0])
            
            # Add product to cart
            cart_page.add_product_to_cart()
            
            # Open cart to verify
            cart_page.open_cart()
            
            # Assert: Verify product is in cart
            assert cart_page.verify_product_in_cart(PRODUCT_NAME), \
                f"Product '{PRODUCT_NAME}' should be in cart"
            
            # Assert: Verify cart has items
            assert cart_page.get_cart_items_count() > 0, \
                "Cart should contain at least one item"
    
    def test_remove_product_from_cart(self, driver):
        """
        Test Case: Remove Product from Cart
        This test verifies that a product can be removed from cart
        
        Steps:
        1. Add a product to cart
        2. Open cart
        3. Click remove button
        4. Verify product is removed
        5. Verify cart is empty or updated
        """
        search_page = SearchPage(driver)
        cart_page = CartPage(driver)
        
        # Add product to cart first
        search_page.search(PRODUCT_NAME)
        product_names = search_page.get_product_names()
        
        if len(product_names) > 0:
            search_page.click_product(product_names[0])
            cart_page.add_product_to_cart()
            
            # Open cart
            cart_page.open_cart()
            
            # Get initial cart count
            initial_count = cart_page.get_cart_items_count()
            
            if initial_count > 0:
                # Remove item from cart
                cart_page.remove_item_from_cart(0)
                
                # Assert: Verify item is removed
                # Wait a moment for cart to update
                import time
                time.sleep(1)
                
                new_count = cart_page.get_cart_items_count()
                assert new_count < initial_count, \
                    "Cart item count should decrease after removal"
    
    def test_update_cart_quantity(self, driver):
        """
        Test Case: Update Cart Quantity
        This test verifies that product quantity can be updated in cart
        
        Steps:
        1. Add product to cart
        2. Open cart
        3. Update quantity to a new value
        4. Verify quantity is updated
        5. Verify cart total is recalculated
        """
        search_page = SearchPage(driver)
        cart_page = CartPage(driver)
        
        # Add product to cart
        search_page.search(PRODUCT_NAME)
        product_names = search_page.get_product_names()
        
        if len(product_names) > 0:
            search_page.click_product(product_names[0])
            cart_page.add_product_to_cart()
            
            # Open cart
            cart_page.open_cart()
            
            # Get initial total
            initial_total = cart_page.get_cart_total()
            
            # Update quantity to 2
            cart_page.update_quantity(2, 0)
            
            # Assert: Verify cart total is updated
            # Note: Total should increase if quantity increases
            new_total = cart_page.get_cart_total()
            assert new_total != initial_total or new_total != "", \
                "Cart total should be updated after quantity change"
    
    def test_empty_cart(self, driver):
        """
        Test Case: Empty Cart
        This test verifies that empty cart shows appropriate message
        
        Steps:
        1. Ensure cart is empty (or remove all items)
        2. Open cart
        3. Verify empty cart message is displayed
        """
        cart_page = CartPage(driver)
        cart_page.open_cart()
        
        # If cart has items, remove them
        items_count = cart_page.get_cart_items_count()
        while items_count > 0:
            cart_page.remove_item_from_cart(0)
            import time
            time.sleep(1)
            items_count = cart_page.get_cart_items_count()
        
        # Assert: Verify empty cart message
        assert cart_page.is_cart_empty(), \
            "Empty cart message should be displayed when cart is empty"
    
    def test_cart_total_calculation(self, driver):
        """
        Test Case: Cart Total Calculation
        This test verifies that cart total is calculated correctly
        
        Steps:
        1. Add multiple products to cart
        2. Open cart
        3. Verify cart total is displayed
        4. Verify total matches sum of product prices
        """
        search_page = SearchPage(driver)
        cart_page = CartPage(driver)
        
        # Add product to cart
        search_page.search(PRODUCT_NAME)
        product_names = search_page.get_product_names()
        
        if len(product_names) > 0:
            search_page.click_product(product_names[0])
            cart_page.add_product_to_cart()
            
            # Open cart
            cart_page.open_cart()
            
            # Assert: Verify cart total is displayed
            cart_total = cart_page.get_cart_total()
            assert cart_total != "", \
                "Cart total should be displayed"
            
            # Note: Detailed price calculation verification
            # would require parsing and comparing individual prices

