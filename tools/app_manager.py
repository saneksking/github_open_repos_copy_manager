# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
from tools.config import Config
from tools.printer import StringDecorator


class AppManager:
    printer = StringDecorator()
    config = Config()

    @classmethod
    def show_head(cls):
        cls.printer.string_decorate()
        cls.printer.string_decorate(cls.config.app_name, symbol='-')
        cls.printer.string_decorate()

    @classmethod
    def show_footer(cls):
        cls.printer.string_decorate(cls.config.help_url)
        cls.printer.string_decorate(cls.config.copyright_, symbol='=')
