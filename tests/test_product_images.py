
from playwright.sync_api import Page, expect

from tests.config import HOMEPAGE_URL, BOOK_IMAGE_SELECTOR, NEXT_PAGE_SELECTOR


def test_product_images(page: Page) -> None:
    page.goto(HOMEPAGE_URL)

    for _ in range(5):
        images = page.locator(BOOK_IMAGE_SELECTOR)

        assert images.count() > 0, "No product images found"

        for image in images.all():
            expect(image).to_be_visible()

            src = image.get_attribute("src")
            alt = image.get_attribute("alt")
            classes = image.get_attribute("class") or ""

            assert src and src.strip(), "Image src is missing or empty"
            assert alt and alt.strip(), "Image alt is missing or empty"
            assert "thumbnail" in classes.split()

        next_page = page.locator(NEXT_PAGE_SELECTOR)

        if next_page.count() == 0:
            break

        current_url = page.url
        next_page.click()
        expect(page).not_to_have_url(current_url)
