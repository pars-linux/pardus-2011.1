#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.insinto("%s/%s/tests" % (get.docDIR(), get.srcNAME()), "tests/*")
    pisitools.insinto("%s/%s/tools" % (get.docDIR(), get.srcNAME()), "tools/*")
    pisitools.dodoc("CREDITS.txt")
