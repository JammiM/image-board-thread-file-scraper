"""Utils File."""

import os
import logging


def create_folder_from_title(title: str, thread_id: str) -> str:
    """Create  folder name from the page title and thread id."""
    # "/3/ - Pixel - 3DCG - chan"

    folder_name_with_id = f"{title}-{thread_id}"

    folder_path = os.path.join(os.getenv("OUTPUT_FOLDER"), folder_name_with_id)

    if not os.path.exists(folder_path):
        os.mkdir(os.path.join(os.getenv("OUTPUT_FOLDER"), folder_name_with_id))
        logging.info("Created folder: %s", folder_name_with_id)
    else:
        logging.info("Folder already exists: %s", folder_name_with_id)
    return folder_name_with_id


def split_up_page_title(title: str) -> list[str]:
    """Return an array of broken up title elements."""
    trimmed_title = title.replace("/", "").strip()

    split_page_title = trimmed_title.split(" - ")

    return split_page_title
