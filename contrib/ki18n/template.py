pkgname = "ki18n"
pkgver = "6.5.0"
pkgrel = 0
build_style = "cmake"
# similar tests broken as alpine
make_check_args = ["-E", "(kcatalog|kcountry|klocalizedstring)test"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "qt6-qtdeclarative-devel",
]
depends = ["iso-codes"]
checkdepends = [
    "iso-codes-locale",
    *depends,
]
pkgdesc = "KDE Gettext-based UI text internationalization"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later AND (LGPL-2.1-only OR LGPL-3.0-or-later)"
url = "https://api.kde.org/frameworks/ki18n/html"
source = (
    f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/ki18n-{pkgver}.tar.xz"
)
sha256 = "7873d36a8ae452745d58100e7cda067eae632c787c1fc5a3c63a7072aacfa7fc"
hardening = ["vis"]


@subpackage("ki18n-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]

    return self.default_devel()
