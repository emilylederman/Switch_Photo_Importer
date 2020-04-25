# Switch Photo Importer
## Overview
This program simply serves to copy media from the Nintendo Switch SD card and store them 
in a human-friendly format. Currently, there are two folders created for storage: one for photos and one for videos,
codified by the current date.

Media is not overwritten by subsequent calls- that is, if the program is run multiple times (on the same date or otherwise)
the pre-existing files in the import folders remain undisturbed.


In theory this should work with media from other devices; testing is still pending.



## How to Use
1. Create the folder where you'd like to store your media
2. Put the unzip-pics.py file in the new folder
3. Copy the "Album" folder from the Switch's SD card (Nintendo -> Album) into the new folder
    - if you only want to import specific files or folders, just add them under a folder called "Album"
4. Run the script

    -**Note that this moves everything from your Album folder!**
5. By default, two new folders are generated:
    - YYYY-MM-DD-Photo-Import
    - YYYY-MM-DD-Video-Import
    
   The new files are formatted as:
    - YYYY-MM-DD_PhotoID.jpg
    - YYYY-MM-DD_VideoID.mp4
   
   Note that the MM and DD may be switched based on location; however, this is trivial.
 
 ##### File Structure
 Before the program is run, the new folder should be structured as follows:
 
         - Storage Folder
            -Album
                - ...
            unzip-pics.py
            
 After running the program, the new folders are generated in the same folder.
 
        - Storage Folder
            -Album
                - ...
            -YYYY-MM-DD-Photo-Import
            -YYYY-MM-DD-Video-Import
            unzip-pics.py