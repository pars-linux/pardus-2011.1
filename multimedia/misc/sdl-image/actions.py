#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "SDL_image-%s" % get.srcVERSION()

def setup():
    autotools.configure("--disable-dependency-tracking \
                         --disable-static \
                         --enable-gif \
                         --enable-jpeg \
                         --enable-tif \
                         --enable-png \
                         --enable-pnm \
                         --enable-bmp \
                         --enable-xcf \
                         --enable-xpm \
                         --enable-tga \
                         --enable-lbm \
                         --enable-pcx")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dobin(".libs/showimage")

    pisitools.dodoc("CHANGES", "COPYING", "README")
