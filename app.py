# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
from tools.app_manager import AppManager


def main():
    app_manager = AppManager()
    app_manager.show_head()

    # We get a list of names
    # Cloning repositories
    # Archiving repositories
    # Upload the resulting archive to Google disk

    app_manager.show_footer()


if __name__ == '__main__':
    main()
