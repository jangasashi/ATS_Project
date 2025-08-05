#utils_file_helper.py

import os

def save_uploaded_file(uploadedfile, folder="uploads"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    filepath = os.path.join(folder, uploadedfile.name)
    with open(filepath, "wb") as f:
        f.write(uploadedfile.getbuffer())
    return filepath