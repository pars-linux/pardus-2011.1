#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = ''

def install():
    pisitools.insinto("/usr/share/jhylafax", "jhylafax-%s-app.jar" % get.srcVERSION())
