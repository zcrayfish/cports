pkgname = "menu-cache"
pkgver = "1.1.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--prefix=/usr",
    "--sysconfdir=/etc",
    "--disable-static",
]
hostmakedepends = [
    "autoconf",
    "automake",
    "glib-devel",
    "gtk-doc-tools",
    "libfm-extra-devel",
    "libtool",
    "pkgconf",
]
makedepends = [
    "gtk+3-devel",
]
pkgdesc = "Caching mechanism for freedesktop.org compliant menus"
license = "LGPL-2.1-or-later"
url = "https://lxde.org"
source = f"https://github.com/lxde/{pkgname}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e8af90467df271c3c8700c840ca470ca2915699c6f213c502a87d74608748f08"

@subpackage("menu-cache-devel")
def _(self):
    return ["usr/include", "usr/lib/*.so", "usr/lib/pkgconfig/*.pc"]
