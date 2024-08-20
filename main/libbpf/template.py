pkgname = "libbpf"
pkgver = "1.4.5"
pkgrel = 0
build_wrksrc = "src"
build_style = "makefile"
make_cmd = "gmake"
make_install_args = ["LIBSUBDIR=lib"]
hostmakedepends = [
    "gmake",
    "pkgconf",
]
makedepends = [
    "elfutils-devel",
    "linux-headers",
    "zlib-ng-compat-devel",
]
pkgdesc = "Linux BPF userspace library"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-only OR BSD-2-Clause"
url = "https://github.com/libbpf/libbpf"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e225c1fe694b9540271b1f2f15eb882c21c34511ba7b8835b0a13003b3ebde8c"
hardening = ["vis", "!cfi"]
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("../LICENSE.BSD-2-Clause")
    # these headers are the 'latest' bpf headers, newer than what linux-headers
    # provides.
    # libbpf headers require using these latest bpf headers (that come from the
    # libbpf bpf-next tree) instead of the released (linux-headers stable) ones,
    # so place them in a separate private dir to use with -I later
    # https://gitlab.alpinelinux.org/alpine/aports/-/issues/13338
    with self.pushd("../include/uapi/linux"):
        self.install_file("bpf.h", "usr/include/bpf/uapi/linux")
        self.install_file("bpf_common.h", "usr/include/bpf/uapi/linux")
        self.install_file("btf.h", "usr/include/bpf/uapi/linux")


@subpackage("libbpf-devel")
def _(self):
    self.depends += ["linux-headers"]
    return self.default_devel()
