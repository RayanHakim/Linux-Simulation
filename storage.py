import json
import os
from filesystem import Folder, File

def save_vfs(root_folder, filename="vfs_data.json"):
    # Fungsi rekursif untuk mengubah Tree jadi Dictionary
    def folder_to_dict(folder):
        data = {"name": folder.name, "type": "folder", "children": []}
        for name, obj in folder.children.items():
            if isinstance(obj, Folder):
                data["children"].append(folder_to_dict(obj))
            else:
                data["children"].append({"name": obj.name, "type": "file", "content": obj.content})
        return data

    with open(filename, "w") as f:
        json.dump(folder_to_dict(root_folder), f, indent=4)
    print("Sistem berhasil disimpan ke vfs_data.json")

def load_vfs(filename="vfs_data.json"):
    # Jika file belum ada, kembalikan folder Root baru
    if not os.path.exists(filename):
        return Folder("/")

    try:
        with open(filename, "r") as f:
            data = json.load(f)
        
        # Fungsi rekursif untuk mengubah Dictionary kembali jadi Tree
        def dict_to_folder(data_dict, parent=None):
            folder = Folder(data_dict["name"], parent=parent)
            for item in data_dict.get("children", []):
                if item["type"] == "folder":
                    folder.children[item["name"]] = dict_to_folder(item, parent=folder)
                else:
                    folder.children[item["name"]] = File(item["name"], item.get("content", ""))
            return folder

        return dict_to_folder(data)
    except Exception as e:
        print(f"Gagal memuat data: {e}")
        return Folder("/")