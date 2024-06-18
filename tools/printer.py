# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
import shutil


class StringDecorator:
    @classmethod
    def _term_width(cls):
        return shutil.get_terminal_size()[0]

    @classmethod
    def string_decorate(cls, text='', symbol='*', print_flag=True):
        if text:
            result_string = f' {text} '.center(cls._term_width(), symbol)
        else:
            result_string = ''.center(cls._term_width(), symbol)

        if print_flag:
            print(result_string)
        else:
            return result_string
