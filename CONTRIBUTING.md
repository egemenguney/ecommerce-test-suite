# Contributing to E-commerce Test Suite

Thank you for your interest in contributing! This is a learning/portfolio project, but contributions are welcome.

## Development Setup

1. Fork the repository
2. Clone your fork
3. Create a virtual environment
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Code Style

- Follow PEP 8 style guide
- Use Black for code formatting
- Maximum line length: 100 characters
- Use type hints where possible
- Write docstrings for all functions and classes

## Adding New Tests

1. Follow the Page Object Model pattern
2. Add appropriate test markers (`@pytest.mark.smoke`, etc.)
3. Include descriptive docstrings
4. Add assertions with clear error messages

## Running Tests

```bash
# All tests
pytest

# Specific test file
pytest tests/test_login.py

# With coverage
pytest --cov=pages --cov=utils
```

## Pull Request Process

1. Create a feature branch
2. Make your changes
3. Run tests and ensure they pass
4. Run code quality checks
5. Update documentation if needed
6. Submit pull request with clear description

## Code Quality Checks

Before submitting PR, ensure:

- ✅ All tests pass
- ✅ Code is formatted with Black
- ✅ No Flake8 errors
- ✅ Pylint score is acceptable
- ✅ Documentation is updated
