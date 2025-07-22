pkgname = "lximage-qt"
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
    "layer-shell-qt-devel",
    "libdbusmenu-lxqt-devel",
    "libexif-devel",
    "libfm-qt-devel",
    "liblxqt-devel",
    "lxqt-globalkeys-devel",
    "lxqt-menu-data",
    "menu-cache-devel",
    "qt6-qttools-devel",
    "qt6-qtwayland-devel",
    "solid-devel",
    "xcb-util-devel",
]
pkgdesc = "Image viewer and screenshot tool for LXQt"
license = "GPL-2.0-or-later"
url = "https://github.com/lxqt/lximage-qt"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "cc2ebfef3a7e2901114e71c2e15a9d1a382fe2d8a2b1468bade67fe0b68f99ea"
