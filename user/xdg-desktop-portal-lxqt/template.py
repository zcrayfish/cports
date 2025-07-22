pkgname = "xdg-desktop-portal-lxqt"
pkgver = "1.2.0"
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
    "libexif-devel",
    "libfm-qt-devel",
    "menu-cache-devel",
    "qt6-qtbase-devel",
    "xcb-util-devel",
    "xdg-desktop-portal-devel",
]
depends = ["xdg-desktop-portal"]
pkgdesc = "LXQt xdg desktop portal"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/xdg-desktop-portal-lxqt"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "227f807b03b3503fc95ceba08895df0353a6508ce8129721a4b33a5251042f9b"
