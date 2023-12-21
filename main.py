from os import getcwd, scandir, rename
from os.path import splitext, exists, join, expanduser


def move_files():
    pass


def main():
    source_dir = getcwd()
    user_current = expanduser("~")
    
    folders =  [
                {file_extension: ".txt", file_path: "Documents"},
                {file_extension: ".pdf", file_path: "Documents"},
                {file_extension: ".png", file_path: "Pictures"},
                {file_extension: ".jpg", file_path: "Pictures"},
                {file_extension: ".jpeg", file_path: "Pictures"},
                {file_extension: ".webp", file_path: "Pictures"},
                {file_extension: ".svg", file_path: "Pictures"},
                {file_extension: ".tiff", file_path: "Pictures"},
                {file_extension: ".mp3", file_path: "Music"},
                {file_extension: ".m4a", file_path: "Music"},
                {file_extension: ".wav", file_path: "Music"},
                {file_extension: ".wave", file_path: "Music"},
                {file_extension: ".flac", file_path: "Music"},
                {file_extension: ".aac", file_path: "Music"},
                {file_extension: ".aiff", file_path: "Music"},
                {file_extension: ".aif", file_path: "Music"},
                {file_extension: ".aifc", file_path: "Music"},
                {file_extension: ".au", file_path: "Music"},
                {file_extension: ".snd", file_path: "Music"},
                {file_extension: ".l16", file_path: "Music"},
                {file_extension: ".pcm", file_path: "Music"},
                {file_extension: ".ape", file_path: "Music"},
                {file_extension: ".wv", file_path: "Music"},
                {file_extension: ".wma", file_path: "Music"},
                {file_extension: ".ogg", file_path: "Music"},
                {file_extension: ".mpc", file_path: "Music"},
                {file_extension: ".mp+", file_path: "Music"},
                {file_extension: ".mpp", file_path: "Music"},
                {file_extension: ".mp4", file_path: "Videos"},
                {file_extension: ".m4v", file_path: "Videos"},
                {file_extension: ".mov", file_path: "Videos"},
                {file_extension: ".wmv", file_path: "Videos"},
                {file_extension: ".webm", file_path: "Videos"},
                {file_extension: ".ogv", file_path: "Videos"},
                {file_extension: ".gif", file_path: "Videos"},
                {file_extension: ".gifv", file_path: "Videos"},
                {file_extension: ".avi", file_path: "Videos"},]

    for files in scandir(source_dir):
        pass


if __name__ == "__main__":
    main()
