pkgname = "qps"
pkgver = "2.11.1"
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
    "libqtxdg-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
depends = ["liblxqt"]
pkgdesc = "LXQt process manager"
license = "GPL-2.0-or-later"
url = "https://github.com/lxqt/qps"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "a40c6ce9d879e6a2d44cc2db41d6a71b9150e5123ee968e90db4e31285ce6436"

