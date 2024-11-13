from typing import List
import json

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    pass

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file paths into a list of json strings"""
    pass

def write_file_list(file_list, output_path):
    if file_list is None or not isinstance(file_list, list):
        raise ValueError("file_list must be a valid list")
    
    try:
        with open(output_path, 'w') as json_file:
            json.dump(file_list, json_file, ensure_ascii=False, indent=4)
        print(f"Data successfully written to {output_path}")
    except Exception as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)

    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)

    write_file_list(processed_file_list, path+'concated.json')