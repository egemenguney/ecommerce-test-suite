# Initialize as Separate Git Repository

This folder should be a separate GitHub repository. Follow these steps to set it up:

## Steps to Create Separate Repository

1. **Navigate to this directory**
   ```bash
   cd ecommerce-test-suite
   ```

2. **Initialize Git repository**
   ```bash
   git init
   ```

3. **Add all files**
   ```bash
   git add .
   ```

4. **Create initial commit**
   ```bash
   git commit -m "Initial commit: E-commerce Test Suite project"
   ```

5. **Create repository on GitHub**
   - Go to https://github.com/new
   - Repository name: `ecommerce-test-suite`
   - Description: "Comprehensive automated testing framework for e-commerce applications using Selenium and Python"
   - Choose Public or Private
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
   - Click "Create repository"

6. **Connect local repository to GitHub**
   ```bash
   git remote add origin https://github.com/egemenguney/ecommerce-test-suite.git
   git branch -M main
   git push -u origin main
   ```

## After Repository is Created

Update the portfolio website link:
- Portfolio component already links to: `/projects/ecommerce-test-suite`
- Project detail page is at: `src/app/projects/ecommerce-test-suite/page.tsx`
- Update GitHub URL in Portfolio component if needed

## Repository Structure

```
ecommerce-test-suite/
├── .github/
│   └── workflows/      # CI/CD pipelines (to be added)
├── tests/              # Test cases
├── pages/              # Page Object Model
├── utils/              # Utilities
├── demo-site/          # Demo e-commerce site
├── conftest.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Next Steps

1. Add GitHub Actions workflow (`.github/workflows/ci.yml`)
2. Add Docker support (Dockerfile, docker-compose.yml)
3. Set up branch protection rules
4. Add project badges to README
5. Configure repository settings (topics, description, etc.)

