#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time-stamp: <2024-03-02 16:32:56 krylon>
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

from dataclasses import dataclass
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


@dataclass(slots=True)
class Position:
    """Position represents a place on a board"""
    x: int
    y: int


@dataclass(slots=True, kw_only=True)
class Piece:
    """A game piece"""

    pid: int
    name: str
    hp: int
    ap: int
    attack_range: int
    pos: Position

    def __init__(self, **fields):
        self.pid = fields.get("pid", 0)
        self.name = fields["name"]
        self.hp = fields["hp"]
        self.ap = fields["ap"]
        self.attack_range = fields.get("attack_range", 1)
        self.pos = fields.get("pos", Position(0, 0))

        assert self.hp > 0, \
            f"Invalid HP: {self.hp} (must be a positive integer)"
        assert self.ap > 0, \
            f"Invalid AP: {self.ap} (must be a positive integer)"
        assert self.attack_range > 0, \
            f"Invalid attack_range: {self.attack_range} (must be a positive integer)"  # noqa: E501


# Local Variables: #
# python-indent: 4 #
# End: #
