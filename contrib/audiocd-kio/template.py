pkgname = "audiocd-kio"
pkgver = "24.05.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "cdparanoia-devel",
    "flac-devel",
    "kconfig-devel",
    "ki18n-devel",
    "kdoctools-devel",
    "kio-devel",
    "kcmutils-devel",
    "libkcddb-devel",
    "libkcompactdisc-devel",
    "libvorbis-devel",
    "qt6-qtbase-devel",
]
# mp3 encoding
depends = ["lame"]
pkgdesc = "KDE bookmarks editor"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kio_audiocd"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/audiocd-kio-{pkgver}.tar.xz"
sha256 = "e48dc6ec0e9f3f964d2fb9d0e0d25ae684ae90348c0295189950134f7928bcd1"


@subpackage("audiocd-kio-devel")
def _(self):
    self.depends += [
        "kio-devel",
        "libkcddb-devel",
        "qt6-qtbase-devel",
    ]
    return self.default_devel()
