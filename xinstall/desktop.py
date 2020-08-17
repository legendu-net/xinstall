"""Install and configure desktop applications.
"""
import sys
import tempfile
from pathlib import Path
import logging
from .utils import (
    is_ubuntu_debian,
    is_linux,
    update_apt_source,
    run_cmd,
    namespace,
    add_subparser,
)
logging.basicConfig(
    format=
    "%(asctime)s | %(module)s.%(funcName)s: %(lineno)s | %(levelname)s: %(message)s",
    level=logging.INFO
)


def nomachine(**kwargs):
    """Install NoMachine.
    """
    args = namespace(kwargs)
    if args.install:
        ver = args.version[:args.version.rindex(".")]
        if is_ubuntu_debian():
            url = f"https://download.nomachine.com/download/{ver}/Linux/nomachine_{args.version}_amd64.deb"
            with tempfile.TemporaryDirectory() as tempdir:
                file = Path(tempdir) / "nomachine.deb"
                cmd = f"curl -sSL {url} -o {file} && dpkg -i {file}"
                run_cmd(cmd)
    if args.config:
        pass
    if args.uninstall:
        pass


def _nomachine_args(subparser):
    subparser.add_argument(
        "-v",
        "--version",
        dest="version",
        default="6.9.2_1",
        help="The version of NoMachine to install."
    )


def _add_subparser_nomachine(subparsers):
    add_subparser(
        subparsers,
        "NoMachine",
        func=nomachine,
        aliases=["nm", "nx"],
        add_argument=_nomachine_args
    )


def lxqt(**kwargs):
    """Install the LXQt desktop environment.
    """
    args = namespace(kwargs)
    if args.install:
        if is_ubuntu_debian():
            update_apt_source()
            cmd = "apt-get install lxqt"
            run_cmd(cmd)
    if args.config:
        pass
    if args.uninstall:
        pass


def _add_subparser_lxqt(subparsers):
    add_subparser(
        subparsers,
        "lxqt",
        func=lxqt,
    )


def pygetwindow(**kwargs):
    """Install and configure the Python package PyGetWindow.
    """
    args = namespace(kwargs)
    if args.install:
        if is_linux():
            sys.exit("PyGetWindow is not supported on Linux currently!")
        cmd = f"{args.pip} install pyobjc-framework-quartz pygetwindow"
        run_cmd(cmd)
    if args.config:
        pass
    if args.uninstall:
        cmd = f"{args.pip} uninstall pyobjc-framework-quartz pygetwindow"
        run_cmd(cmd)


def _add_subparser_pygetwindow(subparsers):
    add_subparser(
        subparsers,
        "pygetwindow",
        func=pygetwindow,
        aliases=["pgw", "getwindow", "gwin"],
    )
