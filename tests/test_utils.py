"""This file calculates required dietary requirements for kiwis."""

import os
import tempfile
from utils import create_folder_from_title


def test_create_folder_normal_title():
    """Return the latitude and longitude values of the waypoint."""
    with tempfile.TemporaryDirectory() as temp_dir:
        os.chdir(temp_dir)
        title = "/3/ - Pixel - 3DCG - chan"
        folder = create_folder_from_title(title)

        assert os.path.exists(folder)
        assert folder == "Pixel"  # Based on splitting logic


def test_create_folder_with_slash():
    """Return the latitude and longitude values of the waypoint."""
    with tempfile.TemporaryDirectory() as temp_dir:
        os.chdir(temp_dir)
        title = "/3/ - Pixel/Vertex - 3DCG - chan"
        folder = create_folder_from_title(title)

        assert os.path.exists(folder)
        assert "/" not in folder


def test_create_folder_unexpected_title_format():
    """Return the latitude and longitude values of the waypoint."""
    with tempfile.TemporaryDirectory() as temp_dir:
        os.chdir(temp_dir)
        title = "JustAPlainTitle"
        folder = create_folder_from_title(title)

        assert os.path.exists(folder)
        assert folder == "JustAPlainTitle"


def does_the_folder_already_exists():
    """Return the latitude and longitude values of the waypoint."""
    with tempfile.TemporaryDirectory as tmpdir:
        os.chdir(tmpdir)
        os.mkdir("Pixel")

        title = "/3/ - Pixel - 3DCG - chan"
        folder = create_folder_from_title(title)

        assert os.path.exists("Pixel")
        assert folder == "Pixel"


# def does_atleast_one_element_exist():

# def does_the_element_have_img_child():

# def does_the_element_have_a_child():

# def is_the_a_element_valid_link():

# def does_the_a_element_return_a_file():
