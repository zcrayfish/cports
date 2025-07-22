pkgname = "libfm-qt"
pkgver = "2.2.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "libexif-devel",
    "lxqt-build-tools",
    "menu-cache-devel",
    "ninja",
    "perl",
    "pkgconf",
]
makedepends = [
    "kwindowsystem-devel",
    "layer-shell-qt-devel",
    "libdbusmenu-lxqt-devel",
    "liblxqt-devel",
    "lxqt-globalkeys-devel",
    "lxqt-menu-data",
    "qt6-qtbase-private-devel",
    "qt6-qttools-devel",
    "qt6-qtwayland-devel",
    "solid-devel",
    "xcb-util-devel",
]
depends = ["menu-cache"]
pkgdesc = "Qt port of libfm"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/libfm-qt"
source = f"{url}/releases/download/{pkgver}/libfm-qt-{pkgver}.tar.xz"
sha256 = "4d8aa86fcfcf424f7f41c4a931e8d804dd12bedc8428931b5bc955345c4313a9"

@subpackage("libfm-qt-devel")
def _(self):
    return ["usr/include", "usr/lib/*.so", "usr/lib/pkgconfig/*.pc", "usr/share/cmake/fm-qt6/*.cmake"]
