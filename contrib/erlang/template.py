pkgname = "erlang"
pkgver = "27.0.1"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--enable-threads",
]
make_check_target = "release_tests"
hostmakedepends = ["perl"]
makedepends = [
    "glu-devel",
    "java-jdk-openjdk21-default",
    "ncurses-devel",
    "openssl-devel",
    "unixodbc-devel",
    "wxwidgets-devel",
]
pkgdesc = "It's erlang lol"
maintainer = "Mara <177581589+catgirlconspiracy@users.noreply.github.com>"
license = "GPL-2.0-or-later"
url = "https://www.erlang.org"
source = f"https://github.com/erlang/otp/releases/download/OTP-{pkgver}/otp_src_{pkgver}.tar.gz"
sha256 = "26d894e2f0dda9d13560af08ea589afc01569df6b5486e565beb5accb99c9cf4"


@subpackage("erlang-devel")
def _(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    return [
        "usr/lib/erlang/usr/include",
        "usr/lib/erlang/usr/lib/*.a",
        "usr/lib/erlang/erts-*/include",
        "usr/lib/erlang/erts-*/lib/internal/*.a",
        "usr/lib/erlang/lib/*/include",
        "usr/lib/erlang/lib/*/lib/*.a",
    ]


@subpackage("erlang-sources")
def _(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    return [
        "usr/lib/erlang/lib/*/c_src",
        "usr/lib/erlang/lib/*/java_src",
        "usr/lib/erlang/lib/*/src",
        "usr/lib/erlang/lib/*/examples",
        "usr/lib/erlang/erts-*/src",
    ]


@subpackage("erlang-wx")
def _(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    return ["usr/lib/erlang/lib/wx-*"]


@subpackage("erlang-crypto")
def _(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    return [
        "usr/lib/erlang/lib/crypto-*",
        "usr/lib/erlang/lib/public_key-*",
        "usr/lib/erlang/lib/ssh-*",
        "usr/lib/erlang/lib/ssl-*",
    ]


@subpackage("erlang-odbc")
def _(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    return [
        "usr/lib/erlang/lib/odbc-*",
    ]


@subpackage("erlang-jinterface")
def _(self):
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "java-jre-headless-openjdk21-default",
    ]
    return [
        "usr/lib/erlang/lib/jinterface-*",
    ]


@subpackage("erlang-base")
def _(self):
    return [
        "usr/bin",
        "usr/lib/erlang/bin",
        "usr/lib/erlang/erts-*",
        "usr/lib/erlang/releases",
    ]


@subpackage("erlang-kernel")
def _(self):
    self.depends = [f"erlang-base={pkgver}-r{pkgrel}"]
    return [
        "usr/lib/erlang/lib/kernel-*",
    ]


@subpackage("erlang-sasl")
def _(self):
    self.depends = [f"erlang-base={pkgver}-r{pkgrel}"]
    return [
        "usr/lib/erlang/lib/sasl-*",
    ]


@subpackage("erlang-compiler")
def _(self):
    self.depends = [f"erlang-base={pkgver}-r{pkgrel}"]
    return [
        "usr/lib/erlang/lib/compiler-*",
    ]


@subpackage("erlang-stdlib")
def _(self):
    self.depends = [f"erlang-base={pkgver}-r{pkgrel}"]
    return [
        "usr/lib/erlang/lib/stdlib-*",
    ]


@subpackage("erlang-erts")
def _(self):
    self.depends = [f"erlang-base={pkgver}-r{pkgrel}"]
    return [
        "usr/lib/erlang/lib/erts-*",
    ]


@subpackage("erlang-erl-interface")
def _(self):
    self.depends = [f"erlang-base={pkgver}-r{pkgrel}"]
    return [
        "usr/lib/erlang/lib/erl_interface-*",
    ]


@subpackage("erlang-eunit")
def _(self):
    self.depends = [f"erlang-base={pkgver}-r{pkgrel}"]
    return [
        "usr/lib/erlang/lib/eunit-*",
    ]
