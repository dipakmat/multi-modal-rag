import os
from modules import loader

def test_load_text(tmp_path):
    file = tmp_path / "sample.txt"
    file.write_text("Hello World")
    assert loader.load_text(str(file)) == "Hello World"

def test_load_pdf():
    # Just checks function executes without crash (dummy pdf)
    try:
        loader.load_pdf("data/sample_inputs/sample.pdf")
    except FileNotFoundError:
        pass  # Skip if file missing

def test_load_image():
    # Just checks function executes without crash
    try:
        loader.load_image("data/sample_inputs/sample.jpg")
    except FileNotFoundError:
        pass