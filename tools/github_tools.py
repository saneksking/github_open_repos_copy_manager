# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
import requests
import os
import shutil
from tools.printer import StringDecorator


class GitHubTolls:

    def __init__(self, username):
        self._username = username
        self._string_decorator = StringDecorator()

    @property
    def username(self):
        return self._username

    @property
    def api_url(self):
        return f'https://api.github.com/users/{self.username}/repos?per_page=100'

    def get_repo_names(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            repo_list = response.json()
            repo_names = [repo['name'] for repo in repo_list]
            return repo_names
        else:
            return []

    def clone_repos(self, folder_path):
        self._string_decorator.string_decorate(
            text=f'Name: {self.username} | Repositories: {len(self.get_repo_names())}',
            symbol='|'
        )
        self._string_decorator.string_decorate()
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
        repos = self.get_repo_names()
        for repo in repos:
            path = folder_path + '/' + repo
            os.system(f'git clone https://github.com/{self.username}/{repo}.git {path}')
            self._string_decorator.string_decorate()
