pkgname = "lxqt-archiver"
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
    "json-glib-devel",
    "libexif-devel",
    "libfm-qt-devel",
    "menu-cache-devel",
    "qt6-qttools-devel",
    "xcb-util-devel",
]
depends = ["lxqt-menu-data"]
pkgdesc = "Desktop-agnostic Qt file archiver"
license = "GPL-2.0-or-later"
url = "https://github.com/lxqt/lxqt-archiver"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "53e4121369e3dc72c74e3ae2323ff277072550c83622486b94ad77b26a993ac6"
