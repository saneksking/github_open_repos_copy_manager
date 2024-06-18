# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
import os
import zipfile


class ArchiveTolls:
    def __init__(self, path):
        self.path = path

    def archive(self):
        if os.path.isdir(self.path):
            with zipfile.ZipFile('repos.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, _, files in os.walk(self.path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        rel_path = os.path.relpath(file_path, os.path.dirname(self.path))
                        zipf.write(file_path, rel_path)
        elif os.path.isfile(self.path):
            with zipfile.ZipFile('archive.zip', 'w') as zipf:
                zipf.write(self.path, arcname='archive.zip')
