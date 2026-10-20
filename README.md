# Enterprise UI Automation Framework

UI automation testing for [Books to Scrape](https://books.toscrape.com/) using Playwright and Pytest.

## Tech Stack
- Python 3.12, Playwright, Pytest
- uv, pytest-html, Allure
- Docker, GitHub Actions

## Test Coverage
1. Homepage validation
2. Random book navigation
3. Book data consistency check
4. Broken link detection
5. Product image validation
6. Login and logout validation

## Setup

Clone the project:

```bash
git clone https://github.com/tanvir-005/Enterprise-UI-Automation-Framework.git
cd Enterprise-UI-Automation-Framework
```

```bash
uv sync
uv run playwright install chromium
```

Create a `.env` file with `USERNAME` and `PASSWORD` for the login test. eg:
```bash
printf "USERNAME=u1\nPASSWORD=p1\n" > .env
```

## Run Tests

```bash
uv run pytest
```

Generate an HTML report:

```bash
uv run pytest --html=reports/report.html --self-contained-html
```

## Docker

```bash
docker build -t books-ui-automation .
docker run --rm books-ui-automation
```

## CI

GitHub Actions runs tests on pushes and pull requests. Reports are uploaded as workflow artifacts.