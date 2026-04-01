def test_google_search(page):
    page.goto("https://www.google.com")
    page.locator("input[name='q']").fill("Playwright Python")
    page.keyboard.press("Enter")
    page.wait_for_selector("text=Playwright")
    assert "Playwright" in page.content()
