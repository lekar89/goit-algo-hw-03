import os
import shutil
import sys

def copy_files_recursive(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for item in os.listdir(source_dir):
        item_path = os.path.join(source_dir, item)
        dest_item_path = os.path.join(dest_dir, item)

        if os.path.isdir(item_path):
            copy_files_recursive(item_path, dest_item_path)
        elif os.path.isfile(item_path):
            try:
                _, ext = os.path.splitext(item)
                sub_dir = os.path.join(dest_dir, ext[1:]) 
                if not os.path.exists(sub_dir):
                    os.makedirs(sub_dir)
                shutil.copy2(item_path, sub_dir)
            except Exception as e:
                print(f"Помилка копіювання")
