pkgname = "qtermwidget"
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
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Terminal widget for QTerminal"
license = "GPL-2.0-or-later"
url = "https://github.com/lxqt/qtermwidget"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "ba4ffbba79cf55aff76243564936f9337beeebdf8c4a8bfa365b9fc88f261ce9"

@subpackage("qtermwidget-devel")
def _(self):
    return ["usr/include", "usr/lib/*.so", "usr/lib/pkgconfig/*.pc", "usr/lib/cmake/qtermwidget6/*.cmake"]
