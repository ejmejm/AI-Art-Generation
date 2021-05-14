from string import ascii_letters, digits

FOLDER_NAME_ALLOW_LIST = set(ascii_letters + digits + '_-')
FILE_NAME_ALLOW_LIST = set(ascii_letters + digits + '_-.')

def sanitize_folder_name(name):
    clean_name = ''
    for c in name:
        if c in FOLDER_NAME_ALLOW_LIST:
            clean_name += c
        else:
            clean_name += '_'
    return clean_name

def sanitize_file_name(name):
    clean_name = ''
    for c in name:
        if c in FILE_NAME_ALLOW_LIST:
            clean_name += c
        else:
            clean_name += '_'
    return clean_name