import hashlib
import os


class HashManager:

    @staticmethod
    def md5(file_path):

        h = hashlib.md5()

        with open(file_path, "rb") as f:

            while True:

                chunk = f.read(8192)

                if not chunk:
                    break

                h.update(chunk)

        return h.hexdigest()

    @staticmethod
    def sha256(file_path):

        h = hashlib.sha256()

        with open(file_path, "rb") as f:

            while True:

                chunk = f.read(8192)

                if not chunk:
                    break

                h.update(chunk)

        return h.hexdigest()

    @staticmethod
    def file_size(file_path):

        return os.path.getsize(file_path)

    @staticmethod
    def is_duplicate(cursor, file_hash):

        cursor.execute(
            "SELECT id,title FROM books WHERE file_hash=?",
            (file_hash,)
        )

        return cursor.fetchone()
