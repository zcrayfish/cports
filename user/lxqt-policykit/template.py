pkgname = "lxqt-policykit"
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
    "liblxqt-devel",
    "polkit-devel",
    "polkit-qt-1-devel",
    "qt6-qttools-devel",
]
depends = [
    "liblxqt",
    "polkit-qt-1",
]
pkgdesc = "LXQt PolicyKit agent"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-policykit"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "d9872d58f03f2085e339dc4cad83486000019a68f4464eb12599a61eaf759a1e"

