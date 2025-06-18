import os
import logging

def create_folder_from_title(title: str) -> str:
    """Create a sanitized folder name from the page title and make the folder."""
    # "/fit/ - Seriously considering joining a local yoga studio  - Fitness - chan"
    # "/3/ - Pixel - 3DCG - chan"
    parts = title.split(" - ")
    if len(parts) < 3:
        logging.warning("Unexpected title format; using full title.")
        folder_name = title
    else:
        parts = parts[1:-2]  # Remove first and last two parts
        folder_name = "".join(parts)

    folder_name = folder_name.replace("/", "_").strip()

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        logging.info(f"Created folder: {folder_name}")
    else:
        logging.info(f"Folder already exists: {folder_name}")
    return folder_name
