import json

def load_data(file_path):
    """Load JSON data from a file."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def process_data(data):
    """Process loaded JSON data."""
    for item in data:
        # Perform operations on each item (JSON object)
        # Example: Print each item
        print(item)

def main():
    # Path to data.json
    input_file = 'visualization_data/data.json'

    # Load data from JSON file
    data = load_data(input_file)

    # Process loaded data
    process_data(data)

if __name__ == "__main__":
    main()
