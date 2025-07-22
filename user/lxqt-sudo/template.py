pkgname = "lxqt-sudo"
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
    "kwindowsystem-devel",
    "liblxqt-devel",
    "qt6-qttools-devel",
]
depends = ["liblxqt"]
pkgdesc = "Qt GUI frontend for sudo / su"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-sudo"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "8e78111c0e86597c8b8003db1e64cdfdd7e738fec2f796d1d528b6b97a45cf91"
