pkgname = "libfm"
pkgver = "1.4.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-gtk=3"]
configure_gen = ["./autogen.sh"]
hostmakedepends = [
    "autoconf",
    "automake",
    "gettext-devel",
    "gtk-doc-tools",
    "intltool",
    "libtool",
    "pkgconf",
    "vala",
]
makedepends = [
    "gtk+3-devel",
]
depends = ["libfm-extra"]
pkgdesc = "Library for file management"
license = "GPL-2.0-or-later"
url = "https://github.com/lxde/libfm"
source = f"{url}/archive/{pkgver}/libfm{pkgver}.tar.gz"
sha256 = "7d7b616411992389a4b7f35796109d605f30bc2ceab84d4081d1665254ebbf82"

@subpackage("libfm-devel")
def _(self):
    return ["usr/include", "usr/lib/*.so", "usr/lib/pkgconfig/*.pc"]
