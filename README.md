# E-commerce Test Suite

[![CI/CD](https://github.com/egemenguney/ecommerce-test-suite/workflows/CI/badge.svg)](https://github.com/egemenguney/ecommerce-test-suite/actions)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Selenium](https://img.shields.io/badge/selenium-4.15.2-green.svg)](https://selenium-python.readthedocs.io/)
[![Pytest](https://img.shields.io/badge/pytest-7.4.3-orange.svg)](https://docs.pytest.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A comprehensive automated testing framework for e-commerce applications using Python, Selenium, and Pytest. This project demonstrates QA Automation skills and Python-Selenium expertise.

## 📋 Project Overview

This test suite implements the Page Object Model (POM) pattern to test various e-commerce functionalities including:
- User authentication (Login)
- Product search
- Shopping cart operations
- Checkout process

## 🛠️ Technologies and Tools

- **Python 3.8+** - Programming language
- **Selenium 4.15.2** - Web automation framework
- **Pytest 7.4.3** - Test framework and runner
- **Pytest-HTML** - HTML test reports
- **Pytest-Xdist** - Parallel test execution
- **WebDriver Manager** - Automatic driver management
- **Python-dotenv** - Environment variable management
- **Allure Pytest** - Advanced test reporting

## 📁 Project Structure

```
ecommerce-test-suite/
├── tests/                  # Test cases
│   ├── test_login.py      # Login functionality tests
│   ├── test_search.py     # Search functionality tests
│   ├── test_cart.py       # Shopping cart tests
│   └── test_checkout.py   # Checkout process tests
├── pages/                  # Page Object Model classes
│   ├── login_page.py      # Login page interactions
│   ├── search_page.py     # Search page interactions
│   ├── cart_page.py       # Cart page interactions
│   └── checkout_page.py   # Checkout page interactions
├── utils/                  # Utility functions
│   ├── driver_setup.py    # WebDriver initialization
│   └── config.py          # Configuration and test data
├── demo-site/             # Demo e-commerce website (for testing)
│   ├── index.html         # Homepage
│   ├── login.html         # Login page
│   ├── products.html      # Product listing
│   ├── cart.html          # Shopping cart
│   ├── checkout.html      # Checkout page
│   └── ...                # Other pages and assets
├── conftest.py            # Pytest fixtures and configuration
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- A web browser (Chrome, Firefox, or Edge)
- Git (optional, for version control)

### Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd ecommerce-test-suite
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the demo e-commerce site**
   ```bash
   # Navigate to demo-site folder
   cd demo-site
   
   # Start local server (choose one):
   # Option 1: Python HTTP Server
   python -m http.server 8000
   
   # Option 2: Use provided script
   # Windows:
   start-server.bat
   # Linux/Mac:
   chmod +x start-server.sh
   ./start-server.sh
   ```
   
   The demo site will be available at: `http://localhost:8000`

5. **Configure environment variables (optional)**
   ```bash
   # Copy the example file
   cp .env.example .env
   
   # Edit .env file if you want to change default settings
   # Default settings work with the demo site
   ```

## ⚙️ Configuration

### Demo Site Credentials

The included demo site uses these credentials:
- **Email**: `test@example.com`
- **Password**: `test123`

### Environment Variables

Edit the `.env` file to configure:

- **BASE_URL**: The e-commerce site URL to test (default: `http://localhost:8000`)
- **TEST_USERNAME**: Test account email (default: `test@example.com`)
- **TEST_PASSWORD**: Test account password (default: `test123`)
- **BROWSER**: Browser to use (chrome, firefox, edge)
- **HEADLESS**: Run tests in headless mode (True/False)
- **IMPLICIT_WAIT**: Implicit wait time in seconds
- **EXPLICIT_WAIT**: Explicit wait time in seconds

## 🧪 Running Tests

### Run all tests
```bash
pytest
```

### Run specific test file
```bash
pytest tests/test_login.py
```

### Run specific test class
```bash
pytest tests/test_login.py::TestLogin
```

### Run specific test method
```bash
pytest tests/test_login.py::TestLogin::test_valid_login
```

### Run tests with markers
```bash
# Run only smoke tests
pytest -m smoke

# Run only regression tests
pytest -m regression

# Run login-related tests
pytest -m login
```

### Run tests in parallel
```bash
pytest -n auto
```

### Generate HTML report
```bash
pytest --html=report.html --self-contained-html
```

### Generate Allure report
```bash
# Run tests with Allure
pytest --alluredir=allure-results

# Generate and open report
allure serve allure-results
```

## 📝 Test Cases

### Login Tests (`test_login.py`)
- ✅ Valid login with correct credentials
- ✅ Invalid email login attempt
- ✅ Invalid password login attempt
- ✅ Empty credentials validation
- ✅ Special characters handling

### Search Tests (`test_search.py`)
- ✅ Search valid product
- ✅ Search invalid/non-existent product
- ✅ Search with special characters
- ✅ Empty search handling
- ✅ Case-insensitive search
- ✅ Search and select product

### Cart Tests (`test_cart.py`)
- ✅ Add product to cart
- ✅ Remove product from cart
- ✅ Update cart quantity
- ✅ Empty cart verification
- ✅ Cart total calculation

### Checkout Tests (`test_checkout.py`)
- ✅ Complete checkout with valid details
- ✅ Checkout without accepting terms
- ✅ Checkout with empty cart
- ✅ Billing details validation

## 🎯 Page Object Model (POM)

This project follows the Page Object Model pattern:

- **Pages**: Each page has its own class with locators and methods
- **Tests**: Test files contain test cases that use page objects
- **Utils**: Common utilities like driver setup and configuration

### Example Usage

```python
from pages.login_page import LoginPage

# Initialize page object
login_page = LoginPage(driver)

# Use page methods
login_page.navigate_to_login()
login_page.login("user@example.com", "password123")
assert login_page.is_login_successful()
```

## 📊 Test Reports

### HTML Report
After running tests, open `report.html` in a browser to view detailed test results.

### Allure Report
For more advanced reporting with Allure:
1. Run tests: `pytest --alluredir=allure-results`
2. Generate report: `allure serve allure-results`

### Screenshots
Failed tests automatically capture screenshots in the `screenshots/` directory.

## 🔧 Troubleshooting

### WebDriver Issues
- Ensure you have the latest browser version installed
- WebDriver Manager will automatically download the correct driver
- If issues persist, manually download drivers from browser vendors

### Import Errors
- Ensure virtual environment is activated
- Verify all dependencies are installed: `pip install -r requirements.txt`
- Check that you're running tests from the project root directory

### Locator Issues
- Update locators in page objects if the website structure changes
- Use browser DevTools to inspect elements and find correct selectors

## 📚 Learning Resources

This project is designed as a learning resource. Key concepts demonstrated:

- **Page Object Model**: Separation of page logic from test logic
- **Explicit Waits**: Handling dynamic content loading
- **Test Fixtures**: Reusable test setup and teardown
- **Test Markers**: Organizing and filtering tests
- **Configuration Management**: Environment-based settings
- **Error Handling**: Robust test execution

## 🤝 Contributing

This is a learning project. Feel free to:
- Add more test cases
- Improve existing tests
- Enhance page objects
- Add new features

## 📄 License

This project is for educational purposes.

## 👤 Author

**Egemen Güney KOÇ**
- Software Developer & QA Automation Engineer
- Portfolio: [egemenguney.net](https://egemenguney.net)
- GitHub: [@egemenguney](https://github.com/egemenguney)

## 🔗 Links

- **Portfolio Website**: [egemenguney.net](https://egemenguney.net)
- **Project Repository**: [GitHub](https://github.com/egemenguney/ecommerce-test-suite)
- **CI/CD Status**: [![CI/CD](https://github.com/egemenguney/ecommerce-test-suite/workflows/CI/badge.svg)](https://github.com/egemenguney/ecommerce-test-suite/actions)

## 🙏 Acknowledgments

- Selenium WebDriver community
- Pytest framework maintainers

## 📝 Demo Site

This project includes a complete demo e-commerce site (`demo-site/`) for testing purposes. The demo site includes:

- ✅ Login/authentication system
- ✅ Product search functionality
- ✅ Shopping cart with add/remove/update
- ✅ Complete checkout process
- ✅ Order confirmation

All locators in the test suite are designed to work with the included demo site. The demo site uses localStorage for data persistence, so no backend server is required.

## 🐳 Docker Support

### Run tests with Docker Compose

```bash
# Build and run tests
docker-compose up --build

# Run tests only
docker-compose run test-suite pytest tests/ -v

# Run specific test
docker-compose run test-suite pytest tests/test_login.py -v
```

### Run with Dockerfile

```bash
# Build image
docker build -t ecommerce-test-suite .

# Run container
docker run --rm ecommerce-test-suite
```

## 🔄 CI/CD Pipeline

This project includes GitHub Actions CI/CD pipeline that:

- ✅ Runs tests on multiple Python versions (3.8-3.12)
- ✅ Tests on multiple browsers (Chrome, Firefox)
- ✅ Generates test reports and coverage
- ✅ Runs code quality checks (Black, Flake8, Pylint)
- ✅ Uploads test artifacts

The pipeline runs automatically on:
- Push to `main` or `develop` branches
- Pull requests to `main` or `develop` branches

View the workflow file: `.github/workflows/ci.yml`

## 📊 Test Coverage

Generate coverage report:

```bash
# Install coverage tool
pip install pytest-cov

# Run tests with coverage
pytest --cov=pages --cov=utils --cov-report=html --cov-report=term

# View HTML report
open htmlcov/index.html
```

## 🛠️ Code Quality

### Pre-commit Hooks

Install and use pre-commit hooks for code quality:

```bash
# Install pre-commit
pip install pre-commit

# Install hooks
pre-commit install

# Run hooks manually
pre-commit run --all-files
```

### Code Formatting

```bash
# Format code with Black
black .

# Check formatting
black --check .
```

### Linting

```bash
# Run Flake8
flake8 .

# Run Pylint
pylint pages/ utils/ tests/
```

## 📝 Logging

The project includes centralized logging. Logs are saved to `logs/` directory with timestamps.

```python
from utils.logger import get_logger

logger = get_logger()
logger.info("Test started")
logger.error("Test failed")
```

## 🎯 Best Practices Implemented

This project demonstrates:

- ✅ **Page Object Model (POM)** - Separation of concerns
- ✅ **Explicit Waits** - Robust element location
- ✅ **Configuration Management** - Environment-based settings
- ✅ **Test Fixtures** - Reusable setup/teardown
- ✅ **Test Markers** - Test organization and filtering
- ✅ **Screenshot on Failure** - Debugging support
- ✅ **Multiple Browser Support** - Cross-browser testing
- ✅ **Parallel Execution** - Faster test runs
- ✅ **CI/CD Integration** - Automated testing
- ✅ **Docker Support** - Containerized testing
- ✅ **Code Quality Tools** - Maintainable codebase
- ✅ **Comprehensive Logging** - Better debugging

---

**Note**: This test suite is designed to work with the included demo site. To test other e-commerce sites, update locators in the page objects according to your target application.

