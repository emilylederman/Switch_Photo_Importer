"""
author: Emily L.
email: erl3193@rit.edu
description: script to unzip photos and videos imported from a Switch into a human-readable format
             testing on other devices pending
"""

from pathlib import Path
import os
import datetime

# extension macros, in case these ever change
PHOTO_EXTENSION = ".jpg"
VIDEO_EXTENSION = ".mp4"


def create_import_directory(directory_name):
    """
    Create a directory to import photos and videos so as long as it doesn't already exist
    :param directory_name: the name of the directory to create
    :return: None
    """
    try:
        os.mkdir(directory_name)
    except FileExistsError:
        print("Directory %s already exists!" % directory_name)


def search_and_rename(destination_directory, extension):
    """
    Search for all files of the given extension and move it as appropriate
    :param destination_directory: the directory to which to copy items
    :param extension: the file extension to search
    :return:
    """
    # gets all files matching the extension in the current folder and any subfolders

    for media_file in Path(os.getcwd() + "/Album/").rglob('*' + extension):
        # check if the file is unaltered (eg first time loaded on the system.
        # this is so that multiple runs don't keep adding extensions on unnecessarily
        if "-" in media_file.name:
            cleaned_media_file_name = media_file.name.split("-")[0] + extension
        else:
            cleaned_media_file_name = media_file.name.split(".")[0] + extension
        # create a new file name as YYYY-MM-DD_ID
        # this splits up the file names into a human-readable format.
        new_file_name = "{YYYY}-{MM}-{DD}_{ID}".format(
            YYYY=cleaned_media_file_name[:4],
            MM=cleaned_media_file_name[4:6],
            DD=cleaned_media_file_name[6:8],
            ID=cleaned_media_file_name[8:]
        )
        # use os.rename to rename + move the found file to the appropriate destination
        os.rename(media_file, destination_directory + "/" + new_file_name)


def main():
    # unique ID for the date of import
    curr_date = str(datetime.date.today())
    pics_dir_name = curr_date + "-Photo-Import"
    vids_dir_name = curr_date + "-Video-Import"

    # create the import directories for photos and videos
    create_import_directory(pics_dir_name)
    create_import_directory(vids_dir_name)

    # Search for new media and rename it into the new folder
    search_and_rename(pics_dir_name, PHOTO_EXTENSION)
    search_and_rename(vids_dir_name, VIDEO_EXTENSION)

    print("Media successfully imported!")

if __name__ == '__main__':
    main()