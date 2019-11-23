from os import path, makedirs


def root_dir():
    return path.dirname(path.dirname(__file__))


def check_path(directory):
    if not path.exists(directory):
        makedirs(directory)


def strip_slash(text):
    first_char = text[0].strip("/")
    more_chars = text[1:]
    return first_char + more_chars


def get_sqlite_uri(folder, file):
    provider = 'sqlite:////'
    db_dir = path.join(root_dir(), folder)
    check_path(db_dir)
    db_path = path.join(db_dir, file)
    return provider + strip_slash(db_path)
