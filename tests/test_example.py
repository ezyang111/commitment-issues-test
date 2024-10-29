import re
import os

def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 5 - 2 == 3
    
# checks all files in the entire directory, ignoring this testing file
# returns true if it detects/suspects a file may have hardcoded an API key
# returns false otherwise
def check_for_hardcoded_api_keys(directory, ignore_file):
    detected = False
    # Define regex patterns for common API key formats
    patterns = [
        r'[A-Za-z0-9-_]{24,}',  # General pattern for random 24+ character strings
        r'(?i)api[-_]?key\s*=\s*["\'][\w-]+["\']', # General pattern for setting api-key
        r'(?i)token\s*=\s*["\'][\w-]+["\']', # General pattern for setting token
        r'["\'][A-Za-z0-9-_]{40}["\']'  # General long strings that may look like keys
    ]

    # Compile regex patterns
    compiled_patterns = [re.compile(pattern) for pattern in patterns]

    # Walk through all files in the directory
    for root, _, files in os.walk(directory):
        for file_name in files:
            # Only check code files (add extensions as needed)
            if file_name.endswith(('.py', '.yml', '.yaml', '.txt')) and file_name != ignore_file:
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read()
                    for pattern in compiled_patterns:
                        matches = pattern.findall(content)
                        if matches:
                            print(f'Potential API key found in {file_path}:')
                            detected = True
                            for match in matches:
                                print(f'  {match}')
    return detected

if __name__ == '__main__':
    repo_directory = '.'  # Set this to the path of your repository
    check_for_hardcoded_api_keys(repo_directory, os.path.basename('test_example.py'))