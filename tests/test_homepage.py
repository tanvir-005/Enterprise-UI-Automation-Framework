from playwright.sync_api import Page, expect
import logging

HOMEPAGE_URL = "https://books.toscrape.com/index.html"
HOMEPAGE_TITLE = "All products | Books to Scrape - Sandbox"

def test_homepage_loads(page: Page) -> None:
    page.goto(HOMEPAGE_URL)

    # match url and page title
    expect(page).to_have_url(HOMEPAGE_URL)
    expect(page).to_have_title(HOMEPAGE_TITLE)

    # confirm headings are visible and not empty
    headings = page.locator("h1, h2, h3, h4, h5, h6")
    for heading in headings.all():
        expect(heading).to_be_visible()
        assert heading.inner_text().strip(), f"heading {heading} is empty"

    # confirm book section is visible and not empty
    books = page.locator("article.product_pod")
    expect(books.first).to_be_visible()
    assert books.count() > 0
