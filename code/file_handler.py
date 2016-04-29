import errno
import os

def get_file_name(image_name):
    current_dir = os.path.dirname(__file__)
    figures_dir = os.path.join(
    current_dir, "../figures")
    try:
        os.makedirs(os.path.abspath(figures_dir))
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(
            path):
            pass
        else:
            raise
    file_name = os.path.join(
    figures_dir, "cmapbubble.png")
    return file_name
