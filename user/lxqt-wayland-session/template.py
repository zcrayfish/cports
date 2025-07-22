pkgname = "lxqt-wayland-session"
pkgver = "0.2.0"
pkgrel = 2
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
    "lxqt-menu-data",
    "qt6-qttools-devel",
    "xdg-user-dirs",
]
#labwc is the fallback compositor, users complain when they select the lxqt wayland session and no compositor is installed!
depends = [
    "qtxdg-tools",
    "layer-shell-qt",
    "lxqt-session",
    "labwc",
]
pkgdesc = "LXQt wayland session files and start scripts"
license = "LGPL-2.1-or-later AND MIT AND BSD-3-Clause AND GPL-3.0-only AND GPL-2.0-only AND CC-BY-SA-4.0"
url = "https://github.com/lxqt/lxqt-wayland-session"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "d7a88964fe705bcf40a6d04eb1d570c01a01d6dc5104dd393dc4effcb5a9cd28"

def post_install(self):
    self.install_license("COPYING")
    self.install_license("COPYING.LESSER")
    self.install_license("LICENSE")
    self.install_license("LICENSE.BSD")
    self.install_license("LICENSE.GPLv2")
    self.install_license("LICENSE.MIT")
