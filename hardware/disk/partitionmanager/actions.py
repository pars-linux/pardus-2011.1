# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import kde4
from pisi.actionsapi import get

WorkDir = "partitionmanager-%s" % get.srcVERSION().replace("_", "-").upper()

def setup():
    shelltools.export("HOME", get.curDIR())
    kde4.configure("-DPARTMAN_KCM=ON \
                    -DPARTMAN_KPART=ON")

def build():
    kde4.make()

def install():
    kde4.install()

    pisitools.dodoc("CHANGES", "COPYING", "README")
