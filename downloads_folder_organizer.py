#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# Created On  : macOS Catalina 10.15.7 (19H15)
# Created On  : Python 3.8.2
# Created By  : Ashik Kumar
# Created Date: Sat, Feb 05 2022 22:27:00 IST
# -----------------------------------------------------------------------------
"""THE MODULE HAS BEEN BUILT FOR ORGANIZING THE DOWNLOADS FOLDER ON MAC OS"""
# -----------------------------------------------------------------------------

import os
from pathlib import Path

# Categorize file types
folder_names = {
    "Audio": {'aif', 'cda', 'mid', 'midi', 'mp3', 'mpa', 'ogg', 'wav', 'wma'},
    "Compressed": {'7z', 'deb', 'pkg', 'rar', 'rpm', 'tar.gz', 'z', 'zip'},
    'Code': {'js', 'jsp', 'html', 'ipynb', 'py', 'java', 'css'},
    'Documents': {'ppt', 'pptx', 'pdf', 'xls', 'xlsx', 'doc', 'docx', 'txt', 'tex', 'epub'},
    'Images': {'bmp', 'gif .ico', 'jpeg', 'jpg', 'png', 'jfif', 'svg', 'tif', 'tiff'},
    'Softwares': {'apk', 'bat', 'bin', 'exe', 'jar', 'msi', 'py'},
    'Videos': {'3gp', 'avi', 'flv', 'h264', 'mkv', 'mov', 'mp4', 'mpg', 'mpeg', 'wmv'},
    'Others': {'NONE'}
}

user = os.getenv('USER')
downloads_path = r"/Users/{}/Downloads".format(user)

# Get all the files from Downloads Folder
only_files = [
    os.path.join(downloads_path, file)
    for file in os.listdir(downloads_path)
    if os.path.isfile(os.path.join(downloads_path, file))
]

# Get all the folders from Downloads Folder
only_folders = [
    os.path.join(downloads_path, file)
    for file in os.listdir(downloads_path)
    if not os.path.isfile(os.path.join(downloads_path, file))
]

# Map each extension to its file type
map_extension_filetype = {extension: fileType
                          for fileType, extensions in folder_names.items()
                          for extension in extensions}

# Create folders only if it does not exist
folder_paths = [
    os.path.join(downloads_path, folder_name) for folder_name in folder_names
]
[os.mkdir(folderPath) for folderPath in folder_paths if not os.path.exists(folderPath)]


# Handle unknown file types
def new_path(old_path):
    extension = str(old_path).split('.')[-1]
    amplified_folder = map_extension_filetype[extension] if extension in map_extension_filetype.keys() else 'Others'
    return os.path.join(
        downloads_path, amplified_folder, str(old_path).split('/')[-1]
    )


[Path(each_file).rename(new_path(each_file)) for each_file in only_files]


# Handle unknown folders
[Path(only_folder).rename(os.path.join(downloads_path, 'Others', str(only_folder).split('/')[-1]))
 for only_folder in only_folders
 if str(only_folder).split('/')[-1] not in folder_names.keys()]

print("Cheers, your Downloads folder is very well organized now!")
