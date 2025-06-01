import os

def ensure_folder_exists(folder_path):
    """
    Ensures that a folder exists. Creates it if it does not.
    
    Args:
        folder_path (str): The path of the folder to check/create.
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
