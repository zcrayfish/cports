pkgname = "libsysstat"
pkgver = "1.1.0"
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
    "qt6-qtbase-devel",
]
pkgdesc = "Library used to query system info and statistics"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/libsysstat"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "996e5e8c43b1364a81a660b56956948c628e919f1d73554df6be152bbec8d430"

@subpackage("libsysstat-devel")
def _(self):
    return ["usr/include", "usr/lib/*.so", "usr/lib/pkgconfig/*.pc", "usr/share/cmake/sysstat-qt6/*.cmake"]
