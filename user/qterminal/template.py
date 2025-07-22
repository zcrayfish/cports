pkgname = "qterminal"
pkgver = "2.2.1"
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
    "qt6-qttools-devel",
    "qtermwidget-devel",
]
depends = ["lxqt-menu-data"]
pkgdesc = "Lightweight Qt-based terminal emulator"
license = "GPL-2.0-or-later"
url = "https://github.com/lxqt/qterminal"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "0cd38c3408bbaf4737a0276cf3d64b4c987716f0ef1f1eb8e9c1485e0c08f5d2"
