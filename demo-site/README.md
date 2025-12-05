# Demo E-commerce Site

A simple static HTML/CSS/JavaScript e-commerce demo site for testing automation scripts.

## Features

- **Login System**: Simple authentication with demo credentials
- **Product Search**: Search functionality with product database
- **Shopping Cart**: Add/remove items, update quantities
- **Checkout Process**: Complete checkout flow with form validation
- **Responsive Design**: Works on desktop and mobile devices

## Demo Credentials

- **Email**: `test@example.com`
- **Password**: `test123`

## Pages

1. **index.html** - Homepage with featured products
2. **login.html** - Login page
3. **products.html** - Product listing and search
4. **cart.html** - Shopping cart
5. **checkout.html** - Checkout form
6. **account.html** - User account page (after login)
7. **success.html** - Order confirmation page

## Running the Site

### Option 1: Simple HTTP Server (Python)

```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000
```

Then open: `http://localhost:8000`

### Option 2: Node.js HTTP Server

```bash
npx http-server -p 8000
```

### Option 3: VS Code Live Server

Install "Live Server" extension in VS Code and right-click on `index.html` → "Open with Live Server"

## Testing with Selenium

Update your test configuration:

```python
BASE_URL = 'http://localhost:8000'
```

## Product Database

The site includes these demo products:
- Laptop ($999.99)
- MacBook ($1299.99)
- iPhone ($799.99)
- iPad ($599.99)
- Headphones ($199.99)
- Keyboard ($99.99)
- Mouse ($49.99)
- Monitor ($299.99)

## Notes

- All data is stored in browser localStorage
- No backend server required
- Perfect for automation testing practice
- All locators are designed to match common e-commerce patterns

