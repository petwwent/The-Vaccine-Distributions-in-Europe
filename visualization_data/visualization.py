import json

def load_data(file_path):
    """Load JSON data from a file."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def main():
    # File path to data.json
    input_file = 'visualization_data/data.json'

    # Load data from JSON file
    raw_data = load_data(input_file)

    # Processed data ready for visualization (if no additional processing is required)
    processed_data = raw_data  # Placeholder for the same data (no modifications)

    return processed_data

if __name__ == "__main__":
    processed_data = main()
