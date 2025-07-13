import os
import logging

def create_folder_from_title(title: str, thread_id: str) -> str:
    """Create a sanitized folder name from the page title and thread id and make's the folder."""
    # "/3/ - Pixel - 3DCG - chan"

    # TODO This could be removed later, and placed into 'split_up_page_title()'
    # parts = title.split(" - ")
    # if len(parts) < 3:
    #     logging.warning("Unexpected title format; using full title.")
    #     folder_name = title
    # else:
    #     parts = parts[1:-2]  # Remove first and last two parts
    #     folder_name = "".join(parts)
    # TODO Down to here
        


    # folder_name = folder_name.replace("/", "_").strip()

    folder_name_with_id = f"{title}-{thread_id}"

    if not os.path.exists(os.path.join(os.getenv("OUTPUT_FOLDER"),folder_name_with_id)):
        os.mkdir(os.path.join(os.getenv("OUTPUT_FOLDER"),folder_name_with_id))
        logging.info(f"Created folder: {folder_name_with_id}")
    else:
        logging.info(f"Folder already exists: {folder_name_with_id}")
    return folder_name_with_id




def split_up_page_title(title:str) -> list[str]:

    trimmed_title = title.replace("/", "").strip()

    split_page_title = trimmed_title.split(" - ")

    return split_page_title
