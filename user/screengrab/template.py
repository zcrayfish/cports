pkgname = "screengrab"
pkgver = "3.0.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "lxqt-build-tools",
    "ninja",
    "perl",
]
makedepends = [
    "kwindowsystem-devel",
    "layer-shell-qt-devel",
    "libexif-devel",
    "libfm-qt-devel",
    "libqtxdg-devel",
    "lxqt-menu-data",
    "menu-cache-devel",
    "qt6-qtbase-devel",
    "qt6-qtbase-private-devel",
    "qt6-qttools-devel",
    "qt6-qtwayland-devel",
    "xcb-util-devel",
]
depends = ["lxqt-menu-data"]
pkgdesc = "Crossplatform tool for quickly making screenshots"
license = "GPL-2.0-or-later"
url = "https://github.com/lxqt/screengrab"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "30ad0428688595eb09ca684133c1bb1b02c4affae302791c4d2eb7990f6ccee7"
