import os

def get_project_root():
    """
    Returns the root directory for the project.
    Assumes the script is run from within the project's folder structure.
    """
    return os.path.dirname(os.path.abspath(__file__))

# Define paths
PROJECT_ROOT = get_project_root()

# Paths for data
RAW_DATA_PATH = os.path.join(PROJECT_ROOT, "raw_data")
PROCESSED_DATA_PATH = os.path.join(PROJECT_ROOT, "processed_data")
TRAINED_MODEL_PATH = os.path.join(PROJECT_ROOT, "trained_model")

# Example usage
if __name__ == "__main__":
    print("Project Root:", PROJECT_ROOT)
    print("Raw Data Path:", RAW_DATA_PATH)
    print("Processed Data Path:", PROCESSED_DATA_PATH)
    print("Trained Model Path:", TRAINED_MODEL_PATH)
