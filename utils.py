import os
import logging

def create_folder_from_title(title: str, thread_id: str) -> str:
    """Create a sanitized folder name from the page title and thread id and make's the folder."""
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

    folder_name_with_id = f"{folder_name}:{thread_id}"

    if not os.path.exists(folder_name_with_id):
        os.mkdir(folder_name_with_id)
        logging.info(f"Created folder: {folder_name_with_id}")
    else:
        logging.info(f"Folder already exists: {folder_name_with_id}")
    return folder_name_with_id
