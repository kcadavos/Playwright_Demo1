import pytest
from playwright.sync_api import sync_playwright


def test_google_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # navigate to Google homepage
        page.goto("https://www.google.com")

        # wait for the page to load completely
        page.wait_for_load_state("load")
        title = page.title()

        # Assert that the title contains "Google"
        assert "Google" in title
        browser.close()
