from playwright.sync_api import Page, expect
from tests.config import USERNAME, PASSWORD

def test_login_logout(page: Page) -> None:
    page.goto("https://quotes.toscrape.com/")
    page.get_by_role("link", name="Login").click()

    page.locator("#username").fill(USERNAME)
    page.locator("#password").fill(PASSWORD)
    page.locator("input[type='submit']").click()

    logout_link = page.get_by_role("link", name="Logout")
    expect(logout_link).to_be_visible()
    expect(logout_link).to_be_enabled()
    