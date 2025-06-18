import os
import shutil
import tempfile
from utils import create_folder_from_title

def test_create_folder_normal_title():
    with tempfile.TemporaryDirectory() as temp_dir:
        os.chdir(temp_dir)
        title = "/3/ - Pixel - 3DCG - chan"
        folder = create_folder_from_title(title)

        assert os.path.exists(folder)
        assert folder == "Pixel"  # Based on splitting logic

def test_create_folder_with_slash():
    with tempfile.TemporaryDirectory() as temp_dir:
        os.chdir(temp_dir)
        title = "/3/ - Pixel/Vertex - 3DCG - chan"
        folder = create_folder_from_title(title)

        assert os.path.exists(folder)
        assert "/" not in folder


def test_create_folder_unexpected_title_format():
    with tempfile.TemporaryDirectory() as temp_dir:
        os.chdir(temp_dir)
        title = "JustAPlainTitle"
        folder = create_folder_from_title(title)

        assert os.path.exists(folder)
        assert folder == "JustAPlainTitle"
