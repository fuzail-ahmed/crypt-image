import os

def cleanup_temp_files(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        else:
            print("File does not exist.")
    except Exception as e:
        print(f"Failed to delete file: {e}")
