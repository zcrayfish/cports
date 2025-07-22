pkgname = "libfm-extra"
pkgver = "1.3.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--prefix=/usr",
    "--sysconfdir=/etc",
    "--disable-static",
    "--with-gtk=3",
    "--with-extra-only",
]
hostmakedepends = [
    "autoconf",
    "automake",
    "cairo-devel",
    "gettext-devel",
    "glib-devel",
    "gtk-doc-tools",
    "intltool",
    "libtool",
    "pango-devel",
    "pkgconf",
    "vala",
]
makedepends = [
    "gtk+3-devel",
]
pkgdesc = "Library for file management"
license = "LGPL-2.1-or-later"
url = "https://lxde.org"
source = f"https://downloads.sourceforge.net/pcmanfm/libfm-{pkgver}.tar.xz"
sha256 = "a5042630304cf8e5d8cff9d565c6bd546f228b48c960153ed366a34e87cad1e5"

@subpackage("libfm-extra-devel")
def _(self):
    return ["usr/include", "usr/lib/*.so", "usr/lib/pkgconfig/*.pc"]

