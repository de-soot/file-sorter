from os import getcwd, scandir, rename
from os.path import splitext, exists, join, expanduser

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
            {"file_extension": ".aif", "folder_path": "Music"},
            {"file_extension": ".aifc", "folder_path": "Music"},
            {"file_extension": ".au", "folder_path": "Music"},
            {"file_extension": ".snd", "folder_path": "Music"},
            {"file_extension": ".l16", "folder_path": "Music"},
            {"file_extension": ".pcm", "folder_path": "Music"},
            {"file_extension": ".ape", "folder_path": "Music"},
            {"file_extension": ".wv", "folder_path": "Music"},
            {"file_extension": ".wma", "folder_path": "Music"},
            {"file_extension": ".ogg", "folder_path": "Music"},
            {"file_extension": ".mpc", "folder_path": "Music"},
            {"file_extension": ".mp+", "folder_path": "Music"},
            {"file_extension": ".mpp", "folder_path": "Music"},
            {"file_extension": ".mp4", "folder_path": "Videos"},
            {"file_extension": ".m4v", "folder_path": "Videos"},
            {"file_extension": ".mov", "folder_path": "Videos"},
            {"file_extension": ".wmv", "folder_path": "Videos"},
            {"file_extension": ".webm", "folder_path": "Videos"},
            {"file_extension": ".ogv", "folder_path": "Videos"},
            {"file_extension": ".gif", "folder_path": "Videos"},
            {"file_extension": ".gifv", "folder_path": "Videos"},
            {"file_extension": ".avi", "folder_path": "Videos"}]

SOURCE_DIR = getcwd()
USER_CURRENT = expanduser("~")


def sort_files(file_path, file_name, file_extension):
    file_path_new = USER_CURRENT
    for dictionary in FOLDERS:
        if file_extension == dictionary["file_extension"]:
            file_path_new = join(USER_CURRENT, dictionary["folder_path"])
            break

    print(file_path_new)


def main():
    for file in scandir(SOURCE_DIR):
        if file.is_file():
            file_tuple = splitext(file)
            sort_files(file_tuple[0], file.name, file_tuple[1])


if __name__ == "__main__":
    main()
