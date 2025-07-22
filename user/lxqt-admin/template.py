pkgname = "lxqt-admin"
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
    "liblxqt-devel",
    "lxqt-globalkeys-devel",
    "lxqt-menu-data",
    "polkit-qt-1-devel",
    "qt6-qttools-devel",
    "qt6-qtwayland-devel",
    "solid-devel",
    "xcb-util-devel",
]
depends = [
    "liblxqt",
    "polkit",
]
pkgdesc = "LXQt system administration tool"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-admin"
source = f"{url}/releases/download/{pkgver}/lxqt-admin-{pkgver}.tar.xz"
sha256 = "185e4d524c2248adc95d952347b5e7d54d6b4644c372b5614cfe01ccdf59f30d"
