// Products page functionality

// Sample products database
const PRODUCTS = [
    { name: 'Laptop', price: 999.99, category: 'electronics' },
    { name: 'MacBook', price: 1299.99, category: 'electronics' },
    { name: 'iPhone', price: 799.99, category: 'electronics' },
    { name: 'iPad', price: 599.99, category: 'electronics' },
    { name: 'Headphones', price: 199.99, category: 'electronics' },
    { name: 'Keyboard', price: 99.99, category: 'electronics' },
    { name: 'Mouse', price: 49.99, category: 'electronics' },
    { name: 'Monitor', price: 299.99, category: 'electronics' },
];

function displayProducts(products) {
    const grid = document.getElementById('products-grid');
    const noResults = document.getElementById('no-results');
    
    if (products.length === 0) {
        grid.style.display = 'none';
        noResults.style.display = 'block';
        return;
    }
    
    grid.style.display = 'grid';
    noResults.style.display = 'none';
    
    grid.innerHTML = products.map(product => `
        <div class="product-card">
            <h4>${product.name}</h4>
            <p class="price">$${product.price.toFixed(2)}</p>
            <button onclick="addToCart('${product.name}', ${product.price})">Add to Cart</button>
        </div>
    `).join('');
}

function searchProducts(searchTerm) {
    const term = searchTerm.toLowerCase().trim();
    
    if (!term) {
        displayProducts(PRODUCTS);
        return;
    }
    
    const filtered = PRODUCTS.filter(product => 
        product.name.toLowerCase().includes(term)
    );
    
    displayProducts(filtered);
    
    // Update message
    const messageDiv = document.getElementById('search-results-message');
    if (messageDiv) {
        if (filtered.length > 0) {
            messageDiv.textContent = `Found ${filtered.length} product(s) for "${searchTerm}"`;
            messageDiv.className = 'alert alert-success';
        } else {
            messageDiv.textContent = `No products found for "${searchTerm}"`;
            messageDiv.className = 'alert alert-danger';
        }
    }
}

// Handle search form submission
document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.getElementById('search-form');
    const searchInput = document.getElementById('search-input');
    
    // Get search term from URL parameter
    const urlParams = new URLSearchParams(window.location.search);
    const searchParam = urlParams.get('search');
    
    if (searchParam) {
        searchInput.value = searchParam;
        searchProducts(searchParam);
    } else {
        displayProducts(PRODUCTS);
    }
    
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const searchTerm = searchInput.value;
            searchProducts(searchTerm);
        });
    }
});

