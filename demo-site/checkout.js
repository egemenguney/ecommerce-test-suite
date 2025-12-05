// Checkout page functionality

document.addEventListener('DOMContentLoaded', function() {
    const cart = getCart();
    
    // Redirect if cart is empty
    if (cart.length === 0) {
        alert('Your cart is empty!');
        window.location.href = 'cart.html';
        return;
    }
    
    // Pre-fill email if logged in
    const userEmail = localStorage.getItem('userEmail');
    if (userEmail) {
        const emailInput = document.getElementById('input-payment-email');
        if (emailInput) {
            emailInput.value = userEmail;
        }
    }
    
    // Handle form submission
    const checkoutForm = document.getElementById('checkout-form');
    checkoutForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Check if terms are accepted
        const termsCheckbox = document.getElementById('terms-checkbox');
        if (!termsCheckbox.checked) {
            alert('Please accept the Terms and Conditions to proceed.');
            return;
        }
        
        // Get form data
        const formData = {
            firstname: document.getElementById('input-payment-firstname').value,
            lastname: document.getElementById('input-payment-lastname').value,
            email: document.getElementById('input-payment-email').value,
            telephone: document.getElementById('input-payment-telephone').value,
            address: document.getElementById('input-payment-address-1').value,
            city: document.getElementById('input-payment-city').value,
            postcode: document.getElementById('input-payment-postcode').value,
            country: document.getElementById('input-payment-country').value,
            zone: document.getElementById('input-payment-zone').value,
        };
        
        // Generate order ID
        const orderId = 'ORD-' + Date.now();
        
        // Store order info (for demo purposes)
        localStorage.setItem('lastOrderId', orderId);
        localStorage.setItem('lastOrderData', JSON.stringify(formData));
        
        // Clear cart
        clearCart();
        
        // Redirect to success page
        window.location.href = 'success.html?order=' + orderId;
    });
});

