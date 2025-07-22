pkgname = "lxqt-powermanagement"
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
    "kidletime-devel",
    "kwindowsystem-devel",
    "liblxqt-devel",
    "lxqt-globalkeys-devel",
    "qt6-qttools-devel",
    "solid-devel",
]
depends = [
    "liblxqt",
    "libxcb",
    "lxqt-globalkeys",
]
pkgdesc = "Power management module for LXQt"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-powermanagement"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "d170b99a0963260f7c98904691afb80b81e72893420671e2c056418e3d059b4d"
