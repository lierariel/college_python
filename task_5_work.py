from os import walk
from os.path import join


# Your code here.

def get_hits(file_path: str, keywords: list):
    file = open(file_path, "r")
    text = file.read()

    results = []

    for keyword in keywords:
        hits = text.count(keyword)
        results.append(hits)

    file.close()

    return results

    
def scan(path: str):
    folder_structure = walk(path)

    found_directories = []

    for root_directory, directories, files in folder_structure:
        for file in files:
            found_directories.append(join(root_directory, file))

    found_directories.sort()
    return found_directories


def check_files_for_hits(root_path: str, keywords: list):
    dictionary = {}

    for path_to_check in scan(root_path):
        hits = get_hits(path_to_check, keywords)
        dictionary[path_to_check] = hits

    return dictionary


if __name__ == '__main__':
    # Your testing here.
    # Ensure any test code you add is tabbed in as part of this if statement.
    
    print(get_hits("C:\\Users\\Victoria_Rouch\\OneDrive - Milton Keynes College O365\\course\\programming\\Task 1\\my_file.txt", " "))
    print(scan("test_data/Structure 1",
    ))

