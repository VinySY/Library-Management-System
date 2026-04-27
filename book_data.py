import json
import os

# Database file name
DB_FILE = "library_data.json"

# Standard CSE books to start with
DEFAULT_BOOKS = {
    "C Programming": 10,
    "Operating Systems": 8,
    "Database Management Systems": 7,
    "Computer Networks": 5,
    "Data Structures & Algorithms": 12,
    "Discrete Mathematics": 6,
    "Software Engineering": 9,
    "Digital Logic Design": 4,
    "Theory of Computation": 3,
    "Artificial Intelligence": 5
}

def load_data():
    # If the file isn't there, just use the defaults
    if not os.path.exists(DB_FILE):
        return DEFAULT_BOOKS.copy(), {}
    
    try:
        with open(DB_FILE, "r") as f:
            data = json.load(f)
            # Using .get() is safer in case the keys are missing
            return data.get("books", DEFAULT_BOOKS), data.get("records", {})
    except (json.JSONDecodeError, KeyError):
        # If the file is messy/empty, don't crash, just reset
        return DEFAULT_BOOKS.copy(), {}

def save_data(books, records):
    try:
        with open(DB_FILE, "w") as f:
            # We wrap everything in one big dictionary before dumping to JSON
            json.dump({"books": books, "records": records}, f, indent=4)
    except Exception as e:
        print(f"Error saving: {e}")

# Load everything up when the module is imported
BOOKS, ISSUED_RECORDS = load_data()