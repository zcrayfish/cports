pkgname = "lxqt-about"
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
    "qt6-qttools-devel",
    "qt6-qtwayland-devel",
    "solid-devel",
    "xcb-util-devel",
]
depends = ["liblxqt"]
pkgdesc = "Information provider about LXQt and the system"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-about"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "c5cb4eaa1c05be347a920dcc97c7892499d483e7e776b4633e390b67c16cd76f"
