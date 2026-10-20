from playwright.sync_api import Page, expect
import random
from tests.config import HOMEPAGE_URL, BOOK_SELECTOR, BOOK_TITLE_SELECTOR, BOOK_PRICE_SELECTOR, PRODUCT_DETAILS_SELECTOR

def test_random_book_data_consistency(page: Page) -> None:
    page.goto(HOMEPAGE_URL)

    books = page.locator(BOOK_SELECTOR)
    book_count = books.count()

    selected_books = random.sample(range(book_count), min(5, books.count()))

    for index in selected_books:
        book = page.locator(BOOK_SELECTOR).nth(index)

        homepage_title = book.locator(BOOK_TITLE_SELECTOR).get_attribute("title")
        homepage_price = book.locator(BOOK_PRICE_SELECTOR).inner_text()

        assert homepage_title, "Book title is missing"
        assert homepage_price, "Book price is missing"

        book.locator(BOOK_TITLE_SELECTOR).click()

        expect(page.locator("h1")).to_have_text(homepage_title)
        expect(page.locator(f"{PRODUCT_DETAILS_SELECTOR} {BOOK_PRICE_SELECTOR}")).to_have_text(
            homepage_price
        )

        page.go_back()

    page.goto(HOMEPAGE_URL)