import hashlib


class Md5:

    def __init__(self, file):

        self.file = file
        self.md5_hash = hashlib.md5()
        self.hash_file = open(self.file, "rb")
        self.content = self.hash_file.read()

    def get_hash(self):
        self.md5_hash.update(self.content)
        self.digest = self.md5_hash.hexdigest()
        return self.digest
