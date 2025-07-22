pkgname = "lxqt-openssh-askpass"
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
    "qt6-qttools-devel",
]
depends = ["liblxqt"]
pkgdesc = "GUI to query passwords on behalf of SSH agent"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-openssh-askpass"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "bb2966427a9462b26059f76ac0504c4d3bf539a6b02e45357c4f9ee99f9b6f3c"
