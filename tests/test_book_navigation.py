import random
from playwright.sync_api import Page, expect
from tests.config import HOMEPAGE_URL, BOOK_SELECTOR, BOOK_TITLE_SELECTOR, PRODUCT_DETAILS_SELECTOR

def test_random_book_navigation(page: Page) -> None:
    page.goto(HOMEPAGE_URL)

    books = page.locator(BOOK_SELECTOR)
    selected_books = random.sample(range(books.count()), 5)

    for index in selected_books:
        book = page.locator(BOOK_SELECTOR).nth(index)
        title = book.locator(BOOK_TITLE_SELECTOR).get_attribute("title")

        assert title, "Book title missing"

        book.locator(BOOK_TITLE_SELECTOR).click()
        expect(page.locator("h1")).to_have_text(title)
        expect(page.locator(PRODUCT_DETAILS_SELECTOR)).to_be_visible()
        expect(page.locator(f"{PRODUCT_DETAILS_SELECTOR} {'.price_color'}")).to_be_visible()

        page.go_back()
        expect(page).to_have_url(HOMEPAGE_URL)
        expect(page.locator(BOOK_SELECTOR).first).to_be_visible()
    