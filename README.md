# UI Automation with Playwright (Python)

This is a simple UI automation project using Playwright and PyTest.  
The example test opens Google, performs a search and checks that results appear.

## Project structure

ui-automation-playwright-python/
│
├── tests/
│   └── test_google_search.py
│
├── playwright.config.py
├── requirements.txt
├── README.md

## How to run

Install dependencies:

pip install -r requirements.txt

Install Playwright browsers:

playwright install

Run tests:

pytest -v
