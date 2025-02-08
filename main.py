from os import getcwd, scandir, rename
from os.path import splitext, exists, join, expanduser

SOURCE_DIR = getcwd() # get current working directory
CURRENT_USER = expanduser("~")

# default folder destinations (should work for most people but can be changed)
# e.g.:
# `DOCUMENTS = "D:\Users\user\Documents"`
DOCUMENTS = join(CURRENT_USER, "Documents")
PICTURES = join(CURRENT_USER, "Pictures")
MUSIC = join(CURRENT_USER, "Music")
VIDEOS = join(CURRENT_USER, "Videos")

# default extensions and their mapped folder destinations (feel free to add more or change)
FOLDERS = [{"file_extension": ".txt", "folder_path": DOCUMENTS},\
            {"file_extension": ".pdf", "folder_path": DOCUMENTS},\
            {"file_extension": ".png", "folder_path": PICTURES},\
            {"file_extension": ".jpg", "folder_path": PICTURES},\
            {"file_extension": ".jpeg", "folder_path": PICTURES},\
            {"file_extension": ".webp", "folder_path": PICTURES},\
            {"file_extension": ".svg", "folder_path": PICTURES},\
            {"file_extension": ".tiff", "folder_path": PICTURES},\
            {"file_extension": ".mp3", "folder_path": MUSIC},\
            {"file_extension": ".m4a", "folder_path": MUSIC},\
            {"file_extension": ".wav", "folder_path": MUSIC},\
            {"file_extension": ".wave", "folder_path": MUSIC},\
            {"file_extension": ".flac", "folder_path": MUSIC},\
            {"file_extension": ".aac", "folder_path": MUSIC},\
            {"file_extension": ".aiff", "folder_path": MUSIC},\
            {"file_extension": ".ogg", "folder_path": MUSIC},\
            {"file_extension": ".mp4", "folder_path": VIDEOS},\
            {"file_extension": ".mov", "folder_path": VIDEOS},\
            {"file_extension": ".webm", "folder_path": VIDEOS},\
            {"file_extension": ".gif", "folder_path": VIDEOS},\
            {"file_extension": ".avi", "folder_path": VIDEOS}]


def sort_files(file_path: str, file_name: str, file_extension: str) -> None:
    file_path_new = None
    for dictionary in FOLDERS:
        if file_extension == dictionary["file_extension"]:
            file_path_new = dictionary["folder_path"]
            break

    if file_path_new != None and exists(file_path_new):
        rename((file_path + file_extension), join(file_path_new, file_name))


def main() -> None:
    for file in scandir(SOURCE_DIR):
        if file.is_file():
            file_tuple = splitext(file)
            sort_files(file_tuple[0], file.name, file_tuple[1])


if __name__ == "__main__":
    main()
