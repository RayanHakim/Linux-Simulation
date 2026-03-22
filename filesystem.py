import time

class File:
    def __init__(self, name, content=""):
        self.name = name
        self.content = content
        self.created_at = time.ctime()

class Folder:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = {}  # Berisi File atau Folder lain
        self.created_at = time.ctime()

    def add_folder(self, name):
        if name not in self.children:
            self.children[name] = Folder(name, parent=self)
            return True
        return False

    def add_file(self, name, content=""):
        self.children[name] = File(name, content)