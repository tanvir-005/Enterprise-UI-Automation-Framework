
import random

from playwright.sync_api import Page, expect


def test_random_book_data_consistency(page: Page) -> None:
    page.goto("https://books.toscrape.com/index.html")

    books = page.locator("article.product_pod")
    book_count = books.count()

    assert book_count >= 5, "The homepage must contain at least five books"

    selected_books = random.sample(range(book_count), 5)

    for index in selected_books:
        book = page.locator("article.product_pod").nth(index)

        homepage_title = book.locator("h3 a").get_attribute("title")
        homepage_price = book.locator(".price_color").inner_text()

        assert homepage_title, "Book title is missing"
        assert homepage_price, "Book price is missing"

        book.locator("h3 a").click()

        expect(page.locator("h1")).to_have_text(homepage_title)
        expect(page.locator(".product_main .price_color")).to_have_text(
            homepage_price
        )

        page.go_back()
        expect(page.locator("article.product_pod").first).to_be_visible()
