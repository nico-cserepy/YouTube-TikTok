"""
This module contains utils for files.
Author: bonsaiskyline
"""
import os


def get_filenames(
    dir_path: str,
    extension: str
):
    """
    Returns:
            list: List of transcription files.
    """
    filenames = [f for f in os.listdir(dir_path) if f.endswith(extension)]
    filenames.sort()
    return filenames
