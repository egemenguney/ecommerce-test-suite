// Global application JavaScript

// Cart management using localStorage
const CART_KEY = 'demo_ecommerce_cart';

function getCart() {
    const cart = localStorage.getItem(CART_KEY);
    return cart ? JSON.parse(cart) : [];
}

function saveCart(cart) {
    localStorage.setItem(CART_KEY, JSON.stringify(cart));
}

function addToCart(productName, price) {
    const cart = getCart();
    const existingItem = cart.find(item => item.name === productName);
    
    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        cart.push({
            name: productName,
            price: price,
            quantity: 1
        });
    }
    
    saveCart(cart);
    updateCartCount();
    
    // Show notification
    alert(`${productName} added to cart!`);
}

function removeFromCart(index) {
    const cart = getCart();
    cart.splice(index, 1);
    saveCart(cart);
    updateCartCount();
    if (typeof loadCart === 'function') {
        loadCart();
    }
}

function updateCartQuantity(index, quantity) {
    const cart = getCart();
    if (quantity <= 0) {
        removeFromCart(index);
    } else {
        cart[index].quantity = quantity;
        saveCart(cart);
        if (typeof loadCart === 'function') {
            loadCart();
        }
    }
}

function updateCartCount() {
    const cart = getCart();
    const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
    const cartCountElements = document.querySelectorAll('#cart-count');
    cartCountElements.forEach(el => {
        el.textContent = totalItems;
    });
}

function clearCart() {
    localStorage.removeItem(CART_KEY);
    updateCartCount();
}

// Update cart count on page load
document.addEventListener('DOMContentLoaded', function() {
    updateCartCount();
    
    // Update account menu based on login status
    const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true';
    const loginLink = document.getElementById('login-link');
    const accountLink = document.getElementById('account-link');
    
    if (isLoggedIn && loginLink) {
        loginLink.textContent = 'My Account';
        loginLink.href = 'account.html';
    }
});

