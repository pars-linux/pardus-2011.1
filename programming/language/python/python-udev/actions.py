#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
    pisitools.remove("/usr/lib/%s/site-packages/pyudev/pyside.py" % get.curPYTHON())

    pisitools.dodoc("CHANGES.rst", "COPYING", "PKG-INFO", "README.rst")
