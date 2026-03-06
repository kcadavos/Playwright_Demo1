import re #regex
from playwright.sync_api import expect #expect gives smart test assertions

def test_google_search (page): #page automatically provided by pytest-playwright fixture
    page.wait_for_timeout(1000) #wait for 30 seconds to load the page and pop up if any
    page.goto("https://google.com/ncr") #NCR no country redirect to avoid the pop up
    
    try:
        page.get_by_role("button",name="Accept all").click(timeout=50000) #click the accept cookies button
    except:
        print ("No pop up to accept")
    
    #type in the search box
    page.get_by_role("combobox", name="Search").fill("Playwright Python")
    page.keyboard.press("Enter") # press enter

    expect(page).to_have_title(re.compile("Playwright",re.IGNORECASE)) #assert the title contains Playwright ignoring case


