pkgname = "lxqt-qtplugin"
pkgver = "2.2.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "lxqt-build-tools",
    "ninja",
    "perl",
    "pkgconf",
]
makedepends = [
    "libdbusmenu-lxqt-devel",
    "libfm-qt-devel",
    "liblxqt-devel",
    "qt6-qtbase-private-devel",
    "qt6-qttools-devel",
]
depends = ["libdbusmenu-lxqt"]
pkgdesc = "Qt-LXQt plugin integration"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-qtplugin"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "e03a0f03e0a4bdc059e72d4c9c5f8e5387d7778cd85b9d53fc7bb8c4403805f0"
