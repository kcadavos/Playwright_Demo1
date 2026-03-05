from playwright.sync_api import sync_playwright

# def main():
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # set to True to hide browser
    page = browser.new_page()
    page.goto("https://www.google.com", wait_until="networkidle")
    print("Page title:", page.title())
    browser.close()

# if __name__ == "__main__":
#    main()
  