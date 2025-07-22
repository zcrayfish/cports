pkgname = "pcmanfm-qt"
pkgver = "2.2.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "lxqt-build-tools",
    "ninja",
    "perl",
]
makedepends = [
    "layer-shell-qt-devel",
    "libexif-devel",
    "libfm-qt-devel",
    "lxqt-menu-data",
    "menu-cache-devel",
    "qt6-qttools-devel",
    "xcb-util-devel",
]
depends = [
    "desktop-file-utils",
    "lxqt-menu-data",
]
pkgdesc = "Qt port of pcmanfm"
license = "GPL-2.0-or-later"
url = "https://github.com/lxqt/pcmanfm-qt"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "a5eeeafa8d02c9ada1b4660c238f95fde08fa13278c9ea5e191ea3bdfba1be8f"
