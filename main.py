from os import getcwd, scandir, rename
from os.path import splitext, exists, join, expanduser

SOURCE_DIR = getcwd()
USER_CURRENT = expanduser("~")

FOLDERS = [
            {"file_extension": ".txt", "folder_path": "Documents"},
            {"file_extension": ".pdf", "folder_path": "Documents"},
            {"file_extension": ".png", "folder_path": "Pictures"},
            {"file_extension": ".jpg", "folder_path": "Pictures"},
            {"file_extension": ".jpeg", "folder_path": "Pictures"},
            {"file_extension": ".webp", "folder_path": "Pictures"},
            {"file_extension": ".svg", "folder_path": "Pictures"},
            {"file_extension": ".tiff", "folder_path": "Pictures"},
            {"file_extension": ".mp3", "folder_path": "Music"},
            {"file_extension": ".m4a", "folder_path": "Music"},
            {"file_extension": ".wav", "folder_path": "Music"},
            {"file_extension": ".wave", "folder_path": "Music"},
            {"file_extension": ".flac", "folder_path": "Music"},
            {"file_extension": ".aac", "folder_path": "Music"},
            {"file_extension": ".aiff", "folder_path": "Music"},
            {"file_extension": ".ogg", "folder_path": "Music"},
            {"file_extension": ".mp4", "folder_path": "Videos"},
            {"file_extension": ".mov", "folder_path": "Videos"},
            {"file_extension": ".webm", "folder_path": "Videos"},
            {"file_extension": ".gif", "folder_path": "Videos"},
            {"file_extension": ".avi", "folder_path": "Videos"}]


def sort_files(file_path, file_name, file_extension):
    file_path_new = None
    for dictionary in FOLDERS:
        if file_extension == dictionary["file_extension"]:
            file_path_new = join(USER_CURRENT, dictionary["folder_path"])
            break

    if file_path_new != None:
        rename(file_path, file_path_new)


def main():
    for file in scandir(SOURCE_DIR):
        if file.is_file():
            file_tuple = splitext(file)
            sort_files(file_tuple[0], file.name, file_tuple[1])


if __name__ == "__main__":
    main()
