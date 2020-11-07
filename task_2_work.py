# Your code here.
def get_hits(file_path: str, keyword: str):

    file = open(file_path, "r")
    text = file.read()
    file.close()

    hits = text.count(keyword)
    return hits

def load_rules(path: str): # function that will open file read it and remove white spaces.
    file = open(path, 'r')
    text = file.read()
    spaces_removed = text.strip()
    split_by_lines = spaces_removed.split()
    file.close()

    return split_by_lines # return a keyword


if __name__ == '__main__':
    # Your testing here.
    # Ensure any test code you add is tabbed in as part of this if statement.
    print(get_hits("C:\\Users\\Victoria_Rouch\\OneDrive - Milton Keynes College O365\\course\\programming\\Task 1\\my_file.txt", "private"))
    print(load_rules("C:\\Users\\Victoria_Rouch\\OneDrive - Milton Keynes College O365\\course\\programming\\Task 2\\example_2.txt"))
    
