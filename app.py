# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
from tools.app_manager import AppManager
from tools.github_tools import GitHubTolls
from tools.archive_tools import ArchiveTolls


def main():
    app_manager = AppManager()
    app_manager.show_head()
    username = input('Input GitHub username: ')
    github_tools = GitHubTolls(username)
    folder_path = './repos'
    archive_tools = ArchiveTolls(folder_path)

    # We get a list of names
    # Cloning repositories
    github_tools.clone_repos(folder_path)
    # Archiving repositories
    archive_tools.archive()
    # Upload the resulting archive to Google disk

    app_manager.show_footer()


if __name__ == '__main__':
    main()
