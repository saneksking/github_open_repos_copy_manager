# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
from tools.config import Config
from tools.printer import StringDecorator


class AppManager:
    _printer = StringDecorator()
    _config = Config()

    @classmethod
    def show_head(cls):
        cls._printer.string_decorate()
        cls._printer.string_decorate(cls._config.app_name)
        cls._printer.string_decorate()

    @classmethod
    def show_footer(cls):
        cls._printer.string_decorate(cls._config.help_url)
        cls._printer.string_decorate(cls._config.copyright_)
