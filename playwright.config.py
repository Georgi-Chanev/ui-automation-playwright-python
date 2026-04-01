import pytest

def pytest_addoption(parser):
    parser.addoption("--headed", action="store_true", help="Run tests in headed mode")
