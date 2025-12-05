// Cart page functionality

function loadCart() {
    const cart = getCart();
    const tableBody = document.getElementById('cart-table-body');
    const emptyCart = document.getElementById('empty-cart');
    const cartItems = document.getElementById('cart-items');
    const cartActions = document.getElementById('cart-actions');
    
    if (cart.length === 0) {
        cartItems.style.display = 'none';
        cartActions.style.display = 'none';
        emptyCart.style.display = 'block';
        return;
    }
    
    cartItems.style.display = 'block';
    cartActions.style.display = 'flex';
    emptyCart.style.display = 'none';
    
    tableBody.innerHTML = cart.map((item, index) => {
        const total = (item.price * item.quantity).toFixed(2);
        return `
            <tr>
                <td>${item.name}</td>
                <td>
                    <input type="number" 
                           value="${item.quantity}" 
                           min="1" 
                           onchange="updateCartQuantity(${index}, parseInt(this.value))"
                           style="width: 60px; padding: 0.5rem;">
                </td>
                <td>$${item.price.toFixed(2)}</td>
                <td>$${total}</td>
                <td>
                    <button onclick="removeFromCart(${index})" 
                            style="background-color: #dc3545; padding: 0.5rem 1rem;">
                        Remove
                    </button>
                </td>
            </tr>
        `;
    }).join('');
    
    // Update total
    const total = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    document.getElementById('cart-total').innerHTML = `<strong>$${total.toFixed(2)}</strong>`;
}

// Load cart on page load
document.addEventListener('DOMContentLoaded', function() {
    loadCart();
    
    // Check if cart is empty and redirect if trying to checkout
    const cart = getCart();
    if (cart.length === 0 && window.location.pathname.includes('checkout')) {
        window.location.href = 'cart.html';
    }
});

