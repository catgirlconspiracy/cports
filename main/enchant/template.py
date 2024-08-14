pkgname = "enchant"
pkgver = "2.8.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-relocatable", "--disable-static"]
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gmake",
    "libtool",
    "pkgconf",
    "vala",
]
makedepends = [
    "aspell-devel",
    "glib-devel",
    "hunspell-devel",
    "icu-devel",
    "libltdl-devel",
    "nuspell-devel",
    "unittest-cpp",
]
pkgdesc = "Generic spell checking library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://abiword.github.io/enchant"
source = f"https://github.com/AbiWord/enchant/releases/download/v{pkgver}/enchant-{pkgver}.tar.gz"
sha256 = "8f19535adb5577b83b00e02f330fe9b9eb40dd21f19e2899636fc4d3a7696375"


@subpackage("enchant-devel")
def _devel(self):
    return self.default_devel()


@subpackage("enchant-progs")
def _progs(self):
    return self.default_progs()
