from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    # Will this be working?
    lines = open(path, 'r').read().split('\n')
    return lines

# Example function in `train_file_list_to_json` branch
def train_file_list_to_json():
    file_list = []
    # Example processing logic to read from "english.txt" and "german.txt" and add to `file_list`
    try:
        with open('english.txt', 'r') as eng_file, open('german.txt', 'r') as ger_file:
            for eng_line, ger_line in zip(eng_file, ger_file):
                file_list.append({"English": eng_line.strip(), "German": ger_line.strip()})
    except FileNotFoundError as e:
        print(f"Error: {e}")
    return file_list  # Ensure this returns a list


    # Template for json file
    template_start = '{\"English\":\"'
    template_mid = '\",\"German\":\"'
    template_end = '\"}'

    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        english_file = process_file(english_file)
        german_file = process_file(german_file)

        processed_file_list.append(template_start + english_file + template_mid + german_file + template_end)
    return processed_file_list

def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    with open(path, 'w') as f:
        for file in file_list:
            f.write(file + '\n')
            
if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)

    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)

    write_file_list(processed_file_list, path+'concated.json')