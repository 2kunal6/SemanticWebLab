import os

def create_file(filename):
    file = open(filename, 'w+')

def append_to_file(filename, content):
    f = open(filename, "a")
    f.write('\n\n' + content)
    f.close()

def create_and_write_file(filename, content):
    f = open(filename, 'w+')
    f.write(content)
    f.close()

def create_folders_and_subfolders(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def create_parent_import(filepath):
    file_parts = filepath.split('/')
    if(len(file_parts) < 2):
        return ''
    if(len(file_parts) == 2):
        return 'import MLalgorithms'
    return 'from ' + '.'.join(file_parts[:-1]) + ' import ' + file_parts[-2]