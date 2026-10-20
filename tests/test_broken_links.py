from playwright.sync_api import Page
from urllib.parse import urldefrag, urljoin, urlparse
from tests.config import HOMEPAGE_URL

def test_broken_links(page: Page) -> None:
    page.goto(HOMEPAGE_URL)

    hrefs = page.locator("a").evaluate_all("(anchors) => anchors.map(anchor => anchor.getAttribute('href'))")
    urls = set()

    for href in hrefs:
        if not href or not href.strip():
            continue

        url = urljoin(HOMEPAGE_URL, href.strip())
        url, _ = urldefrag(url)

        if urlparse(url).scheme in ("http", "https"):
            urls.add(url)

    assert urls, "No HTTP links found on the homepage"

    broken_links = []

    for url in sorted(urls):
        try:
            response = page.request.get(url, timeout=5000)

            if (response.status // 100) != 2:
                broken_links.append(
                    f"{url} returned HTTP {response.status}"
                )

        except Exception as error:
            broken_links.append(f"{url} failed: {error}")

    assert not broken_links, (f"Found {len(broken_links)} broken links:\n" + "\n".join(broken_links))
