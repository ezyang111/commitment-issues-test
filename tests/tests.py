import re
import os
import argparse
    
# checks all files in the entire directory, ignoring this testing file
# returns true if it detects/suspects a file may have hardcoded an API key
# returns false otherwise
def test_check_for_hardcoded_api_keys():
    directory = '.'
    ignore_file = os.path.basename('test_example.py')
    not_detected = True
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
                            not_detected = False
                            for match in matches:
                                print(f'  {match}')
    assert not_detected
    
# parse arguments
def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--message-type')
    parser.add_argument('--impact-type')
    parser.add_argument('--change-type')
    return parser.parse_args(args)

# valid flags for our CLI
VALID_FLAGS = ['--message-type', '--impact-type', '--change-type']

def check_flag_validity(args):
    for arg in args:
        if arg.startswith('--') and arg not in VALID_FLAGS:
            raise ValueError(f"Invalid flag used: {arg}")

def test_invalid_flag():
    args = ['--invalid_flag']
    
    try:
        check_flag_validity(args)
    except ValueError as e:
        assert str(e) == "Invalid flag used: --invalid_flag"
    else:
        assert False, "Expected ValueError for invalid flag, but none was raised."
        
def test_valid_flag():
    args = ['--message-type', 'message']
    check_flag_validity(args)
    parsed_args = parse_args(args)

    assert parsed_args.message_type == 'message', "Expected --message-type to be parsed correctly."