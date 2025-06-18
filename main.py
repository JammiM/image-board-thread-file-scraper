"""Scrape an image thread and create a folder based on the page title."""

import os
import logging
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, Playwright
from utils import create_folder_from_title

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


def run(playwright: Playwright):
    """Run the main logic using Playwright."""
    load_dotenv()
    website_url = os.getenv("WEBSITE_LINK")

    if not website_url:
        logging.error("WEBSITE_LINK environment variable not found.")
        return

    browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()
    page = context.new_page()

    logging.info(f"Navigating to {website_url}")
    page.goto(website_url)

    title = page.title()
    logging.info(f"Page title: {title}")

    create_folder_from_title(title)

    browser.close()


def main():
    """Entrypoint."""
    with sync_playwright() as playwright:
        run(playwright)


if __name__ == "__main__":
    main()
