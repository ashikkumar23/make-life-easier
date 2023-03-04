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
import shutil


# Define file extensions for each category
folder_names = {
    "Audio": {"aif", "cda", "mid", "midi", "mp3", "mpa", "ogg", "wav", "wma"},
    "Compressed": {"7z", "deb", "pkg", "rar", "rpm", "tar.gz", "z", "zip"},
    "Code": {"js", "jsp", "html", "ipynb", "py", "java", "css"},
    "Documents": {
        "ppt",
        "pptx",
        "pdf",
        "xls",
        "xlsx",
        "doc",
        "docx",
        "txt",
        "tex",
        "epub",
    },
    "Images": {"bmp", "gif", "ico", "jpeg", "jpg", "png", "jfif", "svg", "tif", "tiff"},
    "Softwares": {"app", "dmg", "apk", "bat", "bin", "exe", "jar", "msi"},
    "Videos": {"3gp", "avi", "flv", "h264", "mkv", "mov", "mp4", "mpg", "mpeg", "wmv"},
    "Others": {"NONE"},
}


def get_files_and_folders(dir_path):
    """Return lists of files and folders in the specified directory"""
    with os.scandir(dir_path) as entries:
        files = [entry.path for entry in entries if entry.is_file()]
        folders = [entry.path for entry in entries if entry.is_dir()]
    return files, folders


def create_folders(folders, base_dir):
    """Create folders for each category in the specified directory"""
    for folder in folders:
        folder_path = os.path.join(base_dir, folder)
        os.makedirs(folder_path, exist_ok=True)


def get_file_extension(file_path):
    """Return the file extension of the specified file"""
    _, extension = os.path.splitext(file_path)
    print(extension)
    return extension[1:].lower() if extension else None


def get_folder_name(file_extension):
    """Return the category name for the specified file extension"""
    for folder_name, extensions in folder_names.items():
        if file_extension in extensions:
            return folder_name
    return "Others"


def organize_files(files, base_dir):
    """Move files to their corresponding folders"""
    for file in files:
        file_extension = get_file_extension(file)
        print(f"file_extension: {file_extension}")
        folder_name = get_folder_name(file_extension)
        print(f"folder_name: {folder_name}")
        new_file_path = os.path.join(base_dir, folder_name, os.path.basename(file))
        shutil.move(file, new_file_path)


def organize_folders(folders, base_dir):
    """Move folders to the 'Others' category if their name is not in folder_names"""
    for folder in folders:
        if os.path.basename(folder) not in folder_names:
            new_folder_path = os.path.join(base_dir, "Others", os.path.basename(folder))
            shutil.move(folder, new_folder_path)


def organize_downloads_folder():
    """Organize files and folders in the Downloads folder"""
    user = os.getenv("USER")
    downloads_path = os.path.join("/", "Users", user, "Downloads")
    print(f"downloads_path: {downloads_path}")

    files, folders = get_files_and_folders(downloads_path)
    print(f"files: {files}, folders: {folders}")

    create_folders(folder_names, downloads_path)

    organize_files(files, downloads_path)

    organize_folders(folders, downloads_path)

    print("Cheers, your Downloads folder is very well organized now!")


if __name__ == "__main__":
    organize_downloads_folder()
