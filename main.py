"""Scrape an image thread and create a folder based on the page title."""

import os
import logging
from urllib.request import urlretrieve
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, Playwright
from utils import create_folder_from_title, split_up_page_title
# Configure logging
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


def run(playwright: Playwright):
    """Run the main logic using Playwright."""
    # pylint: disable-msg=too-many-locals
    load_dotenv(override=True)
    website_url = os.getenv("WEBSITE_LINK")

    if not website_url:
        logging.error("WEBSITE_LINK environment variable not found.")
        return

    browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()
    page = context.new_page()

    logging.info("Navigating to %s", website_url)

    page.goto(website_url)

    title = page.title()
    logging.info("Page title: %s", title)

    thread_id = page.locator('.thread').get_attribute('id')
    logging.info("Thread ID : %s", thread_id)

    array_title_response = split_up_page_title(title)

    cleaned_title = array_title_response[1]
    thread_category = array_title_response[0]

    create_folder_from_title(cleaned_title, thread_id)

    regex_path = ("xpath=//a[contains(@href,'i.4cdn.org/"
                  + thread_category
                  + "/')]")

    for link in page.locator(regex_path).all():

        url = link.get_attribute("href")

        file_name = url.rsplit('/', 1)[-1]

        complete_file_path = os.path.join(
            os.getenv("OUTPUT_FOLDER"),
            f"{cleaned_title}-{thread_id}",
            file_name)

        check_file_exist = os.path.exists(complete_file_path)

        if check_file_exist is False:

            file_path_to_save_file = os.path.join(
                os.getenv("OUTPUT_FOLDER"),
                f"{cleaned_title}-{thread_id}",
                url.rsplit('/', 1)[-1])

            urlretrieve("https:" + url,  file_path_to_save_file)
            print(file_name + ' downloaded!')

    browser.close()


def main():
    """Entrypoint."""
    with sync_playwright() as playwright:
        run(playwright)


if __name__ == "__main__":
    main()
