#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time-stamp: <2024-03-01 11:34:17 krylon>
#
# /home/krylon/OneDrive/Dokumente/code/boardgame/server/board.py
# created on 29. 02. 2024
# (c) 2024 Benjamin Walkenhorst
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY BENJAMIN WALKENHORST ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

"""
board

(c) 2024 Benjamin Walkenhorst
"""


from typing import NamedTuple


class Field(NamedTuple):
    """One field on the board"""

    elevation: int
    terrain: str


class Board:  # pylint: disable-msg=R0903
    """The Board where it all happens"""

    __slots__ = [
        "size",
        "fields",
    ]

    size: tuple[int, int]
    fields: list[list[Field]]

    def __init__(self, fields: list[list[Field]]):
        self.fields = fields
        self.size = (len(fields), len(fields[0]))

        for i in range(1, len(fields)):
            assert len(fields[i]) == len(fields[0])


# Local Variables: #
# python-indent: 4 #
# End: #
